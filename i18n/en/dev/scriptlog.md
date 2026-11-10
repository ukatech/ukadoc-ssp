# Developer Help: Script log

This page explains the **Script log**.

It also explains the **Error log**, which you can switch to from the bottom left of the Script log.

## Script log

Sakura Script received by a ghost is stored internally, up to the number of entries you set.<br>
The Script log lets you view and save scripts stored this way, and have the ghost speak them again.

### (Bottom left) Script

A drop-down menu for switching to the [Error log](#エラーログ).

### Number of log entries

Sets the number of log entries to store internally.

### Buttons

Performs the following actions on the rows selected in the list and other items.

- **Clear**<br>
  Deletes all contents of the list.
- **Copy**<br>
  Copies the selected script to the clipboard.<br>
  You can paste it into text or another application for testing.
- **Save**<br>
  Opens the save dialog and exports the log in CSV format to the specified location.
- **Run**<br>
  Makes the ghost run the selected log again.

## Error log

Displays a history of errors that occurred while SSP was running.<br>
Check the error details and use them as a reference for resolving the issue.

### Error levels

The icon at the left edge of the list and the word at the beginning of the error message indicate the error level.<br>
They generally mean the following.

- **![](../assets/screenshots/dev/scriptlog/4.png)Critical**<br>
  A serious error has occurred. It may prevent startup or cause the program to stop running.<br>
  It must be fixed immediately.
- **![](../assets/screenshots/dev/scriptlog/3.png)Error**<br>
  An error has occurred. The intended behavior is not working, for example, because part of a file contains an error that cannot be corrected and is being skipped.<br>
  Fix the error to restore normal operation.
- **![](../assets/screenshots/dev/scriptlog/2.png)Warning**<br>
  A minor error has occurred in a file or similar, but SSP has corrected it internally and the program is (probably) working normally.<br>
  Fix it whenever possible, both for compatibility with other baseware and to avoid situations such as “it stopped working even though I didn’t change anything” when SSP’s specifications change.
- **![](../assets/screenshots/dev/scriptlog/1.png)Notice**<br>
  A potential error or risk of some kind has been detected.
- **![](../assets/screenshots/dev/scriptlog/0.png)Info**<br>
  Reference information for system developers. You generally do not need to worry about it.

### (Bottom left) Error

A drop-down menu for switching to the [Script log](#スクリプトログ).

### Number of log entries

Sets the number of log entries to store internally.

### Buttons

Performs the following actions on the rows selected in the list and other items.

- **Clear**<br>
  Deletes all contents of the list.
- **Copy**<br>
  Copies the selected error details to the clipboard.<br>
  You can paste them into text or another application for testing.
- **Save**<br>
  Opens the save dialog and exports the log in CSV format to the specified location.
