# Archive viewer

This is a viewer window that lists the contents of archive files such as ZIP files, like Explorer, and lets you extract them.<br>
You don't need to extract an archive just to view its contents, and you can extract only the files you need by dragging and dropping them. You can view multiple archives in tabs and switch between them.

You can also gather files and folders on your computer to create (compress) a new archive.

## Supported archive formats

The main supported archive formats are listed below.<br>
Formats marked ○ in the "Create" column can also be used to create new archives with this viewer. Other formats can only be viewed and extracted.

| Format | Extension | Create | Notes |
|---|---|---|---|
| ZIP | .zip / .zipx | ○ | Also supports password protection (ZipCrypto / AES-128, 192, and 256). |
| NAR | .nar | − | An archive for distributing ghosts and other items. Its contents are in ZIP format. |
| 7-Zip | .7z | ○ | Supports passwords (AES-256) and header encryption, which also hides file names. |
| LZH | .lzh / .lha | − | A format that has been used in Japan for a long time. |
| CAB | .cab | − | Windows Cabinet. Also recognizes split (multi-volume) archives. |
| Self-extracting archive | .exe | − | Searches for and opens an archive embedded in an executable file. |
| TAR | .tar / .tgz / .txz / .tbz2 / .tlz / .tzst, etc. | − | A format for bundling files used on UNIX systems. Archives combined with the compression methods below can also be opened as-is. |
| Single-file compression | .gz / .bz2 / .xz / .lzma / .zst / .br / .Z | − | gzip / bzip2 / XZ / LZMA / Zstandard / Brotli / UNIX compress. Opens as an archive containing a single file. |
| cpio | .cpio | − | UNIX cpio archives (newc / crc / odc / old binary). |
| ar / Debian package | .deb / .udeb | − | The actual format is an ar archive. |
| RPM package | .rpm | − | A package format used by Red Hat-based systems. |
| CD/DVD image | .iso | − | ISO9660 / Joliet / Rock Ridge / UDF. You can extract files from the image. |
| Disk image | .img | − | Floppy disk images and other disk images in FAT12 / FAT16 / FAT32 formats. |

!!! tip "ヒント"

    The format is identified by the **file contents**, not the extension. Archives still open correctly if you have only changed the extension or if they have no extension.<br>
    Combinations such as `.iso.gz`, where an image has been compressed, are also identified automatically by examining the contents.

## How to open

You can open the Archive viewer in any of the following ways.

- **[Right-click menu](../howto/rclick.md) → “Functions” → “Archive viewer”**<br>
  Opens the viewer with nothing loaded.<br>
  ⇒ See also the [“Functions”](index.md) page.
- **Drag and drop an archive file onto a ghost**<br>
  If the ghost does not respond to the file, dropping an archive file onto the ghost automatically opens it in this viewer.<br>
  The viewer will not start if the file cannot be loaded as an archive.
- **Drag and drop an archive file into the viewer**<br>
  Drop an archive file into the viewer after it has opened to add it as a new tab. You can drop it anywhere in the window (the title bar, tab row, and file list all work the same way).<br>
  If you drop multiple files at once, only files that can be opened as archives will appear in tabs; the rest are ignored.

## Screen layout

- **Menu bar**<br>
  You can perform all operations here (see below for details).
- **Toolbar**<br>
  This displays frequently used operations as buttons. Each button corresponds to a menu item, and hovering over a button displays its function name (tooltip).<br>
  Buttons for operations that are currently unavailable are shown with a gray dotted outline. Each time you press the display toggle button at the far right, its icon changes to reflect the current display mode.
- **Tabs**<br>
  A tab appears for each open archive. Click a tab to switch the archive being displayed.<br>
  The icon at the left end of each tab indicates whether it is a tab for viewing an archive or for creating a new one.
- **List**<br>
  This area displays the contents of the archive. In the "Details" view, the columns **Name・Size・Compressed size・Method・Modified date** are displayed.<br>
  A `-` in the "Compressed size" column means that the compressed size cannot be determined for each individual file in that format (this can happen with formats that compress files together, such as 7-Zip or tar).
- **Status bar**<br>
  At the bottom of the window, the **actual archive format** and **number of items in this folder** are displayed, along with the <strong>current location (folder) within the archive</strong>, from left to right.<br>
  While extracting or compressing, a progress bar appears at the far left.

!!! tip "ヒント"

    "Actual archive format" displays the contents that were actually read, such as `Zip/Deflate/AES-256`, `7Zip/LZMA2/AES-256/Encrypted Header`, `GZip/Tar`, or `UDF Image`. The format is determined by the contents, not the file extension. For example, if a file has the `.exe` extension but contains a ZIP archive, it is displayed as `Zip`.

## Top menu

### Browse and extract

- **Open...\[Ctrl+O\]**<br>
  Opens a file selection dialog and opens the selected archive in a new tab. You can select multiple archives.<br>
  If a tab with the same archive is already open, that tab is selected.
- **Extract...**<br>
  Extracts **only the selected items** in the list to the specified folder. If you select a folder, its contents are extracted along with it.<br>
  Items are extracted with a folder hierarchy based on the folder currently displayed.
- **Extract All...**<br>
  Extracts **the entire contents** of the archive to the specified folder. This preserves the folder hierarchy from the top level of the archive.

!!! tip "ヒント"

    The destination folder is remembered and offered as the default the next time you extract.

### Create an archive

- **New\[Ctrl+N\]**<br>
  Creates an empty "compression tab." Add the items you want to include, then save them as an archive.
- **Add Files...**<br>
  Adds files to the compression tab. You can select multiple files.
