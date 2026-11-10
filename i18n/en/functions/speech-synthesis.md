# Voice synthesis

This feature reads aloud the content that a ghost says in its balloon.<br>
In addition to the voices included with Windows, you can also use voices from external voice synthesis software such as VOICEVOX, or from cloud voice synthesis services.<br>
You can assign a different voice to each character (`\0`, `\1`, `\2` and above).

!!! tip "ヒント"

    This feature makes your ghost speak aloud. To speak to your ghost by voice, see the [Speech recognition](speech-recognition.md) page.

## Getting started

1. Select 「機能」→「音声合成」 from the right-click menu. A check mark appears next to the item, and speech synthesis starts.<br>
   Select it again to turn it off. The on/off state is retained the next time you start SSP.
2. In 「[Speech recognition/voice synthesis](../config/dictation.md)」 under Preferences, select a voice for each character. If you leave the selection as “(System Default),” the default Windows voice is used.
3. If needed, adjust the speaking speed, volume, and pitch. Changes take effect the next time speech is synthesized; you do not need to restart SSP.

If the ghost is speaking when you turn this feature on, that speech will not be read aloud. Reading starts with the next line.

## What is read aloud

Regular text shown in the balloon is read aloud as it appears.<br>
The following are not read aloud:

- Choices and anchors (text that you click to select).
- Emoji and symbols such as “★”. These are skipped with a pause if they appear within a sentence. Lines containing only punctuation are not read aloud either.
- Text that appears instantly without a wait.
- Text that the ghost specifies should not be read aloud (or should use different text for speech). Depending on the ghost, the words read aloud may differ from what appears in the balloon.

The voice used depends on which character is speaking. The voices set for the main character (`\0`), the sub-character (`\1`), and other characters (`\2` and above) are used respectively.<br>
The default pitch is 0 for the main character (`\0`), +5 (slightly higher) for the sub-character (`\1`), and -5 (slightly lower) for characters `\2` and above. This gives each character a slightly different pitch. You can change these settings at any time in 「[Speech recognition/voice synthesis](../config/dictation.md)」 under Preferences.

## Synchronizing speech and text

This section explains the 「Wait for script playback to match voice synthesis progress」 setting in Preferences.

- **Off (default)**<br>
  Balloon text advances at its usual speed. The voice reads along with it.<br>
  In environments where voice synthesis takes time, the text advances ahead of the voice. If the next line starts while the voice is behind, the remainder of the previous line may be skipped.
- **On**<br>
  Script playback waits until the voice catches up. This reduces the gap between the balloon text and the voice, and makes it less likely that speech will be skipped.<br>
  However, if voice synthesis takes time, the ghost's movements will also slow down accordingly.

## Using external voice synthesis software

The 「Select voice」 list includes 「LocalAPI-0」 through 「LocalAPI-9」 and 「CloudAPI-0」 through 「CloudAPI-9」, in addition to the voices included with Windows.<br>
These are slots for using external voice synthesis. Configure one server, voice, and style, and so on, in each slot. You can assign different slots to each character, or share the same slot between characters.

- **LocalAPI**<br>
  Connect to software running on your computer (or another computer on your network). Supported software includes VOICEVOX, VOICEVOX Nemo, SHAREVOX, AivisSpeech, COEIROINK v2, Style-BERT-VITS2, and OpenAI-compatible local servers.
- **CloudAPI**<br>
  Connect to an online service. Supported services include Aivis Cloud API and OpenAI TTS (or compatible services). You need an API key, and charges are subject to the service provider's terms.

Follow these steps to configure a voice.

1. For LocalAPI, start the voice synthesis software first.
2. Open 「[Speech recognition/voice synthesis](../config/dictation.md)」 under Preferences, then select 「LocalAPI-0」 or another slot in the character's 「Select voice」 setting.
3. Click 「Settings...」 to its right, then choose the software under 「Type」.
4. Click 「Browse...」 to display the list of voices registered in the software, then select the voice you want to use. If you know the ID, you can enter it directly instead.
5. Click 「OK」 to close the dialog, then turn on 「機能」→「音声合成」.

The input method for each setting varies by software. For details, see 「[Voice synthesis detailed settings dialog](../config/dictation.md#音声合成の詳細設定ダイアログ-右側の設定ボタン)」.

## If you cannot hear the voice

- Check that 「機能」→「音声合成」 is checked.
- Check that sound is enabled in Preferences under 「Audio output」 and 「Volume」, and in Windows sound settings.
- If you are using external voice synthesis software, check that it is running and that the host name and port number are correct. If the voice list does not appear when you click 「Browse...」, SSP cannot connect to the software.
- For a cloud service, check that the API key is entered correctly.
- If there is a delay before speech starts, voice synthesis is taking time. Turn on 「Synchronization」 to match the ghost's movements to the speech, or turn it off to prioritize the ghost's movements.
- If voice synthesis is not available on your computer, the voice synthesis settings in Preferences will be grayed out and unavailable.
