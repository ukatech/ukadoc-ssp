# Settings: Connection (1)

This page explains the Connection (1) page in the dialog opened by selecting Preferences from the Settings submenu of the right-click menu.

This page contains network connection settings.

You generally do not need to change these settings, but you may need to configure them to perform network updates or similar operations from a machine behind a firewall.

!!! tip "ヒント"

    Some settings are intended for connection environments that are rarely seen today. Consider them a glimpse into the past.

## Settings

### General

- **Network protocol to use**<br>
  Choose how to use IPv4 and IPv6.<br>
  Leaving this set to \[Auto\] is normally fine.<br>
  IPv4=>IPv6 and IPv6=>IPv4 attempt name resolution and similar operations using the first protocol followed by the second.
- **Verify server certificates for SSL/TLS connections**<br>
  Normally, leave this ON. Try turning it OFF temporarily only if you have trouble communicating with a server that supports SSL or similar protocols.<br>
  The mail checker (POP3S) and similar features can be [configured separately](pop.md), so they do not need to be configured here.

### Proxy server settings

- **Automatically use Windows settings**<br>
  Uses the InternetExplorer proxy settings.<br>
  If you are unsure about the settings, we recommend keeping this checked.
- **Use a proxy server**<br>
  If you know your proxy server, enter its name and port number below and check this option to retrieve data through it for headline sensors and similar features.
- **Username / password**<br>
  Set the username and password for a cache server that requires authentication. You can leave these fields blank.

### Network connection prompt

- **When not connected to the Internet**<br>
  For dial-up connections only, check this to monitor the connection status and automatically control the network connection.<br>
  Do not use this in other environments.
- **Always during the following hours**<br>
  When ON, prevents automatic network connections during the specified hours, such as headline checks outside Telehodai hours.<br>
  However, if you manually request a headline check or a ghost requests a mail check, a dialog asks whether to connect.

### Clock synchronization

Specify the SNTP/HTTP server used for NTP time sync.<br>
It also works without specifying a server, with the setting left at \[RANDOM\], so we recommend leaving it as is unless it does not work properly or you have another reason to change it.

- **SNTP server / HTTP server**<br>
  Select the type of server used for NTP time sync.<br>
  NTP time sync using HTTP is not very accurate. Use it only when SNTP is unavailable, such as behind a firewall.
- **Synchronize the clock automatically**<br>
  Automatically synchronizes the clock at the specified interval. The interval can be set in hours.<br>
  This option cannot be selected when SSP is started normally under an administrator account with UAC enabled. For standard users, a confirmation prompt (UAC) may appear each time the clock is adjusted. Even if this setting is off, a confirmation prompt may appear when a ghost performs NTP time sync. For details, see [About SSPH (SSP Helper)](../about/ssph.md#uacの確認画面が出るとき).

## Buttons at the bottom

- **Help**<br>
  Opens help for the current page of the Preferences dialog (that is, this page).<br>
  The "?" mark in the upper-right corner of the dialog does the same.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The "×" mark in the upper-right corner of the dialog does the same.
