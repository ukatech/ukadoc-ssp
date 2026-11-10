# 啟動選項一覽

ssp.exe 可以加上以下選項（開關）啟動。

## 什麼是啟動選項？

這是在啟動 Windows 軟體時切換設定並執行的機制。<br>
如需詳細資訊，請查詢「執行時選項」、「命令列選項」、「啟動選項」等詞彙。

## 使用方法

有各種不同的方法。<br>
例如，也可以透過「命令提示字元」或「執行」使用。<br>
以下說明如何建立專用於選項的捷徑。

1. 建立 ssp.exe 的捷徑。<br>
   例如：在 ssp.exe 上按右鍵→建立捷徑
2. 開啟建立好的捷徑內容。<br>
   例如：在捷徑上按右鍵→內容
3. 確認「目標」欄位中有 ssp.exe 的路徑後，將整個路徑以「""」括起來。
4. 在括起來的路徑後加上一個半形空格，並在後方輸入下列啟動選項。<br>
   例如："C:/User/Document/略/SSP/ssp.exe" --random
5. 直接按下「確定」按鈕關閉內容視窗，並順便替捷徑取個容易辨識的名稱。<br>
   例如：SSP-隨機啟動
6. 執行該捷徑後，與直接啟動 ssp.exe 不同，啟動時會套用選項設定。

## 選項一覽

建議使用 `--オプション名` 格式指定各個選項。為了維持向下相容性，也可以繼續使用 `/x` / `-x` 格式的短選項。

需要指定值的選項，請使用 `--オプション名 値` 格式，並以半形空格分隔選項名稱和值。值中若包含空格，請以「""」括起來。

2.8.97 之後也支援以 `--オプション名=値` 格式指定（例如：`--sstp-listen=9900`）。本頁以空格分隔的格式為主。另外，`/x` 格式的短選項無法使用 `=` 格式。

