# Window mode

This mode displays ghosts inside a single window instead of placing them directly on the desktop.<br>
The inside of the window behaves like a small desktop, and ghosts live only within it.

This is useful when you want to capture the entire window with streaming software or use the desktop for other tasks.<br>
Ghosts will no longer appear in front of other apps or affect the entire desktop.

!!! tip "ヒント"

    Window mode is an experimental feature. Its usability and specifications may change in the future.

!!! tip "ヒント"

    Due to operating system limitations, this feature is unavailable on Windows 7 and earlier. Please use Windows 8 or later.

## Two display modes

- **All ghosts in one window**<br>
  Displays all running ghosts together in a single window (the default).<br>
  You can use it much like a smaller version of your desktop.
- **One window per ghost**<br>
  Provides one window for each ghost.<br>
  You can place ghosts in different locations or capture just one ghost.

## Switching to Window mode

You can switch modes using any of the following methods. The setting is the same whichever method you use, and they always stay in sync.

- **[Right-click menu](../howto/rclick.md) → “Settings”**<br>
  Choose from “Window mode - Off,” “Window mode - All ghosts,” and “Window mode - One per ghost.” The current mode is checked.<br>
  ⇒ See also the “[Settings](../config/index.md)” page.
- **“[Streaming](../config/streamingtool.md)” in Preferences**<br>
  Turn on “Display ghosts in one window,” then choose either “All ghosts in one window” or “One window per ghost.”
- **The window’s “Actions” menu**<br>
  You can also switch between the same three options from the Window mode window itself. Select “Off” to return to the normal desktop display.

Your selection is saved and will be retained the next time you start SSP.<br>
You can also start SSP with the `--windowmode` startup option. ⇒ See the “[List of startup options](option.md)” page.

!!! tip "ヒント"

    You cannot switch modes while a ghost is loading. In this case, the menu and check mark will revert to their previous state, so please try again once loading is complete.<br>
    When switching modes, the ghost’s position is kept at approximately the same proportion of the screen. Even if the available display area changes, the ghost will not end up somewhere unexpected.

## Opening the “Actions” menu

All operations on the window itself are grouped in the “Actions” menu. You can open it using any of the following methods.

- **Right-click inside the window**<br>
  Right-click an area without a ghost or balloon to open the menu. This works whether or not the window frame is shown.
- **The title bar menu**<br>
  When the window frame is shown, right-click the title bar (or click the icon in the upper-left corner) to open a menu containing “Actions.”
- **The `≡` button in the upper-left corner**<br>
  When the window frame is hidden or the window is in full-screen mode, move the mouse over the window to show a `≡` button in the upper-left corner. Click it to open the “Actions” menu.<br>
  A `×` button also appears in the upper-right corner, which you can click to close the window.

## “Actions” menu options

- **Window mode - Off / All ghosts / One per ghost**<br>
  Switches the display mode (as described above).
- **Full screen\[F11\]**<br>
  Expands the window to fill the monitor and hides its frame. Only the ghosts will occupy the screen.<br>
  Press the ESC key or F11 again to restore the previous size. You cannot move the window while it is in full-screen mode.
- **Show window frame**<br>
  Toggles the title bar and window frame (shown by default).<br>
  Hiding the frame gives the window a cleaner appearance and keeps it out of captures. You can still resize a frameless window by dragging its edge. Drag a corner to resize it diagonally.<br>
  When you move the mouse over an edge, a thin line marks the area you can grab. You can also drag an empty area of the window to move it.
- **Integrate backlog/speech history too**<br>
  Displays the backlog (speech history) window inside this window (on by default). ⇒ See “[Integrating the backlog](#バックログの統合)” below.
- **Background - White / Gray / Black / Desktop / Image...**<br>
  Changes the window background (“Desktop” by default).<br>
  “Desktop” reproduces your current desktop wallpaper, including its display method (centered, tiled, scaled to fit the screen, and so on). It updates when you change your wallpaper.<br>
  White, gray, and black are solid colors. Use them when you want to remove the background for streaming or check how a ghost looks.<br>
  Select “Image...” to open a file selection dialog and set any image as the background. The image is enlarged to fill the window while preserving its aspect ratio, and any parts that extend beyond the window are cropped.
- **Screenshot...**<br>
  Saves the contents of the window as a PNG image. In the save dialog, you can choose one of the following two options.<br>
  **PNG** … Saves the view as it appears, including the background.<br>
  **PNG - Transparent background** … Saves only the ghosts and balloons, with a transparent background.<br>
  A file name in the form `ssp_日付_時刻.png` is provided in advance. Buttons that appear when you move the mouse over the window, and lines around its edges, are not captured.
- **Close\[Ctrl+W\]**<br>
  Closes the window. In “One window per ghost” mode, the ghost in that window will exit.

!!! tip "ヒント"

    Appearance settings such as the frame, background, and full-screen mode are remembered separately for each window. In “One window per ghost” mode, you can also set a different background for each ghost.

!!! tip "ヒント"

    **Recommended settings for use with a hologram device** are “Background - Black,” “Show window frame” turned off, and “Integrate backlog/speech history too” turned on.<br>
    A hologram device is a display that makes characters appear to float in the air. Many such devices project an image from a computer screen, and black areas on those devices do not light up, so they appear transparent.<br>
    Therefore, setting the background to black and hiding the frame and other windows makes it look as if only the ghosts and balloons are floating in the air.<br>
    If you want to make the image fill the device’s display area, you can also switch to full-screen mode (F11).

## Integrating the backlog

When “Integrate backlog/speech history too” is on, the backlog window fits inside this window. It will not appear as a separate window on the desktop, so you can capture it as part of the window.

While integrated, the backlog looks like a frameless panel. Move it close to the edge of the window and it will snap neatly into place.<br>
The text size changes to match the zoom level of that ghost’s balloon, so the text in the balloon and speech history stays the same size.<br>
The background color changes to match the window’s background setting. If the background is an image, the color used most often in that image (the dominant color) is used.

!!! tip "ヒント"

    When this setting is off, the backlog opens as a separate window on the desktop, as before.<br>
    This setting applies to all of SSP rather than to individual windows, and it is retained when you switch display modes.

## Taskbar and minimizing

In Window mode, only this window appears on the taskbar. Ghosts and balloons do not appear there individually.<br>
Minimizing the window also hides the ghosts, and restoring it brings them back. Conversely, minimizing all ghosts minimizes the window as well.

## Keyboard shortcuts

The following keys work when the window is in the foreground.

| Key | Function |
|---|---|
| F11 | Toggle full-screen mode |
| ESC | Exit full-screen mode (only while in full-screen mode) |
| Ctrl+W | Close the window |
