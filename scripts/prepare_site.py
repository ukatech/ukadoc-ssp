r"""サイトのビルド（oldstyle/build.py）のために、原稿を _site_src/ へ写す。

- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える
- GitHub では表示できるが Python-Markdown では崩れる書き方を直す
  （段落の直後に空行なしで続くリスト・表の前に空行を入れる）
- 表の中のコードスパンの `\|` を `|` に戻す（GitHub 向けの書き方をサイト向けに直す）
- `_名前_` のように _ で挟んだ書き方（斜体になってしまう）を警告する
- 用語説明（about/reference.md）の見出しにある用語を、本文のほかのページから用語説明へのリンクにする
  （旧 SSP ヘルプの nwordlinks と同じ。見出し・コード・既存のリンク・URL の中はリンクにしない）
- 生の Markdown 原稿を _raw/ に写す（ビルド後に _site へ重ねる。llms.txt から INDEX.md などを辿れるようにする）
- ページ名の表 PAGES（旧 SSP ヘルプのファイル名 → 原稿）を持つ。サイトの HTML のファイル名はこの名前（config-ippan.html など）
- `--lang=<コード>`（例: en）を付けると、日本語の原稿に i18n/<コード>/ の翻訳を重ねたものを _site_src_<コード>/ に写す。
  構造の判定と見出しの id は日本語の原稿から作る（訳した見出しでも `file.md#見出し` のリンクが切れないように）
原稿そのものは書き換えない。materials/（画像の素材）はサイトに含めない。
"""
import os
import posixpath
import re
import shutil
import sys

import markdown
from pymdownx.slugs import slugify

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))


def _lang_arg():
    """--lang=<コード>（例: en）。指定すると、日本語の原稿に i18n/<コード>/ の翻訳を重ねる。無ければ日本語版"""
    for a in sys.argv[1:]:
        if a.startswith('--lang='):
            return a.split('=', 1)[1]
    return None


LANG = _lang_arg()
OUT = os.path.join(ROOT, '_site_src' + (f'_{LANG}' if LANG else ''))
I18N = os.path.join(ROOT, 'i18n', LANG) if LANG else None
# そのまま 1 ファイル 1 ページで写すディレクトリ（入れ子のディレクトリも写す）
DIRS = ['howto', 'functions', 'config', 'dev', 'about']
# 用語説明のページ。この見出しの用語が、ほかのページの本文でリンクになる
GLOSSARY_PAGE = 'about/reference.md'
SITE_URL = 'https://ukatech.shillest.net/ukadoc-ssp/'
# 旧 SSP ヘルプ（HTML 版）のファイル名 → 原稿。サイトの HTML は、この名前の .html として出す（INDEX.md は index.html）。
# SSP は本体設定のヘルプボタンや `--help ファイル名` で、旧ファイル名のページを開くので、名前は変えられない
PAGES = {
    'index': 'INDEX.md',
    'howto-boot': 'howto/boot.md',
    'howto-use': 'howto/use.md',
    'howto-rclick': 'howto/rclick.md',
    'howto-add': 'howto/add.md',
    'howto-verup': 'howto/verup.md',
    'howto-plugin': 'howto/plugin.md',
    'howto-headline': 'howto/headline.md',
    'functions': 'functions/index.md',
    'calendar': 'functions/calendar/index.md',
    'calendar-schedule': 'functions/calendar/schedule.md',
    'calendar-menu': 'functions/calendar/menu.md',
    'sspim': 'functions/sspim/index.md',
    'sspim-addto': 'functions/sspim/addto.md',
    'sspim-sendto': 'functions/sspim/sendto.md',
    'explorer': 'functions/explorer/index.md',
    'explorer-menu': 'functions/explorer/menu.md',
    'pictureviewer': 'functions/pictureviewer.md',
    'archiveviewer': 'functions/archiveviewer.md',
    'windowmode': 'functions/windowmode.md',
    'speech_recognition': 'functions/speech-recognition.md',
    'speech_synthesis': 'functions/speech-synthesis.md',
    'other': 'functions/other.md',
    'shortcut': 'functions/shortcut.md',
    'option': 'functions/option.md',
    'config': 'config/index.md',
    'config-eachghost': 'config/eachghost.md',
    'config-ippan': 'config/ippan.md',
    'config-ghost': 'config/ghost.md',
    'config-ghost2': 'config/ghost2.md',
    'config-folder': 'config/folder.md',
    'config-disp': 'config/disp.md',
    'config-talk': 'config/talk.md',
    'config-dictation': 'config/dictation.md',
    'config-conn1': 'config/conn1.md',
    'config-conn2': 'config/conn2.md',
    'config-pop': 'config/pop.md',
    'config-extprog': 'config/extprog.md',
    'config-im': 'config/im.md',
    'config-i18n': 'config/i18n.md',
    'config-streamingtool': 'config/streamingtool.md',
    'config-dev': 'config/dev.md',
    'information': 'about/information.md',
    'links': 'about/links.md',
    'faq': 'about/faq.md',
    'reference': 'about/reference.md',
    'aboutssp': 'about/ssp.md',
    'dev': 'dev/index.md',
    'dev-scriptlog': 'dev/scriptlog.md',
    'dev-palette': 'dev/palette.md',
    'dev-links': 'dev/links.md',
    'dev-faq': 'dev/faq.md',
}