- [--option 選項](#--option-オプション)
- [一般選項](#一般オプション)
- [離線表面圖像傾印](#オフラインサーフェスダンプ)
- [離線工具](#オフラインツール)
- [其他](#その他)

### --option 選項

可以用逗號分隔並指定多個 --option 選項（例如：`--option bootunlock,standalone`）。

| 開關 | 功能 |
|---|---|
| --option nobootcheck<br>（舊：/o nobootcheck） | 停用異常結束檢查 |
| --option layered<br>（舊：/o layered） | 啟用半透明視窗 |
| --option region<br>（舊：/o region） | 停用半透明視窗（區域模式） |
| --option bootunlock<br>（舊：/o bootunlock） | 略過重複啟動檢查 |
| --option standalone<br>（舊：/o standalone） | 如果 SSP.exe 已經在執行，就停用將安裝或啟動人格等處理委託給執行中的 SSP.exe 的機制，並一律由本身啟動人格或進行安裝。<br>如同時指定略過重複啟動檢查的選項，例如 --option bootunlock,standalone，即可在完全不顯示警告的情況下同時啟動多個 SSP.exe。 |
| --option kiosk<br>（舊：/o kiosk） | 啟用 KIOSK 模式，行為如下。 \[2.6.54～\]<br>啟用 --option bootunlock,standalone<br>一律將 alignmenttodesktop 設為 free<br>不接受滑鼠與鍵盤輸入<br>完全不干涉重複啟動檢查<br>不顯示通知區域圖示與工作列圖示<br>不儲存 SSP 管理的人格或外殼設定<br>不顯示表示正在啟動的視窗<br>不顯示錯誤通知 |
| --option readonly<br>（舊：/o readonly） | 啟用唯讀模式。 \[2.8.96以降\]<br>啟動時完全不對使用者環境進行永久變更。適用於想在不影響設定的情況下測試運作，或想在他人的電腦上暫時執行 SSP 等情況。<br>畫面上的行為及與人格的對話都和平常一樣，不會像 KIOSK 模式那樣阻擋輸入或限制顯示。此模式與 KIOSK 模式相互獨立，也可以如同 --option kiosk,readonly 一樣同時使用。<br><br>行為如下。<br>啟用 --option bootunlock,standalone（若將處理委託給正在執行的 SSP，該執行個體可能會寫入設定）<br>完全不干涉重複啟動檢查<br>不儲存偏好設定、人格、外殼、對話方塊或外掛程式的設定<br>不儲存啟動記錄、使用統計、快取、Cookie、vanish 記錄、SSTP 設定、POP 設定、伺か即時通訊的資訊與記錄<br>不儲存行事曆的行程（schedule.ics）<br>不進行存檔資料共用（不會匯出至雲端，也不會從雲端還原至本機）<br>不寫入登錄檔。不設定檔案關聯、不建立捷徑、不登錄跳躍清單，也不將項目加入「最近使用的項目」<br>不變更桌布或背景色彩<br>不清空資源回收筒<br>即使 vanish，也不會刪除人格資料夾<br>不自動更新本體、人格、對話方塊、外掛程式或語言資源。也不會手動進行線上更新或安裝 NAR<br>不安裝 `initial_install.nar`<br>不使用 SNTP 進行 NTP 時間同步<br><br>設定值本身仍可照常變更，但結束時不會寫回檔案，因此不會沿用至下次啟動。<br>另外，運作所需的暫存檔案（暫存資料夾）仍會照常建立，並在結束時刪除。 |
| --option dontloadmodule<br>（舊：/o dontloadmodule） | 不載入 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 相關模組 |
| --option dpiaware<br>（舊：/o dpiaware） | 以 Per-Monitor V2 DPI Awareness Mode 啟動 |
| --option callghost<br>（舊：/o callghost） | 與 --install 一起使用時，安裝完成後會自動呼叫人格。 |
| --option deletesource<br>（舊：/o deletesource） | 與 --install 一起使用時，NAR 安裝成功後會刪除 NAR。 |

### 一般選項

| 開關 | 功能 |
|---|---|
| --fmo-name FMO名<br>（舊：/f FMO名） | 強制將要寫入的 FMO 名稱改為指定名稱。 |
| --random<br>（舊：/r） | 不受設定影響，隨機啟動人格。 |
| --ghost フォルダ名/ゴースト名<br>（舊：/g フォルダ名/ゴースト名） | 啟動指定的人格。以空白分隔即可同時啟動多個人格。若在 SSP 啟動時指定，會將指定的人格中第一個作為第 1 組人格啟動。<br>2.8.99 以後，若在 SSP 啟動時指定人格資料夾的絕對路徑（例如：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`），且該人格不在載入資料夾中，便會在這次啟動期間，暫時將其上層資料夾（本例中為 `C:\Users\user\Desktop\`）新增為人格載入資料夾，再啟動該人格。僅適用於存在 `ghost\master\descript.txt` 的資料夾。<br>暫時新增的資料夾不會儲存至設定中，並會在資料夾設定畫面中顯示為「(temporary)」，無法編輯或刪除等。此外，也不會列為人格的安裝位置候選項目。若從資料夾設定畫面明確新增相同資料夾，便會將其儲存為一般載入資料夾。<br>若 SSP 已在執行中（指定內容會轉交給執行中的 SSP），則不會執行此處理。 |
| --help<br>（舊：/?） | 使用瀏覽器開啟啟動選項的說明頁面。 |
| --help ファイル名<br>（舊：/? ファイル名） | 使用瀏覽器開啟指定檔名的說明頁面。 |
| --ukagaka-link x-ukagaka-link:URL<br>（舊：/m x-ukagaka-link:URL） | 執行與開啟 x-ukagaka-link:URL 時相同的動作。若在 SSP 啟動時指定，會等到第 1 組人格啟動後才執行。 |
| --install NARファイル名<br>（舊：/i NARファイル名） | 安裝 NAR。若有正在執行的 SSP，會將安裝作業交由該 SSP 處理；若沒有，則會自行執行安裝作業後繼續啟動。<br>以空白分隔即可指定多個 NAR，並依序安裝。<br>即使負責安裝的 SSP 正顯示「尚未安裝人格」的警告對話方塊（「請想辦法處理」對話方塊），也能進行安裝。<br>此外，在這種情況下若也指定了 --option callghost，會自動按下警告對話方塊中的繼續啟動按鈕，並繼續啟動。 |
| --ssf SSFファイル名<br>（舊：/s SSFファイル名） | 執行 [SSF 檔案](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。若在 SSP 啟動時指定，會等到第 1 組人格啟動後才執行。 |
| --windowmode モード \[省略可\] | 2.8.78～ 以實驗性功能「[視窗模式](windowmode.md)」啟動。將人格啟動在視窗內，並把視窗內部視為一個虛擬螢幕，方便進行擷取等操作，也能避免影響整個桌面。<br>2.8.86～ 可指定模式。可指定的模式如下。省略時會沿用上次的設定（初始值為 shared）。<br>shared：將所有正在執行的人格合併在同一個視窗中。<br>perghost：每個人格各自使用一個視窗。<br>從 2.8.86 起，視窗模式的狀態會儲存為設定，因此即使不加上此選項，也會沿用上次的狀態啟動。若要關閉，請從右鍵選單的「設定」或偏好設定中的「串流」切換。 |
| --sstp-listen 待ち受け先 | 暫時指定 SSTP 伺服器的監聽端點後啟動。 \[2.8.97 以後\]<br>不讀取已儲存的 SSTP 伺服器監聽設定，只在指定的監聽端點上監聽。<br>這次啟動期間的監聽設定不會儲存。偏好設定中的 SSTP 伺服器清單只會顯示，無法新增、刪除或切換啟用／停用狀態。<br>預期用途是搭配 --option readonly，建立不會與其他正在執行的 SSP 互相干擾的測試用 SSP。<br><br>監聽端點可以用逗號分隔指定多個。格式如下。<br>連接埠號碼：在 IPv4 和 IPv6 的迴路位址（127.0.0.1 和 ::1）上監聽。例如：9801<br>localhost:連接埠號碼：與只指定連接埠號碼相同。<br>IPv4 位址:連接埠號碼：只在指定的位址上監聽。指定 0.0.0.0 時，會在所有 IPv4 介面上監聽。例如：192.168.0.5:9801<br>\[IPv6 位址\]:連接埠號碼：IPv6 位址必須以\[\]括住。指定 \[::\] 時，會在所有 IPv6 介面上監聽。例如：\[::1\]:9801<br>none：不監聽任何端點。省略監聽端點時也相同。<br><br>位址必須以數字指定（localhost 除外，不能使用主機名稱）。<br>格式錯誤或監聽失敗的端點會被忽略，並記錄在錯誤記錄中。即使發生這種情況，也不會還原為已儲存的設定。<br>請注意，若指定迴路位址以外的位址，其他電腦也會能夠連線至 SSTP。<br><br>範例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont フォント名 \[2.8.75 以後\] | 指定 GUI 使用的字型。並非所有部分都會完全替換，目前選單的部分項目和標題列等仍不會變更。 |

### 離線表面傾印

| 開關 | 功能 |
|---|---|
| --offline-dump 資料夾路徑 | 以離線傾印模式啟動。不實際啟動人格，讀取指定人格資料夾中的surfaces.txt，傾印表面圖像後立即結束。不會載入SHIORI/MAKOTO/PIRO，也不會建立視窗或訊息迴圈。<br>引數請指定人格資料夾的路徑（結尾的\\可省略）。<br>自2.8.98起，離線傾印相關選項（此選項、--dump-output-dir、--dump-error-log）指定相對路徑時，會以啟動SSP時的目前目錄為基準解析。<br><br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 資料夾名稱或名稱 \[可省略\] | 與 --offline-dump 搭配使用。以資料夾名稱（＝shell以下的相對路徑）或名稱指定要傾印的外殼。省略時會使用descript.txt指定的預設外殼（通常是master）。<br>自2.8.98起，找不到指定的外殼時，不會改用預設外殼傾印，而是將Error記錄到錯誤記錄檔，且不輸出任何內容。 |
| --dump-scope (範圍ID) \[可省略\] | 與 --offline-dump 搭配使用。指定傾印圖像的範圍ID。省略時為0。 |
| --dump-surface-list 清單 \[可省略\] | 與 --offline-dump 搭配使用。以逗號分隔指定要傾印的表面。可省略surface編號的前綴（surface）。也可以使用[surfaces.txt的表面ID指定擴充格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>範例：`--dump-surface-list "0,1,10"`<br>省略此選項時不會傾印表面（可搭配 --dump-error-log，只輸出剖析錯誤）。<br>自2.8.98起，前綴不只可在第一個項目省略，也可在各個項目省略（例如 `"0,surface1"`）。此外，若指定的單一編號表面不存在，會將Warning記錄到錯誤記錄檔（範圍指定中缺少的編號不會記錄）。 |
| --dump-output-dir 目錄 \[可省略\] | 與 --offline-dump 搭配使用。指定傾印圖像的輸出目錄。省略時會使用目前目錄（2.8.97以前，省略時不會進行傾印）。 |
| --dump-output-prefix 前綴 \[可省略\] | 與 --offline-dump 搭配使用。指定輸出檔名中位於表面編號前面的部分。預設的「surface」會被此字串取代（不會附加在後）。省略時為「surface」。<br>範例：使用 `--dump-output-prefix "x_"` 時，表面0會輸出為 `x_0.png`（而非 `x_surface0.png`）。 |
| --dump-error-log 檔案路徑 \[可省略\] | 與 --offline-dump 搭配使用。將載入外殼時的錯誤記錄（例如surfaces.txt的剖析錯誤）寫入指定路徑。<br>省略 --dump-surface-list，只指定此選項，即可不進行傾印，只執行錯誤檢查。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>輸出格式：含BOM的UTF-8 CSV（換行符號為CRLF）。每行一筆資料，各欄以"括住，欄位中的"會以""跳脫。<br>`"時刻","ゴースト名","レベル","内容"`<br>時間：HH:MM:SS格式。<br>等級：Info / Notice / Warning / Error / Critical / System 其中之一。<br>內容：記錄本文。自2.8.94起，SERIKO相關記錄會附上定義來源檔案（相對於人格資料夾的路徑）和行號，例如 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。重複定義的記錄也會一併列出先前定義的位置，格式為 `(檔案名稱:Line=n)`。<br>自2.8.94起，指定此選項時，最多會保留10000筆記錄，也不會將相似內容的記錄彙整成摘要行（等級System），因此不會遺漏記錄。<br>若沒有任何記錄，不會建立檔案（即使指定路徑已有檔案，也不會覆寫或刪除）。<br><br>結束代碼：自2.8.94起，處理程序會依記錄中最嚴重的等級，以對應的結束代碼結束。<br>0：沒有記錄，或只有Info/Notice<br>1：有Warning（沒有Error/Critical）<br>2：有Error（沒有Critical）<br>3：有Critical<br>若人格本身載入失敗（例如無法讀取指定資料夾中的descript.txt），不會輸出記錄，結束代碼也會是0。 |
| --dump-surface-option 選項 \[可省略\] \[2.8.57以後\] | 指定離線傾印功能的選項。可指定以下項目。<br>backlog：裁切與回溯記錄功能相同的區域（臉部周圍）。但不會縮放，會直接輸出合成圖像。<br>collision：繪製碰撞判定的形狀和名稱後輸出。與開發用面板中的碰撞判定顯示相同，但名稱一律會顯示，且不會繪製表面外框、有效範圍、重疊判定範圍等外框矩形。\[2.8.98以後\]<br>自2.8.98起，可用逗號分隔指定多個選項（例如：`--dump-surface-option backlog,collision`）。<br>若未透過此選項指定collision，無論使用者設定（開發用面板中的碰撞判定顯示）為何，都不會繪製碰撞判定。 |
| --dump-bind 換裝指定 \[可省略\] \[2.9.05以後\] | 與 --offline-dump 搭配使用。指定傾印時的換裝狀態。<br>可用分號分隔多組「類別名稱,零件名稱,ON/OFF」。意義與[`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_)相同；在互斥類別中開啟某個零件時，同一類別中的其他零件會關閉。<br>零件名稱留空或指定為 `__ALL__` 時，會套用至該類別中的所有零件。<br>ON/OFF指定為1或true時代表開啟，指定為0或false時代表關閉。省略時視為開啟（`\![bind]` 省略時會切換狀態，但此選項不會切換狀態）。<br>範例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基準狀態是外殼的descript.txt所指定的各零件預設值（`sakura.bindgroup*.default`），不會使用使用者最後一次換裝的狀態（`shell\profile`中的儲存值）。只會從基準狀態變更指定的零件。<br>換裝會套用至 --dump-scope 指定的範圍。<br>若指定不存在的類別或零件，會記錄Warning（--dump-error-log的結束代碼為1），並忽略該指定，繼續傾印。<br>類別名稱和零件名稱前後的空白不會移除，因此逗號後面請勿加入空白。 |
| --dump-animation 動畫ID \[可省略\] \[2.9.05以後\] | 與 --offline-dump 搭配使用。像`\i[ID]`一樣播放指定動畫，並依序輸出每個影格的圖像。只能指定一個ID（除了數字，也可像`\i[ID]`一樣使用surfaces.txt中為動畫設定的名稱）。<br>每個表面會先輸出與一般傾印相同的圖像（runonce動畫播放一輪後的狀態）為 `surface0.png`，接著每當指定動畫的圖樣前進時，就依從0開始的4位數連號輸出 `surface0_0000.png`、`surface0_0001.png`…等圖像。--dump-output-prefix和 --dump-surface-option的指定也會套用至連號圖像。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always等動畫會像一般傾印一樣運作，指定動畫則會在其上播放。連號輸出的對象只有指定動畫本身的圖樣；即使always動畫前進，輸出張數也不會增加。<br>指定動畫播放至最後一個圖樣時即結束（always動畫則在播放一輪時結束）。即使因其他動畫的stop或互斥而停止，也會在此時結束。<br>以start、alternativestart、parallelstart啟動的其他動畫不會列入連號輸出。若指定動畫包含這些圖樣，會記錄Warning（但仍會繼續輸出）。<br>start、stop類型的圖樣不會改變圖像，因此不會計為連號中的一個影格。<br>若指定的ID不存在於該表面，或因換裝而失效、處於互斥狀態等原因而無法播放，會記錄Warning，該表面只會輸出一般的一張圖像。<br>連號圖像最多輸出10000張（至 `_9999`）；達到上限時會記錄Warning並停止輸出。 |

### 離線工具

| 開關 | 功能 |
|---|---|
| --offline-tool 種別 \[2.9.01以降\] | 以離線工具模式啟動。不啟動人格，從 --target-dir 指定的資料夾建立 NAR、更新定義檔或壓縮檔後立即結束。不會觸發任何人格事件，也不會建立視窗或訊息迴圈。<br>處理方式與 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 相同，但沒有輸出位置限制（例如只能存放在 SSP 管理的資料夾），可自由指定。<br>種類請指定下列其中一種（不區分大小寫）。<br><br>nar：建立 NAR 檔案。`developer_options.txt` 中的 nonar 設定、.narignore 等排除規則，會與一般建立 NAR 時相同地套用。如果資料夾根目錄沒有 install.txt，會從 descript.txt（或 `ghost\master\descript.txt`）判斷種類與名稱，並在目標資料夾建立 install.txt 後一併收錄。若無法判斷種類與名稱，則會失敗。<br>updatedata：建立更新定義檔。如果 --output 的檔名以 .dau 結尾，會建立與 updates2.dau 相同格式的檔案；否則會建立 updates.txt 格式的檔案，且只建立指定的單一檔案。既不會建立也不會刪除目標資料夾根目錄或 `ghost\master` 中的 updates2.dau / updates.txt。`developer_options.txt` 中的 noupdate 設定、.updateignore 等排除規則，會與一般情況相同地套用。<br>archive：直接壓縮目標資料夾。不會讀取 .narignore 等排除規則（不會收錄隱藏檔案及隱藏資料夾）。格式由 --output 的副檔名決定，若為 .7z 則使用 7z 格式，否則使用 zip 格式。<br><br>無論指定哪種種類，若輸出檔案已存在，都會覆寫。若輸出位置位於目標資料夾內，則不會收錄該檔案本身。輸出資料夾必須事先存在。<br>若 --target-dir 或 --output 指定相對路徑，會以啟動 SSP 時的目前目錄為基準解析。<br><br>結束代碼：<br>0：成功<br>1：引數無效（種類不明、未指定 --target-dir 或 --output、--target-dir 不存在或不是資料夾）<br>2：建立失敗（無法寫入輸出位置、無法判斷 NAR 的種類與名稱、updatedata 遇到無法讀取的檔案或層級過深（超過 32 層）等）。失敗時也可能留下部分建立的檔案<br><br>範例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>範例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>範例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 資料夾路徑 \[2.9.01以降\] | 與 --offline-tool 搭配使用（必填）。指定處理目標資料夾（結尾的 \\ 可省略）。建立 NAR 或更新定義檔時，請指定人格等內容的根資料夾（包含 descript.txt、install.txt 或 ghost 資料夾的資料夾）。 |
| --output 檔案路徑 \[2.9.01以降\] | 與 --offline-tool 搭配使用（必填）。指定要建立的檔案路徑。 |
| --password 密碼 \[省略可\] \[2.9.01以降\] | 與 --offline-tool 的 nar 或 archive 搭配使用。使用指定的密碼建立 AES 加密 ZIP（若為 7z 格式，則使用 7z 加密）。updatedata 會忽略此設定。<br>密碼會以原文保留在命令列中，請妥善處理。 |

### 其他

| 開關 | 功能 |
|---|---|
| `initial_install.nar` | 這不是啟動選項，但若在與 ssp.exe 相同的資料夾中放置名為 <strong>`initial_install.nar`</strong> 的 NAR 檔案，SSP 啟動時會以靜默方式（不顯示確認對話方塊）覆蓋安裝。安裝完成後，`initial_install.nar` 會自動刪除。可用於隨 SSP 一併附帶人格等內容進行散布。 \[2.7.52～\] |
