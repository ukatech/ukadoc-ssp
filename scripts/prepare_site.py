r"""GitHub Pages 用に原稿を _site_src/ へ写す。

- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える
- GitHub では表示できるが Python-Markdown では崩れる書き方を直す
  （段落の直後に空行なしで続くリスト・表の前に空行を入れる）
- 表の中のコードスパンの `\|` を `|` に戻す（GitHub 向けの書き方をサイト向けに直す）
- `_名前_` のように _ で挟んだ書き方（斜体になってしまう）を警告する
- 用語説明（about/reference.md）の見出しにある用語を、本文のほかのページから用語説明へのリンクにする
  （旧 SSP ヘルプの nwordlinks と同じ。見出し・コード・既存のリンク・URL の中はリンクにしない）
- 旧 SSP ヘルプのファイル名（config-ippan.html など）のページに、今のページへ転送する HTML を置く（REDIRECTS）
原稿そのものは書き換えない。materials/（画像の素材）はサイトに含めない。
"""
import json
import os
import posixpath
import re
import shutil
import sys

from pymdownx.slugs import slugify

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, '_site_src')
# そのまま 1 ファイル 1 ページで写すディレクトリ（入れ子のディレクトリも写す）
DIRS = ['howto', 'functions', 'config', 'dev', 'about']
# 用語説明のページ。この見出しの用語が、ほかのページの本文でリンクになる
GLOSSARY_PAGE = 'about/reference.md'
SITE_URL = 'https://ukatech.github.io/ukadoc-ssp/'
# 旧 SSP ヘルプ（HTML 版）のファイル名 → 今のページ（サイトのルートに旧ファイル名の .html を置いて転送する）。
# SSP は本体設定のヘルプボタンや `--help ファイル名` で、旧ファイル名のページを開く。index.html はサイトのトップそのもの
REDIRECTS = {
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


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


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


def read_glossary():
    """用語説明のページの H2 以下の見出し → [(用語, 見出しの id)]（ページ内の並び順）"""
    used = set()
    in_fence = False
    words = []
    for line in read(GLOSSARY_PAGE).split('\n'):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            m = HEADING_LINE.match(line)
            if m:
                slug = unique_id(heading_slug(m.group(2)), used)
                if len(m.group(1)) >= 2:
                    words.append((m.group(2), slug))
    if not words:
        sys.exit(f'エラー: {GLOSSARY_PAGE} に用語の見出しが無い')
    return words


def glossary_linker(words):
    # 並びの先頭の用語を優先する（nwordlinks が用語の順に置き換えていくのと同じ）
    pattern = re.compile('|'.join(re.escape(w) for w, _ in words), re.I)
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


REDIRECT_HTML = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>ページが移動しました</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex">
<script>location.replace({target_js});</script>
</head>
<body>
<p>このページは移動しました。自動で移動しない場合は <a href="{target}">{target}</a> を開いてください。</p>
</body>
</html>
"""


def write_redirect(old_stem, new_md):
    """旧ファイル名のページ（サイトのルートの <旧>.html）に、新しいページへ転送する HTML を置く"""
    new_dir = new_md[:-len('.md')]
    if posixpath.basename(new_dir) == 'index':
        # index.md のページの URL は <ディレクトリ>/
        new_dir = posixpath.dirname(new_dir)
    target = new_dir + '/'
    write(f'{old_stem}.html', REDIRECT_HTML.format(url=SITE_URL + target, target=target, target_js=json.dumps(target)))


def render(src, text, dst, linker):
    """原稿 src（ROOT からの相対パス）の本文 text を、サイトのページ dst（OUT からの相対パス）用に直す"""
    check_underscore_em(text, src)
    text = fix_markdown(text)
    if src != GLOSSARY_PAGE:
        text = linker(text, dst)
    return text


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    linker = glossary_linker(read_glossary())
    write('index.md', render('INDEX.md', read('INDEX.md'), 'index.md', linker))
    shutil.copy(os.path.join(ROOT, '.nav.yml'), os.path.join(OUT, '.nav.yml'))
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    for d in DIRS:
        for base, _, names in os.walk(os.path.join(ROOT, d)):
            for name in sorted(names):
                rel = os.path.relpath(os.path.join(base, name), ROOT).replace(os.sep, '/')
                if name.endswith('.md'):
                    write(rel, render(rel, read(rel), rel, linker))
                elif name == '.nav.yml':
                    write(rel, read(rel))
    for old, new in REDIRECTS.items():
        if not os.path.exists(os.path.join(ROOT, new)):
            sys.exit(f'エラー: REDIRECTS の {old} の行き先 {new} が無い')
        write_redirect(old, new)


if __name__ == '__main__':
    main()
