# Speech recognition

This is SSP's built-in speech recognition feature.<br>
It cannot recognize free-form sentences, but it lets you reliably give commands by voice.

You can choose the recognition engine to use and train it to improve accuracy from 「[Speech recognition/Voice synthesis](../config/dictation.md)」 in Preferences.

!!! tip "ヒント"

    For information about the feature that reads a ghost's lines aloud, see the 「[Voice synthesis](speech-synthesis.md)」 page.

## Getting started

1. Connect a microphone to your computer (a headset is also fine).
2. From the right-click menu, select 「Functions」→「Speech recognition」. A small window (the palette) labeled 「Speech recognition」 opens.
3. Check that the palette's volume meter moves when you speak into the microphone. If it does not, check that the correct microphone is selected and check 「Audio input source」 in 「[Speech recognition/Voice synthesis](../config/dictation.md)」 in Preferences.
4. Then speak to the ghost, following the steps in 「Basic operation」 below.

Speech recognition works only while the palette is open. Close it using the 「×」 at the upper right of the palette or the Esc key to stop speech recognition.<br>
If you exit SSP while the palette is open, it will open automatically the next time you start SSP, and recognition will resume. If you no longer need it, close the palette before exiting.<br>
The palette remembers its position.

!!! tip "ヒント"

    In environments where speech recognition is unavailable, for example because no speech recognition engine is installed on the computer, opening the palette will not recognize anything. In that case, the speech recognition options in Preferences are also grayed out.

## Understanding the palette

The palette consists of three sections—「Conversation partner」, 「Request」, and 「Content」—with a volume meter and status display below them.<br>
The highlighted section shows what you should say next.

- **Conversation partner**<br>
  Shows who you are speaking to (in the format 「Character name | Ghost name」).
- **Request**<br>
  Shows the words of the choice in the balloon that was recognized most recently.
- **Content**<br>
  Shows a list of options to choose from after selecting something from 「Menu」. The palette extends downward to show the list only while this section is in use.
- **Volume meter**<br>
  Shows the volume of the sound picked up by the microphone. If it does not move when you speak, your voice is not being picked up.
- **Status display at the lower right**<br>
  Shows the last words recognized. Use it to check when the words recognized differ from what you expected.<br>
  Right after startup, 「\[Ready\]」 is shown. 「\[Update/Pause\]」 or 「\[ModeChange/Pause\]」 appears briefly when the choices are updated or the section changes (speech is not recognized during this time, so wait a moment and try speaking again).

## Basic operation

When you start, the 「Conversation partner」 section is highlighted, and the other sections are inactive.<br>
First, clearly say who you want to talk to.

The sequence is: 「Call the conversation partner → Make a request (→ Select content if needed)」.<br>
For example: say 「Emily」 → say 「Menu Shell」 → say 「3」 from the displayed list → Emily's shell changes.

### Conversation partner

The name of the person you want to give voice commands to. Say any of the following names of a **currently running ghost** to speak to that ghost:

- The ghost's name
- The name of the main character (`\0`)
- The name of a sub character (`\1`) …… Calling this name means you are speaking to that ghost's **sub character**.

For example, for Emily/Phase4.5, say 「Emily」, 「Teddy」, or 「Emilio」. Usually, 「Emily」 is best.<br>
When you call a name, the conversation partner is shown in the section, and the palette moves on to 「Request」. If the ghost supports it, a menu also appears in the balloon as soon as you call its name.<br>
When you start or exit a ghost, the list of names you can call is updated automatically. Names of ghosts that are not running will not be recognized.

### Request

Say the request you want the ghost to carry out. The following requests can be recognized.

| What to say | Function |
|---|---|
| A choice or anchor displayed in the balloon | All displayed choices and anchors can be recognized. When recognized, the choice or anchor is selected. The words that can be recognized are updated automatically when choices appear or disappear. |
| 「Menu Shell」 | Shell switching feature ⇒ Select 「Content」 |
| 「Menu Change ghost」 | Change ghost feature ⇒ Select 「Content」 |
| 「Menu Call another ghost」 | Ghost calling feature ⇒ Select 「Content」 |
| 「Menu Balloon」 | Balloon switching feature ⇒ Select 「Content」 |
| 「Cancel」 | Cancel the request and return to 「Conversation partner」 |
| The name of another conversation partner | Switch the conversation partner to that person. |

Say 「Menu」 followed by the item name. The item name is the name shown in the right-click menu (such as 「Shell」 or 「Balloon」).<br>
Say 「Cancel」 to cancel the request and return to the 「Conversation partner」 section. To change who you are speaking to, you can also call the name of the person you want to speak to without saying 「Cancel」 first.

### Content

This section appears when there are multiple options to choose from, such as after selecting 「Menu Shell」.<br>
Say the name of an option shown in the list, or one of the special commands below.

- The list shows up to 10 items per page, with numbered icons from 1 to 10. If there are many items, they are split across pages.
- The 「Change ghost」 and 「Call another ghost」 lists include all installed ghosts, not just those that are running. You can select a ghost by its name, or by the name of its main character or sub character.
- The 「Shell」 list includes the shells of the conversation partner's ghost. The 「Balloon」 list includes all installed balloons.
- After you make a selection, the palette returns to 「Conversation partner」 for 「Change ghost」, and to 「Request」 for all other selections.

| What to say | Function |
|---|---|
| A number (spoken in Japanese) | Say the number shown on the icon before an option to get the same result as selecting that item. |
| 「Next」, 「Previous」 | Turn to the next or previous page of choices. 「Next」 appears in the list only when there is a next page, and 「Previous」 appears only when there is a previous page. |
| 「Forward」, 「Back」 | Turn 10 pages at a time. 「Forward」 appears in the list only when there are pages more than 10 pages ahead, and 「Back」 appears only when you are on page 11 or later. |
| 「Cancel」 | Cancel the selection and return to 「Request」 |

## If speech is not recognized correctly

- Check whether the volume meter moves. If it does not, the microphone may not be selected or may be muted. Check 「Audio input source」 and the microphone volume in Windows sound settings.
- Recognition works better in a quiet place if you speak clearly in one breath. Say long names without pausing.
- If your environment supports 「Training」, which teaches the recognition engine the characteristics of your voice, run it from 「[Speech recognition/Voice synthesis](../config/dictation.md)」 in Preferences to improve recognition.
- Check that you are calling the correct name. Only the names of running ghosts can be recognized.
- If a choice appears but your words are not recognized, recognition may be paused while the choices are updated right after they appear. Wait a moment and try speaking again.
