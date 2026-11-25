# 启动选项列表

启动 ssp.exe 时可以附加以下选项（开关）。

## 什么是启动选项？

启动 Windows 软件时，可以通过启动选项切换设置后运行。<br>
如需了解详情，请搜索“运行时选项”“命令行选项”或“启动选项”等词语。

## 使用方法

有多种使用方法。<br>
例如，也可以通过“命令提示符”或“运行”使用。<br>
这里介绍如何创建专门用于启动选项的快捷方式。

1. 创建 ssp.exe 的快捷方式。<br>
   例：右键单击 ssp.exe→创建快捷方式
2. 打开创建的快捷方式的属性。<br>
   例：右键单击快捷方式→属性
3. 确认属性的“目标”栏中有 ssp.exe 的路径后，用“""”将整个路径括起来。
4. 在括起来的路径后添加一个半角空格，然后输入下列启动选项。<br>
   例："C:/User/Document/略/SSP/ssp.exe" --random
5. 按“确定”按钮关闭属性，再为快捷方式取一个容易辨认的名称。<br>
   例：SSP-随机启动
6. 运行该快捷方式时，与普通启动 ssp.exe 不同，SSP 会以应用了选项设置的状态启动。

## 选项列表

建议各选项使用 `--オプション名` 格式。为保持向后兼容，仍可使用 `/x` / `-x` 格式的短选项。

对于需要值的选项，请像 `--オプション名 値` 这样，用半角空格分隔选项名和值。如果值中包含空格，请用“""”括起来。

从 2.8.97 起，也支持 `--オプション名=値` 格式（例：`--sstp-listen=9900`）。本页面主要采用空格分隔的写法。请注意，`/x` 格式的短选项不能使用 `=` 格式。

