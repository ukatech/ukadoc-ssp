# Features

This page explains the various SSP features that you can use from the “Features” submenu of the [right-click menu](../howto/rclick.md).

The item names may vary depending on the ghost, but their positions stay the same.<br>
If you find the menu difficult to understand, you can turn off the ghost-defined menu items in Preferences under “[Ghost (1)](../config/ghost.md)”.

!!! tip "ヒント"

    Some items in this submenu (such as Force exit from restricted mode, Script log, and Developer palette) are displayed only when [Developer mode is on](../config/ippan.md), but they are omitted from this page.<br>
    For details about the menu and its features in Developer mode, see the “[Help for developers](../dev/index.md)” page.

## When an item is grayed out and cannot be selected

Depending on the ghost’s state, some items may be unavailable, as described below. This does not mean something is broken.

- **When you open the menu for a ghost temporarily launched via SSTP or another method**<br>
  “Calendar,” “SSP messenger,” and “NTP time sync” are unavailable.<br>
  To make the ghost run in the normal state, use “Keep temporarily launched ghost.”
- **While the ghost is minimized, or while it cannot accept input (restricted mode)**<br>
  In addition to the items above, “Address bar,” “Check for baseware updates,” and “Reload ghost” are unavailable.
- **Other cases**<br>
  “SSP messenger” is unavailable while “Use IP Messenger compatibility mode” is turned off under “[IM](../config/im.md)” in Preferences.<br>
  “Keep temporarily launched ghost” is available only for ghosts that were temporarily launched.

## Details about each item

### Calendar

Launches the schedule management tool included with SSP.<br>
Select it again to close the calendar if it is already open. (A check mark appears next to the item while it is open.)<br>
Shortcut key: Ctrl - D<br>
⇒For details, see the “[Calendar](calendar/index.md)” page.

### SSP messenger

Launches the messenger feature included with SSP.<br>
Shortcut key: Ctrl - M<br>
⇒For details, see the “[SSP messenger](sspim/index.md)” page.

### NTP time sync

Connects to an external server to check whether your computer’s clock is out of sync and, if necessary, corrects it to the right time.<br>
Recent operating systems seem to sync the time automatically. Use this feature if you need to sync it manually or are using an older operating system.

When you select it, the ghost starts talking about “contacting the server.” Once the result is available, the ghost reports how far off the clock was.<br>
If the connection fails, the ghost tells you that it failed.<br>
Whether the clock is actually changed depends on the ghost’s response. Some ghosts ask you for confirmation, while others simply report the result.

- You need administrator privileges on the operating system to change the clock. If you do not have the required privileges, a confirmation dialog (UAC) may appear.
- You can configure the server to use under “[Connection (1)](../config/conn1.md)” in Preferences. You can also configure automatic time sync at regular intervals in the same place. When time sync runs automatically, the clock is corrected without any conversation with the ghost.
- Depending on settings such as the time allowed for network connections, a dialog may appear before the feature runs, asking whether it can connect.
- This feature may be disabled or have no effect in some environments.

### Explorer

Launches Explorer, which you can use to manage ghosts, balloons, shells, headlines, plugins, and more.<br>
Shortcut key: Ctrl - E<br>
⇒For details, see the “[Explorer](explorer/index.md)” page.

### Picture viewer

Launches a viewer for displaying and making simple edits to image files.<br>
⇒For details, see the “[Picture viewer](pictureviewer.md)” page.

### Archive viewer

Launches a viewer for displaying and making simple edits to archive files.<br>
When launched, no archive is open yet. If the viewer is already open, it is brought to the foreground instead of opening a new window.<br>
⇒For details, see the “[Archive viewer](archiveviewer.md)” page.

### Backlog

Displays the backlog (history of things the ghost has said). Use it to review past conversations if you missed something the ghost said.<br>
Shortcut key: Ctrl - B