HEADING_LINE = re.compile(r'^(#{1,6}) +(.+?)(?: +#+)? *$')
LINK_MD = re.compile(r'\[([^\]]*)\]\([^)]*\)')

BLOCK_START = re.compile(r'^\s*(?:[-*+]\s|\d+\.\s|\|)')
FENCE = re.compile(r'^\s*(```|~~~)')
INDEX_LINK = re.compile(r'(\]\((?:\.\./)*)INDEX\.md')
CODE_SPAN = re.compile(r'`[^`]*`')

# oldstyle/build.py と同じ Markdown の設定（見出しの id を日本語の原稿から数えるのに使う）
MD_EXTENSIONS = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists', 'pymdownx.superfences', 'toc']
MD_CONFIG = {'toc': {'slugify': slugify(case='lower')}}

# `_w` や `get_property` のように _ を含む名前は、コードスパンの外に書くと斜体になってしまう。
# 斜体は *var* で書く決まりにして、コードスパンの外の _名前_ を警告する（Python-Markdown と同じ判定）
UNDERSCORE_EM = re.compile(r'(?<!\w)_(?!_)(.+?)(?<!_)_(?!\w)')
NOT_EM = re.compile(r'`[^`]*`|<[^>]+>|https?://\S+|\]\([^)]*\)')
ESCAPED = re.compile(r'\\.')

# 用語をリンクにしない範囲: コードスパン、画像、リンク、<URL>、HTML タグ、URL
PROTECTED = re.compile(
    r'`+[^`\n]*`+'
    r'|!\[[^\]]*\]\([^)]*\)(?:\{[^}\n]*\})?'
    r'|\[[^\]]*\]\([^)]*\)'
    r'|<https?://[^>\s]+>'
    r'|</?[A-Za-z][^>\n]*>'
    r'|https?://\S+'
)
# 見出し・admonition の先頭行・表の区切り行には用語リンクを付けない
NO_LINK_LINE = re.compile(r'^\s*(?:#{1,6}\s|!!!\s|\|[\s:|-]+\|\s*$)')


def unescape_table_code(line):
    # GitHub では表のコードスパン内の | を \| と書く必要があるが、
    # Python-Markdown はコードスパン内の | を区切りとみなさず \ をそのまま表示してしまう
    return CODE_SPAN.sub(lambda m: m.group(0).replace('\\|', '|'), line)


def fix_markdown(text):
    out = []
    in_fence = False
    prev = ''
    for line in text.split('\n'):
        if FENCE.match(line):
            if not in_fence and prev.strip() != '':
                out.append('')
            in_fence = not in_fence
        elif not in_fence and BLOCK_START.match(line):
            # 直前が本文の行（空行・同種のブロック・見出し以外）なら空行を入れる
            if prev.strip() != '' and not BLOCK_START.match(prev) and not prev.startswith((' ', '\t')):
                out.append('')
            if line.lstrip().startswith('|'):
                line = unescape_table_code(line)
        out.append(line)
        prev = line
    return INDEX_LINK.sub(r'\1index.md', '\n'.join(out))


