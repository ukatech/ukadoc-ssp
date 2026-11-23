# 启动选项列表

启动 ssp.exe 时可以附加以下选项（开关）。

## 什么是启动选项？

启动 Windows 软件时，可以通过启动选项切换设置后再运行。<br>
有关详情，请搜索“运行选项”“命令行选项”或“启动选项”等词语。

## 使用方法

使用方法有多种。<br>
例如，也可以通过“命令提示符”或“运行”使用。<br>
这里介绍如何为特定选项创建专用快捷方式。

1. 创建 ssp.exe 的快捷方式。<br>
   例如：右键单击 ssp.exe→创建快捷方式
2. 打开所创建快捷方式的属性。<br>
   例如：右键单击快捷方式→属性
3. 确认属性的“目标”栏中有 ssp.exe 的路径，然后用“""”将整个路径括起来。
4. 在括起来的路径后输入一个半角空格，再输入下方的启动选项。<br>
   例如："C:/User/Document/略/SSP/ssp.exe" --random
5. 按“确定”按钮关闭属性，再给快捷方式起一个容易辨认的名称。<br>
   例如：SSP-随机启动
6. 运行该快捷方式时，与直接启动 ssp.exe 不同，SSP 将以应用了选项设置的状态启动。

## 选项列表

建议各选项使用 `--オプション名` 格式。为保持向后兼容，仍可使用 `/x` / `-x` 格式的短选项。

对于需要值的选项，请像 `--オプション名 値` 一样，用半角空格分隔选项名和值。如果值中包含空格，请用“""”括起来。

2.8.97 及以后版本也支持 `--オプション名=値` 格式（例如：`--sstp-listen=9900`）。本页面以空格分隔的格式为主。请注意，`/x` 格式的短选项不能使用 `=` 格式。

