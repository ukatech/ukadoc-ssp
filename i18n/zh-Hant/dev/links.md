# 開發者說明：開發連結集

這裡整理了有助於製作伺か (Ukagaka)/SSP 相關內容的資訊、程式、素材、工具等連結。

為避免冗長，這裡不會再次列出相關網站；不過，若要發布內容並在發布後宣傳，可以善用另一份[連結集](../about/links.md)中的網站，想辦法讓使用者看見，大家都能受益。

- [規格書・參考資料](#仕様書リファレンス)
- [SHIORI](#shiori)
- [素材・程式・工具下載處](#素材プログラムツール配布元)
- [其他](#その他)

## 規格書・參考資料

| バナー | 網站 | 介紹 |
|---|---|---|
| [![UKAODC](../assets/banners/ukadoc_banner1.png)](http://ssp.shillest.net/ukadoc/manual/index.html) | **UKADOC**<br><http://ssp.shillest.net/ukadoc/manual/index.html> | SSP 的官方規格文件集。<br>提供 Sakura Script 和 SHIORI Event 的參考資料。 |
| [![SDN on the web.](../assets/banners/sdn.png)](http://www.boreas.dti.ne.jp/~sdn/saori.html) | **SAORI/1.0（SDN on the web 內）**<br><http://www.boreas.dti.ne.jp/~sdn/saori.html> | 這是 SHIORI 功能擴充模組「SAORI」的規格書。<br>內容是提供給技術人員和 SAORI 開發者參考的；若要了解人格端實際使用 SAORI 的方式，請參閱各 SAORI 的說明。<br>尋找 SAORI 時，[下文](#素材プログラムツール配布元)提到的「さおりん」或許能派上用場。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.ooyashima.net/db/) | **大八州.NET**<br><http://www.ooyashima.net/db/> | 這是伺か相關的非官方規格集。<br>雖然是非官方資料，但資訊相當充實且容易理解，也值得搭配其他資料一起閱讀。 |
| [![SAKURA SCRIPT WIKI](../assets/banners/sakurascriptwiki.png)](http://www36.atwiki.jp/sakurascript/pages/1.html) | **Sakura Script wiki**<br><http://www36.atwiki.jp/SakuraScript/pages/1.html> | 這是 Sakura Script 相關的整理 wiki。<br>其中有許多比 ukadoc 更深入的解說，例如使用範例，歡迎搭配使用。 |
| [![UKATEC](../assets/banners/ukatec.png)](http://wikiwiki.jp/ukatec/) | **UKATEC**<br><http://wikiwiki.jp/ukatec/> | 這是整理伺か相關內容製作資訊的 wiki。<br>除了人格之外，也收集了外殼、對話方塊及其他各類內容的製作者資訊連結與文章。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/) | **駄でべろぱ的小知識 wiki**<br><http://emily.shillest.net/specwiki/> | 通稱駄でべ。這裡是不特定開發者與技術人員自由記錄各種筆記的地方。<br>目前仍在更新的筆記，與過去（部分已遭棄置）的資料或討論痕跡混雜在一起，閱讀時請留意撰寫時間。 |
| [![伺か](../assets/banners/usadasakura.png)](http://usada.sakura.vg/) | **うさださくら**<br><http://usada.sakura.vg/> | 這是伺か原作者的發布網站。<br>雖然已經停止更新很久，但在開發時若需要查閱舊規格等資料，仍可回到這裡參考。 |

## SHIORI

這裡依個人判斷與偏好介紹幾種 SHIORI（雖然也大致考量了 2014 年當時仍在持續開發、使用率較高等因素）。<br>
除此之外，尤其是通用語言類的 SHIORI，還有很多種類，有興趣的話請自行搜尋。

### 里々

里々（さとり）是目前使用者最多的 SHIORI。<br>
它的辭典語法使用全形符號，並經過設計，讓使用者能輕鬆撰寫對話；此外，它貼心地自動處理了複雜的部分，因此深受沒有程式設計經驗的使用者，以及最重視隨機談話的人格製作者支持。<br>
此外，志願者也整理了完善的文件，並開發了實用的人格製作工具與範本人格，因此可說是開發環境相當完善的 SHIORI。

另一方面，由於內部會自動處理各種工作，這種不透明性可能妨礙使用者理解 SHIORI 或 SSP 原本的功能與作用，初學者在進行進階開發時也容易遇到困難。<br>
此外，它不擅長快速執行複雜處理，且無法區分語法符號與一般字串，因此也有「函式引數分隔符問題」等固有弱點，整體而言不太適合處理「困難或複雜的工作」。

對沒有程式設計經驗的初學者來說，里々是最優先推薦的 SHIORI；不過，若想製作附有小遊戲的人格，或人格的開發目標有所不同，即使一開始的門檻稍高，也建議考慮使用 YAYA 或華和梨等其他 SHIORI。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/satoriya.xhtml) | **里々／整備班客製版（整備班內）**<br><http://ms.shillest.net/satoriya.xhtml> | 目前負責維護與發布里々的網站。本家停止開發後，由這裡接手維護。 |
| [![里々wiki](../assets/banners/satorib.png)](http://soliton.sub.jp/satori/) | **里々 wiki**<br><http://soliton.sub.jp/satori/> | 這是介紹里々與提供技巧的 wiki。雖然是非官方資料，但實際上扮演著里々使用手冊的角色。<br>與其他 SHIORI 的 wiki 相比，這裡的資訊也相當充實，是容易向初學者推薦里々的原因之一。 |
| [![さとりすと](../assets/banners/satolist.png)](http://wikiwiki.jp/satolist/) | **さとりすと wiki**<br><http://wikiwiki.jp/satolist/> | 這是里々人格編輯器「さとりすと」的線上使用手冊。<br>它不只是單純的文字編輯器，也內建了各種有助於開發的工具，可說是接近整合式開發環境的軟體。<br>如果打算開始使用里々製作人格，不妨先安裝看看。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.geocities.jp/poskoma/) | **電力驅動的うにゅう・廢屋之夏**<br><http://www.geocities.jp/poskoma/> | 這是本家發布與提供里々下載的網站。 |

### Aya/YAYA

Aya（あや）是採用類似 C 語言語法的 SHIORI。<br>
Aya 結束開發後，YAYA（やや）在承襲其基本語法與功能的同時，以非官方形式持續開發。

它具備分支與迴圈等基本控制結構；與里々相比，對有程式設計經驗的人來說，是一種更容易直覺上手的 SHIORI。<br>
此外，它也內建文字操作、檔案操作、基本數學運算，以及使用正規表示式處理字串等功能，適合用於想實作較複雜功能的人格。

不過，陣列是（雖然有模擬的方法）一維陣列，也尚未實作關聯陣列。<br>
由於沒有類別等機制，因此無法以物件導向的方式撰寫；與通用語言類型的 SHIORI 相比，功能也沒那麼強大或靈活。<br>
此外，雖然說是類似 C 語言，但仍有許多獨特的慣例，需要花時間熟悉。

另外，Aya 和 YAYA 本身的特色是以單純的通用語言 DLL 設計。<br>
對 SHIORI 等通訊規格的支援，以及提供人格基本功能的部分，全部都交由辭典處理（隨附於範本人格）。<br>
因此，Aya 和 YAYA 可藉由替換系統辭典，不只作為 SHIORI，也能作為以 DLL 為核心的其他伺か子系統，例如 SAORI 或 PLUGIN。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/yaya.xhtml) | **YAYA/Yet Another AYA（整備班內）**<br><http://ms.shillest.net/yaya.xhtml> | 這裡維護並發佈 YAYA，也就是 Aya 的非官方後繼版本。<br>目前仍持續提供支援，而且比 Aya 增加了一些功能，因此推薦剛開始使用的人選擇這個版本。 |
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/yayame.xhtml) | **哈囉 YAYA 世界（整備班內）**<br><http://ms.shillest.net/yayame.xhtml> | 這是 YAYA 的範本人格。<br>其中包含使用 YAYA 作為 SHIORI 時不可或缺的系統辭典，以及提供額外功能的範本辭典。若要開始使用 YAYA 製作人格，請先下載這個範本。 |
| [![文屋](../assets/banners/ayaya.png)](http://emily.shillest.net/ayaya/) | **Aya 小屋**<br><http://emily.shillest.net/ayaya/> | 這是彙整 Aya/YAYA 相關資訊的 Wiki。<br>YAYA 開發者也會積極參與編輯，實質上也發揮了參考手冊的作用。<br>此外，這裡也會發佈用於將 YAYA 當作 SAORI/MAKOTO/PLUGIN 使用的系統辭典。 |
| [![no banner](../assets/banners/nobanner.png)](http://umeici.onjn.jp/) | **umeici.onjn.jp**<br><http://umeici.onjn.jp/> | 這是原版 Aya 的發佈處。<br>此外也有發佈 Aya 專用的除錯工具「玉」，似乎也能用於 YAYA。 |

### 華和梨

華和梨（かわり）是一種 SHIORI，其特色是可使用具備階層結構的辭典，以及容易撰寫的多層項目呼叫，能夠簡單又有效地產生類似《どこいつ》的隨機談話。<br>
它也具備充足的程式撰寫與除錯功能，因此能妥善處理複雜的工作。<br>
也可以將它當作 SAORI 使用，因此或許能補足里々等系統的不足。

不過，由於通用性高，代表可以從系統核心開始撰寫處理流程，也就是說，必須自行撰寫；因此一般會透過負責補足這部分的「中介軟體」來使用。

此外，它有許多移植環境，即使在 Windows 以外的作業系統上，人格通常也能正常運作。<br>
可說是支撐著伺か世界的 SHIORI。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![華和梨](../assets/banners/kawari.png)](http://kawari.sourceforge.net/) | **可程式化準 AI 華和梨**<br><http://kawari.github.io/> | 這是華和梨的公開與發佈處。<br>這裡也提供參考手冊等資料。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html) | **なごやか。**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html> | 這個網站提供許多內容，包括華和梨入門課程、解說文章、範本等。<br>用於將華和梨當作 SAORI 使用的檔案集「さおりの華和梨」也在這裡。<br>如果想全面瞭解華和梨，請先閱讀官方手冊和這個網站的內容。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8) | **從里々移轉至華和梨指南：不使用中介軟體篇（駄でべwiki 內）**<br><http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8> | 這篇文章從華和梨特色之一的「中介軟體」是什麼，以及嘗試不使用中介軟體製作華和梨人格會遇到什麼情況等角度，進行解說。<br>想深入瞭解華和梨的設計，或是想嘗試製作中介軟體時，這篇文章會很有幫助。<br>如標題所示，這篇文章雖然定位為從里々移轉的指南之一，但內容大致上也可以獨立閱讀。 |
| [![no banner](../assets/banners/nobanner.png)](http://sourceforge.jp/projects/keeps/) | **OpenKEEPS**<br><http://sourceforge.jp/projects/keeps/> |  |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html) | **華和梨之香（なごやか 內）**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://rimuhamate.sakura.ne.jp/KarinDocument/index.html) | **華和梨範本「かりん」（リムハマテ 內）**<br><http://rimuhamate.sakura.ne.jp/KarinDocument/index.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://paripari.if.land.to/) | **華和梨範本《パリパリ》（osm 內）**<br><http://paripari.if.land.to/> |  |
| [![The Gift](../assets/banners/gift.png)](http://priest.so.land.to/ghost/wish.html) | **Wish ～ 華和梨範本（The Gift 內）**<br><http://priest.so.land.to/ghost/wish.html> |  |
| [![K.H mix 1st Edition](../assets/banners/K.Hmix.png)](http://khmix.sakura.ne.jp/ghost.shtml) | **華和梨範例人格「GOA Lilith」（K.Hmix 1st Edition 內）**<br><http://khmix.sakura.ne.jp/ghost.shtml> | 上述都是具代表性的華和梨中介軟體（範本）。<br>各自的特色就請直接參閱連結頁面了……。 |

### 燈

燈（あかり）是具備非常有特色的內建函式的 SHIORI。<br>
具體來說，它從一開始就具備 FTP 通訊、收發電子郵件、序列通訊、使用 SQLite 操作資料庫、多執行緒處理等功能。<br>
其字典語法比起標榜類似 C 語言寫法的語言 YAYA，更明確地接近 C 語言語法。<br>
它也具備關聯陣列（字典型）和多維陣列，應該足以實作某種程度的複雜處理和進階功能。

使用範例人格中實作的系統字典，也可以使用里々風格的語法撰寫談話。<br>
不過，它不像原版里々、YAYA、華和梨的各種中介軟體那樣提供完善的支援；若要自行擴充，就必須正面挑戰類似 C 語言的語法，因此完全沒有程式設計經驗的人可能會覺得有些困難。<br>
由於這種尖銳的設計，能發揮其潛力的人格可能有限，但它可說是具有獨特風格、別具一格的 SHIORI。

此外，只要準備好用來建構標頭的字典，也可以將它做為 SAORI 使用。<br>
另外，它具備可讓後述的通用語言系 SHIORI「tkytk」以擴充 DLL 形式呼叫的機制，因此可以從 tkytk 使用燈的獨特功能。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![no banner](../assets/banners/yaten.png)](http://le.silk.to/?p=dll) | **夜天燈火**<br><http://le.silk.to/?p=dll> | 燈的開發與發佈來源。<br>這裡除了有官方參考資料，也有範例人格和測試工具等。 |

### MiyoJS

Miyo（美代・みよ）是以「讓程式設計師容易使用的 SHIORI」為概念的 SHIORI。MiyoJS 是以 JavaScript 實作的版本。<br>
它採用既有語言 JavaScript 和其他通用技術，將「處理」與「資料」分開，並以最低限度的 SHIORI 功能搭配外掛程式擴充，藉此協助製作易於維護的人格。<br>
基本上以字典＝資料為主，單純處理的人格只要撰寫字典就能輕鬆完成。<br>
若想實作更複雜的功能，也能清楚地進行擴充。<br>
由於它是較新的 SHIORI，（擴充）功能仍有所不足，但預期會逐步改善。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![MiyoJS](../assets/banners/miyojs.png)](https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md) | **MiyoJS - SHIORI 子系統「美代」 for JavaScript**<br><https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md> | MiyoJS（以及美代整體）的開發與發佈來源。<br>這裡也有範例人格和官方文件。 |

### tkytk

tkytk（ツキヨタケ）是通用語言系 SHIORI 之一，以指令碼語言 Lua 實作。<br>
基本上不只字典部分，SHIORI 通訊協定的處理也需要用 Lua 撰寫到某種程度（反過來說，也就能自由設計）。<br>
文件方面則需要參考網路上各種 Lua 相關資料。<br>
不過，關於人格基本功能的部分，可以參考原作者公開的範例人格，以及實際以 tkytk 製作的人格「スチームにしき」中的範例。

這點不只適用於 tkytk，也適用於所有通用語言系 SHIORI；對沒有經驗的人來說，可能會有許多困難。<br>
但對熟悉相關技術的人來說，應該會發現它有許多容易上手的地方。<br>
或者，也可以藉此機會抱著學習程式語言（使用 tkytk 時就是 Lua）的想法來嘗試看看。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://kinoko.pw/ukagaka/tkytk.html) | **きのこぱわー**<br><http://kinoko.pw/> | tkytk 的開發與發佈來源。<br>這裡也有範例人格。 |

### 美坂

美坂（みさか）是由原版伺か（MATERIA）的作者設計的 SHIORI。<br>
它的設計理念與里々相似，能讓人格不必撰寫系統，就能立即具備一般人格常有的功能。<br>
它不像里々那樣幾乎什麼都能處理，而是取捨了平衡良好的功能，可說是相對容易掌握的 SHIORI。

現在才開始製作人格的話，與里々等相比，停止開發可說是它的一項缺點，但在運作上沒有太大的問題。

| バナー | 網站 | 介紹 |
|---|---|---|
| [![美坂](../assets/banners/misaka.png)](http://lovelove.rabi-en-rose.net/index_misaka.php) | **美坂（面屋　內）**<br><http://lovelove.rabi-en-rose.net/index_misaka.php> | 美坂的開發與發佈來源。 |

## 素材、程式與工具發佈來源

| バナー | 網站 | 介紹 |
|---|---|---|
| [![freeshell wiki](../assets/banners/freeshellwiki.png)](http://wikiwiki.jp/feeshell/) | **freeshell wiki**<br><http://wikiwiki.jp/feeshell/> | 免費外殼的彙整 wiki。<br>想尋找可免費使用的外殼素材時，請參考這裡。 |
| [![整備班 The Maintenance Shop](../assets/banners/maintenance.png)](http://ms.shillest.net/) | **維護班**<br><http://ms.shillest.net/> | ばぐとら研直營網站，提供各式各樣的內容。<br>這裡有代表性的 SHIORI：里々、YAYA，以及適合公開發佈的工具、素材，當然也有人格。 |
| [![no banner](../assets/banners/nobanner.png)](http://priest.so.land.to/nisesakura/saorin.html) | **さおりん**<br><http://priest.so.land.to/nisesakura/saorin.html> | SAORI 彙整網站。<br>負責補足已停止更新的「さおこれ」。 |

## 其他

| バナー | 網站 | 介紹 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://ukadev.shillest.net/) | **伺か開發資訊搜尋**<br><http://ukadev.shillest.net/> | 這是一個搜尋表單，可一次搜尋多個提供伺か相關開發資訊的網站。<br>想查詢資料時，除了使用一般搜尋網站，也可以試著在這裡搜尋，會比較容易找到想要的資訊。 |
| [![no banner](../assets/banners/nobanner.png)](http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi) | **撞名檢查器**<br><http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi> | 人格名稱或人格資料夾名稱若與其他人格重複，有時會造成問題（例如弄錯人格的溝通對象）。<br>這個工具會搜尋資料庫中的輸入字串，並在發現與既有名稱重複時通知您。<br>不過，由於資料庫的來源較舊，尚未收錄近期的人格。即使這裡沒有檢查出重複，也請不要掉以輕心。 |
| [![no banner](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89) | **如果要散布人格（駄でべwiki 內）**<br><http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89> | 這是一篇整理免費租用空間相關資訊的文章。<br>人格這種創作作品的一項優秀特色，就是具備線上更新功能。<br>免費租用空間是提供實現這項功能不可或缺的伺服器的重要方式。<br>不過，依服務內容而定，有些空間可能不適合散布人格等內容，因此需要先行調查。<br>這篇文章能在這方面提供很大的幫助。<br>此外，如果您知道這裡沒有的資訊，也請踴躍提供給這個網站，應該能幫助到許多人。 |
