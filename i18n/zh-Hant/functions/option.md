# 啟動選項一覽

啟動 ssp.exe 時，可以附加以下選項（開關）。

## 什麼是啟動選項？

這是在啟動 Windows 軟體時，切換設定來執行的機制。<br>
詳情請搜尋執行選項、命令列選項、啟動選項等詞彙。

## 使用方法

有多種使用方法。<br>
例如，也可以從「命令提示字元」或「執行」使用。<br>
以下介紹建立專用於啟動選項的捷徑的方法。

1. 建立 ssp.exe 的捷徑。<br>
   例：在 ssp.exe 上按右鍵→建立捷徑
2. 開啟建立好的捷徑內容。<br>
   例：在捷徑上按右鍵→內容
3. 確認內容的「目標」欄位中有 ssp.exe 的路徑後，將整個路徑用「""」括起來。
4. 在括起來的路徑後面加上一個半形空格，然後填入以下啟動選項。<br>
   例："C:/User/Document/略/SSP/ssp.exe" --random
5. 按下「確定」按鈕關閉內容，並順便為捷徑取個容易辨識的名稱。<br>
   例：SSP-隨機啟動
6. 執行該捷徑時，便會與直接啟動 ssp.exe 不同，以套用選項設定的狀態啟動。

## 選項一覽

建議各選項使用 `--オプション名` 格式。為了向下相容，仍可繼續使用 `/x` / `-x` 格式的短選項。

需要指定值的選項，請如 `--オプション名 値` 所示，以半形空格分隔選項名稱和值。若值中包含空格，請用「""」括起來。

2.8.97 以後的版本也接受 `--オプション名=値` 格式作為輔助方式（例：`--sstp-listen=9900`）。本頁以空格分隔的寫法為主。請注意，`/x` 格式的短選項不能使用 `=` 格式。

