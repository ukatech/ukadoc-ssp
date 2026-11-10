# Settings: Display

This page explains the “Display” page of the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

Use this page to configure display settings.

## Item descriptions

- **Do not change the cursor (takes effect from the next ghost load)**<br>
  When ON, the mouse cursor will not change, even with balloons that include a mouse cursor.<br>
  Turn this ON if you do not want balloons to change the mouse cursor.
- **Desktop bottom offset (normally, 0 is fine)**<br>
  Specify how many pixels to offset from the bottom of the desktop.<br>
  For example, you can use this setting to prevent the taskbar from being covered when “Automatically hide the taskbar” is enabled.
- **Match menu width to background image**<br>
  Normally, the menu is only as wide as its menu items. This setting matches its width to that of the menu image included with the ghost.<br>
  This makes the entire ghost menu image visible.
- **Show preview images when selecting menu items**<br>
  When you select an item in the right-click menu, such as Change ghost, call, Change shell, or Change balloon, a preview image (thumbnail.png) is shown if one is available.<br>
  In the \[—\] state, previews are shown only in menus. In the \[✓\] state, previews are also shown when you hover over items in Explorer.
- **Menu vertical spacing (default: 2)**<br>
  Set the spacing between rows in the right-click menu.<br>
  The default spacing of 2 matches Windows menus, but you can change it as needed to make the menu easier to read.
- **Group some menus into submenus**<br>
  If you have configured multiple folders to load in [Settings: Folders](folder.md), turn this ON to group menu items by folder.<br>
  This applies to all menus for which you can configure folders, including ghosts and balloons.<br>
  This is useful if you have installed many ghosts and want to organize how they are displayed.
- **Maximum number of characters in ghost and balloon menus (5–255)**<br>
  This setting can help if long names cause the menu to fill the screen. Names that exceed the number of characters specified here are truncated with "..." at the end.<br>
  If your screen is small, set a lower limit.
- **Maximum number of entries in the Recently Used menu (2–255)**<br>
  The number of items to keep in the “Recently Used” history. Items launched or used before this number of most recent entries are removed.
- **Show even during Flip3D (Vista or later)**<br>
  Keep the character and balloon visible while switching windows with Flip3D. Use this if you want the character to stay visible at all times.
- **Show character windows in the taskbar**<br>
  Normally, windows displaying characters do not appear in the taskbar. However, you may want them to appear to use jump lists or previews in Windows 7 or later.<br>
  Enable this option to use those features.
- **Minimize when a full-screen app starts**<br>
  Automatically minimize the ghost when you start an application that displays in full screen, such as a game.
- **Show character windows on all virtual desktops (Windows 10 or later)**<br>
  Show character windows on all virtual desktops, regardless of which virtual desktop is currently selected. This feature is available in Windows 10 or later.
- **Bring other windows to the front when you click a character**<br>
  Windows that are not associated with a specific character display, such as Explorer and log windows, will also be brought to the front when clicked.<br>
  Windows can easily end up behind others and become hard to find, so this is normally best left ON.
- **High-DPI support \[SSP must be restarted\]**<br>
  Improves SSP display in high-DPI environments. You must restart SSP after changing this setting.
- **Automatically move off-screen windows onto the screen**<br>
  When the monitor resolution changes, a monitor is turned off, or the monitor configuration differs from the previous launch, the shell is automatically moved into the usable area of a monitor.<br>
  Turning this setting off may resolve some issues in multi-monitor environments, but you will need to manually reset the position if the window moves off-screen.

### Translucent windows

This setting enables the feature for creating translucent windows, also known as “Layered Window,” which was introduced in Windows 2000.<br>
It is enabled by default when available.

- **Use cross-fading**<br>
  Use fade-in and fade-out effects to gradually transition between character expressions or when showing or hiding balloons and other elements.
- **Increase transparency while dragging**<br>
  Make the character window more transparent while you drag it, so you can see what is underneath.
- **(Transparency settings for the main window/balloons/Calendar)**<br>
  Adjust the transparency of each window by moving its slider.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the current page of the Preferences dialog (that is, this page).<br>
  The “?” button in the upper-right corner of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button in the upper-right corner of the dialog does the same thing.
