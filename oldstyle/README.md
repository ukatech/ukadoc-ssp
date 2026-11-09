# oldstyle: 旧 SSP ヘルプの見た目を模した静的サイト

旧 SSP ヘルプ（`ukatech/ukadoc` の `ssphelp/*.html`。手元では `../ukadoc-old/ssphelp/`）の見た目と構造を、このリポジトリの Markdown 原稿から再現する自前のビルド。Zensical・MkDocs は使わない（以前の Zensical 版は `old-zensical` ブランチ）。見た目だけを真似て、HTML は HTML5（旧版の XHTML 1.0・IE 向けの補い・Google 翻訳・jQuery・lunr は使わない）。

```sh
python oldstyle/build.py              # scripts/prepare_site.py で _site_src/ を作り、_site/ に出力する
python oldstyle/build.py --no-prepare # _site_src/ を作り直さない
python oldstyle/check.py              # _site/ の内部リンク（ファイル・アンカー・画像・スクリプト）を調べる
python -m http.server -d _site        # プレビュー（file:// でも動く）
```

必要なもの: `pip install -r requirements.txt`（`Markdown` `pymdown-extensions` `mdx_truly_sane_lists` `lxml` `PyYAML`）。

## 作り

| 場所 | 内容 |
|---|---|
| `build.py` | `.nav.yml` から章立てを読み、原稿 → HTML → 旧版の構造に組む。リンク・画像のパスは出力の名前に書き換え、行き先が無ければエラーで止まる |
| `static/` | 旧版の `about.css`（そのまま）と背景画像 `image/background.png`、補いの `oldstyle.css`、`search.js`（サイト内検索）、`translate.js`（翻訳ボタン）。ビルドで出力のルートにそのまま置く |
| `templates/page.html` | 1 ページの HTML5 の枠（`$title` などを `string.Template` で埋める） |
| `check.py` | 出力のリンク・アンカー・画像の検査（旧 `zensical build --strict` の代わり。CI でも走る） |
| `../scripts/prepare_site.py` | 原稿を `_site_src/` に写して整える（用語リンク・空行補い・`_raw/`）。ページ名の表 `PAGES` もここ |

## ページの構造（旧版と同じ ID）

```
body > #page
  nav#menu      … #search（検索欄 + 翻訳ボタン）、#index（目次の入れ子の ul）
  div#main      … nav#breadcrumb、main#contents、nav#navigation（前 / 次）
```

- 出力のファイル名は旧版と同じ（`howto-boot.html` など。`PAGES`）。Zensical 版の URL（`howto/boot/`）には転送用の HTML を置く
- 旧版は `float` で左右に分けていたが、ここでは `flex`。幅が 800px 以下では、検索欄 → 本文 → 目次の縦並びになる
- 旧版の部品への対応: `!!! tip "ヒント"` → `div.Hint`、【 で始まる太字 → `strong.Condition`、`### Q:` → `div.QnA`（`h3.Q` と `div.A`）、1 列目が「バナー」の表 → `table.Links`
- オフライン用のアーカイブ `ukadoc-ssp-offline.zip` を、`build.py` が `_site/` のルートに作る（`build_offline_zip()`）。サイト一式（HTML・CSS・JS・画像・`llms.txt`・生の Markdown 原稿）を `ukadoc-ssp/` の下にまとめたもので、zip 自身は含めない。`INDEX.md` の冒頭からリンクしている（絶対 URL）
- 前後のページは `.nav.yml` の深さ優先の順。3 階層目のページは「親:題」の表示（旧版と同じ）
