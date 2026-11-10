# Settings: Ghost (1)

This page explains the “Ghost (1)” page in the dialog opened by selecting “Preferences” from the “Settings” submenu of the right-click menu.

This page covers settings related to ghosts.

These settings apply to all ghosts.

## Item descriptions

- **Select and launch one random ghost (discard the state from the previous session)**<br>
  Launch one random ghost at startup.<br>
  You can keep launching random ghosts at all times by using this together with automatic ghost switching.
- **Select a ghost at startup**<br>
  Displays the ghost selection dialog at startup.
- **Do not use ghost-defined menus (enable on low-performance machines)**<br>
  When checked, SSP ignores the ghost's settings for right-click menu item names and visibility, and displays the default menu instead.<br>
  The right-click menu usually displays text specified by the ghost, but retrieving this text can take some time and may delay the menu from appearing.<br>
  In this case, enable this setting to make the menu appear faster.<br>
  You can also check this setting if you simply find the menu difficult to read.
- **Do not speak when minimized**<br>
  The ghost will not speak at all when minimized to an icon.<br>
  Some ghosts speak just before they are minimized; this setting disables that.
- **Do not detect when characters are off-screen**<br>
  Disables detection of whether characters extend beyond the screen.<br>
  Some ghosts perform this detection independently, in which case this setting is ignored.<br>
  If so, check the settings for each ghost as well.
- **Do not detect overlapping characters**<br>
  Disables detection of whether characters are positioned so that they overlap one another.<br>
  Some ghosts perform this detection independently, so check the ghost's settings as well.
- **Use a key as a middle-click substitute**<br>
  This substitutes for the response to clicking the middle button on a three-button mouse, or pressing the wheel on a mouse with a wheel button. Holding down the key specified here while left-clicking triggers the equivalent of a middle-click.<br>
  You do not need to set this if your mouse has a middle button or equivalent function.
- **Notify ghosts of music playback information**<br>
  Notifies ghosts of information about tracks playing in compatible music playback software, such as the standard Windows media player app. Compatible ghosts can speak or display information such as the title of the track currently playing.

### Network update

These settings are for ghost network updates. You usually do not need to change them.

- **Enable automatic updates at startup**<br>
  At the specified interval in days, automatically checks for updates a short while after a ghost starts.<br>
  Only if an update is available, it behaves as if you had started the update from the menu.
- **Update interval (days)**<br>
  Sets the automatic update interval in days.
- **Enable the key for switching to repair mode**<br>
  If you hold down the key specified here while performing a network update, SSP checks all ghost files and repairs the ghost by updating any corrupted files or files that are not the latest version for any reason.<br>
  You can also set the update check method described below to always use repair mode.
- **Also check for balloon and shell updates when updating**<br>
  When updating a ghost, SSP also updates the balloon and shell currently used by that ghost, but only if they support network updates.<br>
  It may look as though the update is running more than once, but this is normal.
- **Update check method**<br>
  Specifies how to check for updated files.<br>
  “Strict” should be fine in most cases, but if you experience symptoms such as updates always being available or save files being overwritten, try changing this to “Standard.”

### Automatic ghost switching

- **Enable automatic switching**

  You can automatically switch ghosts at the specified interval.<br>
  With “Random,” SSP searches for a ghost to switch to at each interval; with “In order,” it switches ghosts in the order they appear in the menu.

  When multiple ghosts are running, one of the ghosts currently running that can be switched (that is, not in an inactive state such as minimized, and not set to disable automatic switching in [Folder settings](folder.md)) is selected at random at each interval.

### Ghost cache control

- **Enable ghost cache**<br>
  When enabled, the ghost cache feature is turned on.<br>
  The ghost cache feature keeps information in memory when you close some of your running ghosts, allowing them to start faster the next time you launch them.<br>
  Here you can set how many ghosts to cache and how long to keep them in the cache.<br>
  If you have configured temporary ghost launching in [Connection (2)→SSTP](conn2.md) under Preferences, it is a good idea to set a higher value.<br>
  Set the maximum number of ghosts kept in the cache with “Maximum number,” and how long they remain in the cache with “Retention time.”
- **Enable ghost and balloon list cache**<br>
  When enabled, information about the ghosts and balloons installed at startup is kept in memory, reducing the time it takes to list them.<br>
  This is useful if you have a large number installed.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the page currently selected in the Preferences dialog (that is, this page).<br>
  The “?” button at the top right of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button at the top right of the dialog does the same thing.