- **Add Folder...**<br>
  Adds a folder and its entire folder hierarchy to the compression tab. The folder selection dialog only lets you select one folder at a time, so use drag and drop to add multiple folders at once.
- **Delete\[Delete\]**<br>
  Removes the selected items from the list of items to be archived. If you select a folder, its contents are removed along with it.<br>
  Items are removed from the list only; the original files are not deleted.
- **Save Compressed As...\[Ctrl+S\]**<br>
  Saves the items you collected as a single archive file. The format is determined by the extension you choose when saving (`.7z` for 7-Zip; otherwise, ZIP).<br>
  You can set a password by checking "Password" in the save dialog (see below).

!!! tip "ヒント"

    These options are available only in the compression tab. They are grayed out in tabs where you are browsing an archive. Conversely, "Extract" and "Extract All" are available only in browsing tabs.

### Selection and display

- **Select All\[Ctrl+A\]**<br>
  Selects all items in the folder currently displayed.
- **Large Icons / Small Icons / List / Details**<br>
  Changes how the list is displayed (the default is "Details"). These options work the same way as the Explorer view options.<br>
  This setting is shared across all tabs and is retained the next time you start the viewer.

## Mouse and keyboard operations

- **Double-click a folder**<br>
  Opens that folder. To go back up, double-click `..` at the top of the list.
- **Double-click a file**<br>
  Extracts the file and treats it as if you dropped it onto the currently displayed ghost.<br>
  If the ghost does not respond, the file opens in the [Picture viewer](pictureviewer.md), a media player, or another application, just as it would with a regular drop. This is useful when you want to check the contents of an archive without extracting it.
- **Drag an item to Explorer**<br>
  You can extract selected files and folders by dragging them directly to an Explorer folder or the desktop. You can drag multiple selected items at once. Folders are extracted with their entire folder hierarchy.<br>
  Items are extracted directly to the drop destination, rather than being extracted somewhere first and then copied.<br>
  Extraction starts after you drop the items, so you can release the mouse right away, even with a large archive, and continue using the viewer while you wait.<br>
  If you entered the password when opening a password-protected archive, you won't be asked to enter it again.
- **Drag and drop to the viewer**<br>
  Drop an archive file to open it in a new tab.<br>
  However, **while a compression tab is displayed**, dropped files and folders are added as items to be archived.

The main keyboard shortcuts are as follows.

| Key | Function |
|---|---|
| Ctrl+N | New (compression tab) |
| Ctrl+O | Open an archive |
| Ctrl+A | Select all |
| Ctrl+S | Save compressed as |
| Delete | Remove from the items to be archived (compression tab only) |
| Ctrl+W | Close tab |
| Ctrl+Tab | Switch to the next tab |
| Ctrl+Shift+Tab | Switch to the previous tab |

## Details of each feature

### Open a password-protected archive

When you try to open a password-protected archive, you are prompted to enter its password. If it is correct, you won't need to enter it again until you close that window.<br>
For archives with 7-Zip "header encryption," you need to enter the password before the file list can be displayed.

### Create an archive

Open a compression tab with "New," then add files and folders by dragging and dropping them or by using "Add Files" and "Add Folder." Folders are added with their entire folder hierarchy preserved.<br>
While collecting items, you can double-click a folder to open it. Any items you add while that folder is open will be placed in that folder in the archive.<br>
If you add an item with the same name again, it replaces the previous one.

When you have finished collecting items, save them using "Save Compressed As." The compression tab remains open after saving, so you can add more items and save the updated contents under a different name.

### Setting a Password When Compressing

Check “Password” in the save dialog to open a dialog where you can set a password.

- **Enter**<br>
  Type a password of your choice. The characters you enter are masked.
- **Generate**<br>
  Automatically generate a random password. You can specify the types of characters to use (lowercase letters, uppercase letters, numbers, and symbols) and the length (4–64 characters; the default is 16 characters).<br>
  The generated password is displayed as entered, not masked, so you can write it down.

!!! tip "ヒント"

    If you forget the password, you will not be able to extract the contents. Be sure to write down any generated password.<br>
    If the output format is `.7z`, the list of file names is encrypted along with the contents (header encryption). File names cannot be hidden in ZIP archives.

### Warnings for Suspicious Items

If an archive contains items that could cause unexpected results when extracted, their names are displayed in **red**.<br>
If a folder contains such items, its name is also displayed in red, so you can spot them without opening each folder in the hierarchy.

Items are displayed in red if they meet any of the following criteria.

| Type | Details |
|---|---|
| Abnormally high compression ratio | An item that expands to 200 times or more its compressed size (a so-called “zip bomb”). |
| Excessively large | A single file that exceeds 64 GB. |
| Suspicious path | A name that attempts to write outside the archive (for example, one containing `..` or starting with a drive name). SSP automatically neutralizes these paths, but they may be a reason to question the archive’s source. |
| Duplicate name | A file with the same name as another file, differing only in letter case. When extracted, one file will silently overwrite the other. |
| Unusual date | An item with a modification date before 1980 or after 2100. |
| Special item | An item that is not a regular file or folder, such as a symbolic link or device. No actual item is created when it is extracted. |
| Misleading extension | An item whose name contains special control characters that make its displayed extension differ from its actual extension. |

!!! tip "ヒント"

    Red highlighting is only a warning; extraction itself is not stopped.<br>
    SSP automatically neutralizes items that attempt to write outside the archive, and skips special items such as links and devices without creating them. Extracting red-highlighted items will not damage anything outside the archive.

### Extracting Large Archives

While extracting or compressing, a progress bar is displayed at the left end of the status bar. It disappears automatically when processing is complete.