- Each ghost has its own history. Entries are listed from oldest to newest, with the latest at the bottom. When you open the backlog, it shows the latest entry.
- Each entry appears in a speech bubble, with an image of the character’s face to show who was speaking. You can scroll through a long history with the mouse wheel or scrollbar.
- Normally, the backlog appears in a separate window. If you close and reopen it, it appears in the same position and size as before. The bottom of this window shows the date and time of the latest entry (Update: year-month-day hour:minute:second).
- If “Integrate backlog/speech history” is turned on in [Window mode](windowmode.md), the backlog appears in the same window as the ghost. For details, see “[Integrating the backlog](windowmode.md#バックログの統合).”

### Check for SSP updates

Check immediately for SSP updates.

- If a new version is available, a dialog opens showing the version and asking whether you want to update. Select "Yes" to proceed with the update.
- If you already have the latest version or the check fails, a dialog will notify you.

For more information about updating SSP, see the "[Updating SSP](../howto/verup.md)" page.

### Speech recognition

This is command-based speech recognition (it responds to specific, predefined phrases). Select it to open the Speech recognition palette.<br>
⇒For details, see the "[Speech recognition](speech-recognition.md)" page.<br>
You can configure it in Preferences under "[Speech recognition/synthesis](../config/dictation.md)".

### Voice synthesis

The text spoken in the balloon is pronounced as-is using voice synthesis.<br>
Each time you select this item, it switches on or off. A check mark appears next to the item when it is on. The on/off state is retained the next time you start SSP.<br>
⇒For details, see the "[Voice synthesis](speech-synthesis.md)" page.<br>
You can configure the voice, speed, volume, and other settings in Preferences under "[Speech recognition/synthesis](../config/dictation.md)".

### Address bar

Opens an address input box, downloads the file at the URL you enter, and attempts to install it.<br>
This is basically the same as installing a file by **dragging and dropping** a link from a browser.<br>
Use this when, for example, the browser's behavior prevents you from successfully dragging and dropping a link.<br>
Shortcut key: Ctrl - Shift - U

### Open file

Opens a file selection dialog, and SSP attempts to open the selected file.<br>
This is basically the same as **dragging and dropping** a file onto a ghost (if it is a ghost installation file, installation begins).<br>
Use this when, for example, drag-and-drop does not work properly in a Wine environment.<br>
Shortcut key: Ctrl - O

### Select folder

Opens a folder selection dialog, and SSP attempts to open the selected folder.<br>
This is basically the same as **dragging and dropping** a folder onto a ghost.<br>
Use this when, for example, drag-and-drop does not work properly in a Wine environment.<br>
Shortcut key: Ctrl - F

### Release ghost cache

Releases the ghost cache held in memory (so it is no longer kept in memory). This also frees up memory used by SSP.<br>
The cache is managed automatically, so you usually do not need to use this feature.<br>
Use it if memory usage has become high, such as after switching between many ghosts over a long period.<br>
For ghosts whose cache has been released, the cache will no longer speed up startup, so they will take a little longer to start next time.

!!! tip "ヒント"

    When multiple ghosts are running, the ghost cache keeps information about ghosts that you switch away from or close in memory for a limited time. This helps reduce the time needed to restart them.<br>
    You can configure this in Preferences under "[Ghost (1)](../config/ghost.md#ゴーストキャッシュ制御)".

### Organize/update FMO

Organizes and updates SSP information used to communicate with other applications. Any invalid information is removed, and the contents are updated to reflect the current running state.<br>
You generally do not need to use this when running SSP on its own.<br>
This may resolve problems such as SSTP messages not being delivered correctly when you use SSP alongside other applications that use SSTP communication.

### Reload runtime information

Reloads all files for the currently loaded ghosts, balloons, headlines, plugins, and other items.<br>
Use this to apply changes if you directly move or delete files while SSP is running.<br>
This is the same as using File → Reload for every type in [Explorer](explorer/index.md).

### Reload ghost

Reloads the running ghost. This is the same as selecting the currently running ghost again from the Change ghost menu.<br>
Use this to apply changes if you directly edit the ghost's files.

### Keep temporarily launched ghost

Fully loads a ghost that was temporarily launched at a command from SSTP or another source, and keeps it running.<br>
When you do this, the ghost enters the same state as when launched normally, begins its startup talk, and makes all menu features available.<br>
You can select this item only for a temporarily launched ghost.<br>
Shortcut key: Ctrl - K

### Reset shell position

Returns the display position of the ghost whose menu is open to its position at first startup. This applies to all characters in that ghost, including the main and sub characters.<br>
If a ghost has moved off-screen, this may help bring it back.<br>
Shortcut key: Ctrl - Shift - F12

### Reset balloon position

Resets the display position of the balloon belonging to the ghost whose menu is open. Any balloon you have moved by dragging returns to its default position for each character.<br>
This may help restore a balloon that has moved off-screen, for example.<br>
Shortcut key: Ctrl - Shift - F10

### Close balloons

Forcibly closes the balloons of all characters belonging to the ghost whose menu is open.<br>
You can also do this with the “Ctrl-Shift-Del” [shortcut key](shortcut.md).<br>
However, the balloons may not close while the ghost is talking, displaying choices, waiting for input, or in similar situations.
