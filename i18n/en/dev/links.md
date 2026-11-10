# Developer Help: Development Links

This is a collection of links to information, programs, assets, tools, and other resources useful for creating Ukagaka/SSP-related content.

To avoid redundancy, we have not listed them here again, but when publishing your content and promoting it afterward, you can help it reach users by making use of the sites in the other [link collection](../about/links.md). That way, everyone wins.

- [Specifications and references](#仕様書リファレンス)
- [SHIORI](#shiori)
- [Parts, programs, and tool downloads](#素材プログラムツール配布元)
- [Other](#その他)

## Specifications and references

| バナー | Site | Description |
|---|---|---|
| [![UKAODC](../assets/banners/ukadoc_banner1.png)](http://ssp.shillest.net/ukadoc/manual/index.html) | **UKADOC**<br><http://ssp.shillest.net/ukadoc/manual/index.html> | The official collection of SSP specifications.<br>It includes references for Sakura Script and SHIORI events. |
| [![SDN on the web.](../assets/banners/sdn.png)](http://www.boreas.dti.ne.jp/~sdn/saori.html) | **SAORI/1.0 (on SDN on the web)**<br><http://www.boreas.dti.ne.jp/~sdn/saori.html> | The specification for SAORI, a SHIORI extension module.<br>This material is intended for engineers and SAORI developers, so for information about actually using a SAORI from a ghost, refer to that SAORI's documentation.<br>For help finding SAORIs, “Saorin,” mentioned [below](#素材プログラムツール配布元), may be useful. |
| [![no banner](../assets/banners/nobanner.png)](http://www.ooyashima.net/db/) | **Oyashima.NET**<br><http://www.ooyashima.net/db/> | An unofficial collection of Ukagaka specifications.<br>Although unofficial, it contains a wealth of clearly presented information, so you may find it useful to read alongside other materials. |
| [![SAKURA SCRIPT WIKI](../assets/banners/sakurascriptwiki.png)](http://www36.atwiki.jp/sakurascript/pages/1.html) | **Sakura Script Wiki**<br><http://www36.atwiki.jp/SakuraScript/pages/1.html> | A wiki covering Sakura Script.<br>It offers many explanations that go into greater detail than ukadoc, including examples, so make use of it as well. |
| [![UKATEC](../assets/banners/ukatec.png)](http://wikiwiki.jp/ukatec/) | **UKATEC**<br><http://wikiwiki.jp/ukatec/> | A wiki collecting information on creating Ukagaka-related content.<br>It brings together links and articles with information for creators of all kinds of things, not just ghosts, but also shells, balloons, and more. |
| [![Dadebe Wiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/) | **Dadebe Developers' Tips Wiki**<br><http://emily.shillest.net/specwiki/> | Commonly known as Dadebe, this is a place where developers and engineers can freely share all kinds of notes.<br>It contains both current notes and traces of old (and partly abandoned) materials and discussions, so be sure to check when each item was written. |
| [![Ukagaka](../assets/banners/usadasakura.png)](http://usada.sakura.vg/) | **Usada Sakura**<br><http://usada.sakura.vg/> | The distribution site for the original Ukagaka.<br>Updates stopped a long time ago, but you can still refer to it when you need to look up old specifications during development. |

## SHIORI

This section covers a few SHIORI implementations, based on our own judgment and preferences (with some consideration given to factors such as whether they were still being developed and how widely they were used as of 2014).<br>
There are many others, especially SHIORIs based on general-purpose programming languages, so look around if you're interested.

### Satori

Satori is currently the most widely used SHIORI.<br>
Its dictionary notation uses full-width symbols and is designed to make writing talks easy. Its thoughtful design also takes care of complicated processing behind the scenes. These qualities have made it popular with people who have never programmed before, especially those who want to create ghosts centered on random talk.<br>
There is also a wealth of documentation written by volunteers, as well as useful ghost-creation tools and template ghosts, making Satori a SHIORI with a well-supported development environment.

On the other hand, because processing happens automatically behind the scenes, it can be opaque, making it harder to understand the original functions and roles of SHIORI and SSP. This can make more advanced development a stumbling block for beginners.<br>
In addition, Satori is not well suited to fast, complex processing, and it has various specific weaknesses—for example, the “function argument separator problem,” caused by its inability to distinguish syntax symbols from ordinary text. Overall, it has limitations when it comes to “difficult or complicated” tasks.

Satori is the first SHIORI we recommend to beginners with no programming experience. However, depending on what you want your ghost to do—for example, if you want to create a ghost with a mini-game—it is worth considering other SHIORI implementations such as YAYA or Kawari, even if they have a somewhat steeper learning curve at the start.

| バナー | Site | Description |
|---|---|---|
| [![Maintenance Team](../assets/banners/maintenance.png)](http://ms.shillest.net/satoriya.xhtml) | **Satori / Maintenance Team Custom (by the Maintenance Team)**<br><http://ms.shillest.net/satoriya.xhtml> | This is where Satori is currently maintained and distributed. The Maintenance Team took over maintenance after the original developers ended development. |
| [![Satori Wiki](../assets/banners/satorib.png)](http://soliton.sub.jp/satori/) | **Satori Wiki**<br><http://soliton.sub.jp/satori/> | A wiki covering explanations and tips for Satori. Although unofficial, it effectively serves as Satori's manual.<br>It contains a wealth of information, even compared with wikis for other SHIORI implementations, making it one reason Satori is easy to recommend to beginners choosing a SHIORI. |
| [![Satorist](../assets/banners/satolist.png)](http://wikiwiki.jp/satolist/) | **Satorist Wiki**<br><http://wikiwiki.jp/satolist/> | The online manual for Satorist, a Satori ghost editor.<br>It is more than just a text editor: with various tools useful for development built in, it is something like an integrated development environment.<br>If you're starting to create a ghost with Satori, why not give it a try? |
| [![no banner](../assets/banners/nobanner.png)](http://www.geocities.jp/poskoma/) | **Electric Unyuu / Summer at the Ruined House**<br><http://www.geocities.jp/poskoma/> | This is the original site for publishing and distributing Satori. |

### Aya/YAYA

Aya (あや) is a SHIORI with C-like syntax.<br>
After development of Aya ended, YAYA (やや) continued its development unofficially while inheriting Aya's basic syntax and features.

It has basic control structures for branching and loops, and compared with Satori, it can be said to be a SHIORI that is intuitive for people with programming experience to use.<br>
It also provides built-in functions for text and file operations, basic mathematical calculations, and string processing with regular expressions, making it suitable for ghosts that need to implement somewhat complex features.

However, its arrays are one-dimensional (although there are ways to emulate other kinds), and associative arrays are not implemented.<br>
It also has no features such as classes, so you cannot write object-oriented code, and it is not as powerful or flexible as SHIORI implementations based on general-purpose languages.<br>
In addition, despite its C-like syntax, it has various quirks of its own, so some parts may take time to get used to.

One characteristic is that Aya and YAYA themselves are designed simply as general-purpose language DLLs.<br>
All support for communication protocols such as SHIORI, as well as the provision of basic ghost features, is left to the dictionary (included with the template ghost).<br>
As a result, by replacing the system dictionary, Aya and YAYA can serve not only as SHIORI, but also as other Ukagaka subsystems centered around DLLs, such as SAORI and PLUGIN.

| バナー | Site | Description |
|---|---|---|
| [![Maintenance Team](../assets/banners/maintenance.png)](http://ms.shillest.net/yaya.xhtml) | **YAYA/Yet Another AYA (on the Maintenance Team site)**<br><http://ms.shillest.net/yaya.xhtml> | This site maintains and distributes YAYA, the unofficial successor to Aya.<br>It is still supported and includes some features added to Aya, so we recommend using it if you are just getting started. |
| [![Maintenance Team](../assets/banners/maintenance.png)](http://ms.shillest.net/yayame.xhtml) | **Hello YAYA World (on the Maintenance Team site)**<br><http://ms.shillest.net/yayame.xhtml> | This is a template ghost for YAYA.<br>It includes the system dictionary required to use YAYA as a SHIORI, as well as a template dictionary that provides additional features, so download it first if you are starting to create a ghost with YAYA. |
| [![Aya House](../assets/banners/ayaya.png)](http://emily.shillest.net/ayaya/) | **Aya House**<br><http://emily.shillest.net/ayaya/> | This is a wiki compiling information about Aya and YAYA.<br>It also serves as a de facto reference manual, with YAYA's developer actively contributing edits.<br>It also distributes system dictionaries for using YAYA as SAORI/MAKOTO/PLUGIN. |
| [![no banner](../assets/banners/nobanner.png)](http://umeici.onjn.jp/) | **umeici.onjn.jp**<br><http://umeici.onjn.jp/> | This is the original distribution site for Aya.<br>It also distributes Tama, a debugger for Aya. It seems to work with YAYA as well. |

### Kawari

Kawari (かわり) is a SHIORI characterized by dictionaries that can have a hierarchical structure and easy-to-write, multi-level entry calls, which make it possible to create Dokoitsu-style random talk easily and powerfully.<br>
It also has ample features for writing and debugging programs, and can handle complex tasks reliably.<br>
It can also be used as SAORI, so it may be able to make up for shortcomings in Satori and other systems.

However, because it is highly versatile, you can—and must—write processing from the very foundations of the system, so it is usually used through "middleware" that handles this for you.

It has also been ported to many environments, and ghosts generally run without problems even outside Windows.<br>
It can be said to be a SHIORI that supports the Ukagaka community.

| バナー | Site | Description |
|---|---|---|
| [![Kawari](../assets/banners/kawari.png)](http://kawari.sourceforge.net/) | **Programmable Semi-AI Kawari**<br><http://kawari.github.io/> | This is the site for publishing and distributing Kawari.<br>Reference manuals and other resources are also available here. |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html) | **Nagoyaka.**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html> | This site offers a wide range of resources, including introductory lessons, explanatory articles, and templates for Kawari.<br>It also hosts "Saori no Kawari," a file set for using Kawari as SAORI.<br>If you want to learn about Kawari in general, start by reading the official manual and this site. |
| [![SpecWiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8) | **Guide to Migrating from Satori to Kawari: Without Middleware (on SpecWiki)**<br><http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8> | This article explains "middleware," a characteristic feature of Kawari: what it is and what happens when you try to create a Kawari ghost without using it.<br>It should be very helpful if you want to deepen your understanding of Kawari's design or try creating middleware.<br>As the title suggests, it is technically part of a series of articles about migrating from Satori, but you can read it almost entirely on its own. |
| [![no banner](../assets/banners/nobanner.png)](http://sourceforge.jp/projects/keeps/) | **OpenKEEPS**<br><http://sourceforge.jp/projects/keeps/> |  |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html) | **Kawari no Kaori (on Nagoyaka)**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://rimuhamate.sakura.ne.jp/KarinDocument/index.html) | **Kawari Template "Karin" (on Rimuhamate)**<br><http://rimuhamate.sakura.ne.jp/KarinDocument/index.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://paripari.if.land.to/) | **Kawari Template "Paripari" (on osm)**<br><http://paripari.if.land.to/> |  |
| [![The Gift](../assets/banners/gift.png)](http://priest.so.land.to/ghost/wish.html) | **Wish ~ Kawari Template (on The Gift)**<br><http://priest.so.land.to/ghost/wish.html> |  |
| [![K.H mix 1st Edition](../assets/banners/K.Hmix.png)](http://khmix.sakura.ne.jp/ghost.shtml) | **Kawari Sample Ghost "GOA Lilith" (on K.Hmix 1st Edition)**<br><http://khmix.sakura.ne.jp/ghost.shtml> | The above are representative Kawari middleware (templates).<br>We'll leave the details of each one's features to the linked sites... |

### Akari

Akari is a SHIORI with a highly distinctive set of built-in functions.<br>
Specifically, it comes with features such as FTP communications, sending and receiving email, serial communications, database operations using SQLite, and multithreaded processing.<br>
Its dictionary syntax is even closer to C than YAYA, which aims for C-like statements.<br>
It also supports associative arrays (dictionary types) and multidimensional arrays, making it capable of handling somewhat complex processing and implementing advanced features.

You can also write talks using Satori-like syntax by using the system dictionary implemented in the sample ghost.<br>
However, its support is not as extensive as that of the original Satori or the various middleware packages for YAYA and Kawari. If you want to extend it yourself, you will need to tackle its C-like syntax directly, which may be somewhat difficult if you have no prior programming experience.<br>
Because of this specialized design, only a limited number of ghosts may be able to realize its full potential, but it is a SHIORI with a unique character unlike any other.

You can also use it as a SAORI if you prepare a dictionary for constructing headers.<br>
It also has a mechanism for being called as an extension DLL by the general-purpose-language SHIORI “tkytk,” described below, allowing you to use Akari’s unique features from tkytk.

| バナー | Site | Description |
|---|---|---|
| [![no banner](../assets/banners/yaten.png)](http://le.silk.to/?p=dll) | **Yaten Tōka**<br><http://le.silk.to/?p=dll> | This is the development and distribution site for Akari.<br>In addition to the official reference, you can also find sample ghosts and testers here. |

### MiyoJS

Miyo (美代, pronounced Miyo) is a SHIORI built around the concept of “a SHIORI that is easy for programmers to use.” MiyoJS is its JavaScript implementation.<br>
By adopting the existing JavaScript language and other general-purpose technologies, separating “processing” from “data,” and providing minimal SHIORI functionality that can be extended with plugins, it supports the creation of easy-to-maintain ghosts.<br>
It is primarily dictionary- and data-oriented, so you can easily create ghosts with simple behavior using only dictionary entries.<br>
You can also extend it clearly and easily when you want to do something more complex.<br>
As it is a relatively new SHIORI, some (extension) features are missing, but it is expected to improve gradually.

| バナー | Site | Description |
|---|---|---|
| [![MiyoJS](../assets/banners/miyojs.png)](https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md) | **MiyoJS - SHIORI subsystem “Miyo” for JavaScript**<br><https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md> | This is the development and distribution site for MiyoJS (and Miyo in general).<br>You can also find sample ghosts and official documentation here. |

### tkytk

tkytk (Tsukiyotake) is a general-purpose-language SHIORI implemented in the Lua scripting language.<br>
In general, you need to write not only the dictionary but also some of the SHIORI protocol handling in Lua (which also means you can design it freely).<br>
You will also need to refer to the Lua documentation available online.<br>
However, examples of the basic features needed for a ghost are available in the sample ghost published by the original developer and in “Steam Nishiki,” a ghost actually made with tkytk, so you can use them as a reference.

As with any general-purpose-language SHIORI, not just tkytk, it may be difficult for people with no prior experience to get started.<br>
However, those with relevant experience should find many aspects of it easier to work with.<br>
Alternatively, you could try it as an opportunity to learn a programming language (Lua, in the case of tkytk).

| バナー | Site | Description |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://kinoko.pw/ukagaka/tkytk.html) | **Kinoko Power**<br><http://kinoko.pw/> | This is the development and distribution site for tkytk.<br>You can also find sample ghosts here. |

### Misaka

Misaka was designed by the creator of the original Ukagaka (MATERIA).<br>
It has a design philosophy similar to Satori’s: ghosts can quickly provide the features they generally need without requiring you to write the system yourself.<br>
It does not do as much as Satori, but its well-balanced selection of features makes it a relatively easy-to-understand SHIORI.

Although development has ended, which is a drawback compared with Satori and similar SHIORI for anyone starting ghost development now, there are no major issues with its operation.

| バナー | Site | Description |
|---|---|---|
| [![Misaka](../assets/banners/misaka.png)](http://lovelove.rabi-en-rose.net/index_misaka.php) | **Misaka (inside Menya)**<br><http://lovelove.rabi-en-rose.net/index_misaka.php> | This is the development and distribution site for Misaka. |

## Sources for materials, programs, and tools

| バナー | Site | Description |
|---|---|---|
| [![freeshell wiki](../assets/banners/freeshellwiki.png)](http://wikiwiki.jp/feeshell/) | **freeshell wiki**<br><http://wikiwiki.jp/feeshell/> | A wiki compiling free shells.<br>If you are looking for free shell materials, visit this site. |
| [![The Maintenance Shop](../assets/banners/maintenance.png)](http://ms.shillest.net/) | **The Maintenance Shop**<br><http://ms.shillest.net/> | The official site of the Bugtra Research Lab. It has a variety of resources.<br>It offers popular SHIORI such as Satori and YAYA, tools and materials useful for public distribution, and, of course, ghosts. |
| [![no banner](../assets/banners/nobanner.png)](http://priest.so.land.to/nisesakura/saorin.html) | **Saorin**<br><http://priest.so.land.to/nisesakura/saorin.html> | A site compiling SAORI resources.<br>It serves as a supplement to “Saokore,” which is no longer updated. |

## Other

| バナー | Site | Description |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://ukadev.shillest.net/) | **Ukagaka Development Information Search**<br><http://ukadev.shillest.net/> | This search form lets you search multiple sites that cover Ukagaka development information all at once.<br>When you need to look something up, try searching here in addition to using a regular search engine. You may have an easier time finding what you need. |
| [![no banner](../assets/banners/nobanner.png)](http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi) | **Name Collision Checker**<br><http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi> | If a ghost's name or folder name clashes with another ghost's, it can cause problems (such as communicating with the wrong ghost).<br>This tool searches its database for the text you enter and lets you know if it duplicates an existing entry.<br>However, the database is outdated and does not include recent ghosts. Even if nothing is detected here, you should still check carefully. |
| [![no banner](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89) | **If You’re Distributing a Ghost (on the Dada Dev Wiki)**<br><http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89> | This article summarizes free web hosting services.<br>One of the great features of ghosts as creative works is their network update functionality.<br>Free web hosting is a very important way to get the servers needed to make this possible.<br>However, depending on the service, it may not be suitable for distributing content such as ghosts, so you need to do some research.<br>This article should be a great help.<br>If you know of information that is not included here, please consider sharing it there to help others. |
