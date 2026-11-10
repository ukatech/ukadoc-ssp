# Explorer

This dialog window lists ghosts and other items currently recognized by SSP, and lets you perform operations such as switching between them.<br>
It is useful in a variety of situations, such as when you have many ghosts and it is cumbersome to select one from the Change ghost menu, or when you want to move a selected item between [configured folders](../../config/folder.md).

You can also configure SSP to open Explorer every time it starts, so you can select a ghost to launch, from 「[Ghost (1)](../../config/ghost.md)」 in Preferences.

## Basic operations

When you first open Explorer, it displays a list of the currently loaded ghosts.<br>
Use the 「[Type](#種類)」 menu at the top to switch to lists of other items, such as balloons or shells.

The item highlighted in blue in the list is selected. Click an item to select it.<br>
As in Windows Explorer, you can select multiple items by holding down the Ctrl key while clicking them, or select a range by holding down the Shift key. However, only a limited set of operations are available when multiple items are selected.<br>
The selected items are the targets of the button at the bottom right of Explorer (「Change」 when the type is Ghost), and you can also perform various operations from the [function menu (right-click menu)](menu.md) at the top of Explorer.<br>
For items that you switch to and use, such as ghosts, the item currently in use is selected by default.

Double-clicking an item selects it and performs the same operation as pressing the button at the bottom right.

Click a list column heading (such as Name, Author, Path, or Group) to sort the list in ascending or descending order by that column.<br>
An ▲ mark next to a heading indicates ascending order, and a ▼ mark indicates descending order.<br>
This is useful, for example, when sorting by group if you have [configured folders](../../config/folder.md), or when looking for ghosts by a particular author.

For operations available from the right-click/function menu, see the 「[Right-click/function menu](menu.md)」 page.

!!! tip "ヒント"

    Items organized into [folders](../../config/folder.md) also have different-colored icons on the left.<br>
    ![Icon colors for folder organization](../../assets/screenshots/functions/explorer/2.png)

## Menus at the top

### File

- **Reload**<br>
  Checks the folders where ghosts, balloons, and other items are installed, and reflects any new or deleted ghosts.<br>
  You normally do not need to use this, but it can be useful after manually changing files.
- **Close**<br>
  Closes Explorer (the same as the × button at the top right).

### Edit

- **Copy**<br>
  Copies information about the selected item.<br>
  For ghosts, the clipboard receives the ghost name, `\0` name, `\1` name, author name, and distribution URL, separated by spaces.<br>
  For other items, it receives the item name, author name, and distribution URL, separated by spaces.
- **Select all**<br>
  Selects every item in the list.<br>
  Use this when you want to perform an operation on all items at once, such as running a network update for them.<br>
  Note that operating on all items at once can take a long time, depending on the number of items and the operation.
- **Search**<br>
  Searches all items in the list for the entered word and selects the first matching item.<br>
  Author names and other information are also searched.<br>
  Use this when you have many installed items and it is cumbersome to find one with a particular name.
- **Find next**<br>
  Selects the next item matching the current search word.<br>
  Each time you run the search, it moves to the next match; after the last match, it starts again from the first.

### Type

Switches to a list of the selected type.<br>
Only the shells belonging to the ghost from which you opened Explorer are displayed (the ghost name appears at the top of the Explorer window frame in the form 「Explorer - ○○」).

### Functions

The image shows the menu when the type is 「Ghost」.

Performs various operations on the selected item.<br>
The same menu is displayed when you right-click in the list.<br>
For details, see the 「[Right-click/function menu](menu.md)」 page.

### Settings

- **Do not close automatically**<br>
  When enabled, Explorer does not close automatically after you run (switch to) an item selected in Explorer.

## Buttons at the bottom

Each button is available when a list of the type shown in its \[\] brackets is displayed.

- **Close\[All\]**<br>
  Closes Explorer (the same as the × button at the top right).
- **Change\[Ghost/Shell/Balloon\]**<br>
  Switches the ghost, balloon, or shell in use to the selected one.
- **Read aloud\[Headline\]**<br>
  Starts reading aloud the [headline](../../howto/headline.md) from the selected website.
- **Settings/Run\[Plugin\]**<br>
  Launches the [plugin](../../howto/plugin.md), or opens its settings menu.<br>
  The behavior depends on the plugin.
