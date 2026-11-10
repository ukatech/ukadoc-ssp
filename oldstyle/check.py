r"""出力（_site/）の内部リンク・アンカー・画像・スクリプト・CSS の切れを調べる（zensical build --strict の代わり）。

    python oldstyle/check.py [--lang=<コード>]    （--lang を付けると _site/<コード>/ の翻訳版を調べる）

エラーは出力 HTML のファイル名で出る。見つかれば終了コード 1。外部リンク（http: など）は見ない。
"""
import os
import posixpath
import re
import sys
from urllib.parse import unquote

import lxml.html

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
LANG = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--lang=')), None)
SITE = os.path.join(ROOT, '_site', *([LANG] if LANG else []))
EXTERNAL = re.compile(r'^(?:[A-Za-z][A-Za-z0-9+.-]*:|//)')


def main():
    if not os.path.isdir(SITE):
        sys.exit(f'{os.path.relpath(SITE, ROOT)}/ が無い。先に python oldstyle/build.py を実行する')
    pages = {}
    for base, _, names in os.walk(SITE):
        for name in names:
            if name.endswith('.html'):
                rel = os.path.relpath(os.path.join(base, name), SITE).replace(os.sep, '/')
                tree = lxml.html.parse(os.path.join(base, name)).getroot()
                ids = {e.get('id') for e in tree.iter() if isinstance(e.tag, str) and e.get('id')}
                ids |= {e.get('name') for e in tree.iter('a') if e.get('name')}
                pages[rel] = (tree, ids)
    errors = 0
    for rel, (tree, _) in sorted(pages.items()):
        refs = []
        for e in tree.iter():
            if not isinstance(e.tag, str):
                continue
            if e.tag in ('a', 'link') and e.get('href') is not None:
                refs.append((e.tag, e.get('href')))
            elif e.tag in ('img', 'script', 'source') and e.get('src') is not None:
                refs.append((e.tag, e.get('src')))
        for tag, ref in refs:
            if not ref or EXTERNAL.match(ref):
                continue
            path, _, frag = ref.partition('#')
            if path:
                target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), unquote(path)))
            else:
                target = rel
            if target.endswith('/'):
                target += 'index.html'
            full = os.path.join(SITE, target)
            if os.path.isdir(full):
                target = posixpath.join(target, 'index.html')
                full = os.path.join(SITE, target)
            if not os.path.exists(full):
                print(f'{rel}: <{tag}> {ref} の行き先が無い')
                errors += 1
            elif frag and target in pages and unquote(frag) not in pages[target][1]:
                print(f'{rel}: {ref} のアンカーが無い')
                errors += 1
    print(f'{len(pages)} ページを調べた。エラー {errors} 件')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
