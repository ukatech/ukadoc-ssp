# Functions

This page explains the various SSP functions available from the Functions submenu of the [right-click menu](../howto/rclick.md).

Item names may differ depending on the ghost (their positions remain the same).<br>
If you find this confusing, you can turn off ghost-defined menu labels under "[Ghost (1)](../config/ghost.md)" in Preferences.

!!! tip "ヒント"

    This submenu contains some items that appear only when [development mode is on](../config/ippan.md), such as Force exit restricted mode, Script log, and Development palette. These are omitted from this page.<br>
    For information about the menu and its functions in development mode, see the [Developer help](../dev/index.md) page.

## When items are grayed out

Some items may be unavailable depending on the ghost's state, as described below. This is not a malfunction.

- **When you open the menu of a ghost temporarily launched via SSTP or similar**<br>
  "Calendar", "SSP messenger", and "NTP time sync" are unavailable.<br>
  To put the ghost in a normal running state, use "Keep temporarily launched ghost".
- **While the ghost is minimized or is not accepting input (restricted mode)**<br>
  In addition to the above, "Address bar", "Check for SSP updates", and "Reload ghost" are unavailable.
- **Other cases**<br>
  "SSP messenger" is unavailable while "Use IP Messenger compatibility mode" is off under "[IM](../config/im.md)" in Preferences.<br>
  "Keep temporarily launched ghost" is available only for temporarily launched ghosts.

## Item descriptions

### Calendar

Launches the schedule management tool included with SSP.<br>
If it is already open, selecting this item again closes Calendar (the item is checked while it is open).<br>
Shortcut key: Ctrl - D<br>
⇒ For details, see the [Calendar](calendar/index.md) page.

### SSP messenger

Launches the messenger feature included with SSP.<br>
Shortcut key: Ctrl - M<br>
⇒ For details, see the [SSP messenger](sspim/index.md) page.

### NTP time sync

Contacts an external server to check the computer's clock and corrects it if necessary.<br>
Recent operating systems generally synchronize the clock automatically. Use this if you need to synchronize it manually or are using an older OS.

When selected, the ghost starts by saying it is contacting the server, then reports how far off the clock was when the result is available.<br>
If the connection fails, the ghost reports the failure.<br>
Whether the clock is actually changed depends on the ghost's response (some ghosts ask for confirmation, while others only report the result).

