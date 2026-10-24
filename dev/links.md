# 開発者向けヘルプ：開発リンク集

伺か/SSP関連コンテンツの製作に役立つ情報・プログラム・素材・ツールなどのリンク集です。

なお、冗長を避けここに再び載せることはしませんが、コンテンツの公開および公開後の宣伝などには、もう一つの[リンク集](../about/links.md)にあるサイトを活用してユーザの目に触れる工夫をすると、みんなで幸せになれます。

- [仕様書・リファレンス](#仕様書リファレンス)
- [SHIORI](#shiori)
- [パーツ・プログラム・ツール配布元](#素材プログラムツール配布元)
- [その他](#その他)

## 仕様書・リファレンス

| バナー | サイト | 紹介 |
|---|---|---|
| [![UKAODC](../assets/banners/ukadoc_banner1.png)](http://ssp.shillest.net/ukadoc/manual/index.html) | **UKADOC**<br><http://ssp.shillest.net/ukadoc/manual/index.html> | SSPの公式仕様文章集です。<br>Sakura ScriptやSHIORI Eventのリファレンスがあります。 |
| [![SDN on the web.](../assets/banners/sdn.png)](http://www.boreas.dti.ne.jp/~sdn/saori.html) | **SAORI/1.0（SDN on the web内）**<br><http://www.boreas.dti.ne.jp/~sdn/saori.html> | SHIORIの機能拡張モジュールである「SAORI」の仕様書です。<br>内容は技術者・SAORI開発者向けなので、ゴースト側からの実際のSAORIの利用については各SAORIの説明を参照してください。<br>SAORI探しには[後述](#素材プログラムツール配布元)の「さおりん」が役立つでしょう。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.ooyashima.net/db/) | **大八州.NET**<br><http://www.ooyashima.net/db/> | 伺か関係の非公式仕様集です。<br>非公式とはいえかなり充実した情報がわかり易く揃っているので、他の資料と合わせて読む機会もあるでしょう。 |
| [![SAKURA SCRIPT WIKI](../assets/banners/sakurascriptwiki.png)](http://www36.atwiki.jp/sakurascript/pages/1.html) | **さくらスクリプトwiki**<br><http://www36.atwiki.jp/SakuraScript/pages/1.html> | さくらスクリプトに関するまとめwikiです。<br>用例などの面でukadocより踏み込んだ解説も多々あるので、併せて活用しましょう。 |
| [![UKATEC](../assets/banners/ukatec.png)](http://wikiwiki.jp/ukatec/) | **UKATEC**<br><http://wikiwiki.jp/ukatec/> | 伺か関連コンテンツの制作情報をまとめたwikiです。<br>ゴーストに限らず、シェルやバルーン、その他色々なものに関する制作者向けの情報へのリンク・記事を集積しています。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/) | **駄でべろぱの小ネタwiki**<br><http://emily.shillest.net/specwiki/> | 通称駄でべ。不特定多数の開発・技術者が自由に色んなメモをつづる場所です。<br>現在進行形のメモと、過去の（半ば放棄された）資料や議論の痕跡とが混在しているので、書かれた時期に気をつけて読んでいってください。 |
| [![伺か](../assets/banners/usadasakura.png)](http://usada.sakura.vg/) | **うさださくら**<br><http://usada.sakura.vg/> | 本家伺かの配布サイトです。<br>更新は止まって久しいですが、開発中に旧い仕様を調べる必要が出てきた場合などには立ち返りましょう。 |

## SHIORI

ここでは独断と偏見で（2014年現在開発が継続している・利用シェアが高いなどの観点は一応ありますが）SHIORIをいくつか取り上げています。<br>
これ以外にも、特に汎用言語系のSHIORIは色々ありますので、興味があれば探してみてください。

### 里々

里々（さとり）は現在最も多くの利用者をもつSHIORIです。<br>
全角記号による、平易にトークをかけるように工夫された辞書記法や、難しい処理部はすっかり勝手にやってくれる気の利いた設計が、プログラミング未経験者や、何よりもランダムトークを肝にしたゴーストを作りたい層などを中心に支持されています。<br>
また有志によるドキュメントが整っており、有用なゴースト製作ツールやテンプレートゴーストも開発されていて、環境面で恵まれたSHIORIといえます。

一方で、内部的・自動的に処理が行われてしまう結果、その不透明性がSHIORIやSSP本来の機能や役割の理解を妨げ、応用的な開発時に初心者がつまづきやすいところがあります。<br>
加えて、高速に複雑な処理を行うのが苦手である事、構文の記号と単なる文字列の区別がつかないことが原因で「関数の引数区切り字問題」といった固有の弱点を諸々抱えている事などもあり、総じて「難しいこと・ややこしいこと」には向かない面があります。

プログラミング経験がないような初心者には真っ先に勧められるSHIORIですが、ミニゲームを備えたゴーストを作りたいなど、ゴーストの目指すところによっては、多少最初のハードルが高くともYAYAや華和梨など他のSHIORIの利用も考慮に入れておくとよいでしょう。

| バナー | サイト | 紹介 |
|---|---|---|
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/satoriya.xhtml) | **里々／整備班カスタム（整備班　内）**<br><http://ms.shillest.net/satoriya.xhtml> | 現在里々を整備・配布しているところです。本家による開発終了後、メンテナンスを引き継いでいます。 |
| [![里々wiki](../assets/banners/satorib.png)](http://soliton.sub.jp/satori/) | **里々wiki**<br><http://soliton.sub.jp/satori/> | 里々に関する解説やTIPSを扱うwikiです。非公式ですが、実質的に里々のマニュアル的な役割を果たしています。<br>他のSHIORIのwikiなどと比べても充実した情報量を持っており、SHIORI選びにおいて初心者に里々を勧めやすい根拠の一つです。 |
| [![さとりすと](../assets/banners/satolist.png)](http://wikiwiki.jp/satolist/) | **さとりすとwiki**<br><http://wikiwiki.jp/satolist/> | 里々ゴーストエディタ「さとりすと」のオンラインマニュアルです。<br>単なるテキストエディタではなく、開発に役立つ諸々のツールを内蔵した、いわば統合開発環境に近いものとなっています。<br>新たに里々でゴーストを作りはじめる場合、とりあえず導入してみてはいかがでしょうか。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.geocities.jp/poskoma/) | **電気で動くうにゅう・廃屋の夏**<br><http://www.geocities.jp/poskoma/> | 本家の里々公開・配布場所です。 |

### 文/YAYA

文（あや）はC言語風の記法を持つSHIORIです。<br>
文の開発終了後、基本的な文法や機能を受け継ぎつつ、非公式に開発が継続されたものがYAYA（やや）です。

分岐・ループの基本的な制御構造を持ち、里々と比べればプログラミング経験者が直感的に扱いやすいSHIORIといえるでしょう。<br>
また組み込み関数としてテキスト操作・ファイル操作や基本的な数学的計算、正規表現を用いた文字列処理などの機能を備えており、ある程度複雑な機能を実装したいゴーストでの使用に向きます。

しかしながら、配列は（擬似的な方法はありますが）一次元のもので、連想配列は未実装です。<br>
クラスなどの仕組みもないので、オブジェクト指向での記述は出来ず、汎用言語系のSHIORIほどの強力さ・柔軟さはありません。<br>
加えてC言語風とはいっても、様々の独特のクセがあるので慣れが要る部分があるでしょう。

なお特徴として、文・YAYA自体は単なる汎用言語dllとして設計されていることが挙げられます。<br>
SHIORI等の通信規格への対応部分や基本的なゴーストとしての機能の提供部分は、全て辞書側に委ねられています（テンプレートゴーストに同梱）。<br>
これによって文・YAYAは、システム辞書をさしかえる事でSHIORIのみならず、SAORIやPLUGINなどdllをコアとする他の伺かサブシステムとしても活躍しています。

| バナー | サイト | 紹介 |
|---|---|---|
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/yaya.xhtml) | **YAYA/Yet Another AYA（整備班　内）**<br><http://ms.shillest.net/yaya.xhtml> | 文の非公式後継版にあたるYAYAを整備・配布しているところです。<br>現在もサポートが続いていますし、文からいくらか機能の追加もあるので、新たに使い始める場合はこちらの利用をおすすめします。 |
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/yayame.xhtml) | **はろーYAYAわーるど（整備班　内）**<br><http://ms.shillest.net/yayame.xhtml> | YAYAのテンプレートゴーストです。<br>YAYAをSHIORIとして持ちいる場合に必須のシステム辞書および、追加機能を提供するテンプレート辞書を内容に含んでいるので、YAYAでゴーストを作りはじめる場合はまずダウンロードしてみてください。 |
| [![文屋](../assets/banners/ayaya.png)](http://emily.shillest.net/ayaya/) | **文屋**<br><http://emily.shillest.net/ayaya/> | 文/YAYA関連情報のまとめwikiです。<br>YAYA開発者も積極的に編集するなど、実質的なリファレンスマニュアルの役割も果たしています。<br>また、YAYAをSAORI/MAKOTO/PLUGINとして扱うためのシステム辞書もここで配布しています。 |
| [![no banner](../assets/banners/nobanner.png)](http://umeici.onjn.jp/) | **umeici.onjn.jp**<br><http://umeici.onjn.jp/> | 本家文の配布元です。<br>また、文用デバッガ「玉」も配布しています。YAYAでも動くようです。 |

### 華和梨

華和梨（かわり）は階層構造をもてる辞書と記述しやすい多段のエントリ呼び出しで、どこいつ式ランダムトークを簡単かつ強力に生成できることを特徴とするSHIORIです。<br>
プログラム記述やデバッグに関しても十分な機能を持っていて、複雑なこともしっかりできます。<br>
SAORIとしても使えるので里々等の不足を補うこともできるでしょう。

ただ高い汎用性ゆえ、システム根幹から処理を書ける＝書かなければならないので、普通はそれをカバーする「ミドルウェア」を介して使うことになります。

なお移植環境が多く、Windows以外でもまず問題なくゴーストが動きます。<br>
伺か界を下支えするSHIORIといえるでしょう。

| バナー | サイト | 紹介 |
|---|---|---|
| [![華和梨](../assets/banners/kawari.png)](http://kawari.sourceforge.net/) | **プログラマブル準AI 華和梨**<br><http://kawari.github.io/> | 華和梨の公開・配布元です。<br>リファレンスマニュアルなどもこちらにあります。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html) | **なごやか。**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html> | 華和梨の入門講座や解説記事、テンプレートなどの配布物など色々揃ったサイトです。<br>華和梨をSAORIとして扱うためのファイルセット「さおりの華和梨」もこちらにあります。<br>華和梨について全体的に知りたい方はまず本家のマニュアルとここを読みましょう。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8) | **里々から華和梨への移行ガイド・ミドルウェア使わない編（駄でべwiki　内）**<br><http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8> | 華和梨の特徴でもある「ミドルウェア」について、何物であるか、使わずに華和梨ゴーストを作ろうとするとどうなるかといった観点から解説している記事です。<br>華和梨の設計について理解を深めたい場合や、ミドルウェアを作ってみたい場合に大いに役立つでしょう。<br>なお一応タイトルにもある通り里々からの移行記事の一貫という位置づけですが、内容はほぼ独立して読めるものです。 |
| [![no banner](../assets/banners/nobanner.png)](http://sourceforge.jp/projects/keeps/) | **OpenKEEPS**<br><http://sourceforge.jp/projects/keeps/> |  |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html) | **華和梨のかおり（なごやか　内）**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://rimuhamate.sakura.ne.jp/KarinDocument/index.html) | **華和梨テンプレート「かりん」（リムハマテ　内）**<br><http://rimuhamate.sakura.ne.jp/KarinDocument/index.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://paripari.if.land.to/) | **華和梨テンプレート『パリパリ』（osm　内）**<br><http://paripari.if.land.to/> |  |
| [![The Gift](../assets/banners/gift.png)](http://priest.so.land.to/ghost/wish.html) | **Wish ～ 華和梨テンプレート（The Gift　内）**<br><http://priest.so.land.to/ghost/wish.html> |  |
| [![K.H mix 1st Edition](../assets/banners/K.Hmix.png)](http://khmix.sakura.ne.jp/ghost.shtml) | **華和梨サンプルゴースト「GOA Lilith」（K.Hmix 1st Edition内）**<br><http://khmix.sakura.ne.jp/ghost.shtml> | 上記が代表的な華和梨のミドルウェア（テンプレート）です。<br>それぞれの特色などはリンク先へ丸投げ……。 |

### 灯

灯（あかり）は非常に特色ある組み込み関数を備えたSHIORIです。<br>
具体的には、FTP通信、メール送受信、シリアル通信、SQLiteを用いたデータベース操作、マルチスレッド処理などの機能を初めから持っています。<br>
辞書の文法は、C言語風の記述を標榜する文・YAYAと比べても、更にはっきりとC言語の文法に近いものです。<br>
連想配列（辞書型）や多次元の配列も備えており、ある程度複雑な処理や高度な機能の実装に耐えるでしょう。

サンプルゴーストで実装されているシステム辞書を利用すれば、里々風の文法を利用してトークを記述することもできます。<br>
ただし本家里々やYAYA・華和梨の各種ミドルウェアほど手厚いサポートというわけではなく、自力で拡張するならばC言語風の文法に真っ向から取り組む必要があるので、完全なプログラミング未経験者には多少困難があるかもしれません。<br>
こうした尖った設計のため、そのポテンシャルを引き出せるゴーストは限られるかもしれませんが、他にない持ち味のあるSHIORIと言えます。

なお、ヘッダを構築するための辞書さえ用意すれば、SAORIとして利用することも可能です。<br>
また、後述する汎用言語系SHIORI「tkytk」から拡張DLLとして呼ばれるための仕組みを備えており、灯の独特な機能をtkytkから利用できるようになっています。

| バナー | サイト | 紹介 |
|---|---|---|
| [![no banner](../assets/banners/yaten.png)](http://le.silk.to/?p=dll) | **夜天燈火**<br><http://le.silk.to/?p=dll> | 灯の開発・配布元です。<br>公式リファレンスの他、サンプルゴーストおよびテスターなどもこちらにあります。 |

### MiyoJS

Miyo（美代・みよ）は「プログラマにとって使いやすいSHIORI」をコンセプトとするSHIORIです。MiyoJSはそのJavaScriptによる実装です。<br>
既存言語JavaScriptや他汎用技術の採用、「処理」と「データ」の分離、最低限なSHIORIの機能とプラグインによる拡張という方向性で、保守性の高いゴースト制作を支援しています。<br>
基本的に辞書＝データ本位であり、単純な処理のゴーストは辞書記述だけで簡単にできます。<br>
より複雑なことをしたい場合も見通しよく拡張できます。<br>
まだ新しいSHIORIなので(拡張)機能の不足がありますが、徐々に改善されるでしょう。

| バナー | サイト | 紹介 |
|---|---|---|
| [![MiyoJS](../assets/banners/miyojs.png)](https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md) | **MiyoJS - SHIORIサブシステム「美代」 for JavaScript**<br><https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md> | MiyoJS（および美代全般）の開発・配布元です。<br>サンプルゴースト・公式のドキュメントもこちらにあります。 |

### tkytk

tkytk（ツキヨタケ）は汎用言語系のSHIORIの一つで、スクリプト言語Luaによる実装です。<br>
基本的に辞書部分だけでなく、SHIORIプロトコルの処理についてもある程度Luaで書く必要があります（逆に言うと、自由に設計できる）。<br>
ドキュメントも、世の中にあるLuaについてのものを参照する事になります。<br>
ただしゴーストとしての基本的な機能に関する部分は、本家で公開されているサンプルゴーストおよび、実際にtkytkで作られたゴースト「スチームにしき」に例があるので参考にできます。

tkytkに限らず汎用言語系のあらゆるSHIORIについて言える事ですが、未経験者が手を出すには困難が多いかもしれません。<br>
しかし覚えのある人にはむしろ扱いやすい面がたくさんあるはずです。<br>
あるいはこれを機にプログラミング言語（tkytkならLua）を勉強して見るつもりで触ってみるのもいいでしょう。

| バナー | サイト | 紹介 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://kinoko.pw/ukagaka/tkytk.html) | **きのこぱわー**<br><http://kinoko.pw/> | tkytkの開発・配布元です。<br>サンプルゴーストもこちらにあります。 |

### 美坂

美坂（みさか）は本家伺か(MATERIA)の作者によって設計されたSHIORIです。<br>
システムを記述しなくてもゴーストが一般に備える機能をすぐできるようになっているという意味で、里々に似た設計思想のSHIORIです。<br>
里々ほどなんでもやってくれるわけではなく、バランスのよい機能の取捨選択で比較的見通しのよいSHIORIといえるでしょう。

今から始めるゴースト製作に使用するには、開発が終了していることが里々などと比べて難点とは言えますが、動作に大きな支障はありません。

| バナー | サイト | 紹介 |
|---|---|---|
| [![美坂](../assets/banners/misaka.png)](http://lovelove.rabi-en-rose.net/index_misaka.php) | **美坂（面屋　内）**<br><http://lovelove.rabi-en-rose.net/index_misaka.php> | 美坂の開発・配布元です。 |

## 素材・プログラム・ツール配布元

| バナー | サイト | 紹介 |
|---|---|---|
| [![freeshell wiki](../assets/banners/freeshellwiki.png)](http://wikiwiki.jp/feeshell/) | **freeshell wiki**<br><http://wikiwiki.jp/feeshell/> | フリーシェルのまとめwikiです。<br>無料で使えるシェル素材をお探しの方はこちら。 |
| [![整備班 The Maintenance Shop](../assets/banners/maintenance.png)](http://ms.shillest.net/) | **整備班**<br><http://ms.shillest.net/> | ばぐとら研直営サイト。いろいろ置いてます。<br>代表的なSHIORIである里々、YAYAや、公開配布に有用なツール、素材、もちろんゴーストもあります。 |
| [![no banner](../assets/banners/nobanner.png)](http://priest.so.land.to/nisesakura/saorin.html) | **さおりん**<br><http://priest.so.land.to/nisesakura/saorin.html> | SAORIのまとめサイトです。<br>更新停止した「さおこれ」を補完する役割を果たしています。 |

## その他

| バナー | サイト | 紹介 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://ukadev.shillest.net/) | **伺か開発情報検索**<br><http://ukadev.shillest.net/> | 伺か関係の開発情報を扱っている複数サイトを対象にして一括検索できる検索フォームです。<br>なにか調べたい時は通常の検索サイトでの検索に加え、ここで検索してみると探し当てやすいでしょう。 |
| [![no banner](../assets/banners/nobanner.png)](http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi) | **被り負けチェッカー**<br><http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi> | ゴーストの名前やゴーストのフォルダ名は、他のゴーストと被ってしまうと不具合の原因になる事があります（ゴーストのコミュニケート先を間違うなど）。<br>そこで入力した文字列を、データベースから検索し、既存のものと重複している場合には教えてくれる仕組みがこちらです。<br>ただしデータベースのソースが古いため、最近のゴーストが反映されていません。ここで検出されなくても油断はしない方がよいでしょう。 |
| [![no banner](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89) | **ゴースト配布するなら（駄でべwiki　内）**<br><http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89> | 無料レンタルスペースに関するまとめ記事です。<br>ゴーストという創作物の優れた特徴に、ネットワーク更新機能があります。<br>その実現に不可欠なサーバを用意する手段として、無料レンタルスペースの存在は非常に重要です。<br>しかしそのサービスの内容によっては、ゴーストなどのコンテンツ配布には向かない場合もあり、調査が必要になります。<br>そこでこの記事が大いに役立ってくれるでしょう。<br>またここにない情報をご存知なら、積極的にこちらへ提供されると色んな人が助かるはずです。 |
