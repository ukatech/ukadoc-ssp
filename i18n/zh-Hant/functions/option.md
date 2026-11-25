# 啟動選項一覽

啟動 ssp.exe 時，可以加上下列選項（開關）。

## 什麼是啟動選項？

這是在啟動 Windows 軟體時，切換設定後執行的機制。<br>
如需詳細資訊，請查詢執行選項、命令列選項、啟動選項等詞彙。

## 使用方法

使用方法有很多種。<br>
例如，也可以從「命令提示字元」或「執行」使用。<br>
這裡介紹如何建立專用於啟動選項的捷徑。

1. 建立 ssp.exe 的捷徑。<br>
   例：右鍵點擊 ssp.exe→建立捷徑
2. 開啟建立的捷徑內容。<br>
   例：右鍵點擊捷徑→內容
3. 確認內容的「目標」欄位中有 ssp.exe 的路徑後，用「""」將整個路徑括起來。
4. 在括起來的路徑後面加上一個半形空格，然後輸入下列啟動選項。<br>
   例："C:/User/Document/略/SSP/ssp.exe" --random
5. 按下確定按鈕關閉內容視窗，並順便為捷徑取一個容易辨識的名稱。<br>
   例：SSP-隨機啟動
6. 執行該捷徑後，與一般啟動 ssp.exe 不同，SSP 會套用選項設定後啟動。

## 選項一覽

建議各選項使用 `--オプション名` 格式。為了向下相容，仍可使用 `/x` / `-x` 格式的短選項。

需要指定值的選項，請像 `--オプション名 値` 這樣，以半形空格分隔選項名稱和值。若值中包含空白，請用「""」括起來。

2.8.97 以後的版本也支援 `--オプション名=値` 格式作為輔助（例：`--sstp-listen=9900`）。本頁以空白分隔的寫法為主。請注意，`/x` 格式的短選項不能使用 `=` 格式。

