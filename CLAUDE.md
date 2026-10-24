このリポジトリは伺かのベースウェア「SSP」の使い方ヘルプ（Markdown）です。仕様書（さくらスクリプト・SHIORI Event など）は `../ukadoc-spec` にあります。
`../satori-docs` と `../yaya-docs` の構成を手本にしています。

このリポジトリが SSP ヘルプの正本です。旧 HTML 版（`ukatech/ukadoc` の `ssphelp/*.html`）の 1 ページを 1 ファイルに変換したもので、旧版の HTML と JS 検索（`lib/` `assdb.json` `about.css`）はもう使いません。内容を直すときは、このリポジトリの Markdown を直します。

## 構成

| 場所 | 内容 |
|---|---|
| `INDEX.md` | 「はじめに」（サイトのトップページになる） |
| `howto/` | 基本的な使い方 |
| `functions/` | 機能。カレンダー・SSPメッセンジャー・エクスプローラは、ページ兼セクションなので `calendar/` `sspim/` `explorer/` の下に `index.md` を置く |
| `config/` | 設定（本体設定の各タブ） |
| `about/` | 情報・リンク集・よくある質問・用語説明・SSPの基本情報（メニューではフォルダ名を出さずに並ぶ） |
| `dev/` | 開発者向けヘルプ |
| `assets/screenshots/<ページのパス>/` | そのページの画像（`howto/rclick.md` なら `assets/screenshots/howto/rclick/`）。別のページから使い回すときも、元のページのフォルダを指す |
| `assets/banners/` | リンク集のバナー |
| `materials/` | 画像の素材（元の `image/zz_sozai_folder` など、本文から使われていないもの）。サイトには含めない |
| `.nav.yml` | 左メニュー（フォルダごとにある）。メニューの名前はここで決める。ページの H1 は「設定：一般」のように分類を含むので、メニューの名前とは違う |

旧 HTML のファイル名との対応は、`howto-boot.html` → `howto/boot.md`、`config-ippan.html` → `config/ippan.md`、`calendar-schedule.html` → `functions/calendar/schedule.md` のように、接頭辞をフォルダにしたもの。例外は `config.html` `functions.html` `dev.html`（それぞれのフォルダの `index.md`）、`speech_recognition.html` `speech_synthesis.html`（ハイフンに直した）、`aboutssp.html`（`about/ssp.md`）。

## 書式