- [--option 选项](#--option-オプション)
- [一般选项](#一般オプション)
- [离线 Surface 转储](#オフラインサーフェスダンプ)
- [离线工具](#オフラインツール)
- [其他](#その他)

### --option 选项

--option 选项可以用逗号分隔，指定多个值（例如：`--option bootunlock,standalone`）。

| 开关 | 功能 |
|---|---|
| --option nobootcheck<br>（旧版：/o nobootcheck） | 禁用异常退出检查 |
| --option layered<br>（旧版：/o layered） | 启用半透明窗口 |
| --option region<br>（旧版：/o region） | 禁用半透明窗口（区域模式） |
| --option bootunlock<br>（旧版：/o bootunlock） | 跳过重复启动检查 |
| --option standalone<br>（旧版：/o standalone） | 当 SSP.exe 已经运行时，禁用将安装或启动人格等操作委托给运行中的 SSP.exe 的机制，始终由当前进程自行启动人格或执行安装。<br>如 --option bootunlock,standalone 所示，与跳过重复启动检查的选项一起指定，即可在完全没有警告的情况下启动多个 SSP.exe。 |
| --option kiosk<br>（旧版：/o kiosk） | 启用 KIOSK 模式。行为如下。 \[2.6.54～\]<br>启用 --option bootunlock,standalone<br>alignmenttodesktop 始终为 free<br>不接受鼠标和键盘输入<br>完全不干预重复启动检查<br>不显示通知区域图标和任务栏图标<br>不保存由 SSP 管理的人格和外壳设置<br>不显示启动中的窗口<br>不发出错误通知 |
| --option readonly<br>（旧版：/o readonly） | 启用只读模式。 \[2.8.96 及以后版本\]<br>启动时不对用户环境进行任何持久性更改。适用于不想影响设置而测试功能，或在他人的电脑上临时运行 SSP 等情况。<br>屏幕上的行为和与人格的交互与平常相同，不会像 KIOSK 模式那样屏蔽输入或限制显示。此模式独立于 KIOSK 模式，也可以像 --option kiosk,readonly 一样同时使用。<br><br>行为如下。<br>启用 --option bootunlock,standalone（因为如果将操作委托给运行中的 SSP，就会由该进程写入设置）<br>完全不干预重复启动检查<br>不保存任何首选项、人格、外壳、对话框和插件设置<br>不保存启动历史、使用统计、缓存、Cookie、vanish 记录、SSTP 设置、POP 设置，以及伺か (Ukagaka) 即时通讯的信息和日志<br>不保存日历中的日程（schedule.ics）<br>不共享存档数据（既不导出到云端，也不从云端恢复到本地）<br>不写入注册表。不进行文件关联、创建快捷方式、注册跳转列表或添加到“最近使用的项目”<br>不更改桌面壁纸和背景颜色<br>不清空回收站<br>即使发生 vanish，也不删除人格文件夹<br>不自动更新 SSP 本体、人格、对话框、插件和语言资源。也不进行手动在线更新或 NAR 安装<br>不安装 `initial_install.nar`<br>不通过 SNTP 进行 NTP 时间同步<br><br>设置值本身仍可照常更改，但退出时不会写回文件，因此下次启动时不会保留。<br>运行所需的临时文件（临时文件夹）仍会照常创建，并在退出时删除。 |
| --option dontloadmodule<br>（旧版：/o dontloadmodule） | 不加载 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 类模块 |
| --option dpiaware<br>（旧版：/o dpiaware） | 将 DPI 感知模式设为 Per-Monitor V2 后启动 |
| --option callghost<br>（旧版：/o callghost） | 与 --install 同时使用时，安装完成后自动调用人格。 |
| --option deletesource<br>（旧版：/o deletesource） | 与 --install 同时使用时，在 NAR 安装成功后删除 NAR。 |

### 常规选项

| 开关 | 功能 |
|---|---|
| --fmo-name FMO名称<br>（旧: /f FMO名称） | 强制将写入的 FMO 名称更改为指定名称。 |
| --random<br>（旧: /r） | 不受设置影响，随机启动人格。 |
| --ghost 文件夹名/人格名<br>（旧: /g 文件夹名/人格名） | 启动指定的人格。以空格分隔可启动多个人格。2.9.35以后的版本中，除了文件夹名/人格名，还可以指定人格的 UUID（属性系统中的 `uuid`，形如 `R5dVNluBvKjtQqjP0dAuoA==`）。在启动 SSP 时指定的情况下，会将指定的第一个人格作为第1组人格启动。<br>2.8.99以后的版本中，在启动 SSP 时指定人格文件夹的绝对路径（例：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`），如果该人格不在人格读取文件夹中，会将其父文件夹（本例中为 `C:\Users\user\Desktop\`）临时添加到人格读取文件夹中并启动，仅在本次运行期间有效。只支持存在 `ghost\master\descript.txt` 的文件夹。<br>临时添加的文件夹不会保存到设置中，在文件夹设置画面中显示为「(temporary)」，无法编辑或删除，也不会作为人格的安装目标候选。如果在文件夹设置画面中手动添加同一个文件夹，则会将其保存为普通的读取文件夹。<br>如果 SSP 已经启动（即指定内容被传递给运行中的 SSP），则不会执行此处理。 |
| --help<br>（旧: /?） | 在浏览器中打开启动选项的帮助页面。 |
| --help 文件名<br>（旧: /? 文件名） | 在浏览器中打开指定文件名的帮助页面。 |
| --ukagaka-link x-ukagaka-link:URL<br>（旧: /m x-ukagaka-link:URL） | 执行与打开 x-ukagaka-link:URL 相同的操作。在启动 SSP 时指定的情况下，会等待第1组人格启动后再执行。 |
| --install NAR文件名<br>（旧: /i NAR文件名） | 安装 NAR。如果已有运行中的 SSP，则由运行中的 SSP 执行安装；否则自行安装后继续启动。<br>以空格分隔指定多个 NAR 时，会依次安装。<br>即使接收安装任务的 SSP 正显示未安装人格的警告对话框（「请想办法」对话框），也可以处理。<br>此外，在这种情况下如果还指定了 --option callghost，则会自动按下警告对话框中的继续启动按钮，继续启动。 |
| --ssf SSF文件名<br>（旧: /s SSF文件名） | 执行 [SSF 文件](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。在启动 SSP 时指定的情况下，会等待第1组人格启动后再执行。 |
| --windowmode 模式 \[可省略\] | 2.8.78～ 以实验性功能"[窗口模式](windowmode.md)"启动。将窗口内部视为一个虚拟屏幕，在其中启动人格，方便进行截图等操作，也可避免影响整个桌面。<br>2.8.86～ 可以指定模式。可指定的模式如下。省略时遵循上次的设置（初始值为 shared）。<br>shared：将所有运行中的人格集中在一个窗口中。<br>perghost：为每个人格分别创建一个窗口。<br>2.8.86以后的版本会将窗口模式的状态保存为设置，因此即使不指定此选项，也会以上次的状态启动。如需关闭，可通过右键菜单的「设置」或首选项中的「直播」进行切换。 |
| --sstp-listen 监听地址 | 临时指定 SSTP 服务器的监听地址并启动。 \[2.8.97以后的版本\]<br>不读取已保存的 SSTP 服务器监听设置，仅在指定的地址上监听。<br>本次运行期间的监听设置不会保存。首选项中的 SSTP 服务器列表仅供查看，无法添加、删除或切换启用/禁用状态。<br>此选项适合与 --option readonly 组合使用，以启动不干扰其他运行中的 SSP 的测试用 SSP。<br><br>可以用逗号分隔来指定多个监听地址。格式如下。<br>端口号：在 IPv4 和 IPv6 的回环地址（127.0.0.1 和 ::1）上监听。例：9801<br>localhost:端口号：与仅指定端口号时相同。<br>IPv4地址:端口号：仅在指定的地址上监听。指定 0.0.0.0 时，在所有 IPv4 接口上监听。例：192.168.0.5:9801<br>\[IPv6地址\]:端口号：IPv6 地址需用 \[\] 括起来。指定 \[::\] 时，在所有 IPv6 接口上监听。例：\[::1\]:9801<br>none：不监听任何地址。省略监听地址时也相同。<br><br>地址须以数字形式指定（除 localhost 外，不能使用主机名）。<br>格式不正确或监听失败的地址会被忽略，并记录到错误日志中。此时也不会恢复已保存的设置。<br>请注意，指定回环地址以外的地址后，将会接收来自其他电脑的 SSTP。<br><br>例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字体名 \[2.8.75以后的版本\] | 指定 GUI 使用的字体。并非所有字体都会被替换，目前菜单的部分内容和标题栏等不会改变。 |

### 离线表面导出

| 选项 | 功能 |
|---|---|
| --offline-dump 文件夹路径 | 以离线导出模式启动。无需实际启动人格，读取指定人格文件夹中的 surfaces.txt，导出表面图像后立即退出。不会加载 SHIORI/MAKOTO/PIRO，也不会创建窗口和消息循环。<br>参数指定人格的文件夹路径（末尾的 \\ 可省略）。<br>从 2.8.98 起，为离线导出相关选项（此选项、--dump-output-dir、--dump-error-log）指定相对路径时，以启动 SSP 时的当前目录为基准解析。<br><br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 文件夹名或名称 \[可省略\] | 与 --offline-dump 组合使用。通过文件夹名（即 shell 下的相对路径）或名称指定要导出的外壳。省略时使用 descript.txt 中指定的默认外壳（通常为 master）。<br>从 2.8.98 起，如果找不到指定的外壳，不会使用默认外壳导出，而是在错误日志中记录 Error，且不输出任何内容。 |
| --dump-scope (作用域ID) \[可省略\] | 与 --offline-dump 组合使用。指定导出图像的作用域 ID。省略时为 0。 |
| --dump-surface-list 列表 \[可省略\] | 与 --offline-dump 组合使用。以逗号分隔指定要导出的表面。surface 编号的前缀（surface）可以省略。也可以使用 [surfaces.txt 的表面 ID 指定扩展格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>示例：`--dump-surface-list "0,1,10"`<br>省略此选项时不会导出表面（可与 --dump-error-log 组合使用，仅输出解析错误）。<br>从 2.8.98 起，不仅第一个元素，各个元素的前缀都可以省略（如 `"0,surface1"`）。此外，如果通过单独编号而非范围指定的表面不存在，会在错误日志中记录 Warning（范围指定中缺失的编号不会记录）。 |
| --dump-output-dir 目录 \[可省略\] | 与 --offline-dump 组合使用。指定导出图像的输出目录。省略时使用当前目录（2.8.97 及更早版本中，省略时不会执行导出）。 |
| --dump-output-prefix 前缀 \[可省略\] | 与 --offline-dump 组合使用。指定输出文件名中表面编号前面的部分。默认的「surface」会被此字符串替换（而不是在其前面添加）。省略时为「surface」。<br>示例：使用 `--dump-output-prefix "x_"` 时，表面 0 的文件名为 `x_0.png`（而不是 `x_surface0.png`）。 |
| --dump-error-log 文件路径 \[可省略\] | 与 --offline-dump 组合使用。将加载外壳时的错误日志（如 surfaces.txt 的解析错误）写入指定路径。<br>省略 --dump-surface-list，只指定此选项，即可不执行导出，仅进行错误检查。<br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>输出格式：带 BOM 的 UTF-8 CSV（换行符为 CRLF）。每行一条记录，各列用 " 括起，列中的 " 转义为 ""。<br>`"時刻","ゴースト名","レベル","内容"`<br>时间：HH:MM:SS 格式。<br>级别：Info / Notice / Warning / Error / Critical / System 之一。<br>内容：日志正文。从 2.8.94 起，SERIKO 相关日志会附带定义所在的文件（相对于人格文件夹的路径）和行号，如 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。重复定义的日志还会以 `(ファイル名:Line=n)` 的形式附带先前定义的位置。<br>从 2.8.94 起，指定此选项时最多保留 10000 条日志，也不会将内容相似的日志合并为摘要行（System 级别），因此不会遗漏日志。<br>如果没有任何日志，则不会创建文件（即使同一路径已有文件，也不会覆盖或删除）。<br><br>退出代码：从 2.8.94 起，进程会根据已记录日志中的最高严重级别返回相应的退出代码。<br>0：没有日志，或只有 Info/Notice<br>1：存在 Warning（没有 Error/Critical）<br>2：存在 Error（没有 Critical）<br>3：存在 Critical<br>如果人格本身加载失败（如无法读取指定文件夹中的 descript.txt），则不会输出日志，退出代码也为 0。 |
| --dump-surface-option 选项 \[可省略\] \[2.8.57起\] | 指定离线导出功能的选项。可指定以下选项。<br>backlog：裁剪与历史记录功能相同的区域（面部周围）。但不进行缩放，直接输出合成图像。<br>collision：在输出图像上绘制碰撞判定（collision）的形状和名称。与开发用面板中的碰撞判定显示相同，但名称始终显示，且不绘制表面外框、有效范围、重叠判定范围等外接矩形。\[2.8.98起\]<br>从 2.8.98 起，可以用逗号分隔指定多个选项（示例：`--dump-surface-option backlog,collision`）。<br>如果此选项未指定 collision，则无论用户设置（开发用面板中的碰撞判定显示）如何，都不会绘制碰撞判定。 |
| --dump-bind 换装指定 \[可省略\] \[2.9.05起\] | 与 --offline-dump 组合使用。指定导出时的换装状态。<br>可以用分号分隔指定多个「类别名,部件名,ON/OFF」。含义与 [`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_) 相同，在设置为互斥的类别中将某个部件设为 ON 时，同一类别中的其他部件会变为 OFF。<br>部件名留空或设为 `__ALL__` 时，类别中的所有部件都成为操作对象。<br>ON/OFF 使用 1 或 true 表示 ON，使用 0 或 false 表示 OFF。省略时视为 ON（`\![bind]` 省略时会反转，但此处不会反转）。<br>示例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基准状态为外壳的 descript.txt 中指定的各部件默认值（`sakura.bindgroup*.default`），不会使用用户上次换装的状态（`shell\profile` 中的保存值）。只有指定的部件会在此基准上更改。<br>换装应用于 --dump-scope 指定的作用域。<br>如果指定了不存在的类别或部件，会记录 Warning 日志（--dump-error-log 的退出代码为 1），仅忽略该指定并继续导出。<br>类别名和部件名前后的空白不会被去除，因此请勿在逗号后添加空格。 |
| --dump-animation 动画ID \[可省略\] \[2.9.05起\] | 与 --offline-dump 组合使用。与 `\i[ID]` 一样播放指定动画，并以连续编号输出各帧图像。只能指定一个 ID（除了数字，也可以像 `\i[ID]` 一样使用在 surfaces.txt 中为动画设置的名称）。<br>对于每个表面，首先将与普通导出相同的图像（runonce 动画播放一轮后的状态）输出为 `surface0.png`，然后每当指定动画的模式前进一步，就以从 0 开始的 4 位连续编号输出 `surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix 和 --dump-surface-option 的设置也会应用于连续编号的图像。<br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always 等动画与普通导出时一样运行，指定动画会叠加在其上。只有指定动画自身的模式会生成连续编号图像，always 动画前进不会增加图像数量。<br>指定动画进行到最后一个模式时（always 的情况下为播放一轮时）结束。如果被其他动画的 stop 或互斥机制停止，也会在该处结束。<br>由 start、alternativestart、parallelstart 启动的其他动画不会生成连续编号图像。如果指定动画包含这些模式，会记录 Warning 日志（输出会继续）。<br>由于 start、stop 类模式不会改变图像，因此不计为连续编号中的一帧。<br>如果指定 ID 在该表面中不存在，或因换装使其无效、处于互斥状态等原因无法播放，则会记录 Warning 日志，该表面只输出一张普通图像。<br>连续编号图像最多为 10000 张（到 `_9999` 为止），达到上限时会记录 Warning 日志并停止。 |

### 离线工具

| 开关 | 功能 |
|---|---|
| --offline-tool 类型 \[2.9.01及以后版本\] | 以离线工具模式启动。无需启动人格，即可从 --target-dir 指定的文件夹创建 NAR、更新定义文件或压缩包，然后立即退出。不会触发任何人格事件，也不会创建窗口或消息循环。<br>其处理过程与 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 相同，但输出位置没有限制（如仅限 SSP 管理的文件夹等），可以自由指定。<br>类型指定为以下任意一种（不区分大小写）。<br><br>nar：创建 NAR 文件。`developer_options.txt` 中的 nonar 指定、.narignore 等排除规则与通常创建 NAR 时一样生效。如果文件夹根目录下没有 install.txt，则根据 descript.txt（或 `ghost\master\descript.txt`）判断类型和名称，在目标文件夹中创建 install.txt 后将其打包。如果无法判断类型和名称，则创建失败。<br>updatedata：创建更新定义文件。如果 --output 的文件名以 .dau 结尾，则使用与 updates2.dau 相同的格式；否则使用 updates.txt 格式。只创建指定的一个文件，不会创建或删除目标文件夹根目录及 `ghost\master` 下的 updates2.dau / updates.txt。`developer_options.txt` 中的 noupdate 指定、.updateignore 等排除规则与通常一样生效。<br>archive：直接压缩目标文件夹。不读取 .narignore 等排除规则（不打包隐藏文件和隐藏文件夹）。格式由 --output 的扩展名决定，.7z 使用 7z 格式，其他扩展名使用 zip 格式。<br><br>无论指定哪种类型，如果输出文件已存在，都会将其覆盖。如果输出位置位于目标文件夹内，则不会打包该文件本身。输出文件夹必须事先存在。<br>如果为 --target-dir、--output 指定相对路径，则以启动 SSP 时的当前目录为基准解析。<br><br>退出代码：<br>0：成功<br>1：参数无效（类型未知、未指定 --target-dir 或 --output、--target-dir 不存在或不是文件夹）<br>2：创建失败（无法写入输出位置、无法判断 NAR 的类型和名称、updatedata 遇到无法读取的文件或过深的层级（超过32层）等）。失败时也可能留下创建了一部分的文件<br><br>示例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>示例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>示例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 文件夹路径 \[2.9.01及以后版本\] | 与 --offline-tool 配合使用（必需）。指定要处理的文件夹（末尾的\\可省略）。创建 NAR 或更新定义文件时，指定人格等的根文件夹（包含 descript.txt、install.txt 和 ghost 文件夹的文件夹）。 |
| --output 文件路径 \[2.9.01及以后版本\] | 与 --offline-tool 配合使用（必需）。指定要创建的文件的路径。 |
| --password 密码 \[可省略\] \[2.9.01及以后版本\] | 与 --offline-tool 的 nar 或 archive 配合使用。使用指定的密码创建 AES 加密的 ZIP 文件（7z 格式使用 7z 的加密方式）。使用 updatedata 时会忽略此参数。<br>密码会以明文留在命令行中，请注意妥善处理。 |

### 其他

| 开关 | 功能 |
|---|---|
| `initial_install.nar` | 虽然这不是启动选项，但如果在与 ssp.exe 相同的文件夹中放置名为<strong>`initial_install.nar`</strong>的 NAR 文件，SSP 启动时会静默（不显示确认对话框）覆盖安装该文件。安装完成后，`initial_install.nar`会自动删除。可用于将人格等与 SSP 一同打包分发的场景。 \[2.7.52～\] |
