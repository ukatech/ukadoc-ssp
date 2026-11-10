# Settings: Connection (1)

This page explains the “Connection (1)” page in the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

This page contains settings related to network connections.

You should generally not need to change anything here, but you may need to configure these settings to perform network updates from a computer behind a firewall.

!!! tip "ヒント"

    Some of these settings are for connection environments that are rarely seen nowadays. Take them as a glimpse into the past.

## Explanation of Each Setting

### General

- **Network protocol to use**<br>
  Set how IPv4 and IPv6 are used.<br>
  The default \[Auto\] setting should normally work fine.<br>
  IPv4=>IPv6 and IPv6=>IPv4 try name resolution and other operations in the order shown, from the former to the latter.
- **Verify server certificates for SSL/TLS connections**<br>
  Normally, leave this ON. Only try turning it OFF temporarily if you have a problem connecting to a server that supports SSL or similar protocols.<br>
  Note that mail checkers (POP3S), for example, can be [configured separately](pop.md); you do not need to configure them here.

### Proxy Server Settings

- **Automatically use Windows settings**<br>
  Uses the Internet Explorer settings for the proxy configuration.<br>
  If you are unsure about the settings, we recommend leaving this checked.
- **Connect through a proxy server**<br>
  If you know the proxy server details, enter its name and port number in the fields below and check this option. Headline sensors and similar features will then retrieve data through the proxy server.
- **Username / Password**<br>
  Set the username and password for a cache server that requires user authentication. You can leave these fields blank.

### Network Connection Prompts

- **When not connected to the Internet**<br>
  This option is only for dial-up connections. When checked, it monitors the connection status and automatically controls network connections.<br>
  Do not use this option in other environments.
- **Always during the following times**<br>
  When ON, SSP will not connect to the network automatically during the specified time range—for example, for headline sensors outside of the low-cost phone-rate period.<br>
  However, if you manually request a headline check or a ghost requests a mail check, a dialog will ask whether to connect.

### Time Synchronization

Specify the SNTP or HTTP server used for time synchronization.<br>
You can also leave this unspecified and keep the setting at \[RANDOM\]. We recommend leaving it as is unless you have a problem, such as time synchronization not working.

- **SNTP server / HTTP server**<br>
  Select the type of server to use for time synchronization.<br>
  Time synchronization over HTTP is not very accurate. Use it only when SNTP is unavailable, such as behind a firewall.
- **Run time synchronization automatically**<br>
  Runs time synchronization automatically at the specified interval. Set the interval in hours.

## Buttons at the Bottom

- **Help**<br>
  Opens the help for the page currently being configured in the Preferences dialog (that is, this page).<br>
  The “?” button in the upper-right corner of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button in the upper-right corner of the dialog does the same thing.
