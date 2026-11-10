# Settings: Talk/Balloons

This page explains the “Talk/Balloons” page in the dialog opened by selecting “Preferences” from the “Settings” submenu of the right-click menu.

On this page, you can configure ghost talk timing and balloon controls.

## Item descriptions

- **Message speed**<br>
  Sets the speed at which talk and other text is displayed. This sets the delay between displaying each character.<br>
  Ghosts usually control their own delays, so not all ghosts will talk at the same speed.
- **Talk timeout (default = 15 seconds)**<br>
  Sets how long to wait before automatically closing the balloon when displaying regular talk.
- **Choice timeout (default = 30 seconds)**<br>
  Sets how long to wait before automatically closing the balloon when displaying choices.
- **Click-wait timeout (default = Never)**<br>
  Sets how long to wait before continuing without waiting for a click.
- **Always run headline readouts without delays**<br>
  Headline sensor readouts are long, so enabling this option forces them to run in fast-forward mode.<br>
  We recommend enabling this option unless you encounter a problem.
- **Do not time out balloons displaying headlines**<br>
  Balloons used to display the headline/RSS feature will not time out.<br>
  However, they may still be interrupted by ghost functions.
- **Always show the balloon while online**<br>
  While online, the main balloon is always displayed so you can use break controls and check your online status.<br>
  We recommend enabling this option unless you encounter a problem.
- **Do not time out while the cursor is over the balloon**<br>
  When the mouse cursor is inside the balloon, such as while interacting with it, this disables automatically hiding the balloon after a set time.<br>
  However, this option may be ignored if the ghost has intentionally set a time limit.
- **Enable the fast-forward key**<br>
  Enable this option and choose a key to fast-forward script playback (ignore delays) while you hold down that key.

### Choose a sound to play when talking

Plays a sound when something is displayed in a balloon.<br>
If you don't want to miss any talk, you can specify an audio file to play.

### Balloon controls

You can customize how to control the balloon with the mouse.<br>
The traditional behavior is to break the script with a left double-click and switch the balloon's side with a right-click.

- **Do nothing**<br>
  Does nothing.
- **Same as left-click**<br>
  Treats this the same as a single left-click.
- **Break script**<br>
  Stops displaying the script and closes the balloon.<br>
  However, the balloon may not close in some cases, such as while choices are displayed.
- **Switch balloon side**<br>
  Switches the balloon's direction between left and right.<br>
  The balloon will also automatically switch sides if it is about to go off the edge of the screen.
- **Adjust balloon position**<br>
  Enters balloon position adjustment mode.<br>
  The balloon follows the cursor until you left-click the balloon.<br>
  This works like dragging a regular balloon, but can be used in environments where dragging does not work well.
- **Show menu**<br>
  Displays a menu each time so you can choose what to do.

### Legacy support - usually does not need to be configured

These settings are needed when using older ghosts.

- **Talk frequency**<br>
  Adjusts how often the ghost talks spontaneously.<br>
  This is disabled for many ghosts because they manage their own talk timing.
- **Talk about news**<br>
  Sets whether to use the news feature, which reads out the latest information and other items in sequence.<br>
  Normally, you can leave this enabled.<br>
  This is a legacy feature and is no longer supported.

## Buttons at the bottom

- **Help**<br>
  Opens help for the page currently being configured in the Preferences dialog (that is, this page).<br>
  The “?” button at the top right of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button at the top right of the dialog does the same thing.
