# Settings: Mail

This page explains the “Mail” page of the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

Use this page to configure the mail checking feature.

These settings control the feature that checks whether mail has arrived for SSP.

## Item descriptions

- **Also retrieve mail headers (including information such as the subject)**<br>
  Also retrieve mail headers so the ghost can parse them (for example, the subject).<br>
  Turn this OFF if you do not want to pass headers to the ghost.
- **Report the number of new messages as the number of messages**<br>
  Normally, the ghost should say something like “You have XX messages,” but this number is the number of messages remaining on the server, not the number of new messages.<br>
  Enable this setting to have the ghost say the number of new messages instead of the number of messages on the server.
- **Display a message only when there is new mail**<br>
  The ghost will only tell you that mail has arrived when there is new mail.

### Sound to play when mail arrives

When new mail arrives, the audio file configured here will be played. Select a file with the “Browse...” button, clear the sound setting with the “None” button, or check the configured sound with the “Play” button.

### Account settings

To add an account, click the “Add...” button. To delete an account, select it from the list below and click the “Delete” button.<br>
To edit settings, click the “Change...” button. Click the “Copy” button to duplicate an existing configuration and create a new one.

- **Account name**<br>
  Give the account any name that will be easy for you to recognize. It will appear in the mail check menu.
- **Type**<br>
  Supported types are XOAUTH2-POP3/APOP/standard POP3, XOAUTH2-IMAP4/IMAP4, and NNTP.<br>
  Refer to the instructions from your provider or other mail service to configure this setting.<br>
  In most cases, you can connect using POP3 or APOP.<br>
  XOAUTH2-POP3/XOAUTH2-IMAP4 use what is sometimes called “modern authentication.”<br>
  To use this feature, enter your email address as the user ID and your access token as the password.<br>
  Refer to each service’s developer help or similar documentation for information on how to obtain an access token (Bearer token).
- **Server**<br>
  Enter the address of the POP server where your mail is stored.<br>
  The documents from your provider should usually include an item such as “POP server address”; copy that value here (using half-width characters).<br>
  NNTP supports a special format such as nntp.example.com/`fj.*`, where you enter a group name (or a pattern containing wildcards) after the slash
- **Port number**<br>
  You can usually leave this at its default value.<br>
  Change it only if you have been given a specific port number.
- **User ID/Password**<br>
  Enter the user ID and password for your mail account.<br>
  Note that these are usually different from the username and password assigned for connecting to the Internet.<br>
  When using an XOAUTH2 feature, enter your email address and access token instead.<br>
  If you are connecting to an NNTP server that does not require authentication, enter guest/guest.
- **Use SSL/TLS to connect to the server**<br>
  Encrypts the connection to the mail server with SSL/TLS to protect your information.<br>
  You can usually connect without enabling this, but some services, such as Gmail, may always require it.
- **Verify the server’s SSL/TLS certificate**<br>
  This is an additional setting for the SSL/TLS feature above. Normally, leave it ON.<br>
  Some services, including certain free services, may cause a communication error unless you turn this OFF.
- **Automatic check**<br>
  Automatically checks for mail at the specified interval.<br>
  Do not set the interval too short.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the page currently being configured in the Preferences dialog (that is, this page).<br>
  The “?” mark in the upper-right corner of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” mark in the upper-right corner of the dialog does the same thing.
