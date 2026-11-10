# 启动选项列表

启动 ssp.exe 时，可以添加以下选项（开关）。

## 什么是启动选项？

这是 Windows 软件在启动时切换设置并运行的一种机制。<br>
详情请搜索“运行时选项”“命令行选项”或“启动选项”等词语。

## 使用方法

有多种使用方法。<br>
例如，也可以通过“命令提示符”或“运行”来使用。<br>
这里介绍创建专用选项快捷方式的方法。

1. 创建 ssp.exe 的快捷方式。<br>
   例如：右键单击 ssp.exe→创建快捷方式
2. 打开创建好的快捷方式的属性。<br>
   例如：右键单击快捷方式→属性
3. 确认属性中的“目标”栏里有 ssp.exe 的路径，然后用「""」将整个路径括起来。
4. 在括起来的路径后加一个半角空格，然后输入下面的启动选项。<br>
   例如："C:/User/Document/略/SSP/ssp.exe" --random
5. 直接单击“确定”按钮关闭属性，然后给快捷方式取一个容易辨认的名称。<br>
   例如：SSP-随机启动
6. 执行该快捷方式后，启动状态会应用选项设置，与直接启动 ssp.exe 时不同。

## 选项列表

建议使用 `--选项名` 格式指定各选项。为保证向后兼容，也可以继续使用 `/x` / `-x` 格式的短选项。

需要指定值的选项，请使用 `--选项名 值` 的格式，并用半角空格分隔选项名和值。如果值中包含空格，请用「""」括起来。

2.8.97 及之后的版本也支持使用 `--选项名=值` 格式（例如：`--sstp-listen=9900`）。本页以空格分隔的格式为主。另外，`/x` 格式的短选项不能使用 `=` 格式。

