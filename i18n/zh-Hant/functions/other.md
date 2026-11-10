# 其他功能

這裡將介紹其他雜項功能和實驗性功能。

## MCP 伺服器支援功能

可用於伺か相關用途的 MCP（Model Context Protocol）伺服器，除了內建於 SSP 的伺服器之外，還有可搜尋規格文件和人格的線上伺服器。

### SSP 內建的 MCP 伺服器

SSP 可以作為 MCP 伺服器運作，讓 AI（LLM）執行 SakuraScript、讀取屬性系統等。<br>
若要使用此功能，請在 SSP 執行中時開啟 [127.0.0.1:9801/api/mcp/help](http://127.0.0.1:9801/api/mcp/help)，閱讀說明，並嘗試將適當的設定加入 `claude_desktop_config.json` 等檔案中。<br>
目前可使用下列功能。

- `get_active_ghost_list` - 取得目前作用中的人格（角色）清單
- `get_status` - 取得各人格目前的狀態（對話中、等待選項等）。相當於 SSTP EXECUTE GetStatus
- `get_expression_table` - 取得特定人格（角色）可使用的表情清單
- `get_property` - 取得屬性系統的值
- `get_log` - 取得錯誤記錄、腳本記錄、網路記錄、更新記錄和狀態記錄。可依人格名稱或上次取得後的項目（`since_id`）篩選
- SakuraScript - 執行 SakuraScript。指定 strict 後，會如同 SSTP 的 Option: strict，將指定不存在的表面等情況記錄在錯誤記錄中，並可透過 `get_log` 確認
- `raise_event` - 觸發 SHIORI 事件（相當於 SSTP NOTIFY 的 Event），並播放人格回傳的腳本。回傳的腳本也會包含在結果中。可指定 strict
- reload - 重新載入人格、SHIORI（字典）、外殼、對話方塊等。載入時發生的錯誤可透過 `get_log` 確認
- `dump_surface` - 取得角色的圖片（透明 PNG）。省略表面 ID 時，會回傳目前顯示的外觀（尚未套用縮放和透明度）；指定表面 ID 時，則會回傳以初始狀態繪製該表面的圖片。相當於 `\![execute,dumpsurface]`，每次一張
- `dump_balloon` - 取得對話方塊的圖片（透明 PNG）。回傳最後繪製的狀態。相當於 `\![execute,dumpballoon]`。在 hide 中指定 balloonmarker、balloonnum 時，會排除指定項目後重新繪製並回傳（2.9.08 以後）

MCP 伺服器是僅供本機使用的功能，因此透過 SakuraScript 等方式傳送的腳本，會與目標人格自身處理的腳本（Owned SSTP）相同，也可以執行 `\![reload,...]` 等指令。<br>
指定人格的引數（`ghost_name`）除了可填入人格名稱，也可以指定人格根目錄（包含 ghost 和 shell 的資料夾）的完整路徑。

### 透過 MCP 搜尋伺か規格

有可搜尋 UKADOC、YAYA Wiki、里々 Wiki 和蒼空 Wiki 的 MCP 伺服器。<br>
若要使用線上版，請將下列 URL 加入為遠端 MCP 伺服器（例如自訂連接器）。<br>
<https://ssp.shillest.net/ukadoc/mcp><br>
若要在本機執行，請安裝線上版所依據的 ukagaka-doc-mcp，並完成適當設定。<br>
<https://github.com/finelagusaz/ukagaka-doc-mcp>

### 透過 MCP 搜尋人格

有可提供與人格搜尋網站（<https://buynowforsale.shillest.net/ghosts/>）相同搜尋功能的 MCP 伺服器。請將下列 URL 加入為遠端 MCP 伺服器。由於只會處理公開資訊，因此不需要設定驗證。<br>
<https://buynowforsale.shillest.net/ghosts/mcp><br>
詳細資訊請參閱[這裡](https://buynowforsale.shillest.net/ghosts/about.html#mcp)。

### 請 AI 代理程式協助設定

如果您使用 Claude Code、Codex CLI、Cursor 等在本機電腦執行的 AI 代理程式，請在 SSP 執行中時，像下面這樣請代理程式協助設定。

```
SSPのMCPサーバを使えるようにしたい。http://127.0.0.1:9801/api/mcp/help を読んで、あなた自身のMCP設定に追加して。
```

由於在瀏覽器中執行的 AI（例如 claude.ai）無法連線至 127.0.0.1，因此無法使用此方法。

#### 提供 AI 代理程式的設定步驟

1. 取得 `http://127.0.0.1:9801/api/mcp/help`。若無法連線，代表 SSP 尚未執行，請要求使用者啟動 SSP。
2. 將頁面 JSON 中 mcp.exe 的完整路徑設為 command，並以不帶引數的 stdio 格式 MCP 伺服器加入自己的 MCP 設定。該 JSON 是 Claude Desktop 的範例，請轉換為適用於自身的設定格式。
3. 如果使用者希望，也可以將上述線上 MCP 伺服器（<https://ssp.shillest.net/ukadoc/mcp> 和 <https://buynowforsale.shillest.net/ghosts/mcp>）加入為遠端 MCP 伺服器。
4. 如果套用設定需要重新啟動或建立新工作階段，請告知使用者。

## 想用 AI 代理程式製作人格（Vibe Coding）

YAYA 人格範本「紺野ややめ」中，包含適用於 AI 程式設計代理程式的開發套件（Vibe Coding Toolkit）。<br>
其中備有 AI 代理程式用的指示文件（AGENTS.md），以及字典、surfaces.txt 的檢查步驟等。<br>
<https://github.com/YAYA-shiori/konnoyayame><br>
從儲存庫取得的 zip 檔內容不完整，請從 Releases 下載。<br>
套件中使用 SSP 的 --dump-error-log 檢查外殼，以及使用[除錯工具 tama](https://github.com/YAYA-shiori/tama/blob/master/docs/README_JP.md)的 tamac 檢查字典等步驟，請參閱[人格批次檢查（check.md）](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/workflows/check.md)和[開發指令一覽（commands.md）](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/commands.md)。
