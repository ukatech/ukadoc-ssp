# Settings: Development/Other

This page explains the “Development/Other” page in the dialog opened by selecting “Preferences” from the “Settings” submenu of the right-click menu.

This page lets you configure development and other detailed settings.

!!! tip "ヒント"

    This setting is only displayed if you turn ON “Enable developer features” in the “[General](ippan.md)” settings.

These settings are needed for development and other special cases, but for all other purposes, the default settings are fine.<br>
<strong>Do not change these settings unless you have a specific reason to do so.</strong>

## Explanation of each item

- **Change FMO name**<br>
  Changes the name of the FMO that lists the currently running ghosts.<br>
  Usually, the default name, Sakura, is fine.
- **Create update files or NARs when a folder is dropped**<br>
  Determines what happens when you drag and drop a folder onto a ghost.<br>
  During development, turning this ON lets you choose whether to notify the ghost or run a development command.
- **Keep old files during network updates**<br>
  Saves files created temporarily during a network update instead of deleting them.<br>
  You can use this to investigate problems that occurred during a network update.
- **Do not update files with the read-only attribute**<br>
  If a file targeted for a network update has the read-only attribute, it is left unchanged.
- **Hide when a surface does not exist**<br>
  If a surface specified in a script does not exist, the ghost window is hidden (normally, the default surface is displayed).<br>
  This can be used to check for problems in a ghost's scripts.
- **Make it appear that Materia is running**<br>
  Creates the mutex "sakura" and behaves as if Materia is running.<br>
  Software designed to work only with Materia may then work.
- **Prevent Vanish (uninstallation)**<br>
  Prevents Vanish (uninstallation) from being run under any circumstances.<br>
  You can use this to prevent accidental Vanish operations during ghost development, for example.　
- **Unlock multiple-instance lock**<br>
  Normally, only one instance of SSP can run on a machine. Unlock this setting if you want to run multiple instances, for example, to separate development from other use.<br>
  However, SSP itself is not designed to run multiple instances, so some problems may occur.<br>
  Also, if NAR files are associated with SSP, you will not be able to open and install NAR files (drag and drop is still available).
- **Use version control tools for updates when available**<br>
  If a version control tool is used to manage a ghost, launches it and performs an “Update” operation instead of a regular network update.
- **Notify when an error at or above level \[XXX\] occurs**<br>
  When an error at or above the selected level occurs, a balloon notification appears from the task tray icon.<br>
  Ghost authors are recommended to enable notifications for NOTICE during development, or at least for WARNING and above.<br>
  For the meaning of notification levels, see the “[Script log](../dev/scriptlog.md#エラーログ)” page.
- **Use the exception handler**<br>
  If you are helping with debugging or developing a ghost, turn this OFF to allow SSP to “crash properly” in cases such as memory access violations.<br>
  If SSP crashes very frequently, turning this ON may help somewhat, but it is not recommended during development.
- **Include test versions in automatic updates**<br>
  Expands the scope of update checks to include test versions. You can automatically get test versions of upcoming major releases, for example.

### Update definition files

Choose whether to output updates2.dau, updates.txt, or both.

- **Always use UTF-8 encoding**<br>
  Always outputs filenames in UTF-8 when they contain multibyte characters.<br>
  This resolves garbled text at the source, and recent versions of SSP automatically detect the character encoding, so there should be no problems. However, compatibility issues may occur in older environments.
- **Cache file hash calculations**<br>
  Reuses, where possible, hash calculation results from older update definition files.<br>
  This may make generating update definitions somewhat faster when there are many files, but reduces reliability.

### NAR creation location

Set the path where the NAR creation feature outputs NAR files.

- **Specify each time**<br>
  Specify the destination and filename each time.
- **Same as folder**<br>
  Creates the NAR in the same location as the folder of the ghost being packaged.
- **Specified folder**<br>
  Always creates the NAR in the specified folder.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the currently selected page in the Preferences dialog (that is, this page).<br>
  The “?” mark at the top right of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” mark at the top right of the dialog does the same thing.
