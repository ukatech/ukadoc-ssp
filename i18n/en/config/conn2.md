# Settings: Connection (2)

This page explains the “Connection (2)” page in the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

This page contains settings related to network connections.

## Explanation of Each Setting

### Headline

- **Check automatically**<br>
  Turn this ON to have headline sensors run automatically at regular intervals. You can set the interval in minutes.
- **Update the automatic rotation position when running a headline check manually**<br>
  When the automatic check feature runs, it will check the headline after the one you ran manually.<br>
  If you disable this feature, it will check headlines from the top of the list each time.
- **Sound to play when updates are found**<br>
  Specify the sound to play when a headline check finds updates.　

### SSTP Communication

Configure the ports SSP uses to receive SSTP.<br>
SSP uses ports listed here that are turned ON.<br>
※On a computer with multiple IP addresses, SSP listens on all of them.

- **Log SSTP activity**<br>
  Writes scripts and events received through SSTP communication to a file named `log\SSTP.log`.<br>
  Some ghosts use this log to change their talk, so turn this ON if needed.<br>
  Click this option to open a screen where you can specify the maximum log size in KB. Enter the desired maximum size.
- **Make it appear that ghosts that are not running are running**<br>
  Writes information to a specific area to make it appear to other SSTP-compatible software that ghosts which are not running are running.<br>
  Without this setting, “Play with the specified ghost whenever possible” may not work.
- **Do not block SSTP with choices**<br>
  Normally, when SSTP containing choices is received, SSP waits for a choice to be selected before playing any other incoming SSTP, so that it can send the selected choice back to the sender.<br>
  This is a limitation of the specification, but you can change this behavior by turning this ON if blocking on choices causes problems (for example, when playing SSTP Bottle).<br>
  However, tools that expect to receive a choice in response will not work in that case, so use this setting with care.
- **Completely disable ghost-side filtering of SSTP**<br>
  Some ghosts are configured to block all external SSTP or ignore SSTP unless it contains specific instructions, so they may not speak in response to SSTP.<br>
  Turning this ON disables all such filtering, but it goes against the author's intent to prevent the character from acting out of character. Enable it only after careful consideration.
- **Ghost startup**<br>
  Specify what happens when SSTP communication requests that a specific ghost be started.<br>
  Normally, only requests through SSP messenger will start a ghost \[Messenger \[SSTP/1.5\] only\].<br>
  We strongly recommend selecting “Never start” on low-powered computers.<br>
  On computers with enough resources, selecting “Play with the specified ghost whenever possible” makes things livelier (but also less stable).
- **Action after startup**<br>
  Specify when to close ghosts that were started temporarily using the setting above.
- **Maximum number of temporarily started ghosts**<br>
  Specify the maximum number of ghosts that can be started temporarily via SSTP.<br>
  If this number is exceeded, the ghosts that were started earliest will be closed first.
- **Minimum startup interval for temporarily started ghosts**<br>
  Specify the minimum interval between starting ghosts temporarily via SSTP.<br>
  If many requests arrive at once, SSP returns 409 Conflict and does not start a ghost until the specified number of seconds has elapsed since the previous request.<br>
  This setting applies only when a ghost must be started temporarily. If no temporary startup is needed, SSP accepts the request immediately.

## Buttons at the Bottom

- **Help**<br>
  Opens the help for the page currently being configured in the Preferences dialog (that is, this page).<br>
  The “?” button in the upper-right corner of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button in the upper-right corner of the dialog does the same thing.
