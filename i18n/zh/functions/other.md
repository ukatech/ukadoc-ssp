# 其他功能

这里将介绍其他杂项功能和实验性功能。

## MCP 服务器支持功能

与伺か (Ukagaka) 相关的 MCP (Model context protocol) 服务器，除了 SSP 内置的服务器外，还有可用于搜索规范文档和人格的在线服务器。

### SSP 内置的 MCP 服务器

SSP 可以作为 MCP 服务器运行，支持由 AI (LLM) 执行 Sakura Script、读取属性系统等功能。<br>
要使用此功能，请在 SSP 运行时打开[127.0.0.1:9801/api/mcp/help](http://127.0.0.1:9801/api/mcp/help)，阅读说明，然后尝试将相关设置添加到 `claude_desktop_config.json` 等配置文件中。<br>
目前可以使用以下功能。

- `get_active_ghost_list` - 获取当前活动人格（角色）的列表
- `get_status` - 获取各人格的当前状态（正在对话、等待选择项等）。相当于 SSTP EXECUTE GetStatus
- `get_expression_table` - 获取指定人格（角色）可用的表情列表
- `get_property` - 获取属性系统的值
- `get_log` - 获取错误日志、脚本日志、网络日志、更新日志和状态日志。可以按人格名称或上次获取之后的内容（`since_id`）筛选
- SakuraScript - 执行 SakuraScript。指定 strict 后，与 SSTP 的 Option: strict 相同，不存在的 surface 等指定内容会被记录到错误日志中，可通过 `get_log` 查看
- `raise_event` - 触发 SHIORI 事件（相当于 SSTP NOTIFY 的 Event），并播放人格返回的脚本。返回的脚本也会包含在结果中。可以指定 strict
- reload - 重新载入人格、SHIORI（辞书）、外壳、对话框等。载入过程中的错误可通过 `get_log` 查看
- `dump_surface` - 获取角色的图像（透明 PNG）。省略 surface ID 时，返回当前显示的形象（尚未应用缩放和透明度）；指定 ID 时，返回以初始状态绘制的该 surface 单体图像。相当于 `\![execute,dumpsurface]`，每次一张
- `dump_balloon` - 获取对话框的图像（透明 PNG）。返回最后绘制的状态。相当于 `\![execute,dumpballoon]`。在 hide 中指定 balloonmarker、balloonnum 后，会返回排除这些元素并重新绘制的图像（2.9.08 及更高版本）

MCP 服务器仅供本地使用，因此，通过 SakuraScript 等方式发送的脚本会与目标人格自身处理的情况（Owned SSTP）一样处理，`\![reload,...]` 等也可以执行。<br>
指定人格的参数（`ghost_name`）除了可以填写人格名称外，也可以填写人格根目录（包含 ghost 和 shell 的文件夹）的完整路径。

### 让 MCP 能够搜索伺か的规范

有一个可用于搜索 UKADOC、YAYA Wiki、里々 Wiki 和蒼空 Wiki 的 MCP 服务器。<br>
要使用在线版，请将以下 URL 添加为远程 MCP 服务器（例如自定义连接器）。<br>
<https://ssp.shillest.net/ukadoc/mcp><br>
如果想在本地运行，请安装作为在线版基础的 ukagaka-doc-mcp，并进行适当设置。<br>
<https://github.com/finelagusaz/ukagaka-doc-mcp>

### 让 MCP 能够搜索人格

有一个 MCP 服务器可以执行与人格搜索网站（<https://buynowforsale.shillest.net/ghosts/>）相同的搜索。请将以下 URL 添加为远程 MCP 服务器。该服务器仅处理公开信息，因此无需设置身份验证。<br>
<https://buynowforsale.shillest.net/ghosts/mcp><br>
详情请参阅[这里](https://buynowforsale.shillest.net/ghosts/about.html#mcp)。

### 请 AI 代理帮忙进行设置

如果你正在使用 Claude Code、Codex CLI、Cursor 等运行在本地电脑上的 AI 代理，可以在 SSP 运行时像下面这样请求代理帮你设置。

```
SSPのMCPサーバを使えるようにしたい。http://127.0.0.1:9801/api/mcp/help を読んで、あなた自身のMCP設定に追加して。
```

由于运行在浏览器中的 AI（例如 claude.ai）无法连接到 127.0.0.1，因此不能使用此方法。

#### 面向 AI 代理的设置步骤

1. 获取 `http://127.0.0.1:9801/api/mcp/help`。如果无法连接，说明 SSP 尚未运行，请让用户启动 SSP。
2. 将页面 JSON 中 mcp.exe 的完整路径设为 command，并将其作为不带参数的 stdio 格式 MCP 服务器添加到自身的 MCP 设置中。JSON 中的示例适用于 Claude Desktop，请转换为自身使用的设置格式。
3. 如果用户需要，也将上述在线 MCP 服务器（<https://ssp.shillest.net/ukadoc/mcp> 和 <https://buynowforsale.shillest.net/ghosts/mcp>）添加为远程 MCP 服务器。
4. 如果设置生效需要重启或开启新会话，请告知用户。

## 想用 AI 代理制作人格（Vibe Coding）

YAYA 人格模板「紺野ややめ」包含面向 AI 编码代理的开发工具包（Vibe Coding Toolkit）。<br>
其中包含面向 AI 代理的说明文件（AGENTS.md），以及辞书、surfaces.txt 的验证步骤等完整内容。<br>
<https://github.com/YAYA-shiori/konnoyayame><br>
从仓库下载的 zip 文件内容不完整，请从 Releases 下载。<br>
关于工具包中使用 SSP 的 --dump-error-log 检查外壳，以及使用[调试工具 tama](https://github.com/YAYA-shiori/tama/blob/master/docs/README_JP.md)的 tamac 检查辞书的步骤，请参阅[批量检查人格（check.md）](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/workflows/check.md)和[开发命令列表（commands.md）](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/commands.md)。
