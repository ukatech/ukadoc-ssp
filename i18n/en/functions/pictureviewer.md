# Picture viewer

A viewer window for displaying image files and performing simple operations such as zooming, rotating, and cropping, as well as saving and copying images in different formats.<br>
You can check many of the image formats supported by SSP right away, and browse multiple images by opening them in tabs and switching between them.

It’s useful for checking or converting small images, such as shell or balloon assets and photos you’ve taken.

## Supported image formats

The main supported image formats are listed below.<br>
In the “Support” column, **SSP-wide** means formats that SSP itself can load by default (and that can also be used for shells, balloons, and other assets). **Viewer only** means formats that can only be displayed in this picture viewer (via OS WIC codecs).

| Format | Extension | Support | Notes |
|---|---|---|---|
| PNG / APNG | .png / .apng | SSP-wide | Supports alpha (transparency). Can also use an external alpha channel from a .pna file with the same name. Supports APNG (animated PNG) as well. |
| WebP | .webp | SSP-wide | Supports animation and transparency. |
| GIF | .gif | SSP-wide | Supports animation and transparency. |
| MAG | .mag | SSP-wide | Retro format (MAKICHAN GRAPHICS, from the PC-9801 era). |
| Pi | .pi | SSP-wide | Retro format (Pi format from the PC-9801 era). |
| JPEG | .jpg / .jpeg | SSP-wide | Automatically applies EXIF Orientation (the orientation information recorded when the photo was taken). |
| BMP | .bmp | SSP-wide | Windows bitmap. |
| TIFF | .tif / .tiff | SSP-wide | Supports multiple pages (switch between them with Previous page / Next page). |
| X BitMap / X PixMap | .xbm / .xpm | SSP-wide | Text-based image formats for the X Window System. |
| TGA | .tga | SSP-wide | Truevision Targa. Supports transparency. |
| Netpbm (Portable anymap) | .pbm / .pgm / .ppm / .pam / .pnm / .pfm | SSP-wide | Portable bitmap / graymap / pixmap formats. .pfm is a floating-point (HDR) format. |
| PCX | .pcx | SSP-wide | ZSoft Paintbrush. |
| QOI | .qoi | SSP-wide | Quite OK Image Format. |
| ICO | .ico | SSP-wide | Windows icon format. |
| DLL/EXE | .dll / .exe | SSP-wide | Lists the icons stored in DLL and EXE files and displays them one page at a time. |
| PSD | .psd | SSP-wide | Adobe Photoshop. You can load individual layers as well as the merged image. |
| PSP | .psp / .pspimage | SSP-wide | Paint Shop Pro. Version 4.0 and later. You can load individual layers as well as the merged image. |
| OpenRaster | .ora | SSP-wide | You can load individual layers as well as the merged image. |
| Krita | .kra | SSP-wide | You can load individual layers as well as the merged image. |
| CLIP STUDIO | .clip | SSP-wide | You can load individual layers as well as the merged image. |
| GIMP | .xcf | SSP-wide | You can load individual layers. The merged image cannot be loaded (this is not a problem in the viewer, because it composites and displays the individual layers). |
| HEIF / HEIC | .heif / .heic | Viewer only | Requires the OS “[HEIF Image Extensions](https://apps.microsoft.com/detail/9pmmsr1cgpwg)”. |
| AVIF | .avif | Viewer only | Requires the OS “[AV1 Video Extension](https://apps.microsoft.com/detail/9mvzqvxjbq9v)”. |
| JPEG XR | .jxr / .wdp / .hdp | Viewer only | HD Photo. |
| DDS | .dds | Viewer only | DirectDraw Surface. Displays only the first frame. |
| Camera RAW | .cr2 / .nef / .arw, etc. | Viewer only | RAW formats from various manufacturers. Depends on the OS “[Raw Image Extension](https://apps.microsoft.com/detail/9nctdw2w1bh8)”. |

!!! tip "ヒント"

    “Viewer only” formats depend on codecs (image extensions) installed in the OS. The table above shows common examples, and some formats may not be readable in certain environments.<br>
    Also, the “Viewer only” path does not support animation or multiple pages, and always displays only the first frame.

## How to open

You can open the picture viewer in any of the following ways.

- **[Right-click menu](../howto/rclick.md) → “Functions” → “Picture viewer”**<br>
  Opens the viewer with no image loaded.<br>
  ⇒ See the “[Functions](index.md)” page as well.
- **Drag and drop an image file onto a ghost**<br>
  When you drop an image file onto a ghost, it opens automatically in this viewer if the ghost does not respond to the file.<br>
  The viewer will not start if the file cannot be loaded as an image.

After opening the viewer, you can add more images as tabs by selecting “Open image,” pasting from the clipboard, or dragging and dropping images into the viewer.

## Window layout

- **Menu bar**<br>
  You can perform all operations from the “File,” “Edit,” and “View” menus (details below).
- **Toolbar**<br>
  Displays buttons for commonly used operations. Each button corresponds to a menu item; hover over a button to see its function name (tooltip).<br>
  When Crop or Make top-left color transparent is on, its button appears pressed. The background toggle button’s icon changes each time you click it to show the current background (checkerboard / white / black).
- **Tabs**<br>
  Each open image has its own tab. Click a tab to switch the displayed image.
- **Image display area**<br>
  The area where the image is displayed. Scroll bars appear if the image is larger than the area.
- **Status bar**<br>
  The bottom of the window displays the current image’s “dimensions (width × height),” “zoom level,” “rotation angle (with `<| />` shown when flipped horizontally),” and “format.”<br>
  For formats such as WebP, which can use different compression methods with the same extension, `(lossless)` or `(lossy)` is shown after the format name. If different frames in an animation use different methods, `(mixed)` is shown.<br>
  While cropping, the coordinates of the selected area are shown on the left.

## Top Menu

### File

- **Open image...\[Ctrl+O\]**<br>
  Opens the file selection dialog and opens the selected image in a new tab.
- **Reload\[Ctrl+R / F5\]**<br>
  Reloads the currently displayed image from disk.<br>
  Images opened from files are automatically reloaded when changes made externally are detected, but use this command when you want to reload manually.
- **Save as...\[Ctrl+S\]**<br>
  Saves the displayed image. You can choose PNG/BMP/JPEG/WebP (lossless or lossy) as the format.<br>
  If you have rotated, flipped, cropped, or resized the image, it is saved in its current displayed state (as it appears on screen).

### Edit

- **Copy\[Ctrl+C\]**<br>
  Copies the displayed image to the clipboard while preserving transparency.<br>
  If the image is rotated, flipped, or cropped, it is copied in its current displayed state.
- **Paste\[Ctrl+V\]**<br>
  Imports the image on the clipboard as a new tab.
- **Resize...**<br>
  Enter the width and height in the dialog to scale the image.<br>
  The original image is preserved, so specifying the original dimensions restores it (non-destructive).
- **Crop**<br>
  Turns crop mode on or off.<br>
  When enabled, drag on the image with the mouse to specify the area to crop. Only that area is included when you save or copy.

### View

- **Actual size\[Ctrl+0\]**<br>
  Resets the zoom level to 100% (actual size).
- **Zoom in\[Ctrl++\] / Zoom out\[Ctrl+-\]**<br>
  Zooms in or out by a factor of 1.25. The zoom level ranges from 5% to 1600%.
- **Fit to window**<br>
  Automatically adjusts the zoom level so the entire image fits in the window. The zoom level adjusts when you resize the window.
- **Set zoom level...**<br>
  Enter a zoom level (%) directly in the dialog.
- **Previous page\[PageUp\] / Next page\[PageDown\]**<br>
  Move to the previous or next frame (page) in a multipage TIFF or animated image.
- **Rotate left / Rotate right**<br>
  Rotates the display 90 degrees to the left or right. This only rotates the displayed image; the original image data is unchanged (the rotation is reflected when you save or copy).
- **Flip horizontally**<br>
  Flips the display horizontally (mirrors it). This is also a display-only operation; the original image data is unchanged.
- **Black background / White background / Checkerboard background**<br>
  Switches the background shown behind transparent areas (the default is a checkerboard). Use this to check how transparent areas look.<br>
  This setting is shared by all tabs and is retained the next time you start the program.
- **Make top-left color transparent**<br>
  Treats the color at the top-left of the image (coordinates 0,0) as transparent in the display only. This is useful for checking how images without a transparent background look when made transparent.<br>
  This setting is shared by all tabs and is retained the next time you start the program.

!!! tip "ヒント"

    "Make top-left color transparent" only works on images that do not already have transparency (alpha). For images that already have transparent areas, this setting is not applied even when enabled, to prevent unintended areas from disappearing.

## Mouse and Keyboard Controls

Scroll the mouse wheel to zoom in or out around the cursor position.<br>
You can close a tab by middle-clicking it or clicking the "×" button on the tab. You can also right-click a tab and select "Close".<br>
In crop mode, drag on the image to specify the area to crop.

The main keyboard shortcuts are as follows.

| Key | Function |
|---|---|
| Ctrl+O | Open image |
| Ctrl+R / F5 | Reload |
| Ctrl+S | Save as |
| Ctrl+C | Copy |
| Ctrl+V | Paste |
| Ctrl+0 | Actual size (100%) |
| Ctrl++ | Zoom in |
| Ctrl+- | Zoom out |
| PageUp | Previous page |
| PageDown | Next page |
| Ctrl+Tab | Switch to next tab |
| Ctrl+Shift+Tab | Switch to previous tab |

## Feature Details

### Zoom In and Out

The zoom level ranges from 5% to 1600%, and each zoom in or out changes it by a factor of 1.25.<br>
The mouse wheel zooms around the cursor position, so you can quickly zoom in on the area you want to see. Select "Fit to window" to automatically adjust the zoom so the entire image always fits in the window.

### Rotate and Flip Horizontally

You can rotate the image to the left or right (in 90-degree increments) and flip it horizontally. These are display-only operations and do not alter the original image data.

!!! tip "ヒント"

    If you select "Save as" or "Copy" while the image is rotated or flipped, it is output in the orientation shown on screen.<br>
    Note that changing pages or resizing the image clears the rotation, flip, and crop settings.

### Displaying the Background and Transparent Areas

You can choose a black, white, or checkerboard background to display behind transparent areas (the default is a checkerboard). The checkerboard uses a tiled pattern to make transparent areas easier to see.<br>
Combine this with "Make top-left color transparent" to check how images without a transparent color look when made transparent.

### Resize and Crop

With "Resize", you can scale the image by specifying its width and height. The original image is preserved, so you can restore its original dimensions.<br>
Turn "Crop" on and drag on the image to specify the area to crop. The specified area is included when you save or copy, and its coordinates are shown on the left side of the status bar. Cropping is set separately for each tab and does not alter the original image.

### Save and Copy

With “Save As,” you can choose PNG, BMP, JPEG, or WebP (lossless or lossy). Lossless WebP preserves the image quality, while lossy WebP can reduce the file size.<br>
The format initially selected in the save dialog matches the format of the original image. For WebP images, it also checks whether the original was saved losslessly or lossily.<br>
If the original is a JPEG and you have not resized or cropped it, it is saved without re-encoding. In this case, rotation and flipping are applied without degrading image quality (lossless rotation), and metadata such as EXIF is removed.<br>
“Copy” sends the image to the clipboard with its transparency preserved, so you can paste it with transparent areas intact into compatible applications.

### Automatic Reload

When an image opened from a file is updated by external software, the change is detected automatically and the display refreshes after about one second. This is useful when editing an image and checking it in the viewer.

### Multipage Images and Animation

You can switch between frames of multipage TIFFs and animated images such as GIF, APNG, and WebP using “Previous Page” and “Next Page” (they do not play automatically).<br>
You can also switch between PSD layers using “Previous Page” and “Next Page” to view each layer individually.
