# Settings: External Applications

This page explains the “External Applications” page in the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

This page lets you configure applications to launch from SSP.

These are applications that SSP launches as needed. Usually, default settings and other options are detected automatically, so you do not necessarily need to configure them.

## Item descriptions

### Browser settings

Configure the browser to use when opening URLs from recommendations and similar sources.<br>
Set this only if you want to use a different browser.<br>
Usually, if this field is blank, the browser set as the default (which in most cases is Internet Explorer) is used, so you probably do not need to configure it.

### File manager settings

Configure the software to launch when a file management program is needed, such as when you select “Open” from Explorer’s right-click menu.<br>
Usually, if this field is blank, Windows Explorer is launched, so you do not need to configure it.

### Editor settings

Configure the application to use when opening a text file from a ghost.<br>
Usually, if this field is blank, the default application, such as Notepad, is used, so you probably do not need to configure it.

**Arguments**: You can specify arguments to pass to the editor.<br>
%1 is replaced with the file name (full path), and %2 is replaced with the line selected when the file was opened (a number).

### Mail client settings

Configure the mail client to use when a ghost launches a mail program or issues a command to create a new email.<br>
Usually, if this field is blank, the mail client set as the default is used, so you probably do not need to configure it.

**Arguments**: Specify the arguments to use only when sending a new email. Configure how the email address is passed to the mail client when it receives a command to create a new email. The settings differ for each mail client, so refer to its documentation.

The %1 portion is replaced with "mailto:address".

Example for EdMax:　/A="%1"<br>
Example for Becky!Ver2:　"%1"<br>
Example for Outlook Express:　/mailurl:%1

### Version control tools

By running Subversion or Git from SSP, you can update a version control tool using the same operation as updating a regular ghost.<br>
Here you can manually select which of these tools to run.<br>
These tools are usually detected automatically, so you do not need to configure them.

- **Subversion**<br>
  If this field is blank, TortoiseSVN is detected automatically.
- **Git**<br>
  If this field is blank, TortoiseGit is detected automatically.

**Note**:<br>
※If both the browser and mail client fields are blank, the settings in the “Internet” Control Panel are used.<br>
※If the file manager field is blank, Windows Explorer is used.<br>
※If the editor field is blank, the application associated with .txt files is used. Usually, this is Notepad.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the page currently selected in the Preferences dialog (that is, this page).<br>
  The “?” mark at the top right of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” mark at the top right of the dialog does the same thing.