- [--option 选项](#--option-オプション)
- [常规选项](#一般オプション)
- [离线外壳转储](#オフラインサーフェスダンプ)
- [离线工具](#オフラインツール)
- [其他](#その他)

### --option 选项

可以用逗号分隔，指定多个 --option 选项（例如：`--option bootunlock,standalone`）。

| 开关 | 功能 |
|---|---|
| --option nobootcheck<br>（旧版：/o nobootcheck） | 禁用异常退出检查 |
| --option layered<br>（旧版：/o layered） | 启用半透明窗口 |
| --option region<br>（旧版：/o region） | 禁用半透明窗口（区域模式） |
| --option bootunlock<br>（旧版：/o bootunlock） | 跳过重复启动检查 |
| --option standalone<br>（旧版：/o standalone） | 如果 SSP.exe 已经在运行，则禁用将安装或启动人格等操作委托给正在运行的 SSP.exe 的机制，始终由当前实例启动人格或进行安装。<br>与跳过重复启动检查的选项一起指定，例如 --option bootunlock,standalone，即可在完全不显示警告的情况下同时启动多个 SSP.exe。 |
| --option kiosk<br>（旧版：/o kiosk） | 启用 KIOSK 模式。其行为如下。 \[2.6.54～\]<br>启用 --option bootunlock,standalone<br>始终将 alignmenttodesktop 设为 free<br>不接受鼠标和键盘输入<br>完全不干预重复启动检查<br>不显示通知区域图标和任务栏图标<br>不保存由 SSP 管理的人格或外壳设置<br>不显示表示正在运行的窗口<br>不显示错误通知 |
| --option readonly<br>（旧版：/o readonly） | 启用只读模式。 \[2.8.96 及之后的版本\]<br>启动时不会对用户环境进行任何永久性更改。适用于想在不影响设置的情况下测试运行，或想在他人的电脑上临时运行 SSP 等情况。<br>屏幕上的行为以及与人格的对话均与平时相同，不会像 KIOSK 模式那样阻止输入或限制显示。此模式独立于 KIOSK 模式，也可以同时启用，例如 --option kiosk,readonly。<br><br>其行为如下。<br>启用 --option bootunlock,standalone（如果将操作委托给正在运行的 SSP，它可能会写入设置）<br>完全不干预重复启动检查<br>不保存首选项、人格、外壳、对话框和插件的任何设置<br>不保存启动历史记录、使用统计、缓存、Cookie、vanish 记录、SSTP 设置、POP 设置、伺か即时通讯信息及日志<br>不保存日历日程（schedule.ics）<br>不共享存档数据（不导出到云端，也不从云端恢复到本地）<br>不写入注册表。不建立文件关联或快捷方式，不注册跳转列表，也不将项目添加到“最近使用的项目”<br>不更改桌面壁纸或背景色<br>不清空回收站<br>即使执行 vanish，也不删除人格文件夹<br>不自动更新本体、人格、对话框、插件和语言资源。也不执行手动在线更新或安装 NAR<br>不安装 `initial_install.nar`<br>不通过 SNTP 进行时间同步<br><br>设置值本身仍可照常更改，但退出时不会写回文件，因此不会沿用到下次启动。<br>另外，运行所需的临时文件（临时文件夹）仍会照常创建，并在退出时删除。 |
| --option dontloadmodule<br>（旧版：/o dontloadmodule） | 不读取 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 系列模块 |
| --option dpiaware<br>（旧版：/o dpiaware） | 以 Per-Monitor V2 DPI 感知模式启动 |
| --option callghost<br>（旧版：/o callghost） | 与 --install 一起使用时，安装完成后会自动呼出人格。 |
| --option deletesource<br>（旧版：/o deletesource） | 与 --install 一起使用时，如果 NAR 安装成功，则删除 NAR。 |

### 常规选项

| 开关 | 功能 |
|---|---|
| --fmo-name FMO名<br>（旧: /f FMO名） | 强制将写入的FMO名更改为指定值。 |
| --random<br>（旧: /r） | 无论设置如何，随机启动人格 |
| --ghost 文件夹名/人格名<br>（旧: /g 文件夹名/人格名） | 启动指定的人格。用空格分隔可指定多个。若在启动SSP时指定，则会将指定的人格中的第一个作为第1组人格启动。<br>从2.8.99起，在启动SSP时指定人格文件夹的绝对路径（例如：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`），如果该人格不在加载文件夹中，则会在本次启动期间，将其父文件夹（本例中为 `C:\Users\user\Desktop\`）临时添加到人格加载文件夹，然后启动。仅适用于存在 `ghost\master\descript.txt` 的文件夹。<br>临时添加的文件夹不会保存到设置中，并会在文件夹设置画面中显示为「(temporary)」，无法编辑或删除等。此外，它也不会成为人格安装位置的候选项。如果通过文件夹设置画面明确添加了同一文件夹，则会将其保存为常规加载文件夹。<br>如果SSP已经启动（指定内容会传递给正在运行的SSP），则不会执行此处理。 |
| --help<br>（旧: /?） | 在浏览器中打开启动选项帮助页面 |
| --help 文件名<br>（旧: /? 文件名） | 在浏览器中打开指定文件名的帮助页面 |
| --ukagaka-link x-ukagaka-link:URL<br>（旧: /m x-ukagaka-link:URL） | 执行与打开 x-ukagaka-link:URL 时相同的操作。若在启动SSP时指定，则会等待第1组人格启动后再执行。 |
| --install NAR文件名<br>（旧: /i NAR文件名） | 安装NAR。如果SSP已经在运行，则将安装操作交给正在运行的SSP处理；如果没有，则由自身执行安装操作后继续启动。<br>用空格分隔可指定多个文件，以顺序安装多个NAR。<br>即使负责安装的SSP正在显示提示人格尚未安装的警告对话框（“请想办法解决”对话框），也可以处理。<br>此外，在这种情况下，如果同时指定 --option callghost，则会自动按下警告对话框中的继续启动按钮，并继续启动。 |
| --ssf SSF文件名<br>（旧: /s SSF文件名） | 执行[SSF文件](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。若在启动SSP时指定，则会等待第1组人格启动后再执行。 |
| --windowmode 模式 \[可省略\] | 从2.8.78起，可通过实验性功能"[窗口模式](windowmode.md)"启动。启动人格时，会将窗口内视为一个虚拟屏幕，以便更轻松地进行捕获操作等，并避免影响整个桌面。<br>从2.8.86起，可以指定模式。可用模式如下。省略时遵循上次的设置（初始值为shared）。<br>shared：将所有正在运行的人格合并到一个窗口中。<br>perghost：每个人格分别使用一个窗口。<br>从2.8.86起，窗口模式状态会作为设置保存，因此即使不添加此选项，也会按上次的状态启动。若要关闭，请从右键菜单的「设置」或首选项的「直播」中切换。 |
| --sstp-listen 监听地址 | 临时指定SSTP服务器的监听地址并启动。 \[2.8.97以后\]<br>不读取已保存的SSTP服务器监听设置，只在指定的地址上进行监听。<br>本次启动期间的监听设置不会保存。首选项中的SSTP服务器列表仅供查看，无法添加、删除或切换启用/禁用状态。<br>此选项适用于与 --option readonly 组合使用，以启动不与其他正在运行的SSP互相干扰的测试用SSP。<br><br>可用逗号分隔指定多个监听地址。格式如下。<br>端口号：在IPv4和IPv6环回地址（127.0.0.1 和 ::1）上监听。示例：9801<br>localhost:端口号：与仅指定端口号时相同。<br>IPv4地址:端口号：仅在指定地址上监听。指定 0.0.0.0 时，会在所有IPv4网络接口上监听。示例：192.168.0.5:9801<br>\[IPv6地址\]:端口号：IPv6地址须用\[\]括起。指定 \[::\] 时，会在所有IPv6网络接口上监听。示例：\[::1\]:9801<br>none：不进行任何监听。省略监听地址时也相同。<br><br>地址须以数值指定（localhost除外，不能使用主机名）。<br>格式错误或监听失败的地址会被忽略，并记录到错误日志中。即使如此，也不会恢复为已保存的设置。<br>请注意，指定环回地址以外的地址后，将能够接收来自其他电脑的SSTP。<br><br>示例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字体名称 \[2.8.75以后\] | 指定GUI使用的字体。并非所有内容都会完全替换，目前菜单的部分内容和标题栏等仍不会更改。 |

### 离线 surface 转储

| 开关 | 功能 |
|---|---|
| --offline-dump 文件夹路径 | 以离线转储模式启动。不实际启动人格，而是读取指定人格文件夹中的surfaces.txt，转储 surface 图像后立即退出。不会加载SHIORI/MAKOTO/PIRO。也不会创建窗口或消息循环。<br>参数指定人格文件夹路径（末尾的\\可省略）。<br>从2.8.98起，离线转储相关选项（此选项、--dump-output-dir、--dump-error-log）指定相对路径时，会以启动SSP时的当前目录为基准解析。<br><br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 文件夹名或名称 \[可省略\] | 与--offline-dump组合使用。通过文件夹名（即shell下的相对路径）或名称指定要转储的外壳。省略时，使用descript.txt中指定的默认外壳（通常为master）。<br>从2.8.98起，如果找不到指定的外壳，不会改用默认外壳进行转储，而是在错误日志中记录Error且不输出任何内容。 |
| --dump-scope（作用域ID） \[可省略\] | 与--offline-dump组合使用。指定转储图像的作用域ID。省略时为0。 |
| --dump-surface-list 列表 \[可省略\] | 与--offline-dump组合使用。用逗号分隔指定要转储的surface。可以省略surface编号前缀（surface）。也可以使用[surfaces.txt的surface ID指定扩展格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>示例：`--dump-surface-list "0,1,10"`<br>省略此选项时，不会转储surface（可以与--dump-error-log组合使用，仅输出解析错误）。<br>从2.8.98起，不仅第一个元素，各元素都可以省略前缀（例如`"0,surface1"`）。另外，指定为单独编号的surface不存在时，会在错误日志中记录Warning（范围指定中缺少的编号不会记录）。 |
| --dump-output-dir 目录 \[可省略\] | 与--offline-dump组合使用。指定转储图像的输出目录。省略时使用当前目录（2.8.97及更早版本中，省略时不会进行转储）。 |
| --dump-output-prefix 前缀 \[可省略\] | 与--offline-dump组合使用。指定输出文件名中位于surface编号之前的部分。默认的「surface」会被此字符串替换（而非附加）。省略时为「surface」。<br>示例：使用`--dump-output-prefix "x_"`时，surface 0将输出为`x_0.png`（而不是`x_surface0.png`）。 |
| --dump-error-log 文件路径 \[可省略\] | 与--offline-dump组合使用。将加载外壳时的错误日志（例如surfaces.txt的解析错误）写入指定路径。<br>省略--dump-surface-list，仅指定此选项，即可不进行转储，只执行错误检查。<br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>输出格式：带BOM的UTF-8 CSV（换行符为CRLF）。每行一条记录，各列用"括起，列中的"会转义为""。<br>`"時刻","ゴースト名","レベル","内容"`<br>时间：HH:MM:SS格式。<br>级别：Info / Notice / Warning / Error / Critical / System之一。<br>内容：日志正文。从2.8.94起，SERIKO相关日志会附带定义来源文件（相对于人格文件夹的路径）和行号，例如`[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。对于重复定义日志，也会同时注明先前定义的位置，格式为`(文件名:Line=n)`。<br>从2.8.94起，指定此选项时会最多保留10000条日志，也不会将相似内容的日志合并为摘要行（级别为System），因此不会遗漏日志。<br>没有日志时不会创建文件（即使同一路径下已有文件，也不会覆盖或删除）。<br><br>退出代码：从2.8.94起，进程会根据记录日志中最高的级别退出。<br>0：无日志，或仅有Info/Notice<br>1：有Warning（没有Error/Critical）<br>2：有Error（没有Critical）<br>3：有Critical<br>如果人格本身加载失败（例如无法读取指定文件夹中的descript.txt），则不会输出日志，退出代码也为0。 |
| --dump-surface-option 选项 \[可省略\] \[2.8.57起\] | 指定离线转储功能的选项。可指定以下内容。<br>backlog：截取与回溯功能相同的区域（面部周围）。但不会缩放，而是直接输出合成图像。<br>collision：绘制并输出碰撞判定（collision）的形状和名称。与开发用调色板中的碰撞判定显示相同，但名称始终显示，且不会绘制surface边框、有效范围、重叠判定范围等外框矩形。\[2.8.98起\]<br>从2.8.98起，可以用逗号分隔指定多个选项（例如：`--dump-surface-option backlog,collision`）。<br>如果未通过此选项指定collision，则无论用户设置（开发用调色板中的碰撞判定显示）如何，都不会绘制碰撞判定。 |
| --dump-bind 换装指定 \[可省略\] \[2.9.05起\] | 与--offline-dump组合使用。指定转储时的换装状态。<br>可以用分号分隔指定多个「类别名、部件名、ON/OFF」。其含义与[`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_)相同；对于互斥类别，将部件设为ON时，同一类别中的其他部件会设为OFF。<br>部件名留空或设为`__ALL__`时，会将类别中的所有部件作为对象。<br>ON/OFF设为1或true时表示ON，设为0或false时表示OFF。省略时视为ON（`\![bind]`省略时会切换状态，但此选项不会切换状态）。<br>示例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基准状态为外壳的descript.txt中指定的各部件默认值（`sakura.bindgroup*.default`），不会使用用户最后一次换装的状态（`shell\profile`中的保存值）。只有指定的部件会在此基础上发生变化。<br>换装会应用于--dump-scope指定的作用域。<br>指定不存在的类别或部件时，会记录Warning日志（--dump-error-log的退出代码为1），忽略该指定并继续转储。<br>类别名和部件名前后的空格不会被去除，因此逗号后不要加空格。 |
| --dump-animation 动画ID \[可省略\] \[2.9.05起\] | 与--offline-dump组合使用。像`\i[ID]`一样播放指定动画，并按顺序输出每帧图像。只能指定一个ID（除数字外，也可以像`\i[ID]`一样使用surfaces.txt中为动画指定的名称）。<br>对于每个surface，首先会将与常规转储相同的图像（runonce动画运行一轮后的状态）输出为`surface0.png`，随后在指定动画的图案每次推进时，按从0开始的4位序号输出`surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix和--dump-surface-option指定的设置也会应用于序列图像。<br>示例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always等动画会像常规转储时一样运行，指定动画会叠加在其上。只有指定动画自身的图案会作为序列输出对象；即使always动画推进，图像数量也不会增加。<br>指定动画推进到最后一个图案时结束（always动画则在运行一轮后结束）。即使被其他动画的stop或互斥关系停止，也会在此时结束。<br>通过start、alternativestart、parallelstart启动的其他动画不会作为序列输出对象。如果指定动画包含这些图案，会记录Warning日志（但会继续输出）。<br>start、stop系列图案不会改变图像，因此不会计作序列中的一帧。<br>指定的ID在该surface中不存在，或因换装后无效、处于互斥状态等原因无法播放时，会记录Warning日志，该surface只输出常规的一张图像。<br>序列最多输出10000张（到`_9999`为止）；达到上限时会记录Warning日志并停止输出。 |

### 离线工具

| 开关 | 功能 |
|---|---|
| --offline-tool 类型 \[2.9.01以降\] | 以离线工具模式启动。不启动人格，直接使用 --target-dir 指定的文件夹创建 NAR、更新定义文件或压缩包，然后立即退出。不会触发任何人格事件，也不会创建窗口或消息循环。<br>此功能与 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 执行的处理相同，但不限制输出位置（例如，不限于 SSP 管理的文件夹），可以自由指定。<br>类型可指定为以下任意一项（不区分大小写）。<br><br>nar：创建 NAR 文件。与通常创建 NAR 时相同，会应用 `developer_options.txt` 中的 nonar 指定、.narignore 等排除规则。如果文件夹根目录下没有 install.txt，则会根据 descript.txt（或 `ghost\master\descript.txt`）判断类型和名称，在目标文件夹中创建 install.txt 后再将其收录。如果无法判断类型和名称，则会失败。<br>updatedata：创建更新定义文件。如果 --output 指定的文件名以 .dau 结尾，则创建与 updates2.dau 格式相同的文件；否则创建 updates.txt 格式的文件。只会创建指定的一个文件，不会创建或删除目标文件夹根目录及 `ghost\master` 中的 updates2.dau / updates.txt。与通常处理相同，会应用 `developer_options.txt` 中的 noupdate 指定、.updateignore 等排除规则。<br>archive：直接压缩目标文件夹。不会读取 .narignore 等排除规则（不会收录隐藏文件和隐藏文件夹）。格式由 --output 的扩展名决定，扩展名为 .7z 时使用 7z 格式，否则使用 zip 格式。<br><br>无论指定哪种类型，如果输出文件已存在，都会覆盖该文件。如果输出位置位于目标文件夹内，则不会收录该文件本身。输出文件夹必须预先存在。<br>如果 --target-dir 或 --output 指定的是相对路径，则以启动 SSP 时的当前目录为基准解析。<br><br>退出代码：<br>0：成功<br>1：参数无效（类型未知、省略了 --target-dir 或 --output、--target-dir 不存在或不是文件夹）<br>2：创建失败（无法写入输出位置、无法判断 NAR 的类型和名称、updatedata 中存在无法读取的文件或过深的目录层级（超过 32 层）等）。失败时，可能会留下创建到一半的文件<br><br>示例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>示例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>示例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 文件夹路径 \[2.9.01以降\] | 必须与 --offline-tool 组合使用。指定处理目标文件夹（末尾的\\可省略）。对于 NAR 和更新定义文件，请指定人格等内容的根文件夹（包含 descript.txt、install.txt 或 ghost 文件夹的文件夹）。 |
| --output 文件路径 \[2.9.01以降\] | 必须与 --offline-tool 组合使用。指定要创建的文件路径。 |
| --password 密码 \[可省略\] \[2.9.01以降\] | 与 --offline-tool 的 nar 或 archive 组合使用。使用指定的密码创建 AES 加密 ZIP 文件（如果为 7z 格式，则使用 7z 加密）。在 updatedata 中会被忽略。<br>密码会以原样保留在命令行中，请谨慎处理。 |

### 其他

| 开关 | 功能 |
|---|---|
| `initial_install.nar` | 这不是启动选项，但如果在与 ssp.exe 相同的文件夹中放置名为<strong>`initial_install.nar`</strong>的 NAR 文件，启动 SSP 时会以静默方式（不显示确认对话框）覆盖安装。安装完成后，`initial_install.nar`会自动删除。可用于随 SSP 一同打包人格等内容并进行分发。 \[2.7.52～\] |
