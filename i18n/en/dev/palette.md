# Developer Help: Development Palette

This dialog brings together switches for settings useful during development and buttons for launching tools.<br>
It is useful for developing balloons and shells, as well as ghosts.

Settings made with the Development Palette are managed separately for each ghost.

## Checkboxes

### Show collision regions

When checked, regions are displayed with their collision names.<br>
When half-checked, the collision names are hidden. Use this, for example, when the region outlines overlap the names and make them hard to see.<br>
You can also get a general idea of the collision stacking order by looking at how the outlines overlap (regions lower in the order cannot be touched).

The example image shows only rectangular collision regions, but polygonal, circular, and other collision shapes are also supported.

### Balloon test mode

When ON, test displays appear on the `\1` and `\0` balloons.<br>
The numbers shown let you check how many characters fit horizontally and vertically. The following items are also displayed, so you can use them to adjust positions and more.

- Counter showing update progress
- Looping animation played during an update (using `online*.png`)
- Scroll arrows (arrow0/1.png)
- SSTP marker
- SSTP message

### Adjust SERIKO wait

When ON, an input box opens, letting you change the shell animation wait time in percent.<br>
At 100%, frames advance using the wait time specified in the settings.<br>
When OFF, the setting is disabled.<br>
You can use this to check for invalid frames in fast animations with many frames.

### Check for updates only

When ON, a network update triggers the update event, but files are not actually overwritten.<br>
This can help prevent development files from being overwritten by an accidental update, and can also be used to test the behavior of update events.

### Change SHIORI Sender

When ON, an input box opens, letting you change the sender name SSP uses when identifying itself to SHIORI.<br>
When OFF, the setting is disabled.

### Enable SHIORI call log

```
=====send=====
GET SHIORI/3.0
Charset: Shift_JIS
Sender: SSP
SecurityLevel: local
ID: OnSecondChange
Reference0: 193
Reference1: 0
Reference2: 0
Reference3: 1
Reference4: 0


=====response=====
SHIORI/3.0 204 No Content
Charset: Shift_JIS
```

When ON, communication logs between SSP and SHIORI are recorded and saved as `ssp_SHIORI_log.txt` in the ghost's master folder.<br>
Be careful not to include the log in files for updates.<br>
Also, be aware that if you leave logging on all the time, the file may become quite large before you notice.

### Enable SHIORI internal logging

Information about whether this is ON or OFF is sent in the SHIORI Event "`enable_log`".<br>
SHIORI can use this information to control whether its own logging function is ON or OFF.

### Enable SHIORI debugging

When ON, external debugging events such as SHIORIEcho are enabled.<br>
When OFF, these events are ignored because they pose a security risk (SHIORI normally ignores them as well).<br>
Some SHIORI debugging tools will not work unless this is ON (for example, Kawari's La France and Kousui).

### Disable automatic ghost switching

When ON, SSP's [automatic switching feature](../config/ghost.md) is disabled for this ghost.<br>
During development, you may often leave a ghost running, so this prevents it from switching ghosts unexpectedly.

### Disable automatic checks

When ON, automatic RSS/headline checks and email checks will not run while this ghost is running, regardless of the settings.

### Disable automatic updates

When ON, the [automatic update feature](../config/ghost.md) is disabled for this ghost.<br>
This helps prevent development ghost data from being overwritten by an update.

### Do not exit with the `\-` tag

When ON, `\-` (the command to exit a ghost) is ignored if it appears in a script running for this ghost.<br>
This prevents a development ghost from exiting unexpectedly and lets you test talks that contain `\-`.

## Buttons

### Enter script

The SEND box opens, and you can enter Sakura Script to run it directly.<br>
Note that you cannot enter scripts in the dictionary format used by each SHIORI.

### Surface test

Opens a dialog for running various tests of shell behavior.

There are four lists in the center of the dialog.<br>
The leftmost list, labeled **WND**, lets you select the scope to operate on (`\0`, `\1`, `\p[2]`...).<br>
The second list from the left, labeled **Surface**, shows the recognized surfaces. Select a surface here to change the display for the scope selected in the WND list. The numbers next to Surface above the list show the number of surface definitions in surfaces.txt / the total number, including surfaces that have only images and no definitions.<br>
The second list from the right, labeled **ID**, shows the IDs of animations defined for the selected scope. Select an ID to run its animation if it is defined for the currently displayed surface. The number next to ID above the list is the total number of IDs.<br>
The rightmost **COL** list shows the IDs and names of collision regions defined for the selected Surface. The number next to COL above the list is the total number of collision regions.

Click the "▼" button at the bottom left to open the function menu.<br>
Currently, the only available option is "Copy Surface List". Select it to copy a newline-separated list of all recognized surfaces, in the form "`surface**`", to the clipboard.

Next to it, the number of loaded image files and their total size are shown.

There are also three checkboxes next to these.<br>
When **Sort** is ON, the Surface list is sorted by ID in ascending order instead of by the order in which the surfaces are defined.<br>
When **Copy** is ON, selecting a surface copies to the clipboard the script that switches to that surface (for example, `\0\s[1]` to set `\0` to surface1).<br>
When **Script** is ON,

### Show error log

Shows a list of the history of reported errors.<br>
For details, see the [Script log](scriptlog.md#エラーログ) page.

### Temporarily change the current time

Set a time to temporarily replace the current date and time recognized by SSP with the date and time you specify.<br>
This lets you test ghost behavior that varies by date and time without changing the OS clock.

**Present Time** is the virtual date and time currently set in SSP.<br>
**System Time** is the actual date and time inside the OS.<br>
Click the **Apply** button to set the date and time in the input box as the virtual time.<br>
Click the **Reset** button to restore the virtual time to System Time.

### SERIKO Inspector

Displays the shell definitions in a tree view.<br>
For each surfaceID, the element, collision, and animation nodes (branches) are separated, then the nodes for each of their IDs are separated, followed by their components, and so on. This makes the structure of the shell definitions easy to understand at a glance.

Click the **Dump** button at the bottom right to open a file save dialog and output a text file that represents the structure using tabs for indentation.

### Reload

Reloads the items selected from the menu.<br>
Use this when you edit, add, or delete files during development.

### Open/Run

Opens or runs the item selected from the menu.

- **BALLOON**<br>
  **GHOST**<br>
  **SHELL**<br>
  Opens the folders for the currently used balloon, ghost, and shell, respectively.<br>
  You will often need to open these folders during development, so use this when you do.
- **SHIORI LOG**<br>
  Opens the log file created by [Enable SHIORI call log](#shiori呼出ログ有効), above.<br>
  This cannot be selected if the log file has not been created.
- **VCS Uppdate**<br>
  **VCS Commit**<br>
  **VCS Log**<br>
  **VCS Revert**<br>
  **VCS Export**<br>
  Use the version control tool configured under [External applications](../config/extprog.md) in Preferences.
- **UPDATE EVENT/NORMAL**<br>
  **UPDATE EVENT/NONE**<br>
  **UPDATE EVENT/ERROR**<br>
  **UPDATE EVENT/NORMAL GBALLOON**<br>
  You can test the behavior of update events using simulated update results, even when there are no actual updates.<br>
  **NORMAL** simulates the behavior when update files are found and the update completes successfully.<br>
  **NONE** simulates the behavior when no update files are found.<br>
  **ERROR** simulates the behavior when an update is interrupted by an error (MD5 mismatch).<br>
  **NORMAL GBALLOON** simulates the shell and balloon update checks that may also occur during an update, depending on your [Preferences](../config/ghost.md).