- [--option 选项](#--option-オプション)
- [常规选项](#一般オプション)
- [离线 Surface 转储](#オフラインサーフェスダンプ)
- [离线工具](#オフラインツール)
- [其他](#その他)

### --option 选项

--option 选项可以用逗号分隔，指定多个值（例：`--option bootunlock,standalone`）。

| 开关 | 功能 |
|---|---|
| --option nobootcheck<br>（旧: /o nobootcheck） | 禁用异常退出检查 |
| --option layered<br>（旧: /o layered） | 启用半透明窗口 |
| --option region<br>（旧: /o region） | 禁用半透明窗口（区域模式） |
| --option bootunlock<br>（旧: /o bootunlock） | 跳过重复启动检查 |
| --option standalone<br>（旧: /o standalone） | 如果 SSP.exe 已在运行，则禁用将安装、启动人格等操作委托给运行中的 SSP.exe 的机制，始终由自身启动人格或执行安装。<br>与跳过重复启动检查一起指定，例如 --option bootunlock,standalone，即可完全不显示警告地启动多个 SSP.exe。 |
| --option kiosk<br>（旧: /o kiosk） | 启用 KIOSK 模式。行为如下。 \[2.6.54～\]<br>启用 --option bootunlock,standalone<br>alignmenttodesktop 始终为 free<br>不接受鼠标和键盘输入<br>完全不干扰重复启动检查<br>不显示通知区域图标和任务栏图标<br>不保存由 SSP 管理的人格和外壳设置<br>不显示表示正在启动的窗口<br>不发送错误通知 |
| --option readonly<br>（旧: /o readonly） | 启用只读模式。 \[2.8.96以后\]<br>启动时不会对用户环境进行任何持久性更改。适用于希望在不影响设置的情况下测试运行，或在他人的电脑上临时运行 SSP 等情况。<br>屏幕上的行为以及与人格的互动均与通常相同，不会像 KIOSK 模式那样屏蔽输入或限制显示。此模式独立于 KIOSK 模式，也可以像 --option kiosk,readonly 这样组合使用。<br><br>行为如下。<br>启用 --option bootunlock,standalone（因为如果将操作委托给运行中的 SSP，后者会写入设置）<br>完全不干扰重复启动检查<br>不保存首选项、人格、外壳、对话框和插件的任何设置<br>不保存启动历史、使用统计、缓存、Cookie、vanish 记录、SSTP 设置、POP 设置、伺か即时通讯的信息和日志<br>不保存日历的日程（schedule.ics）<br>不进行存档数据共享（既不向云端导出，也不从云端恢复到本地）<br>不写入注册表。不进行文件关联、创建快捷方式、注册跳转列表或添加到“最近使用的项目”<br>不更改桌面壁纸和背景色<br>不清空回收站<br>即使发生 vanish 也不删除人格文件夹<br>不自动更新主体、人格、对话框、插件和语言资源。也不进行手动在线更新或安装 NAR<br>不安装 `initial_install.nar`<br>不通过 SNTP 进行 NTP 时间同步<br><br>仍可正常更改设置值，但退出时不会写回文件，因此下次启动时不会保留。<br>运行所需的临时文件（临时文件夹）仍会照常创建，并在退出时丢弃。 |
| --option dontloadmodule<br>（旧: /o dontloadmodule） | 不载入 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 类模块 |
| --option dpiaware<br>（旧: /o dpiaware） | 将 DPI 感知模式设为 Per-Monitor V2 后启动 |
| --option callghost<br>（旧: /o callghost） | 与 --install 同时使用时，安装完成后会自动调用人格。 |
| --option deletesource<br>（旧: /o deletesource） | 与 --install 同时使用时，成功安装 NAR 后会删除该 NAR。 |

### 常规选项

| 开关 | 功能 |
|---|---|
| --fmo-name FMO名<br>（旧版: /f FMO名） | 强制将写入的FMO名改为指定名称。 |
| --random<br>（旧版: /r） | 不论设置如何，随机启动人格 |
| --ghost 文件夹名/人格名<br>（旧版: /g 文件夹名/人格名） | 启动指定的人格。以空格分隔可启动多个人格。从2.9.35开始，也可以指定人格的UUID（属性系统中的`uuid`，形式如`R5dVNluBvKjtQqjP0dAuoA==`），代替文件夹名/人格名。在SSP启动时指定的情况下，会将指定人格中的第一个作为第1组人格启动。<br>从2.8.99开始，在SSP启动时指定人格文件夹的绝对路径（例：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`）时，如果该人格不在载入文件夹中，则仅在本次运行期间将其父文件夹（本例中为 `C:\Users\user\Desktop\`）临时添加到人格载入文件夹后启动。仅适用于存在 `ghost\master\descript.txt` 的文件夹。<br>临时添加的文件夹不会保存到设置中，在文件夹设置界面中显示为「(temporary)」，无法编辑或删除，也不会成为人格的安装位置候选项。如果通过文件夹设置界面明确添加同一文件夹，则会作为普通载入文件夹保存。<br>如果SSP已经启动（指定内容被传递给运行中的SSP），则不会执行此处理。 |
| --help<br>（旧版: /?） | 在浏览器中打开启动选项的帮助页面 |
| --help 文件名<br>（旧版: /? 文件名） | 在浏览器中打开指定文件名的帮助页面 |
| --ukagaka-link x-ukagaka-link:URL<br>（旧版: /m x-ukagaka-link:URL） | 执行与打开x-ukagaka-link:URL时相同的操作。在SSP启动时指定的情况下，会等待第1组人格启动后再执行。 |
| --install NAR文件名<br>（旧版: /i NAR文件名） | 安装NAR。如果有正在运行的SSP，则将安装处理交给它；否则自行完成安装处理后继续启动。<br>以空格分隔指定多个文件时，会按顺序安装多个NAR。<br>即使接收安装任务的SSP正在显示未安装人格的警告对话框（「请想办法处理」对话框），也可以处理。<br>此外，在此情况下如果同时指定 --option callghost，则会自动按下警告对话框中的继续启动按钮，继续启动。 |
| --ssf SSF文件名<br>（旧版: /s SSF文件名） | 运行[SSF文件](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。在SSP启动时指定的情况下，会等待第1组人格启动后再执行。 |
| --windowmode 模式 \[可省略\] | 2.8.78起：以实验性功能“[窗口模式](windowmode.md)”启动。将窗口内部视为一个虚拟屏幕来启动人格，方便进行捕获等操作，并避免影响整个桌面。<br>2.8.86起：可以指定模式。可指定的模式如下。省略时遵循上次的设置（初始值为shared）。<br>shared：将所有运行中的人格集中在一个窗口中。<br>perghost：为每个人格分别提供一个窗口。<br>2.8.86及以后版本会将窗口模式的状态保存为设置，因此即使不加此选项，也会以上次的状态启动。如需关闭，请在右键菜单的「设置」或首选项的「直播」中切换。 |
| --sstp-listen 监听地址 | 临时指定SSTP服务器的监听地址并启动。 \[2.8.97及以后版本\]<br>不会读取已保存的SSTP服务器监听设置，只在指定的监听地址上监听。<br>本次运行期间的监听设置不会保存。首选项中的SSTP服务器列表仅供查看，无法添加、删除或切换启用/禁用状态。<br>此选项旨在与 --option readonly 组合使用，启动一个不会干扰其他运行中的SSP的测试用SSP。<br><br>可以用逗号分隔指定多个监听地址。格式如下。<br>端口号：在IPv4和IPv6的环回地址（127.0.0.1 和 ::1）上监听。例：9801<br>localhost:端口号：与仅指定端口号时相同。<br>IPv4地址:端口号：仅在指定地址上监听。指定 0.0.0.0 时，在所有IPv4接口上监听。例：192.168.0.5:9801<br>\[IPv6地址\]:端口号：IPv6地址用\[\]括起。指定 \[::\] 时，在所有IPv6接口上监听。例：\[::1\]:9801<br>none：不进行任何监听。省略监听地址时也相同。<br><br>地址须以数字指定（localhost 除外，不能使用主机名）。<br>格式不正确或监听失败的监听地址会被忽略，并记录到错误日志中。此时也不会恢复已保存的设置。<br>请注意，指定环回地址以外的地址后，将允许接收来自其他PC的SSTP。<br><br>例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字体名 \[2.8.75及以后版本\] | 指定GUI使用的字体。并非所有字体都会被替换，部分菜单和标题栏等目前不会改变。 |
| --time-shift 值 \[2.9.39及以后版本\] | 在启动时指定「虚拟更改当前时间」（时间机器）的时间偏移量。用于测试依赖日期或时间的人格。<br>请使用 `--time-shift=+3600` 这样的格式，以 `=` 连接选项和值（因为以 `-` 开头的值在用空格分隔时无法与选项名区分）。<br>此指定仅在本次运行期间有效，不会保存到设置中。即使设置中保存了偏移量，也会优先使用此指定值。<br><br>值可以是以下任一种。<br>+秒数 或 -秒数：直接指定偏移量（秒数）。必须带符号。例：+86400（1天后）、-3600（1小时前）<br>0：将偏移量设为0（保持实际时间）。<br>ISO8601格式的日期时间：计算与实际时间的差值作为偏移量，使时间变为指定日期时间。未指定时区时视为本地时间。时钟不会停止，而是从该日期时间继续前进。例：2026-12-31T23:59:50<br><br>偏移量的大小上限约为200年，不足一秒的部分会被舍去。无法解析的值会被忽略（偏移量保持为0），并记录到错误日志中。<br>使用此指定启动时，不会显示关于设置中残留偏移量的提醒（面向开发者的对话框）。<br><br>例：`ssp.exe --option readonly --time-shift=2026-12-31T23:59:50` |
| --allow-timemachine-control \[2.9.39及以后版本\] | 允许运行期间通过Sakura Script `\![timemachine,set,値]` / `\![timemachine,reset]` 和SSTP的EXECUTE `SetTimeShift` 操作「虚拟更改当前时间」。用于测试。<br>启动时未指定此选项的情况下，这些操作不会执行任何动作，并会在错误日志中记录警告（以防人格的脚本或外部程序更改全局时钟）。<br>偏移量的值格式与 --time-shift 相同。 |

### 离线 Surface 导出

| 开关 | 功能 |
|---|---|
| --offline-dump 文件夹路径 | 以离线导出模式启动。不实际启动人格，而是读取指定人格文件夹中的 surfaces.txt，导出 surface 图像后立即退出。不会加载 SHIORI/MAKOTO/PIRO，也不会创建窗口和消息循环。<br>参数指定人格的文件夹路径（末尾的\\可有可无）。<br>从 2.8.98 起，如果为离线导出相关选项（此选项、--dump-output-dir、--dump-error-log）指定相对路径，将以启动 SSP 时的当前目录为基准解析。<br><br>例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 文件夹名或名称 \[可省略\] | 与 --offline-dump 组合使用。通过文件夹名（即相对于 shell 的路径）或名称指定要导出的外壳。省略时使用 descript.txt 中指定的默认外壳（通常为 master）。<br>从 2.8.98 起，如果找不到指定的外壳，不会使用默认外壳导出，而是在错误日志中记录 Error，且不输出任何内容。 |
| --dump-scope (作用域ID) \[可省略\] | 与 --offline-dump 组合使用。指定导出图像的作用域 ID。省略时为 0。 |
| --dump-surface-list 列表 \[可省略\] | 与 --offline-dump 组合使用。以逗号分隔的方式指定要导出的 surface。surface 编号的前缀（surface）可以省略。也可以使用 [surfaces.txt 中指定 surface ID 的扩展格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>例：`--dump-surface-list "0,1,10"`<br>省略此选项时不会导出 surface（可以与 --dump-error-log 组合使用，仅输出解析错误）。<br>从 2.8.98 起，不仅首个元素，每个元素都可以省略前缀（如 `"0,surface1"`）。此外，如果以单个编号而非范围指定的 surface 不存在，将在错误日志中记录 Warning（范围内缺失的编号不予记录）。 |
| --dump-output-dir 目录 \[可省略\] | 与 --offline-dump 组合使用。指定导出图像的输出目录。省略时使用当前目录（2.8.97 及更早版本中，省略时不会导出）。 |
| --dump-output-prefix 前缀 \[可省略\] | 与 --offline-dump 组合使用。指定输出文件名中 surface 编号之前的部分。默认的「surface」会被此字符串替换（而非附加）。省略时为「surface」。<br>例：使用 `--dump-output-prefix "x_"` 时，surface 0 的文件名为 `x_0.png`（而非 `x_surface0.png`）。 |
| --dump-error-log 文件路径 \[可省略\] | 与 --offline-dump 组合使用。将加载外壳时的错误日志（如 surfaces.txt 的解析错误）写入指定路径。<br>省略 --dump-surface-list 而仅指定此选项，可以不执行导出，只进行错误检查。<br>例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>输出格式：带 BOM 的 UTF-8 CSV（换行符为 CRLF）。每行一条记录，各列用 " 括起，列中的 " 转义为 ""。<br>`"時刻","ゴースト名","レベル","内容"`<br>时间：HH:MM:SS 格式。<br>级别：Info / Notice / Warning / Error / Critical / System 之一。<br>内容：日志正文。从 2.8.94 起，SERIKO 相关日志会附带定义所在的文件（相对于人格文件夹的路径）和行号，例如 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。重复定义的日志还会以 `(ファイル名:Line=n)` 的形式一并标明先前定义的位置。<br>从 2.8.94 起，指定此选项时最多保留 10000 条日志，也不会将内容相似的日志合并为摘要行（级别为 System），因此不会遗漏日志。<br>如果没有任何日志，则不会创建文件（即使同一路径已有文件，也不会覆盖或删除）。<br><br>退出代码：从 2.8.94 起，进程根据记录的日志中最严重的级别返回退出代码。<br>0：没有日志，或仅有 Info/Notice<br>1：有 Warning（无 Error/Critical）<br>2：有 Error（无 Critical）<br>3：有 Critical<br>如果人格本身加载失败（如无法读取指定文件夹中的 descript.txt），则不会输出日志，退出代码也为 0。 |
| --dump-surface-option 选项 \[可省略\] \[2.8.57起\] | 指定离线导出功能的选项。可指定的选项如下。<br>backlog：裁剪与历史记录功能相同的区域（脸部周围）。但不进行缩放，直接输出合成图像。<br>collision：在输出图像中绘制碰撞判定（collision）的形状和名称。与开发用面板中的碰撞判定显示相同，但名称始终显示，且不绘制 surface 外框、有效范围、重叠判定范围等的外接矩形。\[2.8.98起\]<br>从 2.8.98 起，可以用逗号分隔指定多个选项（例：`--dump-surface-option backlog,collision`）。<br>如果此选项未指定 collision，则无论用户设置如何（开发用面板中的碰撞判定显示），都不会绘制碰撞判定。 |
| --dump-bind 换装指定 \[可省略\] \[2.9.05起\] | 与 --offline-dump 组合使用。指定导出时的换装状态。<br>可以用分号分隔指定多个「类别名,部件名,ON/OFF」。含义与 [`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_) 相同：在互斥类别中将某部件设为 ON 时，同一类别中的其他部件会变为 OFF。<br>部件名留空或设为 `__ALL__` 时，以类别中的所有部件为对象。<br>ON/OFF 使用 1 或 true 表示 ON，0 或 false 表示 OFF。省略时按 ON 处理（`\![bind]` 省略时会反转状态，此处不会反转）。<br>例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基准状态是外壳的 descript.txt 中指定的各部件默认状态（`sakura.bindgroup*.default`），不会使用用户最后一次换装的状态（`shell\profile` 中保存的值）。只有指定的部件会在此基础上更改。<br>换装应用于 --dump-scope 指定的作用域。<br>如果指定了不存在的类别或部件，将记录 Warning 日志（--dump-error-log 的退出代码为 1），仅忽略该项指定并继续导出。<br>类别名和部件名前后的空格不会被去除，因此逗号后不要添加空格。 |
| --dump-animation 动画ID \[可省略\] \[2.9.05起\] | 与 --offline-dump 组合使用。以与 `\i[ID]` 相同的方式播放指定动画，并按序号输出每一帧的图像。只能指定一个 ID（除了数字，也可以像 `\i[ID]` 一样使用 surfaces.txt 中赋予动画的名称）。<br>对于每个 surface，首先将与通常导出相同的图像（runonce 动画播放一轮后的状态）输出为 `surface0.png`，随后每当指定动画的模式推进时，以从 0 开始的 4 位连续编号输出 `surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix 和 --dump-surface-option 的设置也适用于连续编号的图像。<br>例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always 等动画会与通常导出时一样运行，指定动画叠加在其上。只有指定动画自身的模式会生成连续编号的图像，always 动画推进不会增加图像数量。<br>当指定动画推进到最后一个模式时结束（always 动画则在播放一轮后结束）。如果因其他动画的 stop 或互斥而停止，也会在此时结束。<br>由 start、alternativestart、parallelstart 启动的其他动画不会生成连续编号的图像。如果指定动画包含这些模式，将记录 Warning 日志（输出会继续）。<br>start、stop 类模式不会改变图像，因此不计为连续编号中的一帧。<br>如果指定的 ID 在该 surface 中不存在，或因换装而被禁用、处于互斥状态等原因无法播放，将记录 Warning 日志，该 surface 仅输出通常的一张图像。<br>连续编号最多输出 10000 张（到 `_9999` 为止），达到上限时将记录 Warning 日志并终止。 |

### 离线工具

| 开关 | 功能 |
|---|---|
| --offline-tool 类型 \[2.9.01及以后\] | 以离线工具模式启动。不启动人格，而是从 --target-dir 指定的文件夹创建NAR、更新定义文件或压缩包，然后立即退出。不会触发任何人格事件，也不会创建窗口或消息循环。<br>处理方式与 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 等效，但可以自由指定输出位置，不受输出位置限制（例如仅限于SSP管理的文件夹）。<br>类型应指定为以下任意一种（不区分大小写）。<br><br>nar：创建NAR文件。`developer_options.txt` 中的 nonar 指定及 .narignore 等排除规则与通常创建NAR时一样适用。如果文件夹根目录下没有install.txt，则根据descript.txt（或`ghost\master\descript.txt`）判断类型和名称，在目标文件夹中创建install.txt后将其打包。如果无法判断类型和名称，则创建失败。<br>updatedata：创建更新定义文件。如果 --output 的文件名以.dau结尾，则使用与updates2.dau相同的格式，否则使用updates.txt格式，只创建指定的一个文件。不会创建或删除目标文件夹根目录及 `ghost\master` 下的 updates2.dau / updates.txt。`developer_options.txt` 中的 noupdate 指定及 .updateignore 等排除规则与通常情况一样适用。<br>archive：直接压缩目标文件夹。不读取 .narignore 等排除规则（不打包隐藏文件和隐藏文件夹）。格式由 --output 的扩展名决定：.7z为7z格式，其他为zip格式。<br><br>无论使用哪种类型，如果输出文件已存在，都会将其覆盖。如果输出位置在目标文件夹内，不会将该输出文件自身打包。输出文件夹必须事先存在。<br>如果为 --target-dir 或 --output 指定相对路径，将以启动SSP时的当前目录为基准解析。<br><br>退出代码：<br>0：成功<br>1：参数无效（类型未知、未指定 --target-dir 或 --output、--target-dir 不存在或不是文件夹）<br>2：创建失败（无法写入输出位置、无法判断NAR的类型和名称、updatedata中存在无法读取的文件或层级过深（超过32层）等）。失败时也可能留下已创建了一部分的文件<br><br>示例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>示例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>示例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 文件夹路径 \[2.9.01及以后\] | 与 --offline-tool 配合使用（必需）。指定要处理的文件夹（末尾的\\可省略）。创建NAR或更新定义文件时，请指定人格等的根文件夹（包含descript.txt、install.txt或ghost文件夹的文件夹）。 |
| --output 文件路径 \[2.9.01及以后\] | 与 --offline-tool 配合使用（必需）。指定要创建的文件的路径。 |
| --password 密码 \[可省略\] \[2.9.01及以后\] | 与 --offline-tool 的 nar 或 archive 配合使用。使用指定的密码创建AES加密的ZIP文件（7z格式则使用7z加密）。使用 updatedata 时会忽略此选项。<br>密码会原样保留在命令行中，请注意妥善处理。 |

### 其他

| 开关 | 功能 |
|---|---|
| `initial_install.nar` | 虽然这不是启动选项，但如果在ssp.exe所在的文件夹中放置名为<strong>`initial_install.nar`</strong>的NAR文件，SSP启动时会静默覆盖安装（不显示确认对话框）。安装完成后，`initial_install.nar`会自动删除。可用于将人格等与SSP打包分发的情况。 \[2.7.52～\] |
