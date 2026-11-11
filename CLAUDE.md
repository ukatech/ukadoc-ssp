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
| `.nav.yml` | 左メニュー・前後のページ・パンくずリストの元（フォルダごとにある）。メニューの名前と並びはここで決める。ページの H1 は「設定：一般」のように分類を含むので、メニューの名前とは違う |
| `oldstyle/` | サイトのビルド（`build.py` `check.py`、旧版の CSS・画像・JS の `static/`、HTML の枠 `templates/`）。原稿ではなく、ビルドの部品 |
| `scripts/prepare_site.py` | 原稿を `_site_src/` に写して整える（ビルドの前処理）。ページ名の表 `PAGES` もここ |
| `scripts/translate.py` | 翻訳版を作るスクリプト（LLM を呼ぶ。「翻訳」を参照） |
| `i18n/<言語>/` | 翻訳版（`en` `zh-Hant` `zh`）。LLM が `scripts/translate.py` で作る機械翻訳で、原稿と同じ相対パス（`.nav.yml` も含む）。**原稿の正本は日本語**で、ここは手で書かない。`i18n/glossary.tsv` は訳語の用語集 |

旧 HTML のファイル名との対応は、`howto-boot.html` → `howto/boot.md`、`config-ippan.html` → `config/ippan.md`、`calendar-schedule.html` → `functions/calendar/schedule.md` のように、接頭辞をフォルダにしたもの。例外は `config.html` `functions.html` `dev.html`（それぞれのフォルダの `index.md`）、`speech_recognition.html` `speech_synthesis.html`（ハイフンに直した）、`aboutssp.html`（`about/ssp.md`）。

## 書式

- UTF-8、LF。文体は「だ/である調」ではなく、旧版どおりの「です/ます調」のまま（旧 HTML 版の文体を引き継いでいる）。新しく書く部分も、そのページの文体に合わせる
- リンクは相対パスで `.md` まで書く（例: `[一般](../config/ippan.md)`、`[フォルダ設定](folder.md#フォルダ個別設定)`）。見出しへのアンカーは GitHub と同じく日本語の見出しをそのまま使う
- 画像は `![説明](../assets/screenshots/howto/use/0.png)` のように Markdown で書く。HTML の `<img>` は使わず、Markdown で書く。表示サイズを変えたいときだけ `![説明](パス){ width="400" }` と書く（GitHub では無視される）
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
- ページを足す・改名・移動したら、`scripts/prepare_site.py` の `PAGES`（旧 SSP ヘルプのファイル名 `config-ippan` など → 原稿）を直す。サイトの HTML は、この名前の `config-ippan.html` として出る。SSP 本体は、本体設定のヘルプボタンや `--help ファイル名` で旧ファイル名のページを開くため、既存の名前は変えられない。原稿があるのに `PAGES` か `.nav.yml` に無いと、ビルドが止まる。新しいページの名前は、旧版にならって `分類-名前`（`config-ippan` など）にする
- 用語を増やすときは、`about/reference.md` に H3 の見出しを足す。見出しの文字がそのままリンクにする言葉になる
- 設定・機能・開発者向けヘルプのページの H1 は「分類：ページ名」の形（例: 設定：一般）になっている。新しいページもそろえる
- 翻訳を回し直す（`python scripts/translate.py`。下の「翻訳」を参照）。新しいページは、回し直すまで翻訳版では日本語のまま出る

## 変換元の HTML について

旧 HTML 版は `../ukadoc-old/ssphelp/`（デプロイされた HTML）と `../ukadoc-old/ssphelp_src/`（ソース）にある。このリポジトリは `ssphelp/` を 1 対 1 で変換して作った。変換のときに次の整理をしている。

- 旧版の検索・翻訳リンク・パンくず・前後のページへのナビ・メニューは、原稿には持ち込んでいない（サイトのビルド `oldstyle/` が `.nav.yml` から作る）
- `config-haishin.html` と `config-ipmes.html` は、メニューにもどこからのリンクにも無く、それぞれ `config-streamingtool.html` と `config-im.html` に置き換わった古い残骸なので、変換していない
- `links.html` が参照していた `image/reikai.gif` は元からファイルが無かったので、画像を省いた
- 元のリンク切れ（`howto-rclick.htm` `conn`、`dev-scriptlog.html` の「スクリプトログ」が `#chapter2` を指していたもの）は直した
- `howto-rclick.html` の画像マップ（クリックで項目へ飛ぶ）は、画像の下に項目へのリンクの一覧を置く形に変えた
- 質問と答えの表（FAQ）は、質問を見出し（`### Q: ...`）、答えを本文にした。リンク集の表は、バナー・サイト・紹介の 3 列の表にした

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が `oldstyle/build.py` と `oldstyle/check.py` を走らせ、https://ukatech.shillest.net/ukadoc-ssp/ に公開する。以前の Zensical 版は `old-zensical` ブランチに残してある。ビルドの仕組みは [`oldstyle/README.md`](oldstyle/README.md)。原稿を書くうえで知っておくことは次のとおり。

