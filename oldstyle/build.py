r"""SSP ヘルプのサイトを作る（旧 SSP ヘルプ（HTML 版）の見た目を模した、自前の静的サイトのビルド）。

    python oldstyle/build.py              # scripts/prepare_site.py で _site_src/ を作り、_site/ に出力する
    python oldstyle/build.py --no-prepare # _site_src/ を作り直さない
    python oldstyle/build.py --lang=en    # i18n/en/ の翻訳を重ねた版だけを _site/en/ に出す（--no-langs: 日本語版だけ）

原稿（Markdown）→ HTML → 旧 SSP ヘルプの構造（左の #menu、上の #breadcrumb、本文の #contents、下の #navigation）に組む。
HTML は HTML5（旧版は XHTML 1.0）。出力のファイル名は旧 SSP ヘルプと同じ（howto-boot.html など）。
詳しくは oldstyle/README.md。
"""
import argparse
import json
import os
import posixpath
import re
import shutil
import string
import subprocess
import sys
import zipfile

import lxml.html
import markdown
import yaml
from lxml import etree
from pymdownx.slugs import slugify

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import prepare_site  # noqa: E402

LANG = prepare_site.LANG                # --lang=<コード>（翻訳版）。無ければ日本語版
SRC = prepare_site.OUT                  # 原稿の写し（_site_src/、翻訳版は _site_src_<コード>/）
RAW = prepare_site.RAW                  # 生の Markdown 原稿の写し（_raw/）
OUT = os.path.join(ROOT, '_site', *([LANG] if LANG else []))   # 翻訳版は _site/<コード>/（日本語版の下）
STATIC = os.path.join(HERE, 'static')
SITE_URL = prepare_site.SITE_URL
# 翻訳版の頁は、画像・添付ファイルなど（日本語版のルートにある共有のもの）を 1 つ上から参照する
BASE = '../' if LANG else ''

# 翻訳版の言語（i18n/<コード>/ があるものだけ、日本語版のビルドの最後に続けてビルドする）
LANGS = ['en', 'zh-Hant', 'zh']

# 画面に出す文言（ビルドが書くもの）。構造の判定に使う日本語の語は、訳文でも原文のまま残し、表示のときだけここで言語ごとの語にする
UI = {
    'ja': {
        'site_name': 'SSP ヘルプ', 'home': 'はじめに', 'breadcrumb': 'パンくずリスト', 'adjacent': '前後のページ', 'contents': '目次',
        'search_ph': 'ヘルプ内検索', 'search_h1': '検索', 'search_button': '検索', 'search_desc': 'SSP ヘルプの内部検索',
        'default_desc': 'SSP の使い方ヘルプ', 'banner': 'バナー', 'dev': '【開発】',
    },
    'en': {
        'site_name': 'SSP Help', 'home': 'Introduction', 'breadcrumb': 'Breadcrumb', 'adjacent': 'Previous and next pages', 'contents': 'Contents',
        'search_ph': 'Search help', 'search_h1': 'Search', 'search_button': 'Search', 'search_desc': 'Search within SSP Help',
        'default_desc': 'User help for SSP', 'banner': 'Banner', 'dev': '[Dev]',
    },
    'zh-Hant': {
        'site_name': 'SSP 說明', 'home': '簡介', 'breadcrumb': '導覽路徑', 'adjacent': '上一頁與下一頁', 'contents': '目錄',
        'search_ph': '搜尋說明', 'search_h1': '搜尋', 'search_button': '搜尋', 'search_desc': 'SSP 說明的站內搜尋',
        'default_desc': 'SSP 使用說明', 'banner': '橫幅', 'dev': '【開發】',
    },
    'zh': {
        'site_name': 'SSP 帮助', 'home': '简介', 'breadcrumb': '导航路径', 'adjacent': '上一页与下一页', 'contents': '目录',
        'search_ph': '搜索帮助', 'search_h1': '搜索', 'search_button': '搜索', 'search_desc': 'SSP 帮助的站内搜索',
        'default_desc': 'SSP 使用帮助', 'banner': '横幅', 'dev': '【开发】',
    },
}
T = UI[LANG or 'ja']
SITE_NAME = T['site_name']


def available_langs():
    """言語メニューに出す言語のコード。日本語 + i18n/<コード>/ があるもの（LANGS の順）"""
    return ['ja'] + [code for code in LANGS if os.path.isdir(os.path.join(ROOT, 'i18n', code))]