- [--option 選項](#--option-オプション)
- [一般選項](#一般オプション)
- [離線表面傾印](#オフラインサーフェスダンプ)
- [離線工具](#オフラインツール)
- [其他](#その他)

### --option 選項

--option 選項可以用逗號分隔，一次指定多個選項（例：`--option bootunlock,standalone`）。

| 開關 | 功能 |
|---|---|
| --option nobootcheck<br>（舊: /o nobootcheck） | 停用異常結束檢查 |
| --option layered<br>（舊: /o layered） | 啟用半透明視窗 |
| --option region<br>（舊: /o region） | 停用半透明視窗（區域模式） |
| --option bootunlock<br>（舊: /o bootunlock） | 跳過重複啟動檢查 |
| --option standalone<br>（舊: /o standalone） | 當 SSP.exe 已經啟動時，停用將安裝或啟動人格等作業交由執行中的 SSP.exe 處理的機制，一律由自身啟動人格或執行安裝。<br>像 --option bootunlock,standalone 這樣與跳過重複啟動檢查一起指定，即可在完全不顯示警告的情況下啟動多個 SSP.exe。 |
| --option kiosk<br>（舊: /o kiosk） | 啟用 KIOSK 模式。行為如下。 \[2.6.54～\]<br>啟用 --option bootunlock,standalone<br>alignmenttodesktop 一律設為 free<br>不接受滑鼠及鍵盤輸入<br>完全不干涉重複啟動檢查<br>不顯示通知區域圖示及工作列圖示<br>不儲存由 SSP 管理的人格及外殼設定<br>不顯示表示啟動中的視窗<br>不顯示錯誤通知 |
| --option readonly<br>（舊: /o readonly） | 啟用唯讀模式。 \[2.8.96以後\]<br>啟動時不對使用者環境進行任何永久性變更。適合用於不想影響設定而試用功能，或暫時在他人的電腦上執行 SSP 等情況。<br>畫面上的行為及與人格的互動均與平常相同，不會像 KIOSK 模式那樣封鎖輸入或限制顯示。此模式獨立於 KIOSK 模式，也可以像 --option kiosk,readonly 這樣一起使用。<br><br>行為如下。<br>啟用 --option bootunlock,standalone（因為若將作業交給執行中的 SSP，該 SSP 就會寫入設定）<br>完全不干涉重複啟動檢查<br>不儲存任何偏好設定、人格、外殼、對話方塊及外掛程式的設定<br>不儲存啟動歷程、使用統計、快取、Cookie、vanish 紀錄、SSTP 設定、POP 設定，以及伺か (Ukagaka) 即時通訊的資訊與記錄<br>不儲存行事曆的行程（schedule.ics）<br>不共用存檔資料（既不匯出至雲端，也不從雲端還原至本機）<br>不寫入登錄。不進行檔案關聯、建立捷徑、註冊跳躍清單或新增至「最近使用的項目」<br>不變更桌面桌布及背景顏色<br>不清空資源回收筒<br>即使執行 vanish 也不刪除人格的資料夾<br>不自動更新主程式、人格、對話方塊、外掛程式及語言資源。也不手動執行線上更新或安裝 NAR<br>不安裝 `initial_install.nar`<br>不透過 SNTP 執行 NTP 時間同步<br><br>設定值本身仍可照常變更，但由於結束時不會寫回檔案，因此下次啟動時不會保留。<br>執行所需的暫存檔（暫存資料夾）仍會照常建立，並在結束時刪除。 |
| --option dontloadmodule<br>（舊: /o dontloadmodule） | 不載入 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 系列 |
| --option dpiaware<br>（舊: /o dpiaware） | 將 DPI 感知模式設為 Per-Monitor V2 後啟動 |
| --option callghost<br>（舊: /o callghost） | 與 --install 同時使用時，安裝完成後會自動呼叫人格。 |
| --option deletesource<br>（舊: /o deletesource） | 與 --install 同時使用時，NAR 安裝成功後會刪除 NAR。 |

### 一般選項

| 開關 | 功能 |
|---|---|
| --fmo-name FMO名稱<br>（舊版: /f FMO名稱） | 強制將寫入的FMO名稱改為指定的名稱。 |
| --random<br>（舊版: /r） | 不論設定為何，都隨機啟動人格。 |
| --ghost 資料夾名稱/人格名稱<br>（舊版: /g 資料夾名稱/人格名稱） | 啟動指定的人格。以空白分隔可啟動多個人格。2.9.35以後，也可以指定人格的UUID（屬性系統的`uuid`，形式如`R5dVNluBvKjtQqjP0dAuoA==`），取代資料夾名稱/人格名稱。若在SSP啟動時指定，會將指定的第一個人格作為第1組人格啟動。<br>2.8.99以後，若在SSP啟動時指定人格資料夾的絕對路徑（例：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`），而該人格不在載入資料夾中，則會僅在本次執行期間，將其上層資料夾（此例中為 `C:\Users\user\Desktop\`）暫時加入人格載入資料夾後啟動。僅適用於存在 `ghost\master\descript.txt` 的資料夾。<br>暫時加入的資料夾不會儲存至設定，在資料夾設定畫面中會顯示為「(temporary)」，無法編輯或刪除，也不會成為人格安裝位置的候選項。若從資料夾設定畫面明確加入相同的資料夾，則會儲存為一般載入資料夾。<br>若SSP已經啟動（指定內容會交給執行中的SSP處理），則不會執行此處理。 |
| --help<br>（舊版: /?） | 在瀏覽器中開啟啟動選項的說明頁面。 |
| --help 檔案名稱<br>（舊版: /? 檔案名稱） | 在瀏覽器中開啟指定檔案名稱的說明頁面。 |
| --ukagaka-link x-ukagaka-link:URL<br>（舊版: /m x-ukagaka-link:URL） | 執行與開啟x-ukagaka-link:URL時相同的操作。若在SSP啟動時指定，會等到第1組人格啟動後才執行。 |
| --install NAR檔案名稱<br>（舊版: /i NAR檔案名稱） | 安裝NAR。若已有執行中的SSP，會將安裝處理交給該SSP；否則會自行安裝後繼續啟動。<br>以空白分隔指定多個檔案時，會依序安裝多個NAR。<br>即使接收安裝處理的SSP正顯示未安裝人格的警告對話方塊（「何とかして下さい」對話方塊），也能處理。<br>此外，在此情況下若同時指定 --option callghost，會自動按下警告對話方塊中的繼續啟動按鈕，繼續啟動。 |
| --ssf SSF檔案名稱<br>（舊版: /s SSF檔案名稱） | 執行[SSF檔案](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。若在SSP啟動時指定，會等到第1組人格啟動後才執行。 |
| --windowmode 模式 \[可省略\] | 2.8.78～ 以實驗性功能「[視窗模式](windowmode.md)」啟動。將視窗內部視為一個虛擬螢幕來啟動人格，方便進行擷取畫面等操作，並避免影響整個桌面。<br>2.8.86～ 可指定模式。可指定的模式如下。省略時會沿用上次的設定（初始值為shared）。<br>shared：將所有執行中的人格集中在同一個視窗中。<br>perghost：每個人格各使用一個視窗。<br>2.8.86以後，視窗模式的狀態會儲存為設定，因此即使不加上此選項，也會以上次的狀態啟動。若要關閉，請從右鍵選單的「設定」或偏好設定的「實況」切換。 |
| --sstp-listen 監聽位置 | 暫時指定SSTP伺服器的監聽位置後啟動。 \[2.8.97以後\]<br>不會載入已儲存的SSTP伺服器監聽設定，只在指定的監聽位置監聽。<br>本次執行期間的監聽設定不會儲存。偏好設定中的SSTP伺服器清單僅供檢視，無法新增、刪除或切換啟用／停用。<br>此選項設計用於搭配 --option readonly，啟動不會與其他執行中的SSP互相干擾的測試用SSP。<br><br>可用逗號分隔指定多個監聽位置。格式如下。<br>連接埠號碼：在IPv4與IPv6的迴路位址（127.0.0.1 與 ::1）上監聽。例：9801<br>localhost:連接埠號碼：與只指定連接埠號碼相同。<br>IPv4位址:連接埠號碼：只在指定的位址上監聽。指定 0.0.0.0 時，會在所有IPv4介面上監聽。例：192.168.0.5:9801<br>\[IPv6位址\]:連接埠號碼：IPv6位址須以\[\]括住。指定 \[::\] 時，會在所有IPv6介面上監聽。例：\[::1\]:9801<br>none：不監聽任何位置。省略監聽位置時也相同。<br><br>位址須以數值指定（localhost 除外，不能使用主機名稱）。<br>格式不正確或監聽失敗的監聽位置會被忽略，並記錄在錯誤記錄中。此時也不會還原為已儲存的設定。<br>請注意，若指定迴路位址以外的位址，便會接受來自其他電腦的SSTP。<br><br>例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字型名稱 \[2.8.75以後\] | 指定GUI使用的字型。並非所有字型都會被取代，部分選單與標題列等目前不會變更。 |
| --time-shift 值 \[2.9.39以後\] | 在啟動時指定「虛擬變更目前時間」（時光機）的時間差。用於測試依賴日期或時間的人格。<br>請以 `--time-shift=+3600` 這類使用 `=` 連接的格式指定（因為以 `-` 開頭的值若以空白分隔，便無法與選項名稱區分）。<br>此指定僅在本次執行期間有效，不會儲存至設定。即使設定中已有儲存的時間差，也會優先使用此指定值。<br><br>值可為以下其中一種。<br>+秒數 或 -秒數：時間差本身（秒數）。必須加上正負號。例：+86400（1天後）、-3600（1小時前）<br>0：將時間差設為0（維持實際時間）。<br>ISO8601格式的日期時間：計算與實際時間的差值，使時間變為指定的日期時間。若未指定時區，則視為本地時間。時鐘不會停止，而是從該日期時間繼續前進。例：2026-12-31T23:59:50<br><br>時間差最大約為200年，不滿1秒的部分會捨去。無法解析的值會被忽略（時間差維持為0），並記錄在錯誤記錄中。<br>使用此指定值啟動時，不會顯示提醒設定中仍有時間差的提示（給開發者的對話方塊）。<br><br>例：`ssp.exe --option readonly --time-shift=2026-12-31T23:59:50` |
| --allow-timemachine-control \[2.9.39以後\] | 允許透過Sakura Script `\![timemachine,set,値]` / `\![timemachine,reset]` 及SSTP的EXECUTE `SetTimeShift`，在執行期間操作「虛擬變更目前時間」。供測試使用。<br>未指定此選項啟動時，這些指令不會執行任何操作，並會在錯誤記錄中記錄警告（避免人格腳本或外部程式改變整體時鐘）。<br>時間差的值的格式與 --time-shift 相同。 |

### 離線表面匯出

| 參數 | 功能 |
|---|---|
| --offline-dump 資料夾路徑 | 以離線匯出模式啟動。不實際啟動人格，而是讀取指定人格資料夾中的 surfaces.txt，匯出表面圖片後立即結束。不會載入 SHIORI/MAKOTO/PIRO，也不會建立視窗及訊息迴圈。<br>請在參數中指定人格的資料夾路徑（結尾的 \\ 可省略）。<br>2.8.98 以後，若為離線匯出相關選項（此選項、--dump-output-dir、--dump-error-log）指定相對路徑，會以啟動 SSP 時的目前目錄為基準解析。<br><br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 資料夾名稱或名稱 \[可省略\] | 與 --offline-dump 搭配使用。以資料夾名稱（＝shell 以下的相對路徑）或名稱指定要匯出的外殼。省略時會使用 descript.txt 中指定的預設外殼（通常是 master）。<br>2.8.98 以後，若找不到指定的外殼，不會使用預設外殼匯出，而是在錯誤記錄中記錄 Error，且不輸出任何內容。 |
| --dump-scope (範圍 ID) \[可省略\] | 與 --offline-dump 搭配使用。指定匯出圖片的範圍 ID。省略時為 0。 |
| --dump-surface-list 清單 \[可省略\] | 與 --offline-dump 搭配使用。以逗號分隔指定要匯出的表面。surface 編號的前綴（surface）可以省略。也可以使用 [surfaces.txt 表面 ID 指定方式的擴充格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>範例：`--dump-surface-list "0,1,10"`<br>省略此選項時不會匯出表面（可搭配 --dump-error-log 僅輸出解析錯誤）。<br>2.8.98 以後，不僅第一個項目，各個項目都可以省略前綴（例如 `"0,surface1"`）。此外，若以單一編號而非範圍指定的表面不存在，會在錯誤記錄中記錄 Warning（不會記錄指定範圍內缺少的編號）。 |
| --dump-output-dir 目錄 \[可省略\] | 與 --offline-dump 搭配使用。指定匯出圖片的輸出目錄。省略時會使用目前目錄（2.8.97 以前省略時不會執行匯出）。 |
| --dump-output-prefix 前綴 \[可省略\] | 與 --offline-dump 搭配使用。指定輸出檔案名稱中表面編號前面的部分。預設的「surface」會被此字串取代（而非附加在後面）。省略時為「surface」。<br>範例：使用 `--dump-output-prefix "x_"` 時，表面 0 的檔名會是 `x_0.png`（而非 `x_surface0.png`）。 |
| --dump-error-log 檔案路徑 \[可省略\] | 與 --offline-dump 搭配使用。將載入外殼時的錯誤記錄（例如 surfaces.txt 的解析錯誤）寫入指定路徑。<br>省略 --dump-surface-list 並只指定此選項，即可不匯出圖片而僅執行錯誤檢查。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>輸出格式：附有 BOM 的 UTF-8 CSV（換行為 CRLF）。每行為一筆記錄，各欄位以 " 包住，欄位中的 " 會跳脫為 ""。<br>`"時刻","ゴースト名","レベル","内容"`<br>時間：HH:MM:SS 格式。<br>層級：Info / Notice / Warning / Error / Critical / System 其中之一。<br>內容：記錄的本文。2.8.94 以後，SERIKO 相關記錄會附上定義來源檔案（相對於人格資料夾的路徑）及行號，例如 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...`。重複定義的記錄也會以 `(ファイル名:Line=n)` 的形式列出先前定義的位置。<br>2.8.94 以後，指定此選項時最多保留 10000 筆記錄，也不會將內容相似的記錄彙整成摘要行（層級為 System），因此不會遺漏記錄。<br>若沒有任何記錄，則不會建立檔案（即使相同路徑已有檔案，也不會覆寫或刪除）。<br><br>結束代碼：2.8.94 以後，程序會依記錄中最嚴重的層級，以對應的結束代碼結束。<br>0：沒有記錄，或只有 Info/Notice<br>1：有 Warning（沒有 Error/Critical）<br>2：有 Error（沒有 Critical）<br>3：有 Critical<br>若人格本身載入失敗（例如無法讀取指定資料夾中的 descript.txt），則不會輸出記錄，結束代碼也會是 0。 |
| --dump-surface-option 選項 \[可省略\] \[2.8.57 以後\] | 指定離線匯出功能的選項。可指定的選項如下。<br>backlog：裁切與談話記錄功能相同的區域（臉部周圍）。但不會縮放，而是直接輸出合成圖片。<br>collision：在圖片上繪製碰撞判定（collision）的形狀及名稱後輸出。與開發用調色盤的碰撞判定顯示相同，但名稱一律顯示，且不會繪製表面外框、有效範圍及重疊判定範圍等外接矩形。\[2.8.98 以後\]<br>2.8.98 以後，可以逗號分隔指定多個選項（範例：`--dump-surface-option backlog,collision`）。<br>若此選項未指定 collision，無論使用者設定（開發用調色盤的碰撞判定顯示）為何，都不會繪製碰撞判定。 |
| --dump-bind 換裝指定 \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。指定匯出時的換裝狀態。<br>可以分號分隔指定多組「類別名稱,部件名稱,ON/OFF」。其意義與 [`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_) 相同，在互斥類別中將某個部件設為 ON 時，同類別的其他部件會設為 OFF。<br>將部件名稱留空或設為 `__ALL__`，即可指定類別中的所有部件。<br>ON/OFF 使用 1 或 true 表示 ON，0 或 false 表示 OFF。省略時視為 ON（`\![bind]` 省略時會反轉，但此處不會反轉）。<br>範例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基準狀態為外殼的 descript.txt 中指定的各部件預設值（`sakura.bindgroup*.default`），不會使用使用者最後一次換裝的狀態（`shell\profile` 內的儲存值）。只有指定的部件會在此基礎上變更。<br>換裝會套用至 --dump-scope 指定的範圍。<br>若指定不存在的類別或部件，會記錄 Warning（--dump-error-log 的結束代碼為 1），僅忽略該項指定並繼續匯出。<br>類別名稱及部件名稱前後的空白不會被移除，請勿在逗號後面加入空白。 |
| --dump-animation 動畫 ID \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。以與 `\i[ID]` 相同的方式播放指定動畫，並以連號輸出各影格的圖片。只能指定一個 ID（除了數值，也可以和 `\i[ID]` 一樣使用 surfaces.txt 中為動畫指定的名稱）。<br>對每個表面，首先輸出與一般匯出相同的圖片（runonce 動畫播放一輪後的狀態），檔名為 `surface0.png`；接著每當指定動畫的圖樣推進，就以從 0 開始的 4 位數連號輸出 `surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix 和 --dump-surface-option 的設定也會套用至連號圖片。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always 等動畫會與一般匯出時一樣運作，指定的動畫則疊加在其上。只有指定動畫本身的圖樣會納入連號輸出，即使 always 動畫推進，圖片數量也不會增加。<br>指定動畫推進至最後一個圖樣時（always 則為播放一輪時）結束。若因其他動畫的 stop 或互斥而停止，也會在該處結束。<br>由 start、alternativestart、parallelstart 啟動的其他動畫不會納入連號輸出。若指定動畫包含這些圖樣，會記錄 Warning（輸出會繼續）。<br>start、stop 類型的圖樣不會改變圖片，因此不計為連號輸出的一個影格。<br>若指定的 ID 不存在於該表面，或因換裝而停用、互斥等原因無法播放，會記錄 Warning，該表面僅輸出一般的一張圖片。<br>連號最多輸出 10000 張（至 `_9999`），達到上限時會記錄 Warning 並停止。 |

### 離線工具

| 參數 | 功能 |
|---|---|
| --offline-tool 類型 \[2.9.01以後\] | 以離線工具模式啟動。不啟動人格，直接從 --target-dir 指定的資料夾建立 NAR、更新定義檔或壓縮檔，然後立即結束。不會發生任何人格事件，也不會建立視窗或訊息迴圈。<br>處理方式與 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 相同，但輸出位置不受限制（例如限於 SSP 管理下的資料夾），可以自由指定。<br>類型請指定以下其中一種（不區分大小寫）。<br><br>nar：建立 NAR 檔案。與一般建立 NAR 時相同，會套用 `developer_options.txt` 的 nonar 設定及 .narignore 等排除設定。若資料夾根目錄沒有 install.txt，會根據 descript.txt（或 `ghost\master\descript.txt`）判定類型和名稱，在目標資料夾中建立 install.txt 後再將其收錄。若無法判定類型和名稱，則會失敗。<br>updatedata：建立更新定義檔。若 --output 的檔案名稱以 .dau 結尾，則使用與 updates2.dau 相同的格式，否則使用 updates.txt 格式，僅建立指定的單一檔案。不會在目標資料夾根目錄或 `ghost\master` 中建立或刪除 updates2.dau / updates.txt。與一般情況相同，會套用 `developer_options.txt` 的 noupdate 設定及 .updateignore 等排除設定。<br>archive：直接壓縮目標資料夾。不讀取 .narignore 等排除設定（不收錄隱藏檔案及隱藏資料夾）。格式由 --output 的副檔名決定：.7z 為 7z 格式，其餘為 zip 格式。<br><br>不論使用哪種類型，若輸出檔案已存在，將會覆寫。若輸出位置位於目標資料夾內，不會收錄該輸出檔案本身。輸出資料夾必須事先存在。<br>若 --target-dir 或 --output 指定的是相對路徑，會以啟動 SSP 時的目前目錄為基準解析。<br><br>結束代碼：<br>0：成功<br>1：引數無效（類型不明、未指定 --target-dir 或 --output、--target-dir 不存在或不是資料夾）<br>2：建立失敗（無法寫入輸出位置、無法判定 NAR 的類型和名稱、updatedata 中有無法讀取的檔案或過深的層級（超過 32 層）等）。失敗時也可能留下建立到一半的檔案<br><br>範例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>範例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>範例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 資料夾路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定要處理的資料夾（結尾的 \\ 可省略）。建立 NAR 或更新定義檔時，請指定人格等的根資料夾（包含 descript.txt、install.txt 和 ghost 資料夾的資料夾）。 |
| --output 檔案路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定要建立的檔案路徑。 |
| --password 密碼 \[可省略\] \[2.9.01以後\] | 與 --offline-tool 的 nar 或 archive 搭配使用。使用指定的密碼建立 AES 加密的 ZIP 檔案（7z 格式則使用 7z 加密）。使用 updatedata 時會忽略此參數。<br>密碼會以原文留在命令列中，請注意保管。 |

### 其他

| 參數 | 功能 |
|---|---|
| `initial_install.nar` | 雖然這不是啟動選項，但若將名為<strong>`initial_install.nar`</strong>的 NAR 檔案放在與 ssp.exe 相同的資料夾中，SSP 啟動時會以靜默方式（不顯示確認對話方塊）覆寫安裝。安裝完成後，`initial_install.nar` 會自動刪除。可用於將人格等項目與 SSP 一同打包發布的情況。 \[2.7.52～\] |