- サイトの見た目と構造は、旧 SSP ヘルプ（`../ukadoc-old/ssphelp/`）を模している: 左に目次と検索（`#menu`）、右に上からパンくずリスト（`#breadcrumb`）・本文（`#contents`）・前後のページ（`#navigation`）。HTML は HTML5 で、JavaScript は検索（`search.js`）と言語切替（`lang.js`）と、狭い画面の目次（`menu.js`）だけ。幅が 800px 以下では、左の目次を畳み、検索欄の左端のボタン（ハンバーガー）で開く引き出しにする（JavaScript が動かなければ、目次は本文の下に出る）
- 出力のファイル名は旧 SSP ヘルプと同じ（`howto-boot.html` `config-ippan.html` など。名前は `scripts/prepare_site.py` の `PAGES` で決める）。Zensical 版の URL（`howto/boot/` など）には、旧名のページへ転送する HTML を置いている
- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする。その際 `INDEX.md` は `index.md`（トップページ）になり、`INDEX.md` へのリンクも書き換えられる。原稿内のリンク（`../config/folder.md#見出し` など）は、ビルドが出力の名前（`config-folder.html#見出し`）に書き換える
- 章立て（左メニュー・パンくず・前後のページ）は `.nav.yml`。メニューの階層がそのまま前後のページの順（深さ優先）になる。前後のページの表示は、3 階層目のページだけ「カレンダー:スケジュール編集」のように親の名前が前に付く（旧版と同じ）
- `llms.txt`（AI エージェント向けの探し方の案内。`INDEX.md` と各ディレクトリの入口だけを書く）はサイトのルートに置かれる。ページごとの一覧は載せないので、ページを足しても直さなくてよい。ディレクトリを足したときは「構成」に 1 行足す
- 生の Markdown 原稿（`README.md` と `CLAUDE.md` 以外の `.md`）は、リポジトリと同じパスでサイトにも置かれる（`prepare_site.py` が `_raw/` に写し、ビルドが出力に重ねる）。`llms.txt` や `INDEX.md` の相対リンクは、このおかげでサイト上でも辿れる
- オフライン用のアーカイブ `ukadoc-ssp-offline.zip` を、ビルドが出力のルートに作る（サイト一式を `ukadoc-ssp/` の下にまとめたもの。`INDEX.md` からリンクしている）。公開 URL を変えたら `INDEX.md` のリンクも直す
- Markdown の拡張は `tables` `admonition` `attr_list` `md_in_html` `mdx_truly_sane_lists` `pymdownx.superfences` `toc`。見出しのアンカーは GitHub と同じく日本語のまま（`pymdownx.slugs.slugify(case='lower')`）で、`prepare_site.py` の用語リンクと同じ変換
- 旧版の部品への対応は、ビルド（`oldstyle/build.py`）と `oldstyle/static/oldstyle.css` が受け持つ: `!!! tip "ヒント"` → `div.Hint`、`**【開発】**` のような 【 で始まる太字 → 緑の `strong.Condition`、`### Q: ...`（と `**A1:**` の段落）→ 旧版の質問と答えの枠 `div.QnA`、1 列目が「バナー」の表 → リンク集の表 `table.Links`
- GitHub では表示できても Python-Markdown では崩れる書き方がある。段落の直後に空行なしで続くリストや表は `prepare_site.py` が空行を補うので、原稿は GitHub 向けのままでよい
- ヘッダ（ロゴ・OGP・ダークモード）は無い。旧版にならって、左上の検索欄と、その右横の翻訳ボタンだけ
- 検索は、ビルド時に作る `search-index.js`（節ごとの本文）を、`search.js` が空白区切りの語の AND で部分一致検索する。旧 SSP ヘルプの lunr による検索の代わり。左上の検索欄に打ち込むとドロップダウンが出て、Enter で `search.html?q=` に全件が並ぶ
- 言語切替は `oldstyle/static/lang.js`（検索欄の右横。見た目は `oldstyle.css` の `.ukadoc-translate`）。日本語版（ルート）の下に、翻訳版（`en/` `zh-Hant/` `zh/`）が同じファイル名で出る。切替先は、頁の `<meta name="ukadoc-langs">`（ビルドが `i18n/` にある言語を書く）で決まる。翻訳版の頁の本文の頭には、機械翻訳である旨と日本語の原文へのリンクの帯を出す。翻訳版が 1 つも無ければ、ボタンは出ない。ブラウザ組み込みの Translator API を使う旧 `translate.js` は、ファイルだけ残してあり、読み込まない

手元で確認するとき（`_site_src/` `_site/` `_raw/` は `.gitignore` 済み）:

```sh
pip install -r requirements.txt
python oldstyle/build.py    # prepare_site.py で _site_src/ を作り、_site/ に出力する。i18n/ のある言語は、続けて _site/<言語>/ に出す（--no-prepare で作り直さない、--no-langs で日本語版だけ、--lang=en でその言語だけ）
python oldstyle/check.py    # 出力のリンク切れ・アンカー切れ・画像の切れを調べる（エラーが 0 件であること。翻訳版は --lang=en など）
python -m http.server -d _site    # http://127.0.0.1:8000/ でプレビュー（file:// でも見られる）
```