# 原稿の写し（_site_src/）でのパス → 出力のページ名（index, howto-boot, ...）
STEM_OF = {('index.md' if md == 'INDEX.md' else md): stem for stem, md in prepare_site.PAGES.items()}

MD_EXTENSIONS = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists', 'pymdownx.superfences', 'toc']
MD_CONFIG = {
    # GitHub と同じく日本語の見出しをそのままアンカーにする（prepare_site.py の heading_slug と同じ変換）
    'toc': {'slugify': slugify(case='lower')},
}

errors = []


def error(msg):
    errors.append(msg)
    print(f'エラー: {msg}', file=sys.stderr)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path) or OUT, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


# ---------------------------------------------------------------- 章立て（.nav.yml）

class Node:
    def __init__(self, title, page=None, depth=0, parent=None):
        self.title = title
        self.page = page          # 原稿の写しでのパス。無ければ見出しだけ（メニューでは文字だけ）
        self.depth = depth        # 最上位の項目が 1
        self.parent = parent
        self.children = []

    @property
    def stem(self):
        return STEM_OF[self.page] if self.page else None

    @property
    def href(self):
        return self.stem + '.html'


def read_nav_file(rel_dir):
    """章立ての .nav.yml。翻訳版では i18n/<言語>/<ディレクトリ>/.nav.yml（メニューの名前の訳）があればそちら"""
    path = os.path.join(ROOT, rel_dir, '.nav.yml')
    if LANG and os.path.isfile(os.path.join(ROOT, 'i18n', LANG, rel_dir, '.nav.yml')):
        path = os.path.join(ROOT, 'i18n', LANG, rel_dir, '.nav.yml')
    if not os.path.exists(path):
        error(f'{posixpath.join(rel_dir, ".nav.yml")} が無い')
        return []
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)['nav']


def parse_entries(entries, rel_dir, parent):
    """.nav.yml（mkdocs-awesome-nav の書式のうち使っている分）の nav を、parent の子にする。
    `index.md`（題なし）は parent 自身のページ、`題: file.md` はページ、`題: フォルダ` は下の .nav.yml、`題: [..]` はページの無い見出し"""
    for entry in entries:
        if isinstance(entry, str):
            if entry != 'index.md':
                error(f'{rel_dir}/.nav.yml: 題の無い {entry} は index.md しか書けない')
                continue
            parent.page = posixpath.join(rel_dir, 'index.md') if rel_dir else 'index.md'
            continue
        (title, value), = entry.items()
        node = Node(title, depth=parent.depth + 1, parent=parent)
        parent.children.append(node)
        if isinstance(value, list):
            parse_entries(value, rel_dir, node)
        elif value.endswith('.md'):
            node.page = posixpath.join(rel_dir, value) if rel_dir else value
        else:
            sub = posixpath.join(rel_dir, value) if rel_dir else value
            parse_entries(read_nav_file(sub), sub, node)


def load_nav():
    root = Node('SSP ヘルプ', depth=0)
    parse_entries(read_nav_file(''), '', root)
    # 最上位の index.md は、題を「はじめに」としてページにする（旧版のメニューの先頭）
    if root.page:
        home = Node(T['home'], page=root.page, depth=1, parent=root)
        root.children.insert(0, home)
        root.page = None
    return root


def flatten(node, out):
    for c in node.children:
        if c.page:
            out.append(c)
        flatten(c, out)
    return out


def menu_html(root, current):
    def li(node):
        label = esc(node.title)
        if node.page:
            cur = ' aria-current="page"' if node is current else ''
            label = f'<a href="{node.href}"{cur}>{label}</a>'
        sub = ''
        if node.children:
            sub = '\n<ul>\n' + '\n'.join(li(c) for c in node.children) + '\n</ul>\n'
        return f'<li>{label}{sub}</li>'
    return '<ul>\n' + '\n'.join(li(c) for c in root.children) + '\n</ul>'


def breadcrumb_html(node):
    if node.page == 'index.md':
        return ''
    chain = []
    n = node
    while n.parent is not None:
        chain.append(n)
        n = n.parent
    chain.reverse()
    home = Node(T['home'], page='index.md')
    items = []
    for n in [home] + chain:
        if n.page:
            items.append(f'<li><a href="{n.href}">{esc(n.title)}</a></li>')
        else:
            items.append(f'<li>{esc(n.title)}</li>')
    return f'<nav id="breadcrumb" aria-label="{esc(T["breadcrumb"])}">\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</nav>\n'