- Changing the clock requires OS administrator privileges. If you do not have permission, a confirmation dialog (UAC) may appear. "SSP Helper" in this dialog is a helper program included with SSP. For details, see [About SSPH (SSP Helper)](../about/ssph.md#uacの確認画面が出るとき).
- You can configure the server under "[Connection (1)](../config/conn1.md)" in Preferences. You can also set the clock to synchronize automatically at regular intervals in the same place. When synchronization is automatic, the clock is corrected without a conversation with the ghost.
- Depending on settings such as the allowed network connection times, a dialog may appear before execution asking whether to connect.
- This feature may be unavailable or have no effect in some environments.

### Explorer

Launches Explorer, which manages ghosts, balloons, shells, headlines, plugins, and more.<br>
Shortcut key: Ctrl - E<br>
⇒ For details, see the [Explorer](explorer/index.md) page.

### Picture viewer

Launches a viewer for displaying and making simple edits to image files.<br>
⇒ For details, see the [Picture viewer](pictureviewer.md) page.

### Archive viewer

Launches a viewer for displaying and making simple edits to archive files.<br>
When selected, it starts without opening an archive. If the viewer is already open, its window is brought to the front instead of opening a new one.<br>
⇒ For details, see the [Archive viewer](archiveviewer.md) page.

### Backlog

Displays the backlog (speech history), so you can review past conversations if you missed something.<br>
Shortcut key: Ctrl - B

- Each ghost has its own history. Statements are listed from oldest at the top to newest at the bottom. When opened, the view is positioned at the latest statement.
- Each statement appears in a speech bubble with an image of the character's face to show who spoke. You can scroll back through long histories using the mouse wheel or scrollbar.
- Normally, the backlog appears in a separate window. When reopened, it retains its previous position and size. The date and time of the latest statement (Update : year-month-day hour:minute:second) appear at the bottom of the window.
- If "Also integrate backlog/speech history" is on in [Window mode](windowmode.md), the backlog appears inside the same window as the ghost. For details, see [Integrating the backlog](windowmode.md#バックログの統合).

### Check for SSP updates

Immediately checks whether an SSP update is available.

- If a new version is available, a dialog displays the version and asks whether to update. Select “Yes” to proceed with the update.
- If SSP is already up to date or the check fails, a dialog notifies you.

For more information about updating SSP, see [Updating SSP](../howto/verup.md).

### Speech recognition

This is a command-based speech recognition feature that responds to specific words. Select it to open the speech recognition palette.<br>
⇒ For details, see [Speech recognition](speech-recognition.md).<br>
You can configure it under [Speech recognition/Synthesis](../config/dictation.md) in Preferences.

### Voice synthesis

Speaks the text displayed in the balloon using voice synthesis.<br>
Select this item to toggle it on or off. A check mark appears next to the item while it is on. The on/off state is retained the next time SSP starts.<br>
⇒ For details, see [Voice synthesis](speech-synthesis.md).<br>
You can configure the voice, speed, volume, and other options under [Speech recognition/Synthesis](../config/dictation.md) in Preferences.

### Address bar

Opens an address input box, downloads the file at the entered URL, and attempts to install it.<br>
This is essentially the same as installing by **dragging and dropping** a link from a browser.<br>
Use this when dragging and dropping a link does not work properly, such as because of browser behavior.<br>
Keyboard shortcut: Ctrl - Shift - U

### Open file

Opens a file selection dialog and has SSP attempt to open the selected file.<br>
This is essentially the same as **dragging and dropping** a file onto a ghost (if it is a ghost installation file, installation begins).<br>
Use this when drag and drop does not work properly, such as in a Wine environment.<br>
Keyboard shortcut: Ctrl - O

### Select folder

Opens a folder selection dialog and has SSP attempt to open the selected folder.<br>
This is essentially the same as **dragging and dropping** a folder onto a ghost.<br>
Use this when drag and drop does not work properly, such as in a Wine environment.<br>
Keyboard shortcut: Ctrl - F

### Release ghost cache

Releases the ghost cache from memory. This also cleans up the memory used by SSP.<br>
The cache is managed automatically, so you normally do not need to use this.<br>
Use it if memory consumption becomes excessive after switching between many ghosts over a long period.<br>
A ghost whose cache was released will take a little longer to start next time because it can no longer benefit from the cache.

!!! tip "ヒント"

    When multiple ghosts are running and you switch or close only some of them, the ghost cache keeps their information in memory for a certain period to save time when restarting them.<br>
    You can configure this under [Ghost (1)](../config/ghost.md#ゴーストキャッシュ制御) in Preferences.

### Clean up/Update FMO

Cleans up and updates the SSP information used to interact with other applications. Invalid information is removed, and the remaining information reflects the current running state.<br>
You generally do not need to use this when using SSP on its own.<br>
When using SSP alongside other applications that communicate via SSTP, this may resolve problems such as SSTP messages not being delivered correctly.

### Reload operational information

Reloads all files for loaded ghosts, balloons, headlines, plugins, and so on.<br>
Use this to reflect changes if you have directly moved or deleted files while SSP is running.<br>
This is equivalent to using File→Reload for every type in [Explorer](explorer/index.md).

### Reload ghost

Reloads the running ghost. This is the same as selecting the currently running ghost again from the Change ghost menu.<br>
Use this to reflect changes after directly editing a ghost's files, for example.

### Keep temporarily started ghost

Fully loads a ghost that was started temporarily by a request via SSTP or similar means and keeps it running.<br>
The ghost enters the same state as when started normally, begins its startup talk, and gains access to the full range of menu functions.<br>
This item can only be selected for a temporarily started ghost.<br>
Keyboard shortcut: Ctrl - K

### Reset shell position

Returns the position of the ghost whose menu is open to its initial startup position. This applies to all characters in that ghost, including the main and secondary characters.<br>
This may help bring a ghost back if it has moved off-screen.<br>
Keyboard shortcut: Ctrl - Shift - F12

### Reset balloon position

Resets the balloon positions for the ghost whose menu is open. Balloons moved by dragging return to their default positions relative to each character.<br>
This may help restore a balloon that has moved off-screen.<br>
Shortcut key: Ctrl - Shift - F10

### Hide balloons

Forcibly closes the balloons for all characters of the ghost whose menu is open.<br>
You can also use the [shortcut key](shortcut.md) "Ctrl-Shift-Del".<br>
However, balloons may not close in some situations, such as while the ghost is speaking, displaying choices, or waiting for input.