def check_underscore_em(text, path):
    in_fence = False
    for lineno, line in enumerate(text.split('\n'), 1):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            # \_ のようにエスケープした文字は区切りにならない
            for m in UNDERSCORE_EM.finditer(ESCAPED.sub('x', NOT_EM.sub(' ', line))):
                print(f'警告: {path}:{lineno}: {m.group(0)} が斜体になる。'
                      f'名前ならコードスパンで囲み、斜体なら *{m.group(1)}* と書く', file=sys.stderr)


def read_ja(rel):
    """日本語の原稿（構造の判定と、見出しの id の計算に使う。翻訳版でもここは日本語を見る）"""
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def read(rel):
    """本文に使う原稿。翻訳版（LANG 指定）では i18n/<LANG>/<rel> があればそちら、無ければ日本語"""
    if I18N:
        path = os.path.join(I18N, rel)
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as f:
                return f.read()
    return read_ja(rel)


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def heading_slug(title):
    # toc 拡張が見出しの id を作るのと同じ変換（リンク記法とコードの記号は除く）
    title = LINK_MD.sub(r'\1', title).replace('`', '')
    return slugify(case='lower')(title, '-')


def unique_id(base, used):
    # Python-Markdown の toc と同じ重複回避（_1, _2, ...）
    while base in used or not base:
        m = re.match(r'^(.*)_([0-9]+)$', base)
        base = f'{m.group(1)}_{int(m.group(2)) + 1}' if m else f'{base}_1'
    used.add(base)
    return base


def glossary_headings(text):
    """用語説明のページの H2 以下の見出し → [(用語, 見出しの id)]（ページ内の並び順）"""
    used = set()
    in_fence = False
    words = []
    for line in text.split('\n'):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            m = HEADING_LINE.match(line)
            if m:
                slug = unique_id(heading_slug(m.group(2)), used)
                if len(m.group(1)) >= 2:
                    words.append((m.group(2), slug))
    return words


def read_glossary():
    """用語説明のページの H2 以下の見出し → [(用語, 見出しの id)]（ページ内の並び順）。
    翻訳版では、用語は訳した見出し、id は日本語の見出しから（位置で対応させる）"""
    words = glossary_headings(read_ja(GLOSSARY_PAGE))
    if not words:
        sys.exit(f'エラー: {GLOSSARY_PAGE} に用語の見出しが無い')
    if LANG:
        local = glossary_headings(read(GLOSSARY_PAGE))
        if len(local) != len(words):
            sys.exit(f'エラー: {GLOSSARY_PAGE} の訳文の見出しの数が原文と合わない（原文 {len(words)}、訳文 {len(local)}）')
        words = [(t, slug) for (t, _), (_, slug) in zip(local, words)]
    return words


def word_pattern(word):
    """用語の正規表現。翻訳版の英語の用語は、語の途中（shell と shellscript など）に当たらないよう、語の切れ目を要求する"""
    pat = re.escape(word)
    if LANG:
        if word[:1].isascii() and word[:1].isalnum():
            pat = r'(?<![A-Za-z0-9])' + pat
        if word[-1:].isascii() and word[-1:].isalnum():
            pat += r'(?![A-Za-z0-9])'
    return pat


def glossary_linker(words):
    # 並びの先頭の用語を優先する（nwordlinks が用語の順に置き換えていくのと同じ）
    pattern = re.compile('|'.join(word_pattern(w) for w, _ in words), re.I)
    slug_of = {w.lower(): s for w, s in words}

    def link_plain(text, target):
        return pattern.sub(lambda m: f'[{m.group(0)}]({target}#{slug_of[m.group(0).lower()]})', text)

    def link_line(line, target):
        out = []
        pos = 0
        for m in PROTECTED.finditer(line):
            out.append(link_plain(line[pos:m.start()], target))
            out.append(m.group(0))
            pos = m.end()
        out.append(link_plain(line[pos:], target))
        return ''.join(out)

    def link_text(text, dst):
        target = posixpath.relpath(GLOSSARY_PAGE, posixpath.dirname(dst) or '.')
        out = []
        in_fence = False
        for line in text.split('\n'):
            if FENCE.match(line):
                in_fence = not in_fence
            elif not in_fence and not NO_LINK_LINE.match(line):
                line = link_line(line, target)
            out.append(line)
        return '\n'.join(out)

    return link_text


def toc_ids(text):
    """サイトの toc 拡張が原稿の見出しに付ける id を、文書順に返す"""
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG, output_format='html')
    md.convert(text)
    ids = []

    def walk(tokens):
        for t in tokens:
            ids.append(t['id'])
            walk(t['children'])
    walk(md.toc_tokens)
    return ids