def nav_label(node):
    # 旧版の前後のページの表示。3 階層目のページは「カレンダー:スケジュール編集」のように親の名前を前に付ける
    if node.depth >= 3 and node.parent is not None:
        return f'{node.parent.title}:{node.title}'
    return node.title


def navigation_html(prev, nxt):
    items = []
    if prev:
        items.append(f'<li class="previous"><a href="{prev.href}" rel="prev">{esc(nav_label(prev))}</a></li>')
    if nxt:
        items.append(f'<li class="next"><a href="{nxt.href}" rel="next">{esc(nav_label(nxt))}</a></li>')
    if not items:
        return ''
    return f'<nav id="navigation" aria-label="{esc(T["adjacent"])}">\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</nav>\n'


# ---------------------------------------------------------------- Markdown → HTML

def resolve(src, href):
    """原稿 src（_site_src/ からのパス）の中のリンク href の行き先。(行き先のパス, フラグメント) か None（外部・ページ内）"""
    if not href or href.startswith(('#', '/', 'mailto:', 'tel:', 'javascript:')) or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', href):
        return None
    path, _, frag = href.partition('#')
    target = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
    return target, frag


def rewrite_links(tree, src):
    for a in tree.iter('a'):
        r = resolve(src, a.get('href'))
        if not r:
            continue
        target, frag = r
        if target in STEM_OF:
            a.set('href', STEM_OF[target] + '.html' + ('#' + frag if frag else ''))
        elif os.path.exists(os.path.join(RAW, target)) and target.endswith('.md'):
            error(f'{src}: {a.get("href")} は HTML のページではない原稿（PAGES に無い）')
        elif os.path.exists(os.path.join(ROOT, target)):
            a.set('href', BASE + target + ('#' + frag if frag else ''))
        else:
            error(f'{src}: リンク先 {a.get("href")} が無い')
    for img in tree.iter('img'):
        r = resolve(src, img.get('src'))
        if not r:
            continue
        target = r[0]
        if os.path.exists(os.path.join(ROOT, target)):
            img.set('src', BASE + target)
            img.set('loading', 'lazy')
        else:
            error(f'{src}: 画像 {img.get("src")} が無い')


def text_of(el):
    return re.sub(r'\s+', ' ', el.text_content()).strip()


def convert_admonitions(tree):
    # !!! tip "ヒント" → 旧版の div.Hint（「HINT:」は CSS で付く）
    for div in tree.xpath('//div[contains(concat(" ", @class, " "), " admonition ")]'):
        classes = div.get('class', '').split()
        title = div.find('p[@class="admonition-title"]')
        if 'tip' in classes and title is not None and text_of(title) == 'ヒント':
            div.remove(title)
            div.set('class', 'Hint')


def convert_conditions(tree):
    # 【開発】【サブ】のような条件の印は、旧版の span.Condition（緑の太字）。翻訳版では、訳文に残した【開発】を、その言語の表記にする
    for s in tree.iter('strong'):
        if text_of(s).startswith('【'):
            s.set('class', 'Condition')
            if LANG and text_of(s) == '【開発】':
                for c in list(s):
                    s.remove(c)
                s.text = T['dev']


def convert_qna(tree):
    """質問と答え（### Q: ... に、**A1:** ... の段落が続く）を、旧版の table.QnA に近い箱にする。
    <div class="QnA"> の中に、質問の見出し（h3.Q）と、答え（div.A）が並ぶ"""
    for h3 in list(tree.iter('h3')):
        if not text_of(h3).startswith('Q:') or h3.getparent() is None:
            continue
        parent = h3.getparent()
        siblings = []
        nxt = h3.getnext()
        while nxt is not None and nxt.tag not in ('h1', 'h2', 'h3'):
            siblings.append(nxt)
            nxt = nxt.getnext()
        box = etree.Element('div')
        box.set('class', 'QnA')
        parent.insert(parent.index(h3), box)
        box.append(h3)
        h3.set('class', 'Q')
        # 見出しの「Q:」は旧版と同じく目立つ色の Head にする
        head = etree.Element('span')
        head.set('class', 'Head')
        head.text = 'Q:'
        head.tail = (h3.text or '')[2:]
        h3.text = None
        h3.insert(0, head)
        current = None
        for el in siblings:
            first = el.find('strong') if el.tag == 'p' else None
            if first is not None and re.match(r'^A\d*:$', text_of(first)) and el.text is None:
                current = etree.SubElement(box, 'div')
                current.set('class', 'A')
                first.set('class', 'Head')
            if current is None:
                current = etree.SubElement(box, 'div')
                current.set('class', 'A')
            current.append(el)