## 翻訳

英語・繁体字中国語・簡体字中国語の版は、日本語の原稿を `scripts/translate.py` で LLM に訳させて `i18n/<言語>/` に置いたもの。サイトでは日本語版の下（`/en/` `/zh-Hant/` `/zh/`）に出る。原稿を書く側が知っておくこと:

- **日本語の原稿を直したら、翻訳を回し直す**: `python scripts/translate.py`。原稿のハッシュ（`i18n/<言語>/.manifest.json`）が変わったファイルだけを、ファイルごと丸ごと訳し直す。結果を `i18n/` ごとコミットする。API の設定はリポジトリ直下の `.env`（`TRANSLATE_API_KEY` `TRANSLATE_BASE_URL`。`.gitignore` 済み）。まず `--dry-run` で量と費用の目安を見られる（全ページ・全言語で 1 ドル未満）
- 訳すのは、原稿（`.md`）と、章立て（`.nav.yml`。メニュー・パンくず・前後のページの名前になる題だけ）。画面の枠の文言（検索欄・パンくずの名前など）は、訳さずに `oldstyle/build.py` の `UI` に言語ごとの語を書いてある
- 訳文は構造を自動で検査する（見出しの数とレベル、リンク先、コードブロック、表、箇条書き、HTML のタグ、**構造の判定に使う日本語の語**）。通らないファイルは置かず、そのページは日本語のまま出る。**訳文に残す日本語の語**: `!!! tip "ヒント"` のタイトル、`【開発】`、表の見出しの「バナー」、`### Q:` の `Q:` と `**A1:**` の印。表示のときだけ `build.py` の `UI` で言語ごとの語に置き換わる（`【開発】` → `[Dev]` など）。コードブロックの中は訳さない
- 見出しの id は日本語の原稿から作るので、訳した見出しでもリンクの `#見出し` は切れない。リンク先の見出しを日本語側で改名したら、翻訳も回し直す
- 用語（ゴースト・シェルなど）の自動リンクは、翻訳版では、訳した `about/reference.md` の見出しの語を、同じ位置の日本語の見出しの id へのリンクにする
- 訳語がぶれる語は `i18n/glossary.tsv`（`ja` `en` `zh-Hant` `zh` の列。タブ区切り）に足し、`python scripts/translate.py --force` で訳し直す。SSP の画面の文言は、`../ssp-i18n`（SSP の言語パック）の同じ項目の訳に合わせている。検査器を直したときは `--recheck` で、書き出し済みの訳文に今の検査を当て直せる
- `i18n/` の訳文を手で直してもよいが、日本語の原稿が変わると次の翻訳で上書きされる。恒久的に直したいことは、用語集か `translate.py` のプロンプトに書く（日本語以外が原文のファイルの、その言語の版は例外で、`i18n/<言語>/` が正本。次の項を参照）
- **日本語以外が原文のファイル**: いまは無い（登録簿 `i18n/originals.json` も置いていない）。英語などで書かれた原文の項目を足すときは、原文を `i18n/<言語>/<原稿と同じパス>` に人の手で置き、`i18n/originals.json` に `{"パス": {"lang": "en"}}` の形で原文の言語（`en` `zh-Hant` `zh`）つきで登録する。日本語の原稿は、その原文から訳して書く
  - 原文の言語の版は**機械翻訳しない・上書きしない**（`translate.py` が飛ばす。`--force` でも同じ）。原文の言い回しがそのままその言語の版になる。見出しの数・順は日本語の原稿と同じにし、他のページ・見出しへのリンクの `#断片` は日本語の見出しにする（翻訳版の見出しの id は日本語の原稿から作る）
  - ほかの言語は、日本語の原稿を訳す（構造の検査の基準）が、同じリクエストに原文を参照として添え、意味・語調・用語は原文から取らせる。原文を直しても訳し直しの対象になる
  - 日本語の原稿か原文を直したら、`translate.py` が警告を出す。もう一方を合わせて直し、`python scripts/translate.py --sync-originals` で「突き合わせ済み」と記録する。そのあと通常どおり `python scripts/translate.py` を回す
  - サイトでは、原文の言語の版でページの頭の見出しに「原文」の印（class `orig-lang`。`scripts/prepare_site.py` が付け、`oldstyle/static/oldstyle.css` が `html[lang]` ごとに字を出す）が付き、ページ頭の機械翻訳の帯にも「印の付いた項目は原文」の一文が足される（`oldstyle/static/lang.js`）。登録して `python oldstyle/build.py --lang=en` で確かめられる（試すだけなら、登録は戻すこと）
- 翻訳版のサイトの検査: `python oldstyle/check.py --lang=en`（画像・`llms.txt`・生の原稿は日本語版のものを共有し、翻訳版の頁は 1 つ上から参照する）