def indented_headings(text):
    """コードブロックの外の見出し行を、字下げ（!!! の囲みの中など）も含めて (行番号, 字下げ, 深さ, 見出し) で返す。
    toc 拡張が拾う見出しは、この字下げ付きのものと、`#` の直後に空白の無い行（Python-Markdown は見出しとみなす）まで含む"""
    in_fence = False
    for i, line in enumerate(text.split('\n')):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            m = re.match(r'^(\s*)(#{1,6})(?:[ \t]+(.+?)|([^#\s].*?))\s*$', line)
            if m:
                yield i, m.group(1), len(m.group(2)), m.group(3) or m.group(4)


def pin_ids(text, rel):
    """翻訳版の見出しに、日本語の原稿から作った id を `{#id}` で固定する。
    訳した見出しの slug が変わっても、ほかのページからの `file.md#見出し` のリンクが切れないようにする"""
    if not I18N:
        return text
    ja = read_ja(rel)
    if text == ja:
        return text
    ids = toc_ids(ja)
    heads = list(indented_headings(text))
    if len(heads) != len(ids):
        sys.exit(f'エラー: {rel}: 訳文の見出しの数が原文と合わない（原文の toc {len(ids)}、訳文 {len(heads)}）')
    lines = text.split('\n')
    for (i, indent, level, title), ident in zip(heads, ids):
        if not re.search(r'\{[^}]*#', title):
            lines[i] = f'{indent}{"#" * level} {title} {{#{ident}}}'
    return '\n'.join(lines)


def render(src, text, dst, linker):
    """原稿 src（ROOT からの相対パス）の本文 text を、サイトのページ dst（OUT からの相対パス）用に直す"""
    check_underscore_em(text, src)
    text = fix_markdown(pin_ids(text, src))
    if src != GLOSSARY_PAGE:
        text = linker(text, dst)
    return text


RAW = os.path.join(ROOT, '_raw')
RAW_SKIP_DIRS = {'scripts', 'oldstyle', 'assets', 'node_modules', 'i18n'}   # i18n（翻訳）は日本語版の生の原稿に混ぜない
RAW_SKIP_FILES = {'README.md', 'CLAUDE.md'}
RAW_EXTRA = []   # .md 以外で、原稿から参照されていて一緒に置くファイル


def build_raw():
    """生の Markdown 原稿を、リポジトリと同じ相対パスで _raw/ に写す。
    _site_src/ は Markdown をページにするための写しなので、生の原稿は別に置く。ビルド後に _site へ重ねる"""
    if os.path.exists(RAW):
        shutil.rmtree(RAW)
    rels = list(RAW_EXTRA)
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(('.', '_')) and d not in RAW_SKIP_DIRS]
        for name in names:
            if name.endswith('.md') and not (base == ROOT and name in RAW_SKIP_FILES):
                rels.append(os.path.relpath(os.path.join(base, name), ROOT))
    for rel in rels:
        dst = os.path.join(RAW, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(os.path.join(ROOT, rel), dst)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    linker = glossary_linker(read_glossary())
    write('index.md', render('INDEX.md', read('INDEX.md'), 'index.md', linker))
    if not LANG:
        build_raw()
    for d in DIRS:
        for base, _, names in os.walk(os.path.join(ROOT, d)):
            for name in sorted(names):
                rel = os.path.relpath(os.path.join(base, name), ROOT).replace(os.sep, '/')
                if name.endswith('.md'):
                    write(rel, render(rel, read(rel), rel, linker))
    for stem, md in PAGES.items():
        if not os.path.exists(os.path.join(ROOT, md)):
            sys.exit(f'エラー: PAGES の {stem} の原稿 {md} が無い')
    # 原稿があるのに PAGES に無いページは、HTML が出ないので止める
    listed = set(PAGES.values())
    for d in DIRS:
        for base, _, names in os.walk(os.path.join(ROOT, d)):
            for name in names:
                rel = os.path.relpath(os.path.join(base, name), ROOT).replace(os.sep, '/')
                if name.endswith('.md') and rel not in listed:
                    sys.exit(f'エラー: {rel} が PAGES に無い（サイトの HTML のファイル名を決めて足す）')


if __name__ == '__main__':
    main()
