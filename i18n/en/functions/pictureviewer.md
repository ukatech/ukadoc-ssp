# Picture viewer

This viewer window displays image files and lets you perform simple operations such as resizing, rotation, and cropping, as well as save or copy images in a different format.<br>
You can quickly view the many image formats supported by SSP and browse multiple images by switching between tabs.

It is useful for checking or converting images such as shell and balloon assets or photos you have taken.

## Supported image formats

The main supported image formats are listed below.<br>
Under "Support", **Throughout SSP** means formats SSP can load natively (and that can also be used for shell and balloon assets), while **Viewer only** means formats that can only be displayed in this Picture viewer (via the OS's WIC codecs).

| Format | Extension | Support | Notes |
|---|---|---|---|
| PNG / APNG | .png / .apng | Throughout SSP | Supports alpha transparency. Can also use external alpha from a .pna file with the same name. Also supports APNG (animated PNG). |
| WebP | .webp | Throughout SSP | Supports animation and transparency. |
| GIF | .gif | Throughout SSP | Supports animation and transparency. |
| MAG | .mag | Throughout SSP | Retro format (MAKICHAN GRAPHICS, from the PC-9801 era). |
| Pi | .pi | Throughout SSP | Retro format (Pi format from the PC-9801 era). |
| JPEG | .jpg / .jpeg | Throughout SSP | Automatically applies EXIF Orientation (orientation information recorded when the photo was taken). |
| BMP | .bmp | Throughout SSP | Windows bitmap. |
| TIFF | .tif / .tiff | Throughout SSP | Supports multiple pages (switch using Previous page / Next page). |
| X BitMap / X PixMap | .xbm / .xpm | Throughout SSP | Text-based image formats for the X Window System. |
| TGA | .tga | Throughout SSP | Truevision Targa. Supports transparency. |
| Netpbm (Portable anymap) | .pbm / .pgm / .ppm / .pam / .pnm / .pfm | Throughout SSP | Portable bitmap, graymap, and pixmap formats. .pfm is a floating-point (HDR) format. |
| PCX | .pcx | Throughout SSP | ZSoft Paintbrush. |
| QOI | .qoi | Throughout SSP | Quite OK Image Format. |
| ICO / CUR | .ico / .cur | Throughout SSP | Windows icon and cursor formats. Supports alpha transparency. If multiple sizes are included, the largest is used. |
| ANI | .ani | Throughout SSP | Windows animated cursor. Supports animation and transparency, and follows the playback order and frame delays. |
| DLL/EXE | .dll / .exe | Throughout SSP | Lists icons stored in DLL or EXE files and displays them one page at a time. |
| PSD | .psd | Throughout SSP | Adobe Photoshop. Can load individual layers as well as the merged image. |
| PSP | .psp / .pspimage | Throughout SSP | Paint Shop Pro. version 4.0 and later. Can load individual layers as well as the merged image. |
| OpenRaster | .ora | Throughout SSP | Can load individual layers as well as the merged image. |
| Krita | .kra | Throughout SSP | Can load individual layers as well as the merged image. |
| CLIP STUDIO | .clip | Throughout SSP | Can load individual layers as well as the merged image. |
| GIMP | .xcf | Throughout SSP | Can load individual layers, but not the merged image (the viewer composites the layers for display, so this is not a problem). |
| HEIF / HEIC | .heif / .heic | Viewer only | Requires the OS's [HEIF Image Extensions](https://apps.microsoft.com/detail/9pmmsr1cgpwg). |
| AVIF | .avif | Viewer only | Requires the OS's [AV1 Video Extension](https://apps.microsoft.com/detail/9mvzqvxjbq9v). |
| JPEG XR | .jxr / .wdp / .hdp | Viewer only | HD Photo. |
| DDS | .dds | Viewer only | DirectDraw Surface. Only the first frame is displayed. |
| Camera RAW | .cr2 / .nef / .arw and others | Viewer only | RAW formats from various manufacturers. Depends on the OS's [Raw Image Extension](https://apps.microsoft.com/detail/9nctdw2w1bh8). |

!!! tip "ヒント"

    "Viewer only" formats depend on the codecs (image extensions) installed in the OS. The table above lists common examples; some may not be readable depending on your environment.<br>
    The "Viewer only" route does not support animation or multiple pages, and always displays only the first frame.

## How to open

You can open the Picture viewer in either of the following ways.

- **[Right-click menu](../howto/rclick.md) → "Functions" → "Picture viewer"**<br>
  Opens the viewer with no image loaded.<br>
  ⇒ See also the [Functions](index.md) page.
- **Drag and drop an image file onto a ghost**<br>
  When you drop an image file onto a ghost, it automatically opens in this viewer if the ghost does not respond to the file.<br>
  The viewer will not open if the file cannot be loaded as an image.

After opening the viewer, you can add more images as tabs using "Open image", pasting from the clipboard, or dragging and dropping files into the viewer.

## Screen layout

- **Menu bar**<br>
  All operations are available from the "File", "Edit", and "View" menus (see below for details).
- **Toolbar**<br>
  This provides buttons for frequently used operations. Each button corresponds to a menu item, and its function name appears as a tooltip when you hover over it.<br>
  The crop and make top-left color transparent buttons appear pressed when enabled. Each time you press the background toggle button, its icon changes to show the current background (checkerboard / white / black).
- **Tabs**<br>
  A tab appears for each open image. Click a tab to switch the displayed image.
- **Image display area**<br>
  This is where the image is displayed. Scrollbars appear if the image is larger than the area.
- **Status bar**<br>
  At the bottom of the window, this shows the current image's "dimensions (width × height)", "zoom level", "rotation angle" (with `<| />` also shown when flipped horizontally), and "format".<br>
  For formats such as WebP, which use the same extension for different compression methods, `(lossless)` or `(lossy)` is shown after the format. If the method differs between frames in an animation, `(mixed)` is shown.<br>
  While cropping, the coordinates of the selected area are shown on the left.

## Top menu

### File

- **Open image...\[Ctrl+O\]**<br>
  Opens a file selection dialog and displays the selected image in a new tab.
- **Reload\[Ctrl+R / F5\]**<br>
  Reloads the currently displayed image from disk.<br>
  Images opened from files are automatically reloaded when external changes are detected, but you can use this to reload them manually.
- **Save as...\[Ctrl+S\]**<br>
  Saves the displayed image. You can choose PNG, BMP, JPEG, or WebP (lossless or lossy).<br>
  If you have rotated, flipped, cropped, or resized the image, it is saved as displayed.

### Edit

- **Copy\[Ctrl+C\]**<br>
  Copies the displayed image to the clipboard while preserving transparency.<br>
  If the image is rotated, flipped, or cropped, it is copied as displayed.
- **Paste\[Ctrl+V\]**<br>
  Imports the image on the clipboard into a new tab.
- **Resize...**<br>
  Scales the image to the width and height specified in a dialog.<br>
  The original image is preserved, and specifying its original dimensions restores it (non-destructive).
- **Crop**<br>
  Toggles cropping mode on or off.<br>
  When enabled, you can drag over the image to select an area to crop. Only that area is saved or copied.

### View

- **Actual size\[Ctrl+0\]**<br>
  Resets the zoom level to 100% (actual size).
- **Zoom in\[Ctrl++\] / Zoom out\[Ctrl+-\]**<br>
  Zooms in or out by a factor of 1.25. The zoom level ranges from 5% to 1600%.
- **Fit to window**<br>
  Automatically adjusts the zoom level so the entire image fits in the window. It adjusts when the window is resized.
- **Set zoom level...**<br>
  Displays the image at a zoom level (%) entered directly in a dialog.
- **Previous page\[PageUp\] / Next page\[PageDown\]**<br>
  Moves to the previous or next frame (page) in a multipage TIFF or animated image.
- **Rotate left / Rotate right**<br>
  Rotates the displayed image 90 degrees left or right at a time. This only affects the display; the original image data is not changed (but the rotation is reflected when saving or copying).
- **Flip horizontally**<br>
  Flips the displayed image horizontally (mirror image). This also only affects the display; the original image data is not changed.
- **Black background / White background / Checkerboard background**<br>
  Changes the background behind transparent areas (the default is checkerboard). Use this to check how transparent areas appear.<br>
  This setting applies to all tabs and is retained the next time you start SSP.
- **Make top-left color transparent**<br>
  Treats colors matching the color at the top-left of the image (coordinates 0,0) as transparent in the display only. This is useful for checking how an image without a transparent background color looks with transparency.<br>
  This setting applies to all tabs and is retained the next time you start SSP.

!!! tip "ヒント"

    “Make top-left color transparent” only works on images that do not originally have transparency (alpha). It is not applied to images that already have transparent areas, even when enabled, to prevent unintended areas from disappearing.

## Mouse and keyboard controls

Turn the mouse wheel to zoom in or out centered on the cursor position.<br>
You can close a tab by middle-clicking it or clicking its “×” button. You can also right-click the tab and select “Close”.<br>
In cropping mode, drag over the image to select the area to crop.

The main keyboard shortcuts are listed below.

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

## Feature details

### Zooming

The zoom level ranges from 5% to 1600%, and each zoom in or out changes it by a factor of 1.25.<br>
The mouse wheel zooms centered on the cursor position, so you can quickly enlarge the area you want to see. Select “Fit to window” to automatically adjust the image so it always fits entirely within the window.

### Rotation and horizontal flipping

You can rotate the image left or right (in 90-degree increments) and flip it horizontally. These operations only affect the display; the original image data itself is not modified.

!!! tip "ヒント"

    If you use “Save as” or “Copy” while the image is rotated or flipped, it is output in the orientation shown.<br>
    Moving between pages or resizing the image clears the rotation, flip, and crop settings.

### Background and transparency display

You can choose black, white, or checkerboard for the background behind transparent areas (the default is checkerboard). The checkerboard background uses tiled squares to make transparent areas easy to see.<br>
Combined with “Make top-left color transparent”, this lets you check how an image without a transparent color looks with transparency.

### Resizing and cropping

“Resize” lets you scale the image by specifying its width and height. Because the original image is preserved, you can also restore its original dimensions.<br>
Turn on “Crop” and drag over the image to select the area to crop. The selected area is used when saving or copying, and its coordinates are displayed on the left side of the status bar. Cropping is set per tab and does not change the original image.

### Saving and copying

Under “Save As”, you can choose PNG, BMP, JPEG, or WebP (lossless or lossy). Lossless WebP preserves image quality, while lossy WebP can reduce the file size.<br>
The format initially selected in the save dialog matches the original image format. For WebP images, it also matches whether the original was saved as lossless or lossy.<br>
If the original is a JPEG and has not been resized or cropped, it is saved without re-encoding. Any rotation or flipping is applied without degrading image quality (lossless rotation), and metadata such as EXIF is removed.<br>
“Copy” sends the image to the clipboard while preserving transparency, so you can paste it with its transparent areas intact into compatible applications.

### Automatic reloading

When an image opened from a file is updated by external software, the viewer detects the change automatically and refreshes the display after about 1 second. This is useful for checking an image in the viewer while editing it.

### Multipage images and animations

For multipage TIFFs and animated images such as GIF, APNG, and WebP, you can use “Previous Page” and “Next Page” to view individual frames (they are not played automatically).<br>
For PSD files, you can also use “Previous Page” and “Next Page” to view each layer individually.
