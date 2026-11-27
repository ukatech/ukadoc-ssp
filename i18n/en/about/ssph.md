# About SSPH (SSP Helper)

If you have noticed an unfamiliar `SSPH.exe` in your SSP folder or on a Windows screen, this page explains what it is.<br>
`data\SSPH.exe` in the folder where SSP is installed is SSPH, a helper program that assists SSP. It is part of SSP and comes with the main SSP program (`ssp.exe`). Its name is short for **SSP Helper**.

SSPH starts only when requested by the main SSP program or another component, and exits as soon as its task is complete. It does not normally run in the background.<br>
If you see “SSP Helper” or “SSPH.exe” in a Windows User Account Control (UAC) prompt and are unsure what it means, see [When a UAC prompt appears](#uacの確認画面が出るとき).

## What is SSPH?

- **File location**<br>
  It is located at `(SSPのフォルダ)\data\SSPH.exe`.
- **File properties**<br>
  On the “Details” tab, the file description is “SSP Helper”, the product name is “SSPH”, and the company name is “SSP BUGTRAQ”.
- **How it starts**<br>
  The main SSP program, the installer, or an uninstall operation from Windows “Installed apps” starts SSPH with the task to perform specified. You do not need to start it yourself. If started without arguments, it exits without doing anything.
- **What it displays**<br>
  Depending on the task, it displays an installation screen, a progress window, or a confirmation message. Otherwise, it displays nothing.
- **Network communication**<br>
  SSPH communicates over the network only when you choose to download a language pack in the installer. It downloads the pack from its distribution site (GitHub).

## What SSPH does

| Situation | SSPH's task | UAC prompt caused by SSPH |
|---|---|---|
| NTP time sync | Sets the computer's clock to the server's time | May appear |
| Installing SSP | Displays the installation screen and copies SSP files to the installation location | Does not appear |
| Updating the main SSP program | Waits for SSP to exit, overwrites files with the downloaded update, and restarts SSP | Does not appear |
| Finding a ghost's update location | Looks up the ghost's update location (`homeurl`) | Does not appear |
| Uninstalling SSP | Deletes the SSP folder and its registration information | Does not appear |

SSPH.exe itself is configured not to request administrator privileges (`asInvoker`). “May appear” in the table means that, only for NTP time sync, the main SSP program asks Windows to start SSPH with administrator privileges.

## When a UAC prompt appears

Changing the computer's clock requires Windows administrator privileges. SSPH appears in a UAC prompt asking whether to allow changes to your device only during NTP time sync.

### When it appears

- When a ghost corrects the clock through “Features→NTP time sync” in the right-click menu. Simply selecting the menu item does not trigger the prompt. It appears after the server query finishes, when the ghost actually corrects the clock.
- When a ghost starts NTP time sync on its own. A ghost can query a time server using the Sakura Script command `\![executesntp]`. If it connects, the `OnSNTPCompare` event is sent, and the ghost can correct the clock by including `\6` in its script. This is why the prompt may appear while a ghost is talking, even if you have not selected the menu item.
- When “Automatically sync the clock” is enabled in Preferences. The clock is corrected at the specified intervals, and a prompt may appear each time. You cannot select this setting when SSP is started normally under an administrator account with UAC enabled (see “When it does not appear” below).

### Understanding the prompt

The prompt displays “SSP Helper” or “SSPH.exe” as the program name. Because SSPH.exe is not digitally signed, the publisher is shown as “Unknown”. The exact appearance varies depending on your version of Windows.

An “Unknown” publisher alone does not tell you whether the file is genuine. Select “Show more details” in the prompt and check the following:

- The program location is `data\SSPH.exe` in your SSP folder.
- The arguments begin with `time` (the signal for NTP time sync).

How the details are displayed also varies depending on your version of Windows. If an unfamiliar file is shown, select “No”.

### If you select “Yes” or “No”

- **Yes**<br>
  SSPH sets the computer's clock to the time obtained from the server and exits. It also accounts for the time elapsed while the prompt was open. SSPH only changes the clock.
- **No**<br>
  The clock is not changed. Other SSP functions are not affected.<br>
  However, the ghost is notified that the clock was corrected (the `OnSNTPCorrect` event). As a result, the ghost may speak as if it corrected the clock, even though the clock was not actually changed.

### When it does not appear

- When SSP is running as an administrator. The main SSP program changes the clock itself, so SSPH is not used and no prompt appears.
- When SSP is started normally under an administrator account with UAC enabled. “Automatically sync the clock” is grayed out and cannot be selected, so a prompt will not appear automatically. However, a prompt will appear as described above when NTP time sync is started from the menu or by a ghost.
- When you are a standard user without administrator privileges. You can select “Automatically sync the clock”. A prompt asking for an administrator password may appear each time the clock is corrected.

### Avoiding confirmation prompts

- Do not use NTP time sync. Recent versions of Windows set the clock automatically.
- We recommend leaving “Run clock synchronization automatically” off. However, even when it is off, a confirmation prompt may appear when a ghost performs NTP time sync.
- We do not recommend running SSP as administrator just to avoid confirmation prompts. Doing so runs SSP and all its ghosts with administrator privileges.

!!! tip "ヒント"

    SSPH does not cause UAC confirmation prompts for operations other than those described here (installation, SSP updates, retrieving ghost update locations, and uninstallation).<br>
    If a confirmation prompt appears during one of these operations, select “Show details” to check the file being launched. If you do not recognize the file, select “No”.

## Details of each operation

### Installing SSP

When you run the SSP installer (a self-extracting exe), `data\SSPH.exe` among the extracted files displays the installation screen. The “Install SSP?” confirmation that appears immediately after you launch the installer comes from the self-extracting component, not SSPH.

- **Installation location**<br>
  If an SSP installation is registered in the file associations, its folder is entered by default. Otherwise, the default is `%LOCALAPPDATA%\Programs\SSP`.
- **Available options**<br>
  These include a Start menu shortcut, file associations, a desktop shortcut, and language pack downloads. By default, the Start menu shortcut and file associations are on, and the desktop shortcut is off. The language pack option is on when a pack is available for your language.
- **UAC-protected folders**<br>
  Folders under `Program Files` or `Windows` require administrator privileges for writing, so you cannot select them as the installation location. Choose another folder (for example, `C:\Users\ユーザー名\SSP`).
- **Folders containing files other than SSP**<br>
  If you select a folder that already contains files but does not contain `ssp.exe` and `data\SSPH.exe`, a confirmation prompt appears. This is because all data in the folder is deleted during uninstallation.

When installation is complete, SSP starts.

### Updating SSP

SSP updates are applied either immediately after downloading or, for updates downloaded and deferred in advance, the next time SSP starts. SSP copies `data\SSPH.exe` as `data\SSPH2.exe`, launches it, and then exits. Because SSP cannot be overwritten while it is running, `SSPH2.exe` waits for SSP to exit before starting the update.

`SSPH2.exe` displays an “Updating SSP...” window and extracts the downloaded update, overwriting existing files. It then deletes the downloaded files and restarts SSP, and the restarted SSP deletes `SSPH2.exe`.

For the update procedure, see [Updating SSP](../howto/verup.md).

### Retrieving a ghost's update location

When SSP needs to know a ghost's update location (`homeurl`), it may ask SSPH to find it. SSPH searches as follows.

1. It reads dictionary files and other files in the ghost's `ghost\master` folder, looking for a `homeurl` entry.
2. If it does not find one, it temporarily loads the ghost's SHIORI and retrieves the `homeurl` resource.

This runs in a separate process from SSP, which waits up to 2 minutes. Any dialogs that open during this time are closed automatically.<br>
While SSPH is running, SSP temporarily renames executable files in the ghost's folder (except those beginning with `perl`, `php`, or `lisp`; for example, `xxx.exe` is renamed to `xxx_exe`). These executable files cannot be launched during this time. When SSPH finishes, their original names are restored.

### Uninstalling SSP

When file associations are enabled, “SSP” is registered in Windows under “Installed apps” (“Programs and Features”). If you remove it from there, SSPH performs the uninstallation.

1. If SSP is running, SSPH asks you to close it first and exits without doing anything.
2. A confirmation prompt warns that “All data, including ghosts, will be deleted.” Select “Yes” to continue.
3. Because SSPH cannot delete itself from the SSP folder, it creates a copy of itself in the temporary folder (`%TEMP%\SSPHUninstall.exe`) and launches it.
4. The copy removes shortcuts, file associations, and other registrations, then deletes everything in the SSP folder (a progress window appears).
5. Finally, it displays a completion message.

If the SSP folder is at the root of a drive (such as `C:\`), nothing is deleted, to avoid deleting the drive's contents.<br>
Everything in the SSP folder is deleted, including ghost data and backups. Move anything you want to keep to another location beforehand.

`SSPHUninstall.exe` is scheduled for deletion when Windows restarts. If it could not be scheduled for deletion, it may remain in the temporary folder. You can delete it if it is still there.

## How to check if it is genuine

Only the following 3 SSPH filenames are associated with SSP.

- `SSPH.exe`: Located in the `data` folder inside the SSP folder. While the installer is running, the copy in the `data` folder of the extracted temporary folder is used.
- `SSPH2.exe`: Created in the same `data` folder only while SSP is being updated.
- `SSPHUninstall.exe`: Created in the Windows temporary folder during uninstallation.

An SSPH file with any other name or in any other location may not belong to SSP. The information displayed in Properties can also be altered, so check the location first.<br>
If you are unsure, compare the file you have with `data\SSPH.exe` from a copy of SSP obtained from [SSP BUGTRAQ](ssp.md#ssp-bugtraq).
