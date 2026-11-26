# Preferences: Connection (2)

This page describes the Connection (2) page of the dialog opened by selecting Preferences from the Settings submenu of the right-click menu.

This page contains settings related to network connections.

## Settings

### Headline

- **Check automatically**<br>
  Turn this on to perform headline checks automatically at regular intervals. You can set the interval in minutes.
- **Update the automatic check starting position when running a headline manually**<br>
  For automatic checks, sets the next headline to run to the one immediately below the one run manually.<br>
  When this option is off, headlines are checked in order from the top each time.
- **Specify a sound to play on updates**<br>
  Specifies the sound to play when a headline check finds an update.

### SSTP communication

Configure the ports SSP uses to receive SSTP.<br>
Ports in the list with at least one of IPv4 or IPv6 enabled are used to listen for SSTP.<br>
By default, ports 9801 and 9821 are set to Local (from this PC only) for both IPv4 and IPv6, and port 11000 is disabled.

The left column of the list shows the port number, and the right column shows its status. The status contains the following information.

- The type of receiving configuration (Local, Global, or Custom). Disabled ports are shown as “Disabled”.
- If listening fails, the reason is shown after “Error:” (or “Partial:” if only some addresses failed). Reasons include “invalid address” (the address format is incorrect), “port in use” (the port is in use elsewhere), “address not available” (the address is not on this PC), and “no address in range” (there are no addresses in the specified range).
- The IP versions used for listening (such as `[IPv4+IPv6]`) and, for Custom, the specified addresses.

The icon on the left differs by receiving configuration type (Global, Local, or Custom) and by whether listening succeeded, partially succeeded, or failed. Disabled ports have a separate icon.

