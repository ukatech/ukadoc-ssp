# Settings: Streaming

This page explains the “Streaming” page of the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

Configure these settings when using a ghost as an auxiliary tool for streaming video or similar purposes. Set them up when using capture or audio-linked features in streaming software.

## Item descriptions

- **Make the character easier to capture with streaming tools**<br>
  Makes the ghost’s character window easier to capture with streaming tools such as OBS.<br>
  Changes how the window is displayed so that streaming software can recognize it more easily when using window capture.
- **Make the balloon easier to capture with streaming tools**<br>
  Makes the ghost’s balloon (the speech bubble) easier to capture with streaming tools.<br>
  Turn this ON if you want to include the balloon in your stream.
- **Automatically animate mouth when audio is detected**<br>
  Detects audio input from a microphone and makes the ghost automatically animate its mouth.<br>
  The character’s mouth will move in sync with audio during streaming, allowing for more natural expressions.
- **Audio input selection**<br>
  Select the audio input device (microphone) to use for the mouth animation feature.<br>
  Choose the microphone to use from the list of audio input devices available on your system.
- **Audio level**<br>
  Adjust the sensitivity of the mouth animation feature.<br>
  Adjust the sensitivity as needed while checking the current input volume on the audio level bar.<br>
  If the sensitivity is too high, the mouth will animate in response to ambient noise; if it is too low, it will not respond to your voice.
- **Display the ghost inside a single window**<br>
  Instead of placing the ghost directly on the desktop, display it inside a single window (Window mode).<br>
  This lets you capture the entire window and avoids affecting the rest of the desktop.<br>
  ⇒See the “[Window mode](../functions/windowmode.md)” page for details.
- **One window for all ghosts / one window per ghost**<br>
  Choose how windows are arranged.<br>
  “One window for all ghosts” displays all running ghosts together in a single window (default).<br>
  “One window per ghost” creates a separate window for each ghost.

!!! tip "ヒント"

    You can also switch Window mode from “Settings” in the [right-click menu](../howto/rclick.md) or from the window’s own “Actions” menu.<br>
    You cannot switch modes while a ghost is loading, and the check mark will revert to its previous state.

## Notes

!!! tip "ヒント"

    Enabling settings for streaming tools may change how windows behave during normal use.<br>
    We recommend turning these settings OFF when you are not streaming.

!!! tip "ヒント"

    When using audio detection, be aware of possible conflicts between the microphone you are using and other applications.<br>
    Simultaneous use with some streaming or audio software may cause problems accessing the audio device.

!!! tip "ヒント"

    In OBS Studio, select “Windows 10 (1903 and up)” for “Capture Method” under “Window Capture.”<br>
    Other capture methods will not capture correctly.<br>
    You can capture the window by itself, so no special plugin is required.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the page currently being configured in the Preferences dialog (that is, this page).<br>
  The “?” mark in the upper-right corner of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” mark in the upper-right corner of the dialog does the same thing.