- UTF-8、LF。文体は「だ/である調」ではなく、旧版どおりの「です/ます調」のまま（旧 HTML 版の文体を引き継いでいる）。新しく書く部分も、そのページの文体に合わせる
- リンクは相対パスで `.md` まで書く（例: `[一般](../config/ippan.md)`、`[フォルダ設定](folder.md#フォルダ個別設定)`）。見出しへのアンカーは GitHub と同じく日本語の見出しをそのまま使う
- 画像は `![説明](../assets/screenshots/howto/use/0.png)` のように Markdown で書く。HTML の `<img>` はサイトでパスが書き換わらないので使わない。表示サイズを変えたいときだけ `![説明](パス){ width="400" }` と書く（GitHub では無視される）
- 改行は行末の `<br>`。段落の中の改行にだけ使い、段落を分けるときは空行にする
- 項目の一覧（設定名と説明など）は、`- **項目名**<br>` の次の行に説明を 2 スペース字下げで書く。説明が複数の段落になるときは、項目名の後に空行を入れて、段落を 2 スペース字下げで続ける。4 スペース字下げにすると、サイトの Markdown（`mdx_truly_sane_lists`）では入れ子のリストが崩れる
- 注意書き（旧 HTML の `Hint`）は `!!! tip "ヒント"`。本文は 4 スペース字下げ
- 操作（右クリックなど）は `**右クリック**`、`【サブ】` `【開発】` のような条件の印も太字で書く
- SSP のメニューの階層は `機能→音声認識` のように「→」で書く
- さくらスクリプトやファイルパス、ファイル名のうち `_` や `*` を含むものは、コードスパンで囲む（`\0` `\![bind]` `initial_install.nar` `SSP\temp\` など）。コードスパンの外の `_名前_` は斜体になってしまうので、`prepare_site.py` が警告する
- 表は GitHub の表の書式で書く。セルの中の改行は `<br>`、`|` は `\|`。表の中のコードスパンの `|` も GitHub 向けに `\|` と書く（`prepare_site.py` がサイト用に `|` へ戻す）
- 用語（ゴースト・シェル・バルーン・ネットワーク更新・ヘッドライン・SHIORI・MAKOTO・SERIKO・MAYUNA・SSTP・サーフィス・伺か・ベースウェア・SakuraScript・さくら側/うにゅう側）は、原稿ではリンクにせず素の文字で書く。サイトでは `prepare_site.py` が `about/reference.md` の見出しへのリンクにする（見出し・コード・既存のリンク・URL の中は除く。旧 SSP ヘルプの nwordlinks と同じ）

## ページを追加・改名したとき

- そのフォルダの `.nav.yml` に加える（メニューの名前もここで決める）。新しいフォルダを作ったら、そのフォルダの `.nav.yml` を作り、上の階層の `.nav.yml` から指す
- 新しいトップレベルのフォルダを作ったら、`scripts/prepare_site.py` の `DIRS` にも加える
- ページを改名・移動したら、`scripts/prepare_site.py` の `REDIRECTS` を直す。`REDIRECTS` は旧 SSP ヘルプのファイル名（`config-ippan` など）→ 今のページで、サイトのルートに `config-ippan.html` のような転送用の HTML を置く。SSP 本体は、本体設定のヘルプボタンや `--help ファイル名` で旧ファイル名のページを開くため、この対応が要る（旧ファイル名のページを増やすことはない）
- 用語を増やすときは、`about/reference.md` に H3 の見出しを足す。見出しの文字がそのままリンクにする言葉になる
- 設定・機能・開発者向けヘルプのページの H1 は「分類：ページ名」の形（例: 設定：一般）になっている。新しいページもそろえる

## 変換元の HTML について

旧 HTML 版は `../ukadoc/ssphelp/`（デプロイされた HTML）と `../ukadoc/ssphelp_src/`（ソース）にある。このリポジトリは `ssphelp/` を 1 対 1 で変換して作った。変換のときに次の整理をしている。

- 旧版の検索・翻訳リンク・パンくず・前後のページへのナビ・メニューは捨てた（サイトの機能に置き換わった）
- `config-haishin.html` と `config-ipmes.html` は、メニューにもどこからのリンクにも無く、それぞれ `config-streamingtool.html` と `config-im.html` に置き換わった古い残骸なので、変換していない
- `links.html` が参照していた `image/reikai.gif` は元からファイルが無かったので、画像を省いた
- 元のリンク切れ（`howto-rclick.htm` `conn`、`dev-scriptlog.html` の「スクリプトログ」が `#chapter2` を指していたもの）は直した
- `howto-rclick.html` の画像マップ（クリックで項目へ飛ぶ）は、画像の下に項目へのリンクの一覧を置く形に変えた
- 質問と答えの表（FAQ）は、質問を見出し（`### Q: ...`）、答えを本文にした。リンク集の表は、バナー・サイト・紹介の 3 列の表にした

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が Zensical（Material for MkDocs の後継。Material テーマ互換）でビルドし、https://ukatech.shillest.net/ukadoc-ssp/ に公開する。ビルドは `zensical build --strict` で、リンク切れ・アンカー切れがあると失敗する。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする。その際 `INDEX.md` は `index.md`（トップページ）になり、`INDEX.md` へのリンクも書き換えられる
- 設定は `mkdocs.yml` をそのまま読ませている。左メニューの章立てと名前は `.nav.yml`（mkdocs-awesome-nav）で決める
- GitHub では表示できても MkDocs（Python-Markdown）では崩れる書き方がある。段落の直後に空行なしで続くリストや表は `prepare_site.py` が空行を補うので、原稿は GitHub 向けのままでよい
- Zensical は 0.0.x の版を固定している（`requirements.txt`）。Material for MkDocs は 2026-11-05 にサポート終了のため移行した（MkDocs 2.0 はプラグインや Material テーマと互換性が無い）
- Zensical のテンプレートは MiniJinja で、`page.file` や `page.is_homepage` が無い。`overrides/main.html` はページの URL（`page.url`）で判定し、ページ別の OGP は `extra.ogp` に URL をキーにして書く
- 見た目は `theme.variant: classic` で従来のまま。ロゴとファビコンは `assets/logo.png`（鈴リボン）、ヘッダの色は `assets/extra.css`（リボンのピンクを暗くした色）

手元で確認するとき（`_site_src/` と `_site/` は `.gitignore` 済み）:

```sh
pip install -r requirements.txt
python scripts/prepare_site.py
zensical build --strict    # 警告（リンク切れ・アンカー切れ）が出ないことを確認する
zensical serve             # http://127.0.0.1:8000/ukadoc-ssp/ でプレビュー
```