- [--option 選項](#--option-オプション)
- [一般選項](#一般オプション)
- [離線 Surface 匯出](#オフラインサーフェスダンプ)
- [離線工具](#オフラインツール)
- [其他](#その他)

### --option 選項

--option 選項可以用逗號分隔來指定多個項目（例：`--option bootunlock,standalone`）。

| 開關 | 功能 |
|---|---|
| --option nobootcheck<br>（舊版: /o nobootcheck） | 停用異常結束檢查 |
| --option layered<br>（舊版: /o layered） | 啟用半透明視窗 |
| --option region<br>（舊版: /o region） | 停用半透明視窗（區域模式） |
| --option bootunlock<br>（舊版: /o bootunlock） | 跳過重複啟動檢查 |
| --option standalone<br>（舊版: /o standalone） | 當 SSP.exe 已經啟動時，停用將安裝或啟動人格等處理交由執行中的 SSP.exe 負責的機制，一律由自身啟動人格或進行安裝。<br>如 --option bootunlock,standalone 所示，與跳過重複啟動檢查一起指定，即可完全不顯示警告地啟動多個 SSP.exe。 |
| --option kiosk<br>（舊版: /o kiosk） | 啟用 KIOSK 模式。行為如下。 \[2.6.54～\]<br>啟用 --option bootunlock,standalone<br>alignmenttodesktop 一律設為 free<br>不接受滑鼠或鍵盤輸入<br>完全不干預重複啟動檢查<br>不顯示通知區域圖示及工作列圖示<br>不儲存 SSP 端管理的人格與外殼設定<br>不顯示啟動中的視窗<br>不顯示錯誤通知 |
| --option readonly<br>（舊版: /o readonly） | 啟用唯讀模式。 \[2.8.96 以後\]<br>啟動時不對使用者環境進行任何永久性變更。適合用於不影響設定地測試功能，或在他人的電腦上暫時執行 SSP 等情況。<br>畫面上的行為及與人格的互動皆與平常相同，不會像 KIOSK 模式那樣阻擋輸入或限制顯示。此模式獨立於 KIOSK 模式，也可以像 --option kiosk,readonly 一樣同時使用。<br><br>行為如下。<br>啟用 --option bootunlock,standalone（因為若將處理交給執行中的 SSP，該 SSP 會寫入設定）<br>完全不干預重複啟動檢查<br>不儲存任何偏好設定、人格、外殼、對話方塊及外掛程式的設定<br>不儲存啟動歷史、使用統計、快取、Cookie、vanish 記錄、SSTP 設定、POP 設定及伺か (Ukagaka) 即時通訊的資訊與記錄<br>不儲存行事曆的行程（schedule.ics）<br>不進行存檔資料共用（既不匯出至雲端，也不從雲端還原至本機）<br>不寫入登錄。不進行檔案關聯、建立捷徑、登錄跳躍清單或新增至「最近使用的項目」<br>不變更桌布或背景色<br>不清空資源回收筒<br>即使發生 vanish 也不刪除人格資料夾<br>不自動更新主程式、人格、對話方塊、外掛程式及語言資源。也不進行手動線上更新或安裝 NAR<br>不安裝 `initial_install.nar`<br>不透過 SNTP 進行 NTP 時間同步<br><br>設定值本身仍可照常變更，但結束時不會寫回檔案，因此不會保留至下次啟動。<br>執行所需的暫存檔案（暫存資料夾）仍會照常建立，並在結束時刪除。 |
| --option dontloadmodule<br>（舊版: /o dontloadmodule） | 不載入 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 相關模組 |
| --option dpiaware<br>（舊版: /o dpiaware） | 將 DPI Awareness Mode 設為 Per-Monitor V2 後啟動 |
| --option callghost<br>（舊版: /o callghost） | 與 --install 同時使用時，安裝完成後會自動呼叫人格。 |
| --option deletesource<br>（舊版: /o deletesource） | 與 --install 同時使用時，NAR 安裝成功後會刪除該 NAR。 |

### 一般選項

| 參數 | 功能 |
|---|---|
| --fmo-name FMO名稱<br>（舊版: /f FMO名稱） | 強制將寫入的 FMO 名稱改為指定的名稱。 |
| --random<br>（舊版: /r） | 不論設定為何，隨機啟動人格。 |
| --ghost 資料夾名稱/人格名稱<br>（舊版: /g 資料夾名稱/人格名稱） | 啟動指定的人格。以空白分隔可啟動多個人格。自 2.9.35 起，也可以指定人格的 UUID（屬性系統的 `uuid`，格式如 `R5dVNluBvKjtQqjP0dAuoA==`）來代替資料夾名稱/人格名稱。在 SSP 啟動時指定的話，會將指定的人格中第一個作為第 1 組人格啟動。<br>自 2.8.99 起，在 SSP 啟動時指定人格資料夾的絕對路徑（例：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`）時，若該人格不在載入資料夾中，則僅在本次執行期間將其父資料夾（此例中為 `C:\Users\user\Desktop\`）暫時加入人格載入資料夾後啟動。僅適用於含有 `ghost\master\descript.txt` 的資料夾。<br>暫時加入的資料夾不會儲存至設定中，在資料夾設定畫面中會顯示為「(temporary)」，且無法編輯或刪除等，也不會成為人格安裝位置的候選項目。若從資料夾設定畫面明確加入相同的資料夾，則會作為一般載入資料夾儲存。<br>如果 SSP 已經啟動（指定內容會交給執行中的 SSP 處理），則不會執行此處理。 |
| --help<br>（舊版: /?） | 在瀏覽器中開啟啟動選項的說明頁面。 |
| --help 檔案名稱<br>（舊版: /? 檔案名稱） | 在瀏覽器中開啟指定檔案名稱的說明頁面。 |
| --ukagaka-link x-ukagaka-link:URL<br>（舊版: /m x-ukagaka-link:URL） | 執行與開啟 x-ukagaka-link:URL 時相同的動作。在 SSP 啟動時指定的話，會等到第 1 組人格啟動後才執行。 |
| --install NAR檔案名稱<br>（舊版: /i NAR檔案名稱） | 安裝 NAR。如果已有執行中的 SSP，會將安裝作業交給該 SSP；否則會自行安裝後繼續啟動。<br>以空白分隔指定多個 NAR 時，會依序安裝。<br>即使接收作業的 SSP 正顯示未安裝人格的警告對話框（「請想想辦法」對話框），也能處理。<br>此外，在這種情況下若同時指定 --option callghost，會自動按下警告對話框中的繼續啟動按鈕，繼續啟動。 |
| --ssf SSF檔案名稱<br>（舊版: /s SSF檔案名稱） | 執行 [SSF 檔案](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。在 SSP 啟動時指定的話，會等到第 1 組人格啟動後才執行。 |
| --windowmode 模式 \[可省略\] | 2.8.78 起，以實驗性功能「[視窗模式](windowmode.md)」啟動。將視窗內部視為一個虛擬螢幕來啟動人格，方便擷取畫面等操作，也能避免影響整個桌面。<br>2.8.86 起，可以指定模式。可指定的模式如下。省略時會依照上次的設定（初始值為 shared）。<br>shared：將所有執行中的人格集中在同一個視窗。<br>perghost：每個人格各使用一個視窗。<br>自 2.8.86 起，視窗模式的狀態會儲存至設定中，因此即使不加此選項，也會以上次的狀態啟動。若要關閉，可從右鍵選單的「設定」或偏好設定的「直播」切換。 |
| --sstp-listen 監聽位址 | 暫時指定 SSTP 伺服器的監聽位址後啟動。 \[2.8.97 以後\]<br>不會載入已儲存的 SSTP 伺服器監聽設定，只會在指定的位址監聽。<br>本次執行期間的監聽設定不會儲存。偏好設定中的 SSTP 伺服器清單僅供檢視，無法新增、刪除或編輯（只能使用重新監聽的「Retry Listen」）。<br>此選項預計與 --option readonly 搭配使用，以啟動不會干擾其他執行中 SSP 的測試用 SSP。<br><br>可以逗號分隔指定多個監聽位址。格式如下。<br>連接埠號碼：在 IPv4 與 IPv6 的迴路位址（127.0.0.1 與 ::1）監聽。例：9801<br>localhost:連接埠號碼：與僅指定連接埠號碼時相同。<br>IPv4位址:連接埠號碼：僅在指定的位址監聽。指定 0.0.0.0 時，會在所有 IPv4 介面監聽。例：192.168.0.5:9801<br>\[IPv6位址\]:連接埠號碼：IPv6 位址須以 \[\] 括住。指定 \[::\] 時，會在所有 IPv6 介面監聽。例：\[::1\]:9801<br>none：完全不監聽。省略監聽位址時也一樣。<br><br>位址須以數值指定（除 localhost 外，不能使用主機名稱）。<br>格式錯誤或監聽失敗的位址會被忽略，並記錄至錯誤記錄。此時也不會恢復為已儲存的設定。<br>請注意，指定迴路位址以外的位址時，將會接受來自其他電腦的 SSTP。<br><br>例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字型名稱 \[2.8.75 以後\] | 指定 GUI 使用的字型。並非所有字型都會被替換，目前選單的部分內容和標題列等不會改變。 |
| --time-shift 值 \[2.9.39 以後\] | 在啟動時指定「目前時間的虛擬變更」（時間機器）的時間差。供測試依賴日期或時間的人格使用。<br>請以 `--time-shift=+3600` 這類使用 `=` 連接的格式指定（因為以 `-` 開頭的值在以空白分隔時無法與選項名稱區分）。<br>此指定僅在本次執行期間有效，不會儲存至設定中。即使設定中已有儲存的時間差，也會以此指定為優先。<br><br>值可為以下任一種。<br>+秒 或 -秒：時間差本身（秒數）。必須加上正負號。例：+86400（1 天後）、-3600（1 小時前）<br>0：將時間差設為 0（維持實際時間）。<br>ISO8601 格式的日期時間：計算該日期時間與實際時間的差距，作為時間差。若未指定時區，則視為本地時間。時鐘不會停止，而是從該日期時間繼續前進。例：2026-12-31T23:59:50<br><br>時間差的幅度最長約為 200 年，不足 1 秒的部分會捨去。無法解析的值會被忽略（時間差維持為 0），並記錄至錯誤記錄。<br>以此指定啟動時，不會顯示提醒設定中仍有時間差的訊息（給開發者的對話方塊）。<br><br>例：`ssp.exe --option readonly --time-shift=2026-12-31T23:59:50` |
| --allow-timemachine-control \[2.9.39 以後\] | 允許透過 Sakura Script `\![timemachine,set,値]` / `\![timemachine,reset]` 以及 SSTP 的 EXECUTE `SetTimeShift`，在執行期間變更「目前時間的虛擬變更」。供測試使用。<br>啟動時若未指定此選項，這些指令不會執行任何動作，並會在錯誤記錄中記下警告（避免人格腳本或外部程式更動整體時鐘）。<br>時間差的值的格式與 --time-shift 相同。 |

### 離線 Surface 匯出

| 參數 | 功能 |
|---|---|
| --offline-dump 資料夾路徑 | 以離線匯出模式啟動。不實際啟動人格，而是讀取指定人格資料夾中的 surfaces.txt，匯出 Surface 圖片後立即結束。不會載入 SHIORI/MAKOTO/PIRO，也不會建立視窗或訊息迴圈。<br>請在引數中指定人格的資料夾路徑（結尾的 \\ 可省略）。<br>自 2.8.98 起，離線匯出相關選項（本選項、--dump-output-dir、--dump-error-log）若指定相對路徑，會以啟動 SSP 時的目前目錄為基準解析。<br><br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 資料夾名稱或名稱 \[可省略\] | 與 --offline-dump 搭配使用。以資料夾名稱（即 shell 下的相對路徑）或名稱指定要匯出的外殼。省略時會使用 descript.txt 中指定的預設外殼（通常為 master）。<br>自 2.8.98 起，如果找不到指定的外殼，不會改用預設外殼匯出，而是在錯誤記錄中記錄 Error，且不輸出任何內容。 |
| --dump-scope (範圍 ID) \[可省略\] | 與 --offline-dump 搭配使用。指定匯出圖片的範圍 ID。省略時為 0。 |
| --dump-surface-list 清單 \[可省略\] | 與 --offline-dump 搭配使用。以逗號分隔指定要匯出的 Surface。Surface 編號的前綴（surface）可省略。也可以使用 [surfaces.txt 的 Surface ID 指定擴充格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>範例：`--dump-surface-list "0,1,10"`<br>省略此選項時不會匯出 Surface（可搭配 --dump-error-log 僅輸出解析錯誤）。<br>自 2.8.98 起，不僅第一個項目，每個項目都可以省略前綴（例如 `"0,surface1"`）。此外，如果以單一編號而非範圍指定的 Surface 不存在，會在錯誤記錄中記錄 Warning（範圍指定中缺少的編號不會記錄）。 |
| --dump-output-dir 目錄 \[可省略\] | 與 --offline-dump 搭配使用。指定匯出圖片的輸出目錄。省略時使用目前目錄（2.8.97 以前省略時不會執行匯出）。 |
| --dump-output-prefix 前綴 \[可省略\] | 與 --offline-dump 搭配使用。指定輸出檔案名稱中位於 Surface 編號之前的部分。預設的「surface」會被此字串取代（不是附加在後面）。省略時為「surface」。<br>範例：使用 `--dump-output-prefix "x_"` 時，Surface 0 會是 `x_0.png`（不是 `x_surface0.png`）。 |
| --dump-error-log 檔案路徑 \[可省略\] | 與 --offline-dump 搭配使用。將載入外殼時的錯誤記錄（例如 surfaces.txt 的解析錯誤）寫入指定路徑。<br>省略 --dump-surface-list 並僅指定此選項，即可不執行匯出，只進行錯誤檢查。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>輸出格式：帶有 BOM 的 UTF-8 CSV（換行使用 CRLF）。每行為一筆記錄，各欄位以 " 包住，欄位中的 " 會跳脫為 ""。<br>`"時刻","ゴースト名","レベル","内容"`<br>時間：HH:MM:SS 格式。<br>層級：Info / Notice / Warning / Error / Critical / System 其中之一。<br>內容：記錄的內文。自 2.8.94 起，SERIKO 相關記錄會附上定義來源檔案（相對於人格資料夾的路徑）和行號，例如 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。重複定義的記錄也會以 `(ファイル名:Line=n)` 的形式附上先前定義的位置。<br>自 2.8.94 起，指定此選項時最多保留 10000 筆記錄，且不會將內容相似的記錄彙整成摘要行（層級為 System），因此不會遺漏記錄。<br>如果沒有任何記錄，則不會建立檔案（即使相同路徑已有檔案，也不會覆寫或刪除）。<br><br>結束代碼：自 2.8.94 起，程序會依照已記錄項目中最嚴重的層級，以相應的結束代碼結束。<br>0：沒有記錄，或只有 Info/Notice<br>1：有 Warning（沒有 Error/Critical）<br>2：有 Error（沒有 Critical）<br>3：有 Critical<br>如果人格本身載入失敗（例如無法讀取指定資料夾中的 descript.txt），不會輸出記錄，結束代碼也會是 0。 |
| --dump-surface-option 選項 \[可省略\] \[2.8.57 以後\] | 指定離線匯出功能的選項。可指定的內容如下。<br>backlog：裁切與歷史記錄功能相同的區域（臉部周圍）。但不會進行縮放，會直接輸出合成圖片。<br>collision：在輸出圖片上繪製碰撞判定（collision）的形狀和名稱。與開發用面板的碰撞判定顯示相同，但名稱一律顯示，且不會繪製 Surface 外框、有效範圍、重疊判定範圍等外接矩形。\[2.8.98 以後\]<br>自 2.8.98 起，可以逗號分隔指定多個選項（例如：`--dump-surface-option backlog,collision`）。<br>如果此選項未指定 collision，無論使用者設定（開發用面板的碰撞判定顯示）為何，都不會繪製碰撞判定。 |
| --dump-bind 換裝指定 \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。指定匯出時的換裝狀態。<br>可以分號分隔指定多組「類別名稱,部件名稱,ON/OFF」。其意義與 [`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_) 相同：在互斥類別中將某個部件設為 ON 時，同一類別的其他部件會變為 OFF。<br>將部件名稱留空或設為 `__ALL__` 時，會以類別中的所有部件為對象。<br>ON/OFF 使用 1 或 true 表示 ON，0 或 false 表示 OFF。省略時視為 ON（`\![bind]` 省略時會反轉狀態，但此處不會反轉）。<br>範例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基準狀態為外殼的 descript.txt 中指定的各部件預設值（`sakura.bindgroup*.default`），不會使用使用者最後一次換裝的狀態（`shell\profile` 內的儲存值）。只有指定的部件會在此基礎上變更。<br>換裝會套用至 --dump-scope 指定的範圍。<br>如果指定不存在的類別或部件，會記錄 Warning（--dump-error-log 的結束代碼為 1），僅忽略該項指定並繼續匯出。<br>類別名稱和部件名稱前後的空白不會被移除，因此請勿在逗號後加入空白。 |
| --dump-animation 動畫 ID \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。與 `\i[ID]` 相同地播放指定動畫，並以連號輸出每個畫格的圖片。只能指定一個 ID（除了數值外，也可以和 `\i[ID]` 一樣，使用在 surfaces.txt 中為動畫指定的名稱）。<br>對每個 Surface，首先將與一般匯出相同的圖片（runonce 動畫播放一輪後的狀態）輸出為 `surface0.png`，接著每當指定動畫的模式推進時，就以從 0 開始的 4 位數連號輸出 `surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix 和 --dump-surface-option 的設定也會套用至連號圖片。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always 等動畫會與一般匯出時一樣運作，指定動畫則疊加於其上。只有指定動畫本身的模式會產生連號圖片，即使 always 動畫推進，圖片數量也不會增加。<br>指定動畫推進到最後一個模式時（always 則為播放一輪時）結束。如果因其他動畫的 stop 或互斥而停止，也會在該時點結束。<br>由 start、alternativestart、parallelstart 啟動的其他動畫不會產生連號圖片。如果指定動畫包含這些模式，會記錄 Warning（輸出會繼續進行）。<br>由於 start、stop 類型的模式不會改變圖片，因此不算作連號中的一個畫格。<br>如果指定的 ID 不存在於該 Surface，或因換裝而停用、處於互斥狀態等原因無法播放，會記錄 Warning，並只輸出該 Surface 的一張一般圖片。<br>連號最多為 10000 張（至 `_9999`），達到上限時會記錄 Warning 並停止輸出。 |

### 離線工具

| 開關 | 功能 |
|---|---|
| --offline-tool 類型 \[2.9.01以後\] | 以離線工具模式啟動。不啟動人格，從 --target-dir 指定的資料夾建立 NAR、更新定義檔案或壓縮檔後立即結束。不會發生任何人格事件，也不會建立視窗或訊息迴圈。<br>處理方式與 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 相同，但輸出位置不受限制（例如只能在 SSP 管理的資料夾中），可自由指定。<br>類型請指定以下其中一種（不區分大小寫）。<br><br>nar：建立 NAR 檔案。`developer_options.txt` 的 nonar 設定及 .narignore 等排除設定，與一般建立 NAR 時一樣適用。如果資料夾根目錄沒有 install.txt，會根據 descript.txt（或 `ghost\master\descript.txt`）判斷類型與名稱，在目標資料夾中建立 install.txt 後再收錄。若無法判斷類型與名稱，則會失敗。<br>updatedata：建立更新定義檔案。如果 --output 的檔名以 .dau 結尾，則使用與 updates2.dau 相同的格式，否則使用 updates.txt 格式，僅建立指定的單一檔案。不會建立或刪除目標資料夾根目錄及 `ghost\master` 中的 updates2.dau / updates.txt。`developer_options.txt` 的 noupdate 設定及 .updateignore 等排除設定，與一般情況一樣適用。<br>archive：直接壓縮目標資料夾。不讀取 .narignore 等排除設定（不收錄隱藏檔案及隱藏資料夾）。格式由 --output 的副檔名決定，.7z 為 7z 格式，其他則為 zip 格式。<br><br>無論使用哪種類型，若輸出檔案已存在，皆會覆寫。若輸出位置位於目標資料夾內，則不會收錄該檔案本身。輸出資料夾必須事先存在。<br>若 --target-dir・--output 指定的是相對路徑，則以啟動 SSP 時的目前工作目錄為基準解析。<br><br>結束代碼：<br>0：成功<br>1：參數無效（類型未知、未指定 --target-dir・--output、--target-dir 不存在或不是資料夾）<br>2：建立失敗（無法寫入輸出位置、無法判斷 NAR 的類型與名稱、updatedata 中有無法讀取的檔案或層級過深（超過 32 層）等）。失敗時可能仍會留下已建立到一半的檔案<br><br>範例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>範例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>範例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 資料夾路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定處理目標的資料夾（結尾的\\可省略）。建立 NAR 或更新定義檔案時，請指定人格等項目的根資料夾（包含 descript.txt、install.txt 或 ghost 資料夾的資料夾）。 |
| --output 檔案路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定要建立的檔案路徑。 |
| --password 密碼 \[可省略\] \[2.9.01以後\] | 與 --offline-tool 的 nar 或 archive 搭配使用。使用指定的密碼建立 AES 加密的 ZIP（7z 格式則使用 7z 的加密方式）。在 updatedata 中會被忽略。<br>密碼會原樣保留在命令列中，請注意處理方式。 |

### 其他

| 開關 | 功能 |
|---|---|
| `initial_install.nar` | 雖然這不是啟動選項，但若在與 ssp.exe 相同的資料夾中放置名為<strong>`initial_install.nar`</strong>的 NAR 檔案，SSP 啟動時便會靜默覆寫安裝（不顯示確認對話方塊）。安裝完成後，`initial_install.nar`會自動刪除。可用於將人格等項目與 SSP 一同打包發佈的情況。 \[2.7.52～\] |
