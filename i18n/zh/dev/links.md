# 面向开发者的帮助：开发链接集

这里汇集了有助于制作伺か/SSP相关内容的信息、程序、素材和工具等链接。

另外，为避免冗余，这里不再重复列出相关链接；不过，在发布内容以及发布后的宣传等方面，利用另一份[链接集](../about/links.md)中的网站，让更多用户看到你的作品，大家都会受益。

- [规格书与参考资料](#仕様書リファレンス)
- [SHIORI](#shiori)
- [素材、程序与工具的发布站点](#素材プログラムツール配布元)
- [其他](#その他)

## 规格书与参考资料

| バナー | 网站 | 介绍 |
|---|---|---|
| [![UKAODC](../assets/banners/ukadoc_banner1.png)](http://ssp.shillest.net/ukadoc/manual/index.html) | **UKADOC**<br><http://ssp.shillest.net/ukadoc/manual/index.html> | SSP的官方规格文档集。<br>其中包含Sakura Script和SHIORI Event的参考资料。 |
| [![SDN on the web.](../assets/banners/sdn.png)](http://www.boreas.dti.ne.jp/~sdn/saori.html) | **SAORI/1.0（SDN on the web内）**<br><http://www.boreas.dti.ne.jp/~sdn/saori.html> | 这是SHIORI功能扩展模块「SAORI」的规格书。<br>内容面向技术人员和SAORI开发者；关于如何在人格端实际使用SAORI，请参阅各SAORI的说明。<br>寻找SAORI时，或许可以参考[下文](#素材プログラムツール配布元)提到的「さおりん」。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.ooyashima.net/db/) | **大八州.NET**<br><http://www.ooyashima.net/db/> | 这是伺か相关的非官方规格资料集。<br>虽然是非官方资料，但内容相当丰富、易于理解，也可以结合其他资料一起阅读。 |
| [![SAKURA SCRIPT WIKI](../assets/banners/sakurascriptwiki.png)](http://www36.atwiki.jp/sakurascript/pages/1.html) | **さくらスクリプトwiki**<br><http://www36.atwiki.jp/SakuraScript/pages/1.html> | 这是关于Sakura Script的汇总wiki。<br>其中有不少关于用例的深入讲解，建议与ukadoc配合使用。 |
| [![UKATEC](../assets/banners/ukatec.png)](http://wikiwiki.jp/ukatec/) | **UKATEC**<br><http://wikiwiki.jp/ukatec/> | 这是汇总伺か相关内容制作信息的wiki。<br>其中收集了面向制作者的信息链接和文章，内容不仅涉及人格，也包括外壳、对话框等各种内容。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/) | **駄でべろぱの小ネタwiki**<br><http://emily.shillest.net/specwiki/> | 通称「駄でべ」。这是一个供不特定多数的开发者和技术人员自由记录各种备忘的地方。<br>其中既有正在更新的备忘，也混杂着过去的资料和讨论痕迹（有些已经基本搁置），请留意内容的撰写时间。 |
| [![伺か](../assets/banners/usadasakura.png)](http://usada.sakura.vg/) | **うさださくら**<br><http://usada.sakura.vg/> | 这是伺か原版的发布网站。<br>虽然已经停止更新很久了，但在开发过程中需要查阅旧规格时，不妨回到这里看看。 |

## SHIORI

这里根据个人判断和偏好（虽然也会考虑截至2014年仍在持续开发、使用率较高等因素）介绍几种SHIORI。<br>
除此之外，尤其是通用语言类的SHIORI还有很多，有兴趣的话可以自行寻找。

### 里々

里々（さとり）是目前使用者最多的SHIORI。<br>
它采用全角符号，设计了便于编写谈话的辞典语法；对于复杂的处理部分，也会贴心地自动完成。这些特点尤其受到没有编程经验的用户，以及最想制作以随机谈话为核心的人格的用户支持。<br>
此外，还有志愿者编写的完善文档，也开发了实用的人格制作工具和模板人格，因此可以说它拥有良好的开发环境。

另一方面，由于内部会自动执行处理，这种不透明性可能妨碍用户理解SHIORI和SSP本身的功能与职责，初学者在进行进阶开发时也容易遇到困难。<br>
此外，它不擅长高速执行复杂处理；由于无法区分语法符号和普通字符串，还存在诸如「函数参数分隔符问题」等自身的弱点。总体来说，它不太适合处理「困难或复杂的事情」。

对于没有编程经验的初学者，最值得优先推荐的SHIORI就是里々。不过，如果你想制作带有迷你游戏的人格等，也可以根据人格的目标，考虑使用YAYA或華和梨等其他SHIORI，即使它们的初始学习门槛稍高一些。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![整備班](../assets/banners/maintenance.png)](http://ms.shillest.net/satoriya.xhtml) | **里々／整備班定制版（整備班内）**<br><http://ms.shillest.net/satoriya.xhtml> | 这里目前负责维护和发布里々。在原作者停止开发后，接手了后续维护工作。 |
| [![里々wiki](../assets/banners/satorib.png)](http://soliton.sub.jp/satori/) | **里々wiki**<br><http://soliton.sub.jp/satori/> | 这是介绍里々并提供技巧的wiki。虽然是非官方的，但实际上发挥着里々手册的作用。<br>与其他SHIORI的wiki相比，它的信息也相当丰富，这也是初学者选择SHIORI时容易被推荐使用里々的原因之一。 |
| [![さとりすと](../assets/banners/satolist.png)](http://wikiwiki.jp/satolist/) | **さとりすとwiki**<br><http://wikiwiki.jp/satolist/> | 这是里々人格编辑器「さとりすと」的在线手册。<br>它不只是普通的文本编辑器，还内置了各种有助于开发的工具，可以说接近集成开发环境。<br>如果你打算开始用里々制作人格，不妨先试着安装看看。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.geocities.jp/poskoma/) | **電気で動くうにゅう・廃屋の夏**<br><http://www.geocities.jp/poskoma/> | 这是里々原版的公开和发布网站。 |

### Aya/YAYA

Aya（あや）是采用类似 C 语言语法的 SHIORI。<br>
Aya 停止开发后，YAYA（やや）在继承其基本语法和功能的基础上，以非官方形式继续开发。

它具备分支、循环等基本控制结构，与里々相比，编程经验丰富的人更容易凭直觉使用，是一种 SHIORI。<br>
此外，它还提供文本操作、文件操作、基本数学计算以及使用正则表达式处理字符串等内置函数，适合希望实现一定复杂功能的人格使用。

不过，数组只有一维（虽然有模拟实现的方法），尚未实现关联数组。<br>
它也没有类等机制，因此无法采用面向对象的方式编写；与通用语言类 SHIORI 相比，功能的强大程度和灵活性有所不足。<br>
此外，虽然语法类似 C 语言，但有许多独特之处，需要花些时间熟悉。

Aya/YAYA 的一个特点是，它们本身只是作为通用语言 DLL 而设计的。<br>
与 SHIORI 等通信规范的兼容部分，以及提供人格基本功能的部分，都交由辞典负责（随模板人格附带）。<br>
因此，只要替换系统辞典，Aya/YAYA 不仅可以作为 SHIORI 使用，也能作为 SAORI、PLUGIN 等以 DLL 为核心的其他伺か子系统使用。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![整备班](../assets/banners/maintenance.png)](http://ms.shillest.net/yaya.xhtml) | **YAYA/Yet Another AYA（整备班 内）**<br><http://ms.shillest.net/yaya.xhtml> | 这里维护并发布作为 Aya 非官方后继版本的 YAYA。<br>目前仍在持续提供支持，而且相较于 Aya 还增加了一些功能，因此建议初次使用时选择 YAYA。 |
| [![整备班](../assets/banners/maintenance.png)](http://ms.shillest.net/yayame.xhtml) | **Hello YAYA World（整备班 内）**<br><http://ms.shillest.net/yayame.xhtml> | 这是 YAYA 的模板人格。<br>其中包含将 YAYA 用作 SHIORI 时必需的系统辞典，以及提供附加功能的模板辞典。使用 YAYA 开始制作人格时，请先下载试用。 |
| [![文屋](../assets/banners/ayaya.png)](http://emily.shillest.net/ayaya/) | **Aya 文档站**<br><http://emily.shillest.net/ayaya/> | 这是汇总 Aya/YAYA 相关信息的 wiki。<br>YAYA 开发者也会积极参与编辑，因此实际上也发挥着参考手册的作用。<br>此外，这里还发布了用于将 YAYA 用作 SAORI/MAKOTO/PLUGIN 的系统辞典。 |
| [![no banner](../assets/banners/nobanner.png)](http://umeici.onjn.jp/) | **umeici.onjn.jp**<br><http://umeici.onjn.jp/> | 这里是原版 Aya 的发布来源。<br>此外，这里也提供 Aya 调试器「玉」，似乎也能在 YAYA 中运行。 |

### Kawari

Kawari（かわり）是一种 SHIORI，其特点是支持层级结构的辞典和易于编写的多层条目调用，因此可以轻松而强大地生成类似「どこいつ」风格的随机谈话。<br>
它也具备足够的程序编写和调试功能，能够妥善实现复杂功能。<br>
它还可以作为 SAORI 使用，因此也能弥补里々等的不足。

不过，由于通用性很高，既可以也必须从系统根本开始编写处理逻辑，因此通常会通过负责处理这些工作的「中间件」来使用。

此外，它有许多移植环境，因此人格通常也能在 Windows 以外的环境中正常运行。<br>
可以说，它是支撑着伺か领域的 SHIORI。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![华和梨](../assets/banners/kawari.png)](http://kawari.sourceforge.net/) | **可编程准 AI 华和梨**<br><http://kawari.github.io/> | 这里是华和梨的发布来源。<br>这里也提供参考手册等资料。 |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html) | **なごやか。**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/index.html> | 这个网站提供华和梨入门课程、解说文章、模板等各种资料。<br>用于将华和梨作为 SAORI 使用的文件集「さおりの華和梨」也可以在这里找到。<br>想要全面了解华和梨的话，可以先阅读官方手册和这里的资料。 |
| [![駄でべwiki](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8) | **从里々迁移到华和梨的指南：不使用中间件篇（駄でべwiki 内）**<br><http://emily.shillest.net/specwiki/index.php?%E3%82%89%E3%81%8F%E3%81%A0%E5%B1%8B%2F%E9%87%8C%E3%80%85%E3%81%8B%E3%82%89%E8%8F%AF%E5%92%8C%E6%A2%A8%E3%81%B8%E3%81%AE%E7%A7%BB%E8%A1%8C%E3%82%AC%E3%82%A4%E3%83%89%E3%83%BB%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E7%B7%A8> | 这篇文章围绕华和梨的特点之一「中间件」展开，介绍中间件是什么，以及不使用中间件制作华和梨人格会遇到什么情况。<br>无论是想深入了解华和梨的设计，还是想尝试制作中间件，这篇文章都会很有帮助。<br>如标题所示，这篇文章原本属于从里々迁移的系列，不过内容基本上可以独立阅读。 |
| [![no banner](../assets/banners/nobanner.png)](http://sourceforge.jp/projects/keeps/) | **OpenKEEPS**<br><http://sourceforge.jp/projects/keeps/> |  |
| [![no banner](../assets/banners/nobanner.png)](http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html) | **华和梨的香气（なごやか 内）**<br><http://www.h3.dion.ne.jp/~konecofa/nagoyaka/download/menu.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://rimuhamate.sakura.ne.jp/KarinDocument/index.html) | **华和梨模板「かりん」（リムハマテ 内）**<br><http://rimuhamate.sakura.ne.jp/KarinDocument/index.html> |  |
| [![no banner](../assets/banners/nobanner.png)](http://paripari.if.land.to/) | **华和梨模板「パリパリ」（osm 内）**<br><http://paripari.if.land.to/> |  |
| [![The Gift](../assets/banners/gift.png)](http://priest.so.land.to/ghost/wish.html) | **Wish ～ 华和梨模板（The Gift 内）**<br><http://priest.so.land.to/ghost/wish.html> |  |
| [![K.H mix 1st Edition](../assets/banners/K.Hmix.png)](http://khmix.sakura.ne.jp/ghost.shtml) | **华和梨示例人格「GOA Lilith」（K.Hmix 1st Edition 内）**<br><http://khmix.sakura.ne.jp/ghost.shtml> | 以上是有代表性的华和梨中间件（模板）。<br>各自的特色请参阅对应链接……。 |

### 灯

灯（あかり）是一款配备了极具特色的内置函数的 SHIORI。<br>
具体来说，它从一开始就具备 FTP 通信、收发邮件、串行通信、使用 SQLite 操作数据库、多线程处理等功能。<br>
与标榜使用类似 C 语言的写法的文·YAYA 相比，它的字典语法更加接近 C 语言语法。<br>
它还支持关联数组（字典型）和多维数组，足以实现一定复杂度的处理和高级功能。

利用示例人格中实现的系统字典，也可以使用类似里々的语法编写对话。<br>
不过，它的支持不如原版里々、YAYA、华和梨的各种中间件那么完善；如果想自行扩展，就需要正面学习类似 C 语言的语法，因此完全没有编程经验的用户可能会觉得有些困难。<br>
由于这种设计颇为独特，能够发挥其潜力的人格可能有限，但它确实是一款拥有独特风格的 SHIORI。

此外，只要准备好用于构建头部的字典，也可以将它用作 SAORI。<br>
它还具备可作为扩展 DLL 供下文介绍的通用语言类 SHIORI「tkytk」调用的机制，因此可以通过 tkytk 使用灯的独特功能。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![no banner](../assets/banners/yaten.png)](http://le.silk.to/?p=dll) | **夜天燈火**<br><http://le.silk.to/?p=dll> | 灯的开发和发布来源。<br>这里除了有官方参考资料，还有示例人格和测试工具等。 |

### MiyoJS

Miyo（美代・みよ）是一款以「让程序员易于使用的 SHIORI」为理念的 SHIORI。MiyoJS 是它的 JavaScript 实现。<br>
它采用现有语言 JavaScript 和其他通用技术，将「处理」与「数据」分离，并以最低限度的 SHIORI 功能和通过插件扩展为方向，帮助用户制作易于维护的人格。<br>
它基本上以字典＝数据为中心，简单的处理可以只编写字典就轻松实现。<br>
即使想实现更复杂的功能，也可以清晰地进行扩展。<br>
由于它还是一款较新的 SHIORI，部分（扩展）功能尚不完善，但今后会逐步改进。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![MiyoJS](../assets/banners/miyojs.png)](https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md) | **MiyoJS - SHIORI子系统「美代」 for JavaScript**<br><https://github.com/Narazaka/miyojs/blob/master/Readme.ja.md> | MiyoJS（以及美代整体）的开发和发布来源。<br>这里还有示例人格和官方文档。 |

### tkytk

tkytk（ツキヨタケ）是一款通用语言类 SHIORI，使用脚本语言 Lua 实现。<br>
通常不仅要编写字典部分，还需要用 Lua 编写一定程度的 SHIORI 协议处理（换句话说，也可以自由设计）。<br>
相关文档也需要参考网络上关于 Lua 的资料。<br>
不过，有关人格基本功能的部分，可以参考官方发布的示例人格，以及实际使用 tkytk 制作的人格「スチームにしき」中的示例。

不仅是 tkytk，所有通用语言类 SHIORI 都有可能让没有经验的用户觉得难以上手。<br>
但对于有相关经验的人来说，它应该有许多更容易使用的地方。<br>
也可以借此机会，以学习编程语言（使用 tkytk 时就是 Lua）为目的，尝试使用它。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://kinoko.pw/ukagaka/tkytk.html) | **きのこぱわー**<br><http://kinoko.pw/> | tkytk 的开发和发布来源。<br>这里也有示例人格。 |

### 美坂

美坂（みさか）是由原版伺か（MATERIA）的作者设计的 SHIORI。<br>
它的设计理念与里々相似，无需编写系统，就能轻松实现人格通常具备的功能。<br>
它不像里々那样什么都能帮你实现，而是通过合理取舍功能，成为一款相对易于理解的 SHIORI。

如果现在开始制作人格，使用它的缺点是已经停止开发，相较于里々等软件而言会有所不便，但运行方面没有重大问题。

| バナー | 网站 | 介绍 |
|---|---|---|
| [![美坂](../assets/banners/misaka.png)](http://lovelove.rabi-en-rose.net/index_misaka.php) | **美坂（面屋　内）**<br><http://lovelove.rabi-en-rose.net/index_misaka.php> | 美坂的开发和发布来源。 |

## 素材、程序和工具的发布来源

| バナー | 网站 | 介绍 |
|---|---|---|
| [![freeshell wiki](../assets/banners/freeshellwiki.png)](http://wikiwiki.jp/feeshell/) | **freeshell wiki**<br><http://wikiwiki.jp/feeshell/> | 免费外壳素材汇总 wiki。<br>如果您正在寻找可免费使用的外壳素材，请访问这里。 |
| [![整備班 The Maintenance Shop](../assets/banners/maintenance.png)](http://ms.shillest.net/) | **整備班**<br><http://ms.shillest.net/> | ばぐとら研直营网站，提供各种资源。<br>这里有知名 SHIORI 里々、YAYA，以及适用于公开发布的工具、素材，当然也有人格。 |
| [![no banner](../assets/banners/nobanner.png)](http://priest.so.land.to/nisesakura/saorin.html) | **さおりん**<br><http://priest.so.land.to/nisesakura/saorin.html> | SAORI 汇总网站。<br>它承担着补充已停止更新的「さおこれ」的作用。 |

## 其他

| バナー | 网站 | 介绍 |
|---|---|---|
| [![no banner](../assets/banners/nobanner.png)](http://ukadev.shillest.net/) | **伺か开发信息搜索**<br><http://ukadev.shillest.net/> | 这是一个搜索表单，可以一次性搜索多个发布伺か相关开发信息的网站。<br>想查询信息时，除了使用常规搜索网站，也可以试着在这里搜索，会更容易找到所需内容。 |
| [![no banner](../assets/banners/nobanner.png)](http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi) | **名称重复检查器**<br><http://ghosttown.mikage.jp/cgi-bin/check/gd_checker.cgi> | 人格名称或人格文件夹名称如果与其他人格重复，可能会导致问题（例如联系错人格等）。<br>这个工具可以在数据库中搜索输入的字符串，并在发现与现有名称重复时告知您。<br>不过，由于数据库源数据较旧，尚未收录近期的人格。即使这里没有检测出来，也请不要掉以轻心。 |
| [![no banner](../assets/banners/specwiki.png)](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89) | **人格发布指南（收录于駄でべwiki）**<br><http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89> | 这是一篇关于免费租用空间的汇总文章。<br>人格这一创作形式的一大优势，是具备在线更新功能。<br>要实现这一功能，服务器必不可少，因此免费租用空间非常重要。<br>不过，根据服务内容的不同，有些空间可能不适合发布人格等内容，因此需要进行调查。<br>这篇文章会对您大有帮助。<br>此外，如果您知道这里没有的信息，积极提供给他们，也能帮助到许多人。 |
