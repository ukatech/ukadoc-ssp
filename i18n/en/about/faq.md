# Frequently Asked Questions

This page lists information known at the time this help was written about questions that are commonly asked about SSP.<br>
Check here before asking a question.

- [Questions about how to use SSP](#操作方法などの質問)
- [Questions about problems and unexpected behavior](#不具合あやしい動作についての質問)
- [Other questions](#その他の質問)

## Questions about how to use SSP

### Q: My balloon or shell has moved off-screen, and I can't get it back.

**A1:** You can restore its position using “Reset shell position” or “Reset balloon position” in [Keyboard shortcuts](../functions/shortcut.md).<br>
You can also use these features from the [Functions menu](../functions/index.md) in the right-click menu. (Even if the shell is off-screen, you can open the menu by right-clicking the ghost icon in the task tray.)<br>
However, this method won't work if the position is already wrong when SSP starts for the first time.<br>
In that case, contact the ghost author.

### Q: I have so many ghosts (and balloons) that it's hard to find them in the menus. Is there a way to make this easier?

**A1:** Are you using [folders](../config/folder.md)?<br>
When you organize items into folders, the menus are divided into submenus for each folder, which should make them easier to find.<br>
![Example of the ghost menu with items organized into folders](../assets/screenshots/config/folder/3.png)

**A2:** Use [Explorer](../functions/explorer/index.md).<br>
You can sort items by author or installation date, and there's also a search function, so it should be easy to find what you're looking for.<br>
Explorer is also useful when you've organized items into folders, since you can sort the folders as well.

**A3:** If you use the item you're looking for often, it may be listed under “Recently used” in the [right-click menu](../howto/rclick.md).<br>
You can change the maximum number of items to remember in “[Display](../config/disp.md)” in Preferences.

### Q: I want to run a network update for several ghosts at once.

**A1:** You can do this in [Explorer](../functions/explorer/index.md).<br>
With the list selected, press Ctrl + A to select all ghosts, then right-click and choose “Network update.”

### Q: I want to set the scaling ratio for all ghosts and balloons in SSP at once.

**A1:** You can do this in [Ghost (2)](../config/ghost2.md).<br>
Click the shared scaling button and set the ratio. When you close the settings window, it will be applied to all ghosts that don't have an individual scaling ratio set.

## Questions about problems and unexpected behavior

### Q: How do I report a bug? Who should I contact, and how?

**A1:** Read “How to report a bug (for Ukagaka)” in the [Links](links.md#その他) section.

### Q: When I run a network update, it always says that something doesn't match at the MD5 check or something like that.

**A1:** If you have a utility that modifies network traffic, temporarily disable it.<br>
Examples include antivirus software and firewall software.

**A2:** Try updating your network drivers (specialized software for using wireless or wired LAN).

**A3:** Contact the ghost author.<br>
If the ghost reports the name of the file that caused the MD5 mismatch, including that information may help.

### Q: My ghost has stopped talking. I've checked the settings in its own menu, and nothing seems to be set to stop it from talking.

**A1:** Some ghosts may stop talking when they extend beyond the edge of the screen.<br>
Even when it doesn't look like the ghost extends beyond the screen, part of the character window may be outside the screen because the area that isn't displayed (transparent) is still included. Try placing the ghost with a little extra room around it.

### Q: The ghost's expressions and other things look wrong (especially when changing a ghost-specific mode), or it says obviously incorrect things.

**A1:** Check whether [Settings: Legacy specification support](../config/index.md) is turned ON.

### Q: SSP keeps showing errors. It seems to keep working when I use it, but what should I do?

**A1:** It's safe to ignore the errors if you're just using SSP; they won't cause problems.<br>
The ghost author may appreciate it if you report the error details.

### Q: SSP suddenly crashes.

**A1:** Some users have reported greater stability when they turn off the [crossfade feature](../config/disp.md).

**A2:** Try turning ON [Use the exception handler](../config/dev.md). However, this isn't recommended while developing ghosts, since it can make errors harder to notice.

**A3:** A file named STACKTRC.TXT may have been created in the same folder as ssp.exe.<br>
If so, please report it to the [SSP BUGTRAQ ToDo](ssp.md).<br>
The file contains all the environment information, but it will be easier to fix the problem if you also provide as much detail as possible, such as which ghost was running and what settings you changed from their default values.<br>
For details, see the earlier question, “[How do I report a bug?](#q-バグ報告の仕方を教えてください誰にどう報告すればよいですか)”.

**A3:** Even if STACKTRC.TXT wasn't created, please report the issue to ToDo if SSP crashes frequently.<br>
When you do, provide as much detail as possible about your environment, the steps that make the problem easy to reproduce, and how often it occurs.

### Q: SSP won't start after I switched to a very buggy ghost.

**A1:** The settings file is data → profile → app.dat in the folder containing ssp.exe.<br>
Delete it, or delete any lines in it that look relevant (lines beginning with something like “Ghost”), to return to the default ghost.<br>
You can also do the same thing by moving the relevant ghost somewhere outside the ghost folder so SSP can't find it.<br>
SSP also includes a feature that automatically performs these actions if it stops during startup.

**A2:** Try deleting realize.txt in data → profile in the folder containing ssp.exe, as well as the profile folders created inside each ghost.<br>
Alternatively, you can extract SSP to a different location to create a clean copy, then move only the ghost, balloon, and other folders over.

## Other questions

### Q: What does SSP stand for?

**A1:** It originally stood for Sakura Script Player, but it no longer stands for anything.<br>
This may come as a surprise, but it doesn't stand for Shima-Shima-Panchu.

### Q: I want to talk with someone about ghosts!

**A1:** You may find people on “Kairanban” in the [Links](links.md) section, or on Twitter.