- **Add...**<br>
  Adds a port. Opens the [SSTP port settings](#sstpポートの設定) dialog.
- **Delete**<br>
  Deletes the port selected in the list.
- **Edit...**<br>
  Changes the settings of the port selected in the list. You can also double-click a port in the list.
- **Right-click**→**Retry Listen**<br>
  This option appears in the menu when you right-click a port in the list. It retries listening on that port.<br>
  Use it to retry a port that failed to listen, or to refresh the addresses a port specified by range (CIDR) listens on after this PC's address changes, such as through DHCP.

While SSP is running with the `--sstp-listen` startup option, the list is read-only: you cannot add, delete, or edit ports (only Retry Listen is available).

!!! tip "ヒント"
    If you select Global or specify a non-Local address with Custom, SSTP from other PCs will also be accepted. Use these settings only on trusted networks.<br>
    As of 2.9.40, HTTP requests accepted on the same port as SSTP (all paths, including the test page, MCP, and POST requests to `/api/sstp/v1` for SSTP over HTTP) on Global ports are allowed only from your own PC (`127.0.0.1` and `::1`) and the LAN (within the network ranges assigned to this PC's network adapters, including `fe80::/10` and `169.254.0.0/16` on the same link). Requests from other sources (on the internet) receive `403`. Custom ports follow the specified address settings and do not restrict request sources. Ordinary SSTP (without HTTP) is not subject to this restriction.

- **Log SSTP**<br>
  Writes scripts and events received through SSTP communication to a file named `log\SSTP.log`.<br>
  Some ghosts use this log to change their talk, so turn this on if needed.<br>
  Clicking this opens a screen where you can specify the maximum log size in KB. Enter the desired maximum size.
- **Make ghosts that are not running appear to be running**<br>
  Writes information to a designated area so that other SSTP-compatible software sees ghosts that are not running as if they were running.<br>
  Without this setting, “Play with the specified ghost whenever possible” may not work.
- **Do not block on SSTP with choices**<br>
  Normally, when SSTP with choices is received, other incoming SSTP is not played until a choice is selected, so that the selected choice can be sent back to the sender.<br>
  This is a limitation of the specification, but you can turn this on to change the behavior if blocking on choices is a problem (for example, when playing SSTP Bottle).<br>
  However, tools that expect a choice to be returned will not work in this case, so use this option with care.
- **Completely disable SSTP filtering within ghosts**<br>
  Some ghosts are configured to block all external SSTP or ignore SSTP that does not meet certain conditions, and may not speak SSTP messages.<br>
  Turning this on disables all such filtering, but it overrides the author's intention to prevent the character from behaving out of character. Consider this carefully before enabling it.
- **Launch ghosts**<br>
  Specifies what happens when an SSTP message instructs SSP to launch a particular ghost.<br>
  Normally, ghosts are launched only in response to instructions via SSP messenger \[Messenger \[SSTP/1.5\] only\].<br>
  On less powerful machines, “Never launch” is strongly recommended.<br>
  On more powerful machines, selecting “Play with the specified ghost whenever possible” makes things livelier (but also less stable).
- **Action after launch**<br>
  Specifies when to close ghosts temporarily launched by the setting above.
- **Maximum number of temporarily launched ghosts**<br>
  Specifies the maximum number of ghosts temporarily launched via SSTP.<br>
  When this number is exceeded, ghosts are closed in the order they were launched, starting with the oldest.
- **Minimum launch interval for temporarily launched ghosts**<br>
  Specifies the interval between launches of ghosts temporarily launched via SSTP.<br>
  If many requests arrive at once, SSP returns 409 Conflict and does not launch a ghost until the number of seconds specified here has elapsed since the previous request.<br>
  This setting applies only when a ghost needs to be launched temporarily. Otherwise, requests are accepted immediately.

### SSTP port settings

This dialog opens when you select “Add...” or “Edit...” under SSTP communication. Configure the following settings for each port.

- **Port number**<br>
  The port number to listen on. Specify a number from 1 to 65535.<br>
  You cannot use the same number as another port.<br>
  In 2.9.39 and earlier, two custom ports could share the same number if their specified addresses did not overlap. In 2.9.40 and later, even custom ports cannot share the same number (because custom ports also listen on loopback, as described below). If an older configuration contains multiple custom ports with the same number, only the first one listed is loaded.
- **IPv4・IPv6**<br>
  The IP versions to listen on. If you clear both checkboxes, the port is disabled and does not listen.
- **Reception settings**<br>
  Choose where to accept SSTP from.

  - **Local (this PC only)**<br>
    Accepts SSTP only from this PC (127.0.0.1 and ::1). This is the default.
  - **Global (allow all)**<br>
    Listens on all addresses. Also accepts SSTP from other PCs.
  - **Custom**<br>
    Listens on the specified addresses. You can enter addresses in the field below only when Custom is selected.<br>
    In 2.9.40 and later, if the address field does not include loopback (`127.0.0.1` and `::1`), the port also automatically listens on loopback for each checked IP version. These addresses do not appear in the address field, and you do not need to add them. This allows connections from your PC via `localhost`. Nothing is added if the specification already includes loopback, as with `0.0.0.0`, `::`, or `127.0.0.0/8`.

    - Specify numeric addresses (hostnames cannot be used). You can specify multiple addresses separated by commas. Example: `192.168.0.5, ::1`
    - You can also specify a range (CIDR), such as `192.168.192.0/24`. When you specify a range, SSP listens on all addresses currently assigned to this PC that fall within it. Even in an environment where addresses change via DHCP, specifying a range lets you listen on new addresses simply by restarting SSP or right-clicking the list and selecting “Retry Listen” to start listening again.<br>
      `127.0.0.0/8` is a loopback range. When the prefix length is the maximum for the address (32 for IPv4, 128 for IPv6), it is equivalent to a single address.
    - A specified address is used only if its IP version (IPv4 or IPv6) is checked. For example, an IPv4 address is not used unless IPv4 is checked.
    - The settings are saved even if you specify an incorrectly formatted address, an address not assigned to this PC, or a range that contains none of this PC’s addresses. In that case, listening fails and an error appears in the list. If the format is invalid, SSP does not listen on any address, including loopback.
    - If none of the specified addresses are used (for example, because their versions do not match the checked versions), SSP listens only on loopback, and the list displays “Partial: no usable protocol”.
- **This PC’s networks**<br>
  This read-only field is below the custom address field. It displays the networks of addresses currently assigned to this PC as comma-separated CIDR ranges, such as `192.168.192.0/24, 2001:db8:1::/64`. If the prefix length is unknown, only the address is displayed.<br>
  You can select and copy these entries and paste them directly into the address field.

## Buttons at the bottom

- **Help**<br>
  Opens help for the current page in the Preferences dialog (that is, this page).<br>
  The “?” mark at the top right of the dialog does the same.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” mark at the top right of the dialog does the same.
