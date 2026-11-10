# Explorer: Right-click/function menu

This page explains the menu displayed when you right-click an item selected in Explorer, or open the 「Functions」 menu while an item is selected.

The menu items are as follows. (**Default** items are run when you double-click the item. The button at the bottom right of Explorer has the same effect.)

## Common items

- **Delete**<br>
  Uninstalls the selected item.
- **Open folder**<br>
  Opens the folder containing the selected item's files in Windows Explorer.
- **Move folder (group)\[All except shells\]**<br>
  Moves the selected item to another [load folder (group)](../../config/folder.md).<br>
  Note that you cannot do this for an item that is currently running.<br>
  This item cannot be selected if there is only one folder.
- **Open distribution URL**<br>
  Opens the website where the selected item is distributed.<br>
  Nothing happens if the information cannot be found.
- **Open README**<br>
  Opens the selected item's README file.<br>
  Nothing happens if the README file cannot be found.
- **Network update**<br>
  For ghosts, performs only a network update without launching the ghost.<br>
  For other items, this menu is normally used to perform a network update.
- **Create update files**<br>
  Creates updates2.dau/updates.txt files for network updates.<br>
  ※To ensure compatibility, the same files are also created under ghost/master, in addition to the ghost's root folder.
- **Create NAR**<br>
  Packages the selected item into a single file for distribution online.
- **Create update files and NAR**<br>
  Creates update files and a NAR in one operation.

## Ghost items

- **Change: Default**<br>
  Switches from the current ghost to another one.
- **Call ghost**<br>
  Launches another ghost while leaving the current ghost as it is.
- **Create startup shortcut**<br>
  Creates a desktop shortcut to launch SSP with the selected ghost.
- **Set as default ghost**<br>
  Sets the currently selected ghost as the one to launch by default, such as when restarting after an error.<br>
  The icon to the left of the configured ghost in the list changes to 【![Default mark](../../assets/screenshots/functions/explorer/menu/5.png)】.
- **Set as preferred speaking ghost**<br>
  Sets the currently selected ghost as the one to speak by preference for SSTP and similar requests that do not specify a speaking ghost.<br>
  The icon to the left of the configured ghost in the list changes to 【![Preferred speaking mark](../../assets/screenshots/functions/explorer/menu/6.png)】.<br>
  ※If the same ghost is set as both the default ghost and the preferred speaking ghost, the icon appears as 【![Default and preferred speaking marks](../../assets/screenshots/functions/explorer/menu/7.png)】.
- **Bulk update using RSS update information**<br>
  Automatically retrieves the latest update information and runs a network update for all characters that have updates.

## Balloon items

- **Change: Default**<br>
  Switches the current balloon to another one.
- **Set as default balloon**<br>
  Sets the balloon to use by default when a ghost does not specify a balloon to use, or when the specified balloon is unavailable.<br>
  The icon to the left of the configured balloon in the list changes to 【![Default mark](../../assets/screenshots/functions/explorer/menu/5.png)】.

## Shell items

- **Change: Default**<br>
  Switches the current shell to another one.

## Headline items

- **Read aloud: Default**<br>
  Starts the headline service and reads the headlines aloud.
- **Open webpage**<br>
  Opens the site that provides the RSS/headline feed in a browser.

## Plugin items

- **Settings/Run: Default**<br>
  Opens the plugin's settings or runs it. The exact behavior depends on the plugin.
- **Enable/Disable**<br>
  Enables or disables the plugin.<br>
  When disabled, the plugin is recognized but not loaded.
