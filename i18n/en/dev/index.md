# Developer Help

This page introduces developer features available in SSP, along with a few tips for developing ghosts and other content.

For those of you who have been enjoying ghosts and now want to try making one yourself.<br>
Or those of you who installed SSP with the intention of creating a mascot application from scratch.<br>
There should also be useful information for those interested in creating content such as balloons and shells, rather than ghosts.

Unfortunately, SSP's help alone explains very little about how to make anything.<br>
This page is intended only to explain SSP's features.<br>
However, as a starting point, we've also prepared a few extras: a collection of [links](links.md) and [frequently asked questions](faq.md). We hope you'll use them as a starting point and explore the sites linked there.

## What to Do First

In Preferences, open [General](../config/ippan.md) and turn ON "Enable developer features".<br>
The first time you turn this ON, a dialog may appear. If so, just proceed through it.

This will make the settings in [Development / Miscellaneous](../config/dev.md) available and add several items to the "Features" section of the right-click menu.<br>
It will also add settings to [Ghost preferences](../config/eachghost.md) and its [default settings](../config/ghost2.md).

## Adjusting Settings

We recommend the following settings during development.

### Preferences - [Ghost (1)](../config/ghost.md)

- **Update check method**<br>
  <strong>Strict (SSP default setting)</strong>.

### Preferences - [Development / Miscellaneous](../config/dev.md)

- **Create update files and NARs when a folder is dropped**<br>
  **ON**.<br>
  This makes it easy to create update files and NARs.
- **Do not include files with the read-only attribute in updates**<br>
  **ON**.<br>
  This is a precaution to keep unnecessary files out of updates.
- **Hide when a surface does not exist**<br>
  **ON**.<br>
  Normally, if a script specifies an undefined surface, the ghost displays its default expression (for example, surface0 for the `\0` side).<br>
  However, this can make it difficult to notice a mistake in a surface specification. Turning this setting ON to hide the surface completely can make such mistakes easier to spot.
- **Suppress Vanish (uninstall) execution**<br>
  **ON**.<br>
  This helps prevent accidents such as accidentally deleting a ghost during development.<br>
  You may want to turn it OFF only when testing what happens during uninstallation.
- **Notify when errors at or above level ○○ occur**<br>
  **NOTICE**.<br>
  NOTICE-level notifications can also help you spot possible errors in your code.
- **Use a version control tool for updates when available**<br>
  **ON**.<br>
  Using a version control tool can help you recover from serious problems.
- **Use the exception handler**<br>
  **OFF**.<br>
  This setting prevents SSP from stopping and the ghost from ending unexpectedly when a serious error occurs, such as an access violation while accessing memory.<br>
  This is useful for users, but for developers it can cause signs of errors to go unnoticed.

### Preferences - [Folders](../config/folder.md)

It is useful to create a folder specifically for ghosts under development, and keep your in-progress ghosts and ghosts with development support features together in it.<br>
For that folder, we recommend turning on all the checkboxes in its folder-specific settings.<br>
This prevents various events that could cause problems during testing.<br>
You can also configure the same settings for individual ghosts using the development palette described below, but setting them here helps prevent accidental mishaps.<br>
Of course, this also makes it easier to find ghosts when you have many installed.

## Developer Features

### 1,Script log

Displays a history of the scripts SSP has received and executed. You can perform actions such as having a script spoken again or copying it.<br>
You can also switch to the error log, which contains a history of error notifications.<br>
⇒[Details](scriptlog.md)

### 2,Force Exit from Restricted Modes

Forcibly exits modes that restrict certain actions, such as passive mode and induction mode (these modes are normally started and ended by the ghost using Sakura Script controls).<br>
If these modes are not turned off at the right time, they may effectively prevent you from using SSP. This feature can help in such situations.<br>
On the other hand, if a mode is turned off when it should still be active, unexpected actions or behavior may occur and cause further problems.<br>
Therefore, this feature is intended not as a regular emergency measure for users, but as a tool for developers to use while investigating and fixing problems that prevent a mode from ending normally.

### 3,Development Palette

Opens a window for controlling settings and tools that are very useful during development.<br>
⇒[Details](palette.md)

## Development Links

A collection of useful sites and tools for creating and developing content.<br>
⇒[Development Links](links.md)

## Development FAQ

Answers to common beginner questions about development and how to handle problems.<br>
⇒[Development FAQ](faq.md)
