# Preferences: Connection (2)

This page explains the Connection (2) page of the dialog opened by selecting Preferences from the Settings submenu of the right-click menu.

On this page, you can configure network connection settings.

## Settings

### Headline

- **Check automatically**<br>
  Turn this on to perform headline checks automatically at regular intervals. You can set the interval in minutes.
- **Update automatic check starting position when running a headline manually**<br>
  When automatic checking is enabled, the next headline to run is set to the one below the headline you ran manually.<br>
  If this feature is disabled, headlines are checked in order from the top each time.
- **Specify sound to play on update**<br>
  Specify the sound to play when a headline check finds an update.

### SSTP communication

Configure the ports SSP uses to receive SSTP.<br>
Ports in the list with at least one of IPv4 or IPv6 enabled are used to listen for SSTP.<br>
By default, ports 9801 and 9821 are set to Local for both IPv4 and IPv6 (accessible only from this PC), and port 11000 is disabled.

The left column of the list shows port numbers, and the right column shows their status. The status includes the following:

- The reception type (Local, Global, or Custom). Disabled ports are shown as "Disabled".
- If listening fails, the reason follows "Error:" (or "Partial:" if only part of the attempt failed). Examples include "invalid address" (the address format is invalid), "port in use" (the port is being used elsewhere), "address not available" (the address is not on this PC), and "no address in range" (no address falls within the range).
- The IP versions being listened on (such as `[IPv4+IPv6]`) and, for Custom, the specified addresses.

The icon on the left also changes according to the reception type (Global, Local, or Custom) and whether listening succeeded, partially succeeded, or failed. Disabled ports have a dedicated icon.

- **Add...**<br>
  Add a port. The [SSTP port settings](#sstpポートの設定) dialog opens.
- **Delete**<br>
  Delete the port selected in the list.
- **Edit...**<br>
  Change the settings of the port selected in the list. You can also double-click a port in the list.
- **Right-click**→**Retry Listen**<br>
  This option appears in the menu when you right-click a port in the list. It restarts listening on that port.<br>
  Use it to retry a port that failed to listen, or to refresh the listening addresses for a port specified by a range (CIDR) after this PC's address changes, such as through DHCP.

When SSP is started with the `--sstp-listen` launch option, the list is read-only and ports cannot be added, deleted, or edited (only Retry Listen is available).

!!! tip "ヒント"
    Selecting Global or Custom with a non-Local address allows SSTP from other PCs. Use these options only on trusted networks.

- **Log SSTP**<br>
  Write the contents of scripts and events received through SSTP communication to a file named `log\SSTP.log`.<br>
  Some ghosts use this log to change their talk content, so turn this on if needed.<br>
  Click to open a screen where you can specify the maximum log size in KB. Enter the desired maximum size.
- **Make inactive ghosts appear to be running**<br>
  Write information to a specific area so that other SSTP-compatible software sees inactive ghosts as if they were running.<br>
  If this setting is disabled, "Play with the specified ghost whenever possible" may not work.
- **Do not block on SSTP with choices**<br>
  Normally, when SSTP with choices is received, other incoming SSTP messages are not played until a choice is selected, so that the selected choice can be returned to the sender.<br>
  This is a limitation of the specification, but you can change the behavior by turning this on when blocking on choices is undesirable (such as during SSTP Bottle playback).<br>
  However, tools that expect a choice to be returned will not work in that case, so use this setting with care.
- **Completely disable SSTP filtering within ghosts**<br>
  Some ghosts are configured to block all external SSTP or ignore SSTP without certain specifications, and may therefore not speak SSTP content.<br>
  Turning this on disables all such filtering, but it overrides the author's intention to keep the character in character, so enable it only after careful consideration.
- **Launch ghost**<br>
  Specify what to do when an SSTP message requests that a particular ghost be launched.<br>
  Normally, ghosts are launched only for requests via SSP messenger \[Messenger \[SSTP/1.5\] only\].<br>
  On less powerful machines, "Never launch" is strongly recommended.<br>
  On more powerful machines, selecting "Play with the specified ghost whenever possible" makes things livelier (but also less stable).
- **Action after launch**<br>
  Specify when to close ghosts temporarily launched by the setting above.
- **Maximum number of temporarily launched ghosts**<br>
  Specify the maximum number of ghosts to launch temporarily via SSTP.<br>
  If this number is exceeded, previously launched ghosts are closed in order, starting with the oldest.
- **Minimum launch interval for temporarily launched ghosts**<br>
  Specify the interval between launches of ghosts temporarily launched via SSTP.<br>
  If many requests arrive at once, SSP returns 409 Conflict and does not launch a ghost until the number of seconds set here has elapsed since the previous request.<br>
  This setting applies only when a ghost needs to be launched temporarily. Otherwise, requests are accepted immediately.

### SSTP port settings

This dialog opens from "Add..." or "Edit..." under SSTP communication. Configure the following settings for one port.

- **Port number**<br>
  The port number to listen on. Specify a value from 1 to 65535.<br>
  You cannot use the same number as another port. However, Custom ports can share a number if their specified addresses do not overlap.
- **IPv4・IPv6**<br>
  The IP versions to listen on. If you clear both checkboxes, the port is disabled (it does not listen).
- **Reception type**<br>
  Select where to accept SSTP from.

  - **Local (this PC only)**<br>
    Accept SSTP only from this PC (127.0.0.1 and ::1). This is the default.
  - **Global (allow all)**<br>
    Listen on all addresses. SSTP from other PCs is also accepted.
  - **Custom**<br>
    Listen only on the specified addresses. The address field below can be edited only when Custom is selected.

    - Specify numeric addresses (hostnames cannot be used). You can specify multiple addresses separated by commas. Example: `192.168.0.5, ::1`
    - You can also specify a range (CIDR), such as `192.168.192.0/24`. When you specify a range, SSP listens on all addresses currently assigned to this PC that fall within that range. Even in an environment where addresses change through DHCP, specifying a range lets SSP pick up new addresses simply by restarting listening (restart SSP or right-click the port in the list and select "Retry Listen").<br>
      `127.0.0.0/8` is the loopback range. When the prefix length is the maximum for the address (32 for IPv4, 128 for IPv6), it is equivalent to a single address.
    - An address is used only when its version (IPv4 or IPv6) is checked. For example, an IPv4 address is not used unless IPv4 is checked.
    - Settings are saved even if you specify an incorrectly formatted address, an address not on this PC, or a range containing none of this PC's addresses. In that case, listening fails and an error appears in the list.
- **This PC's networks**<br>
  This read-only field is below the Custom address field. It displays the networks of addresses currently assigned to this PC as comma-separated CIDRs, such as `192.168.192.0/24, 2001:db8:1::/64`. If the prefix length is unknown, only the address is displayed.<br>
  You can select and copy the contents and paste them directly into the address field.

## Buttons at the bottom

- **Help**<br>
  Open the help for the current page of the Preferences dialog (that is, this page).<br>
  The "?" icon at the upper right of the dialog does the same.
- **Close**<br>
  Close the Preferences dialog.<br>
  The "×" icon at the upper right of the dialog does the same.