def convert_tables(tree):
    for table in tree.iter('table'):
        head = table.find('.//th')
        if head is not None and text_of(head) == 'バナー':
            table.set('class', 'Links')
            if LANG:     # 判定に使う「バナー」は訳文でも原文のまま残してある。表示だけその言語の語にする
                head.text = T['banner']


def render(src, text):
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG, output_format='html')
    html = md.convert(text)
    tree = lxml.html.fragment_fromstring(html, create_parent='div')
    rewrite_links(tree, src)
    convert_admonitions(tree)
    convert_conditions(tree)
    convert_qna(tree)
    convert_tables(tree)
    return tree


def inner_html(tree):
    out = (tree.text or '')
    out = esc(out) if out.strip() else ''
    for c in tree:
        out += etree.tostring(c, method='html', encoding='unicode')
    return out


def description_of(tree):
    for p in tree.iter('p'):
        t = text_of(p)
        if t:
            return t[:110] + ('…' if len(t) > 110 else '')
    return T['default_desc']


def search_entries(tree, label, stem):
    """検索の索引の行: [ページの名前, 節の題, URL, 本文]。節は H1〜H3 の区切り"""
    entries = []
    title, frag, buf = label, '', []

    def flush():
        text = ' '.join(buf).strip()
        if text or title:
            entries.append([label, title, stem + '.html' + ('#' + frag if frag else ''), re.sub(r'\s+', ' ', text)])

    def blocks(parent):
        for el in parent:
            if not isinstance(el.tag, str):
                continue
            if el.tag == 'div' and el.get('class') == 'QnA':
                yield from blocks(el)
            else:
                yield el

    for el in blocks(tree):
        if el.tag in ('h1', 'h2', 'h3'):
            flush()
            buf = []
            title = text_of(el)
            frag = el.get('id', '')
        else:
            buf.append(text_of(el))
    flush()
    return entries


# ---------------------------------------------------------------- 出力

def frame_fields():
    """page.html の枠に埋める、言語ごとの値"""
    return dict(lang=LANG or 'ja', langs=','.join(available_langs()), base=BASE,
                l_contents=esc(T['contents']), l_search_ph=esc(T['search_ph']))


def build_pages():
    root = load_nav()
    pages = flatten(root, [])
    nodes = {n.page: n for n in pages}
    for md in STEM_OF:
        if md not in nodes:
            error(f'{md} が .nav.yml に無い（メニューに出せない）')
    if errors:
        return None
    template = string.Template(read(os.path.join(HERE, 'templates', 'page.html')))
    index = []
    for i, node in enumerate(pages):
        tree = render(node.page, read(os.path.join(SRC, node.page)))
        prev = pages[i - 1] if i > 0 else None
        nxt = pages[i + 1] if i + 1 < len(pages) else None
        links = ''
        if prev:
            links += f'<link rel="prev" href="{prev.href}">\n'
        if nxt:
            links += f'<link rel="next" href="{nxt.href}">\n'
        links += f'<link rel="canonical" href="{SITE_URL}{LANG + "/" if LANG else ""}{"" if node.stem == "index" else node.href}">\n'
        title = node.title if node.stem != 'index' else T['home']
        write(node.href, template.substitute(
            title=esc(f'{title} - {SITE_NAME}'), description=esc(description_of(tree)), links=links,
            menu=menu_html(root, node), breadcrumb=breadcrumb_html(node),
            content=inner_html(tree), navigation=navigation_html(prev, nxt), **frame_fields()))
        index.extend(search_entries(tree, nav_label(node), node.stem))
    # 検索頁と、検索の索引（大きいので、使うときに search.js が読み込む）
    search = (f'<h1>{esc(T["search_h1"])}</h1>\n<form id="search-form" action="search.html">\n<p><input id="search-q" name="q" type="search" size="30" autocomplete="off"> '
              f'<button type="submit">{esc(T["search_button"])}</button></p>\n</form>\n<div id="search-results"></div>\n')
    write('search.html', template.substitute(
        title=esc(f'{T["search_h1"]} - {SITE_NAME}'), description=esc(T['search_desc']), links='<meta name="robots" content="noindex">\n',
        menu=menu_html(root, None), breadcrumb='', content=search, navigation='', **frame_fields()))
    write('search-index.js', 'window.SSP_INDEX=' + json.dumps(index, ensure_ascii=False, separators=(',', ':')) + ';\n')
    return pages


