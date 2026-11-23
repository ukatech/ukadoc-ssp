# 啟動選項一覽

啟動 ssp.exe 時，可以加上下列選項（開關）。

## 什麼是啟動選項？

這是在啟動 Windows 軟體時，切換設定後執行的機制。<br>
如需詳細資訊，請查詢執行時選項、命令列選項、啟動選項等詞彙。

## 使用方法

使用方法有很多種。<br>
例如，也可以透過「命令提示字元」或「執行」使用。<br>
這裡介紹建立專用於啟動選項的捷徑的方法。

1. 建立 ssp.exe 的捷徑。<br>
   例：在 ssp.exe 上按右鍵→建立捷徑
2. 開啟建立的捷徑的內容。<br>
   例：在捷徑上按右鍵→內容
3. 確認內容的「目標」欄位中有 ssp.exe 的路徑後，將整個路徑用「""」括起來。
4. 在括起來的路徑後面加上一個半形空格，再輸入下列啟動選項。<br>
   例："C:/User/Document/略/SSP/ssp.exe" --random
5. 按下確定按鈕關閉內容，順便為捷徑取個容易辨識的名稱。<br>
   例：SSP-隨機啟動
6. 執行該捷徑時，就能以套用選項設定的狀態啟動，有別於直接啟動 ssp.exe。

## 選項一覽

建議各選項使用 `--オプション名` 格式。為了向下相容，仍可繼續使用 `/x` / `-x` 格式的短選項。

需要指定值的選項，請依照 `--オプション名 値` 的格式，以半形空格分隔選項名稱和值。如果值包含空格，請用「""」括起來。

2.8.97 以後的版本也支援 `--オプション名=値` 格式作為輔助（例：`--sstp-listen=9900`）。本頁以空格分隔的寫法為主。請注意，`/x` 格式的短選項無法使用 `=` 格式。

