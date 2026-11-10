# Settings: Ghost preferences

!!! tip "ヒント"

    The default settings for the options available here are configured in “[Ghost (2)](ghost2.md)” under Preferences. Ghost preferences take precedence over Preferences.

## Item descriptions

Checkboxes shown as partially checked (■) are unset (= use the default settings).

- **Mute sounds**<br>
  Stop all sounds controlled through SSP so that no sound is played.<br>
  Note, however, that some ghosts can play sounds on their own, without using SSP, and those sounds cannot be controlled here.
- **Always keep in front**<br>
  Always keep the character at the front of the desktop, whether or not it is speaking.
- **Ignore SERIKO Move (turn ON on low-powered machines)**<br>
  Force features that keep the ghost moving, such as floating effects, to turn OFF.<br>
  This can reduce the load if window movement is placing a significant load on your system.
- **Enable balloon position correction**<br>
  Set whether to correct the balloon position when you **drag** it.<br>
  Disable this if you do not want the correction feature to operate.

### Developer options

!!! tip "ヒント"

    This item is shown only when [developer options are enabled](ippan.md).

- **Ignore undefined surfaces**<br>
  Ignore miscellaneous image files, such as those used for animation, that are not defined as ghost expressions. Normally, you can leave this OFF.<br>
  Enabling this can cause problems, especially with older ghosts.
- **Show hidden elements**<br>
  Show all items that are set to “not displayed in a way that users can interact with,” for spoiler prevention or internal use.<br>
  The change may not take effect until you reload the ghost.<br>
  We recommend using this for debugging only.

### Shell scale

Settings related to the character display scale.

- **Scale balloons too**<br>
  Scale balloons in conjunction with the character.
- **Interpolation when scaling (slow)**<br>
  Set whether to use interpolation to improve the appearance when scaling up or down.<br>
  When ON, this makes scaling relatively slow, but improves the appearance.
- **Balloon interpolation (somewhat slow)**<br>
  Set whether to use interpolation to improve the appearance when scaling balloons up or down.<br>
  When ON, this makes scaling relatively slow, but turning it OFF may make text difficult to read.

### Free character movement

Set whether the character can be moved freely by **dragging** it.

- **Always allow free movement**<br>
  Always allow free movement.
- **Use ghost settings**<br>
  Follow the settings configured by the ghost.
- **Always restrict movement**<br>
  Make the character snap to the bottom of the screen.

### Bring to front when speaking

Set whether the character comes to the front when speaking while behind other windows.

- **Bring to front**<br>
  Bring the character to the front.
- **Except during updates**<br>
  Bring the character to the front, except when speaking during an update.
- **Do not bring to front**<br>
  Do not bring the character to the front (that is, do not make it come to the front).
- **Move behind other windows when finished speaking**<br>
  When checked, the character moves behind other windows after it finishes speaking.

## Buttons at the bottom

- **Default settings**<br>
  Opens the “[Ghost (2)](ghost2.md)” page of the Preferences dialog.<br>
  The settings on the Ghost (2) page are the defaults for ghost-specific settings (used when no setting is specified).
- **Reset(&R)**<br>
  Reset all settings to their defaults.<br>
  You can configure the default settings in “[Ghost (2)](ghost2.md)” under Preferences.
- **Apply(&A)**<br>
  Save the current settings.
- **OK**<br>
  Save the current settings and close the dialog.