REDIRECT_HTML = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>ページが移動しました</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex">
<script>location.replace({target_js} + location.hash);</script>
</head>
<body>
<p>このページは移動しました。自動で移動しない場合は <a href="{target}">{target}</a> を開いてください。</p>
</body>
</html>
"""


def write_old_url_redirects():
    """Zensical 版のサイトの URL（howto/use/ など）から、今のページへ転送する HTML を置く"""
    for md, stem in STEM_OF.items():
        if md == 'index.md':
            continue
        d = md[:-len('.md')]
        if posixpath.basename(d) == 'index':
            d = posixpath.dirname(d)
        target = posixpath.relpath(stem + '.html', d)
        write(posixpath.join(d, 'index.html'), REDIRECT_HTML.format(
            url=SITE_URL + stem + '.html', target=target, target_js=json.dumps(target)))


def copy_static():
    for name in os.listdir(STATIC):
        src = os.path.join(STATIC, name)
        dst = os.path.join(OUT, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)
    if LANG:
        return      # 画像（assets/）・llms.txt・生の原稿は、日本語版のものを共有する（翻訳版は 1 つ上から参照）
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copy(os.path.join(ROOT, 'llms.txt'), os.path.join(OUT, 'llms.txt'))
    # 生の Markdown 原稿（llms.txt や INDEX.md の相対リンクを、サイト上でも辿れるようにする）
    shutil.copytree(RAW, OUT, dirs_exist_ok=True)


OFFLINE_ZIP = 'ukadoc-ssp-offline.zip'


def build_offline_zip():
    """出力したサイト一式（HTML・CSS・JS・画像・llms.txt・生の Markdown 原稿）を、オフラインで読める zip にする。
    展開すると `ukadoc-ssp/` の下に出る。zip 自身は含めない。サイトのルートに置かれ、公開される"""
    zip_path = os.path.join(OUT, OFFLINE_ZIP)
    files = []
    for dirpath, dirs, names in os.walk(OUT):
        dirs.sort()
        for name in sorted(names):
            path = os.path.join(dirpath, name)
            if path != zip_path:
                files.append(path)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files:
            rel = os.path.relpath(path, OUT).replace(os.sep, '/')
            z.write(path, 'ukadoc-ssp/' + rel)
    return len(files), os.path.getsize(zip_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-prepare', action='store_true', help='_site_src/ を作り直さない')
    ap.add_argument('--lang', help='翻訳版だけを _site/<コード>/ に出す（i18n/<コード>/ の訳文を重ねる）')
    ap.add_argument('--no-langs', action='store_true', help='日本語版だけを作る（翻訳版を続けて作らない）')
    args = ap.parse_args()
    if not args.no_prepare:
        prepare_site.main()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    copy_static()
    pages = build_pages()
    if pages is None or errors:
        sys.exit(f'ビルドに失敗: エラー {len(errors)} 件')
    print(f'{len(pages)} ページを {os.path.relpath(OUT)} に出力した')
    if not LANG:
        write_old_url_redirects()
        if not args.no_langs:
            # 日本語版の後ろに、翻訳のある言語（i18n/<コード>/ があるもの）を _site/<コード>/ へ続けてビルドする
            for code in available_langs()[1:]:
                subprocess.run([sys.executable, os.path.abspath(__file__), f'--lang={code}'], check=True)
        # オフライン zip は、翻訳版も含めて最後に作る（言語メニューのリンク先が zip の中にもあるように）
        n, size = build_offline_zip()
        print(f'{OFFLINE_ZIP}: {n} ファイル、{size / 1024 / 1024:.1f} MB')


if __name__ == '__main__':
    main()