- [--option 選項](#--option-オプション)
- [一般選項](#一般オプション)
- [離線 Surface 傾印](#オフラインサーフェスダンプ)
- [離線工具](#オフラインツール)
- [其他](#その他)

### --option 選項

--option 選項可以用逗號分隔，指定多個選項（例：`--option bootunlock,standalone`）。

| 開關 | 功能 |
|---|---|
| --option nobootcheck<br>（舊版: /o nobootcheck） | 停用異常結束檢查 |
| --option layered<br>（舊版: /o layered） | 啟用半透明視窗 |
| --option region<br>（舊版: /o region） | 停用半透明視窗（區域模式） |
| --option bootunlock<br>（舊版: /o bootunlock） | 跳過重複啟動檢查 |
| --option standalone<br>（舊版: /o standalone） | 當 SSP.exe 已經啟動時，停用將安裝或啟動人格等處理交由執行中的 SSP.exe 執行的機制，一律由自身啟動人格或進行安裝。<br>如 --option bootunlock,standalone 所示，與跳過重複啟動檢查的選項一起指定，即可在完全不顯示警告的情況下啟動多個 SSP.exe。 |
| --option kiosk<br>（舊版: /o kiosk） | 啟用 KIOSK 模式。行為如下。 \[2.6.54～\]<br>啟用 --option bootunlock,standalone<br>alignmenttodesktop 一律設為 free<br>不接受滑鼠及鍵盤輸入<br>完全不干預重複啟動檢查<br>不顯示通知區域圖示及工作列圖示<br>不儲存由 SSP 管理的人格及外殼設定<br>不顯示表示啟動中的視窗<br>不顯示錯誤通知 |
| --option readonly<br>（舊版: /o readonly） | 啟用唯讀模式。 \[2.8.96 以後\]<br>啟動時不會對使用者環境進行任何永久性變更。適合用於不想更動設定就試用功能，或想在他人的電腦上暫時執行 SSP 等情況。<br>畫面行為和與人格的互動皆與平常相同，不會像 KIOSK 模式一樣封鎖輸入或限制顯示。此模式與 KIOSK 模式相互獨立，也可以如 --option kiosk,readonly 所示同時使用。<br><br>行為如下。<br>啟用 --option bootunlock,standalone（若將處理交由執行中的 SSP 執行，該 SSP 就會寫入設定）<br>完全不干預重複啟動檢查<br>完全不儲存偏好設定、人格、外殼、對話方塊及外掛程式的設定<br>不儲存啟動歷程、使用統計、快取、Cookie、vanish 記錄、SSTP 設定、POP 設定、伺か (Ukagaka) 即時通訊的資訊與記錄<br>不儲存行事曆的行程（schedule.ics）<br>不進行儲存資料共用（不匯出至雲端，也不從雲端還原至本機）<br>不寫入登錄。不進行檔案關聯、建立捷徑、登錄跳躍清單及新增至「最近使用的項目」<br>不變更桌面桌布及背景色彩<br>不清空資源回收筒<br>即使發生 vanish 也不刪除人格資料夾<br>不自動更新主程式、人格、對話方塊、外掛程式及語言資源。也不進行手動線上更新及 NAR 安裝<br>不安裝 `initial_install.nar`<br>不透過 SNTP 進行 NTP 時間同步<br><br>設定值本身仍可照常變更，但結束時不會寫回檔案，因此下次啟動時不會保留。<br>運作所需的暫存檔案（暫存資料夾）仍會照常建立，並在結束時刪除。 |
| --option dontloadmodule<br>（舊版: /o dontloadmodule） | 不載入 SHIORI/MAKOTO/PLUGIN/HEADLINE/CALENDAR 類模組 |
| --option dpiaware<br>（舊版: /o dpiaware） | 將 DPI Awareness Mode 設為 Per-Monitor V2 後啟動 |
| --option callghost<br>（舊版: /o callghost） | 與 --install 同時使用時，安裝完成後會自動呼叫人格。 |
| --option deletesource<br>（舊版: /o deletesource） | 與 --install 同時使用時，NAR 安裝成功後會刪除 NAR。 |

### 一般選項

| 參數 | 功能 |
|---|---|
| --fmo-name FMO名稱<br>（舊: /f FMO名稱） | 強制將寫入的 FMO 名稱改為指定的名稱。 |
| --random<br>（舊: /r） | 不論設定為何，隨機啟動人格。 |
| --ghost 資料夾名稱/人格名稱<br>（舊: /g 資料夾名稱/人格名稱） | 啟動指定的人格。以空格分隔可啟動多個人格。2.9.35 以後，也可以指定人格的 UUID（屬性系統的 `uuid`，格式如 `R5dVNluBvKjtQqjP0dAuoA==`），代替資料夾名稱/人格名稱。若在啟動 SSP 時指定，會將指定的第一個人格作為第 1 組人格啟動。<br>2.8.99 以後，若在啟動 SSP 時指定人格資料夾的絕對路徑（例：`ssp.exe --ghost "C:\Users\user\Desktop\myGhost"`），且該人格不在載入資料夾中，會僅在本次執行期間暫時將其上層資料夾（此例中為 `C:\Users\user\Desktop\`）加入人格載入資料夾後啟動。僅適用於存在 `ghost\master\descript.txt` 的資料夾。<br>暫時加入的資料夾不會儲存至設定，在資料夾設定畫面中會顯示為「(temporary)」，無法編輯或刪除，也不會成為人格安裝位置的候選項目。若從資料夾設定畫面明確加入相同的資料夾，則會作為一般載入資料夾儲存。<br>若 SSP 已在執行中（指定的參數會傳遞給執行中的 SSP），則不會進行此處理。 |
| --help<br>（舊: /?） | 在瀏覽器中開啟啟動選項的說明頁面。 |
| --help 檔案名稱<br>（舊: /? 檔案名稱） | 在瀏覽器中開啟指定檔案名稱的說明頁面。 |
| --ukagaka-link x-ukagaka-link:URL<br>（舊: /m x-ukagaka-link:URL） | 執行與開啟 x-ukagaka-link:URL 時相同的動作。若在啟動 SSP 時指定，會等到第 1 組人格啟動後再執行。 |
| --install NAR檔案名稱<br>（舊: /i NAR檔案名稱） | 安裝 NAR。若已有執行中的 SSP，會將安裝處理交給該 SSP；否則會自行安裝後繼續啟動。<br>以空格分隔指定多個 NAR 時，會依序安裝。<br>即使接手處理的 SSP 正顯示未安裝人格的警告對話方塊（「何とかして下さい」對話方塊），也能處理。<br>此外，在該情況下若也指定 --option callghost，會自動按下警告對話方塊中的繼續啟動按鈕，繼續啟動。 |
| --ssf SSF檔案名稱<br>（舊: /s SSF檔案名稱） | 執行 [SSF 檔案](https://emily.shillest.net/specwiki/?SSP/%E4%BB%95%E6%A7%98%E6%9B%B8/SSF%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)。若在啟動 SSP 時指定，會等到第 1 組人格啟動後再執行。 |
| --windowmode 模式 \[可省略\] | 2.8.78～ 以實驗性功能「[視窗模式](windowmode.md)」啟動。將視窗內視為一個虛擬螢幕來啟動人格，讓畫面擷取等操作更容易，或避免影響整個桌面。<br>2.8.86～ 可以指定模式。可指定的模式如下。省略時會依照上次的設定（初始值為 shared）。<br>shared：將所有執行中的人格集中在一個視窗中。<br>perghost：每個人格各使用一個視窗。<br>2.8.86 以後，視窗模式的狀態會儲存為設定，因此即使不加此選項，也會以上次的狀態啟動。若要關閉，請從右鍵選單的「設定」或偏好設定的「配信」切換。 |
| --sstp-listen 監聽位置 | 暫時指定 SSTP 伺服器的監聽位置並啟動。 \[2.8.97 以後\]<br>不會載入已儲存的 SSTP 伺服器監聽設定，只會在指定的監聽位置監聽。<br>本次執行期間的監聽設定不會儲存。偏好設定中的 SSTP 伺服器清單僅供檢視，無法新增、刪除或切換啟用/停用。<br>此功能預計與 --option readonly 搭配使用，以啟動不會干擾其他執行中 SSP 的測試用 SSP。<br><br>可以用逗號分隔，指定多個監聽位置。格式如下。<br>連接埠號碼：在 IPv4 和 IPv6 的迴圈位址（127.0.0.1 和 ::1）上監聽。例：9801<br>localhost:連接埠號碼：與僅指定連接埠號碼相同。<br>IPv4 位址:連接埠號碼：僅在指定的位址上監聽。指定 0.0.0.0 時，會在所有 IPv4 介面上監聽。例：192.168.0.5:9801<br>\[IPv6 位址\]:連接埠號碼：IPv6 位址須以 \[\] 括住。指定 \[::\] 時，會在所有 IPv6 介面上監聽。例：\[::1\]:9801<br>none：不監聽任何位置。省略監聽位置時也相同。<br><br>位址須以數值指定（除 localhost 外，不能使用主機名稱）。<br>格式不正確或監聽失敗的監聽位置會被忽略，並記錄於錯誤記錄中。此時也不會恢復已儲存的設定。<br>請注意，指定迴圈位址以外的位址時，將會接受來自其他 PC 的 SSTP。<br><br>例：`ssp.exe --option readonly --sstp-listen 9900,[::1]:9901` |
| --guifont 字型名稱 \[2.8.75 以後\] | 指定 GUI 使用的字型。並非所有字型都會完全替換，目前部分選單和標題列等仍不會改變。 |

### 離線表面轉存

| 參數 | 功能 |
|---|---|
| --offline-dump 資料夾路徑 | 以離線轉存模式啟動。不實際啟動人格，而是讀取指定人格資料夾中的 surfaces.txt，轉存表面圖片後立即結束。不會載入 SHIORI/MAKOTO/PIRO，也不會建立視窗或訊息迴圈。<br>參數請指定人格的資料夾路徑（結尾的 \\ 可省略）。<br>2.8.98 以後，離線轉存相關選項（此選項、--dump-output-dir、--dump-error-log）若指定相對路徑，會以啟動 SSP 時的目前目錄為基準解析。<br><br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0,1" --dump-output-dir "C:\dump"` |
| --dump-shell 資料夾名稱或名稱 \[可省略\] | 與 --offline-dump 搭配使用。以資料夾名稱（即 shell 以下的相對路徑）或名稱指定要轉存的外殼。省略時使用 descript.txt 中指定的預設外殼（通常為 master）。<br>2.8.98 以後，若找不到指定的外殼，不會改用預設外殼轉存，而是在錯誤記錄中記錄 Error，不輸出任何內容。 |
| --dump-scope (範圍 ID) \[可省略\] | 與 --offline-dump 搭配使用。指定轉存圖片的範圍 ID。省略時為 0。 |
| --dump-surface-list 清單 \[可省略\] | 與 --offline-dump 搭配使用。以逗號分隔指定要轉存的表面。surface 編號的前綴（surface）可省略。也可以使用 [surfaces.txt 的表面 ID 指定擴充格式](https://ssp.shillest.net/ukadoc/manual/descript_shell_surfaces.html#caption_surfacebraceID)。<br>範例：`--dump-surface-list "0,1,10"`<br>省略此選項時不會轉存表面（可搭配 --dump-error-log 僅輸出解析錯誤）。<br>2.8.98 以後，不僅第一個項目，每個項目的前綴都可以省略（例如 `"0,surface1"`）。此外，以單一編號而非範圍指定的表面不存在時，會在錯誤記錄中記錄 Warning（不記錄指定範圍內缺少的編號）。 |
| --dump-output-dir 目錄 \[可省略\] | 與 --offline-dump 搭配使用。指定轉存圖片的輸出目錄。省略時使用目前目錄（2.8.97 以前省略時不會進行轉存）。 |
| --dump-output-prefix 前綴 \[可省略\] | 與 --offline-dump 搭配使用。指定輸出檔名中加在表面編號之前的部分。預設的「surface」會替換成此字串（不是附加在後面）。省略時為「surface」。<br>範例：使用 `--dump-output-prefix "x_"` 時，表面 0 的檔名為 `x_0.png`（不是 `x_surface0.png`）。 |
| --dump-error-log 檔案路徑 \[可省略\] | 與 --offline-dump 搭配使用。將載入外殼時的錯誤記錄（例如 surfaces.txt 的解析錯誤）寫入指定路徑。<br>省略 --dump-surface-list 並只指定此選項，即可不進行轉存，僅執行錯誤檢查。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-error-log "C:\dump\error.csv"`<br><br>輸出格式：帶有 BOM 的 UTF-8 CSV（換行為 CRLF）。每行為一筆記錄，各欄位以 " 包住，欄位中的 " 會跳脫為 ""。<br>`"時刻","ゴースト名","レベル","内容"`<br>時間：HH:MM:SS 格式。<br>等級：Info / Notice / Warning / Error / Critical / System 其中之一。<br>內容：記錄的本文。2.8.94 以後，SERIKO 相關記錄會像 `[SERIKO] shell\master\surfaces.txt:Line=12:Surface=10 ...` 一樣附上定義來源檔案（相對於人格資料夾的路徑）與行號。重複定義的記錄也會以 `(ファイル名:Line=n)` 的形式附上先前定義的位置。<br>2.8.94 以後，指定此選項時最多保留 10000 筆記錄，也不會將內容相似的記錄彙整為摘要行（等級為 System），因此不會遺漏記錄。<br>若沒有任何記錄，則不會建立檔案（即使相同路徑已有檔案，也不會覆寫或刪除）。<br><br>結束代碼：2.8.94 以後，程序會依記錄中最嚴重的等級，以對應的結束代碼結束。<br>0：沒有記錄，或僅有 Info/Notice<br>1：有 Warning（沒有 Error/Critical）<br>2：有 Error（沒有 Critical）<br>3：有 Critical<br>如果人格本身載入失敗（例如無法讀取指定資料夾中的 descript.txt），不會輸出記錄，結束代碼也會是 0。 |
| --dump-surface-option 選項 \[可省略\] \[2.8.57 以後\] | 指定離線轉存功能的選項。可指定的選項如下。<br>backlog：裁切與歷史記錄功能相同的區域（臉部周圍）。但不會縮放，而是直接輸出合成圖片。<br>collision：繪製碰撞判定（collision）的形狀與名稱後輸出。與開發用面板的碰撞判定顯示相同，但名稱會一直顯示，且不會繪製表面外框、有效範圍、重疊判定範圍等外接矩形。\[2.8.98 以後\]<br>2.8.98 以後，可用逗號分隔指定多個選項（範例：`--dump-surface-option backlog,collision`）。<br>若此選項未指定 collision，無論使用者設定（開發用面板的碰撞判定顯示）為何，都不會繪製碰撞判定。 |
| --dump-bind 換裝指定 \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。指定轉存時的換裝狀態。<br>可用分號分隔指定多組「類別名稱,部件名稱,ON/OFF」。其意義與 [`\![bind]`](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html#_!_bind,カテゴリ名,パーツ名,数値_) 相同，在互斥的類別中將部件設為 ON 時，同類別的其他部件會變為 OFF。<br>部件名稱留空或設為 `__ALL__` 時，會以該類別中的所有部件為對象。<br>ON/OFF 使用 1 或 true 表示 ON，0 或 false 表示 OFF。省略時視為 ON（`\![bind]` 省略時會反轉，但此處不會反轉）。<br>範例：`--dump-bind "頭,帽子;服,制服;アクセサリ,__ALL__,0"`<br><br>基準狀態為外殼的 descript.txt 中指定的各部件預設值（`sakura.bindgroup*.default`），不會使用使用者最後的換裝狀態（`shell\profile` 內儲存的值）。只有指定的部件會在此基準上變更。<br>換裝會套用至 --dump-scope 指定的範圍。<br>若指定不存在的類別或部件，會記錄 Warning（--dump-error-log 的結束代碼為 1），只忽略該項指定並繼續轉存。<br>類別名稱及部件名稱前後的空白不會被移除，請勿在逗號後面加入空白。 |
| --dump-animation 動畫 ID \[可省略\] \[2.9.05 以後\] | 與 --offline-dump 搭配使用。以與 `\i[ID]` 相同的方式播放指定動畫，並依序輸出各影格的圖片。只能指定一個 ID（除了數值，也可以像 `\i[ID]` 一樣使用 surfaces.txt 中為動畫設定的名稱）。<br>對每個表面，首先將與一般轉存相同的圖片（runonce 動畫播放一輪後的狀態）輸出為 `surface0.png`，接著每當指定動畫的圖樣推進時，便以從 0 開始的 4 位數序號輸出為 `surface0_0000.png`、`surface0_0001.png`……。--dump-output-prefix 與 --dump-surface-option 的設定也會套用至連號圖片。<br>範例：`ssp.exe --offline-dump "C:\SSP\ghost\myGhost" --dump-surface-list "0" --dump-animation 10 --dump-output-dir "C:\dump"`<br><br>runonce、always 等動畫會與一般轉存時一樣運作，指定動畫則疊加在其上。只有指定動畫本身的圖樣會列入連號輸出，即使 always 動畫推進，圖片數量也不會增加。<br>指定動畫推進至最後一個圖樣時（always 則為播放一輪時）結束。若因其他動畫的 stop 或互斥而停止，也會在該處結束。<br>由 start、alternativestart、parallelstart 啟動的其他動畫不會列入連號輸出。若指定動畫包含這些圖樣，會記錄 Warning（繼續輸出）。<br>由於 start、stop 類型的圖樣不會改變圖片，因此不計為連號的一個影格。<br>若指定的 ID 不存在於該表面，或因換裝而停用、處於互斥狀態等原因無法播放，會記錄 Warning，該表面只輸出一般的單張圖片。<br>連號最多為 10000 張（到 `_9999` 為止），達到上限時會記錄 Warning 並中止。 |

### 離線工具

| 參數 | 功能 |
|---|---|
| --offline-tool 類型 \[2.9.01以後\] | 以離線工具模式啟動。不啟動人格，直接從 --target-dir 指定的資料夾建立 NAR、更新定義檔案或壓縮檔，完成後立即結束。不會觸發任何人格事件，也不會建立視窗或訊息迴圈。<br>處理內容與 Sakura Script 的 `\![execute,createnar]` / `\![execute,createupdatedata]` / `\![execute,compressarchive]` 相同，但輸出位置沒有限制（例如限於 SSP 管理下的資料夾等），可自由指定。<br>類型請指定以下其中一項（不區分大小寫）。<br><br>nar：建立 NAR 檔案。與一般建立 NAR 時相同，會套用 `developer_options.txt` 的 nonar 設定及 .narignore 等排除規則。若資料夾根目錄中沒有 install.txt，會根據 descript.txt（或 `ghost\master\descript.txt`）判定類型和名稱，在目標資料夾中建立 install.txt 後將其收錄。若無法判定類型和名稱，則會失敗。<br>updatedata：建立更新定義檔案。若 --output 的檔名以 .dau 結尾，則使用與 updates2.dau 相同的格式，否則使用 updates.txt 的格式，僅建立指定的一個檔案。不會在目標資料夾根目錄或 `ghost\master` 中建立或刪除 updates2.dau / updates.txt。與一般情況相同，會套用 `developer_options.txt` 的 noupdate 設定及 .updateignore 等排除規則。<br>archive：直接壓縮目標資料夾。不會讀取 .narignore 等排除規則（不收錄隱藏檔案和隱藏資料夾）。格式由 --output 的副檔名決定，.7z 使用 7z 格式，其他則使用 zip 格式。<br><br>無論使用哪種類型，若輸出位置的檔案已存在，會將其覆寫。若輸出位置位於目標資料夾內，則不會收錄輸出檔案本身。輸出資料夾必須事先存在。<br>若 --target-dir 或 --output 指定的是相對路徑，則以啟動 SSP 時的目前工作目錄為基準解析。<br><br>結束代碼：<br>0：成功<br>1：引數無效（類型不明、未指定 --target-dir 或 --output、--target-dir 不存在或不是資料夾）<br>2：建立失敗（無法寫入輸出位置、無法判定 NAR 的類型和名稱、updatedata 遇到無法讀取的檔案或過深的目錄層級（超過 32 層）等）。失敗時也可能留下建立到一半的檔案<br><br>範例：`ssp.exe --offline-tool nar --target-dir "C:\src\myGhost" --output "C:\out\myGhost.nar"`<br>範例：`ssp.exe --offline-tool updatedata --target-dir "C:\src\myGhost" --output "C:\out\updates2.dau"`<br>範例：`ssp.exe --offline-tool archive --target-dir "C:\src\data" --output "C:\out\data.7z" --password "pass"` |
| --target-dir 資料夾路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定處理對象的資料夾（結尾的\\可省略）。建立 NAR 或更新定義檔案時，請指定人格等項目的根資料夾（包含 descript.txt、install.txt 或 ghost 資料夾的資料夾）。 |
| --output 檔案路徑 \[2.9.01以後\] | 與 --offline-tool 搭配使用（必填）。指定要建立的檔案路徑。 |
| --password 密碼 \[可省略\] \[2.9.01以後\] | 與 --offline-tool 的 nar 或 archive 搭配使用。以指定的密碼建立 AES 加密的 ZIP 檔案（7z 格式則使用 7z 加密）。updatedata 會忽略此參數。<br>密碼會以明文保留在命令列中，請注意處理方式。 |

### 其他

| 參數 | 功能 |
|---|---|
| `initial_install.nar` | 雖然這不是啟動選項，但若在與 ssp.exe 相同的資料夾中放置名為<strong>`initial_install.nar`</strong>的 NAR 檔案，SSP 啟動時便會以靜默方式（不顯示確認對話方塊）覆寫安裝。安裝完成後，`initial_install.nar` 會自動刪除。可用於將人格等項目與 SSP 一同打包發布的情況。 \[2.7.52～\] |
