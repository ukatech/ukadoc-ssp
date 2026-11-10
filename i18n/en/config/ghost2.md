# Settings: Ghost (2)

This page explains the “Ghost (2)” page of the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

This page lets you configure the default settings for individual ghosts.

These settings are the defaults for [Ghost preferences](eachghost.md).

## Description of each setting

- **Mute sounds**<br>
  Stops all sound features controlled by SSP, so no sound will play.<br>
  This does not apply if a ghost plays sounds on its own, without relying on SSP.
- **Always on top**<br>
  Always displays the ghost in front of everything else on the desktop, whether or not it is speaking.
- **Ignore SERIKO Move (turn on for low-powered machines) \[shell-specific\]**<br>
  Forces features that keep a ghost in constant motion, such as floating, to turn off.<br>
  Turning this on can reduce the load if window movement is putting a heavy load on your machine.
- **Enable balloon position adjustment**<br>
  Sets whether you can adjust the balloon’s position by **dragging** it.<br>
  Turn this off if you don’t want position adjustment to work.

### Development options

!!! tip "ヒント"

    This item is displayed only when [development options are turned on](ippan.md).

- **Ignore undefined surfaces \[shell-specific\]**<br>
  Ignores miscellaneous image files, such as animation images, that are not defined as character expressions. It is usually fine to leave this off.<br>
  Turning it on can cause problems, especially with older ghosts.
- **Show hidden elements**<br>
  Displays all items that are set to “not displayed in a way that users can interact with,” for spoiler prevention or internal use.<br>
  The change may not take effect until you reload the ghost.<br>
  We recommend using this for debugging only.

### Shell scaling \[shell-specific\]

These settings are related to the character display scale.

- **Scale balloon along with character**<br>
  Scales the balloon along with the character using the same scale.
- **Smoothing when scaling (slower)**<br>
  Sets whether to smooth the image so it looks better when scaling it up or down.<br>
  When turned on, it looks better, but performance may be slower.
- **Balloon smoothing (slightly slower)**<br>
  Sets whether to smooth the balloon so it looks better when scaling it up or down.<br>
  When turned on, performance may be slower. When turned off, the text may be harder to read.
- **Common shell scaling settings...**<br>
  Sets the scaling for all characters. The value set here becomes the default, and you can then set a different value for each character.
- **Common balloon scaling settings...**<br>
  Sets the scaling for all balloons. The value set here becomes the default, and you can then set a different value for each balloon.

### Free character movement \[shell-specific\]

Sets whether you can move the character freely by **dragging** it.

- **Always allow free movement**<br>
  Always lets you move the character freely.
- **Use ghost setting**<br>
  Uses the setting specified by the ghost.
- **Always restrict movement**<br>
  Keeps the character anchored to the bottom of the screen.

### Bring to front when speaking

Sets whether the ghost comes to the front when it is behind other windows and starts speaking.

- **Bring to front**<br>
  Brings the ghost to the front.
- **Except during updates**<br>
  Brings the ghost to the front, except when it speaks during an update.
- **Do not bring to front**<br>
  Does not bring the ghost to the front (that is, it does not “bring it to the front”).
- **Move behind other windows after speaking**<br>
  When checked, moves the ghost behind other windows after it finishes speaking.

### Reset settings for all ghosts to default

When run, this resets all [individual ghost settings](eachghost.md) to the current SSP settings.

<strong>\[shell-specific\] = shell-specific setting</strong>

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the current page in Preferences (that is, this page).<br>
  The “?” button in the upper-right corner of the dialog does the same.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button in the upper-right corner of the dialog does the same.
