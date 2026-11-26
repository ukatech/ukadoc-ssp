# Settings: Connection (2)

This page describes the Connection (2) page of the Preferences dialog, opened from Preferences in the Settings submenu of the right-click menu.

This page lets you configure network connection settings.

## Settings

### Headline

- **Check automatically**<br>
  Turn this on to check headlines automatically at regular intervals. You can set the interval in minutes.
- **Update the automatic check starting position when a headline is run manually**<br>
  When checking automatically, start with the headline immediately below the one last run manually.<br>
  When this is turned off, each check proceeds in order from the top.
- **Specify a sound to play on updates**<br>
  Specify a sound to play when a headline check finds an update.

### SSTP communication

Configure the ports SSP uses to receive SSTP.<br>
Ports in the list with at least one of IPv4 or IPv6 enabled are used to listen for SSTP.<br>
By default, ports 9801 and 9821 are set to Local (this PC only) for both IPv4 and IPv6, and port 11000 is disabled.

The left column shows the port number, and the right column shows its status. The status includes the following:

- The reception type (Local, Global, or Custom). Disabled ports are shown as “Disabled”.
- If listening fails, “Error:” appears, or “Partial:” if only some addresses failed, followed by the reason. Reasons include “invalid address” (the address format is invalid), “port in use” (the port is used elsewhere), “address not available” (the address is not on this PC), and “no address in range” (no address falls within the range).
- The IP versions being listened on (such as `[IPv4+IPv6]`) and, for Custom, the specified addresses.

The icon on the left differs by reception type (Global, Local, or Custom) and by whether listening succeeded, partially succeeded, or failed. Disabled ports have their own icon.

- **Add...**<br>
  Add a port. This opens the [SSTP port settings](#sstpポートの設定) dialog.
- **Delete**<br>
  Delete the selected port from the list.
- **Edit...**<br>
  Change the settings for the selected port. You can also double-click a port in the list.
- **Right-click**→**Retry Listen**<br>
  This menu item appears when you right-click a port in the list. It retries listening on that port.<br>
  Use it to retry a port that failed to listen, or to refresh the addresses used by a port specified with a range (CIDR) after this PC's addresses change, such as through DHCP.

When SSP is started with the `--sstp-listen` launch option, the list is read-only and you cannot add, delete, or edit ports (only Retry Listen is available).

!!! tip "ヒント"
    If you select Global or specify a non-Local address under Custom, SSP will also accept SSTP from other PCs. Use this only on trusted networks.

- **Log SSTP**<br>
  Write scripts and events received through SSTP communication to a file named `log\SSTP.log`.<br>
  Some ghosts use this log to change their talk, so turn this on as needed.<br>
  Clicking this opens a screen where you can specify the maximum log size in KB. Enter the desired value.
- **Make ghosts that are not running appear to be running**<br>
  Write information to a specific area so that other SSTP-compatible software sees ghosts that are not running as if they were running.<br>
  If this setting is off, “Play using the specified ghost whenever possible” may not work.
- **Do not block on SSTP with choices**<br>
  Normally, when SSTP with choices is received, other incoming SSTP is not played until a choice is selected, so that the selection can be sent back to the sender.<br>
  This is a limitation of the specification, but you can turn this on to change the behavior if blocking on choices is a problem, such as when playing SSTP Bottle.<br>
  Be careful when using this option, as tools that expect a choice to be returned will not work.
- **Completely disable SSTP filtering within ghosts**<br>
  Some ghosts are configured to block all external SSTP or ignore SSTP without specific attributes, and may not speak SSTP messages.<br>
  Turning this on disables all such filtering, but it also overrides the author's intention to prevent the character from acting out of character, so consider carefully before enabling it.
- **Start ghosts**<br>
  Specify what happens when an SSTP message instructs SSP to start a specific ghost.<br>
  Normally, ghosts are started only in response to instructions via SSP messenger \[Messenger \[SSTP/1.5\] only\].<br>
  On less powerful machines, “Do not start any” is strongly recommended.<br>
  On more capable machines, selecting “Play using the specified ghost whenever possible” makes things livelier (but also less stable).
- **Action after starting**<br>
  Specify when to close ghosts temporarily started by the setting above.
- **Maximum number of temporarily started ghosts**<br>
  Specify the maximum number of ghosts temporarily started via SSTP.<br>
  If this number is exceeded, previously started ghosts are closed in order, starting with the oldest.
- **Minimum interval between temporary ghost starts**<br>
  Specify the interval between ghosts temporarily started via SSTP.<br>
  If many requests arrive at once, SSP returns 409 Conflict and does not start a ghost until the number of seconds set here has elapsed since the previous request.<br>
  This setting applies only when a ghost needs to be started temporarily. Otherwise, requests are accepted immediately.

### SSTP port settings

This dialog opens from “Add...” or “Edit...” under SSTP communication. Configure the following for one port.

- **Port number**<br>
  The port number to listen on. Specify a value from 1 to 65535.<br>
  You cannot use the same number as another port, unless both use Custom and their specified addresses do not overlap.
- **IPv4・IPv6**<br>
  The IP versions to listen on. If you clear both checkboxes, the port is disabled and does not listen.
- **Reception type**<br>
  Select where to accept SSTP from.

  - **Local (this PC only)**<br>
    Accept SSTP only from this PC (127.0.0.1 and ::1). This is the default.
  - **Global (allow all)**<br>
    Listen on all addresses. SSTP from other PCs is also accepted.
  - **Custom**<br>
    Listen only on the specified addresses. The address field below is editable only when Custom is selected.

    - Specify numeric addresses (hostnames cannot be used). You can specify multiple addresses separated by commas. Example: `192.168.0.5, ::1`
    - You can also specify a range (CIDR), such as `192.168.192.0/24`. When you specify a range, SSP listens on all addresses currently assigned to this PC that fall within it. Even in an environment where addresses change through DHCP, specifying a range lets you listen on the new addresses by restarting SSP or selecting “Retry Listen” from the list's right-click menu.<br>
      `127.0.0.0/8` is the loopback range. When the prefix length is the maximum for the address (32 for IPv4 and 128 for IPv6), it is equivalent to a single address.
    - An address is used only when its IP version (IPv4 or IPv6) is checked. For example, an IPv4 address is not used unless IPv4 is checked.
    - The settings are saved even if you specify an incorrectly formatted address, an address not on this PC, or a range containing none of this PC's addresses. In that case, listening fails and an error appears in the list.
- **This PC's networks**<br>
  This read-only field below the Custom address field displays the networks of addresses currently assigned to this PC as comma-separated CIDR ranges, such as `192.168.192.0/24, 2001:db8:1::/64`. If the prefix length is unknown, only the address is displayed.<br>
  You can select and copy the contents and paste them directly into the address field.

## Buttons at the bottom

- **Help**<br>
  Open help for the current page of the Preferences dialog (that is, this page).<br>
  The “?” mark at the upper right of the dialog does the same.
- **Close**<br>
  Close the Preferences dialog.<br>
  The “×” mark at the upper right of the dialog does the same.
