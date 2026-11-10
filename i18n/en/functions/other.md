# Other features

This section describes miscellaneous and experimental features.

## MCP server support

MCP (Model Context Protocol) servers for Ukagaka include the one built into SSP, as well as online servers for searching specifications and ghosts.

### SSP built-in MCP server

SSP can act as an MCP server, allowing an AI (LLM) to run Sakura Script and read the property system.<br>
To use this feature, start SSP, open [127.0.0.1:9801/api/mcp/help](http://127.0.0.1:9801/api/mcp/help), read the instructions, and add the appropriate settings to `claude_desktop_config.json` or a similar file.<br>
The following features are currently available:

- `get_active_ghost_list` - Get a list of active ghosts (characters)
- `get_status` - Get the current status of each ghost (such as talking or waiting for a choice). Equivalent to SSTP EXECUTE GetStatus
- `get_expression_table` - Get a list of expressions available for a specific ghost (character)
- `get_property` - Get the value of the property system
- `get_log` - Get error logs, script logs, network logs, update logs, and status logs. You can filter by ghost name or by entries since the previous retrieval (`since_id`)
- SakuraScript - Run SakuraScript. When strict is specified, references to nonexistent surfaces and similar errors are recorded in the error log, as with SSTP's Option: strict, and can be checked with `get_log`
- `raise_event` - Raise a SHIORI event (equivalent to the Event in SSTP NOTIFY) and play the script returned by the ghost. The returned script is also included in the result. strict can be specified
- reload - Reload a ghost, SHIORI (dictionary), shell, balloon, and more. Errors during loading can be checked with `get_log`
- `dump_surface` - Get an image of the character (transparent PNG). If you omit the surface ID, the currently displayed appearance is returned (before scaling or transparency is applied). If you specify an ID, the specified surface is rendered in its initial state. Equivalent to `\![execute,dumpsurface]`; one image per request
- `dump_balloon` - Get an image of the balloon (transparent PNG). Returns the last rendered state. Equivalent to `\![execute,dumpballoon]`. If you specify balloonmarker or balloonnum in hide, the image is redrawn without them (from 2.9.08)

The MCP server is a local-only feature, so scripts sent through SakuraScript and similar means are handled in the same way as scripts from the target ghost itself (Owned SSTP), and commands such as `\![reload,...]` can also be run.<br>
For the argument that specifies a ghost (`ghost_name`), you can specify either the ghost name or the full path to the ghost's root folder (the folder containing ghost and shell).

### Search Ukagaka specifications with MCP

An MCP server is available for searching UKADOC, YAYA Wiki, Satori Wiki, and Aozora Wiki.<br>
To use the online version, add the following URL as a remote MCP server (such as a custom connector).<br>
<https://ssp.shillest.net/ukadoc/mcp><br>
To run it locally, install ukagaka-doc-mcp, which the online version is based on, and configure it appropriately.<br>
<https://github.com/finelagusaz/ukagaka-doc-mcp>

### Search for ghosts with MCP

An MCP server is available that provides searches equivalent to those on the ghost search site (<https://buynowforsale.shillest.net/ghosts/>). Add the following URL as a remote MCP server. It only handles public information, so no authentication settings are needed.<br>
<https://buynowforsale.shillest.net/ghosts/mcp><br>
For details, see [this page](https://buynowforsale.shillest.net/ghosts/about.html#mcp).

### Have an AI agent configure it for you

If you use a local AI agent such as Claude Code, Codex CLI, or Cursor, start SSP and ask the agent to configure it as follows:

```
SSPのMCPサーバを使えるようにしたい。http://127.0.0.1:9801/api/mcp/help を読んで、あなた自身のMCP設定に追加して。
```

This method won't work with browser-based AIs (such as claude.ai), because they cannot connect to 127.0.0.1.

#### Setup instructions for AI agents

1. Retrieve `http://127.0.0.1:9801/api/mcp/help`. If you cannot connect, SSP is not running, so ask the user to start it.
2. Use the full path to mcp.exe in the JSON on the page as the command, and add it to your own MCP settings as a stdio MCP server with no arguments. The JSON is an example for Claude Desktop, so adapt it to your own settings format.
3. If the user wants, also add the online MCP servers above (<https://ssp.shillest.net/ukadoc/mcp> and <https://buynowforsale.shillest.net/ghosts/mcp>) as remote MCP servers.
4. If applying the settings requires a restart or a new session, let the user know.

## Create a ghost with an AI agent (Vibe Coding)

The YAYA ghost template “Konno Yayame” includes a development kit (Vibe Coding Toolkit) for AI coding agents.<br>
It provides a full set of resources, including instructions for AI agents (AGENTS.md) and procedures for validating dictionaries and surfaces.txt.<br>
<https://github.com/YAYA-shiori/konnoyayame><br>
A ZIP downloaded from the repository is incomplete, so download it from Releases.<br>
For instructions on checking shells with SSP's --dump-error-log and checking dictionaries with tamac from the [debugging tool tama](https://github.com/YAYA-shiori/tama/blob/master/docs/README_JP.md), both of which are used within the kit, see [Bulk ghost checks (check.md)](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/workflows/check.md) and [Development command list (commands.md)](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/commands.md).
