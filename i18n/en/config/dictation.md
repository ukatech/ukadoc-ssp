# Settings: Speech recognition/voice synthesis

This page explains the “Speech recognition/voice synthesis” page in the dialog opened by selecting “Preferences” in the “Settings” submenu of the right-click menu.

Use this page to configure SSP's speech recognition and voice synthesis features.

For instructions on using these features, see the “[Speech recognition](../functions/speech-recognition.md)” and “[Voice synthesis](../functions/speech-synthesis.md)” pages.

!!! tip "ヒント"

    If your computer cannot use speech recognition or voice synthesis, the items in the corresponding group will be grayed out and unavailable. <br>
    “(System Default)” for each item means that the option selected in Windows settings will be used. In most cases, you can leave it as is.

## Item descriptions

### Speech recognition

Select Function→Speech recognition to open and use the recognition palette.

!!! tip "ヒント"

    Changes to the settings in this section are applied immediately to any open recognition palette. You do not need to restart SSP.

- **Recognition engine**<br>
  Change the speech recognition engine. “(System Default)” uses the engine selected in the Speech Recognition control panel.<br>
  If your computer has multiple recognition engines installed, select one that suits the language you speak.
- **Profile**<br>
  Switch the training data used to improve recognition accuracy. “(System Default)” uses the profile selected in the Speech Recognition control panel.<br>
  Switch profiles to use different training results for each user.
- **Recognition engine settings, Microphone settings, and Training**<br>
  These options are available only for some recognition engines. They are usually all disabled.<br>
  When an option is available, click it to open the settings screen provided by the recognition engine. “Microphone settings” lets you adjust the microphone volume, while “Training” lets you train the engine to recognize your voice more accurately.
- **Audio input source**<br>
  Switch the audio input source, such as a microphone jack or headset. “(System Default)” uses the source selected in the Speech Recognition control panel.<br>
  The “Settings...” button on the right is available only if the selected input source has its own settings screen.

### Voice synthesis

Turn on Function→Voice synthesis to use this feature.

!!! tip "ヒント"

    Changes to the settings in this section take effect from the next time speech is read aloud. You do not need to restart SSP.

- **`\0` (main character)**<br>
  Configure the voice for the main character (`\0`). You can select a voice, adjust its pitch, and use the Settings button to configure advanced options.
- **`\1` (sub character)**<br>
  Configure the voice for the sub character (`\1`). You can select a voice (it can be the same as `\0` or `\2`), adjust its pitch, and use the Settings button to configure advanced options.
- **`\2` and later (other characters)**<br>
  Configure voices for additional characters from `\2` onward. You can select a voice (it can be the same as `\0` or `\1`), adjust its pitch, and use the Settings button to configure advanced options.
- **Voice selection**<br>
  The list contains voices installed in Windows and options for using external voice synthesis services: “LocalAPI-0–9” and “CloudAPI-0–9”.<br>
  To use a “LocalAPI-” or “CloudAPI-” option, select it, then click “Settings...” on the right to configure the connection and other details.<br>
  For Windows voices, the “Settings...” button is available only if that voice has its own settings screen.
- **Pitch**<br>
  Sets the pitch of the voice. Choose a value from -10 to 10, where 0 is the default. Higher numbers produce a higher-pitched voice.<br>
  The default values are 0 for `\0`, +5 (slightly higher) for `\1`, and -5 (slightly lower) for `\2` and later.
- **Audio output device**<br>
  Switch the output device used for audio, such as speakers or a headphone jack. Use the Settings button to configure advanced options.
- **Speaking speed**<br>
  Adjust the reading speed for voice synthesis. Use the slider to set a speed from “Slow” to “Fast”. Adjust it from the default position.<br>
  This setting applies to all characters.
- **Volume**<br>
  Adjust the volume level for voice synthesis. Use the slider to set a value from 0% to 100%. The default is 100%.<br>
  This setting applies to all characters.
- **Wait for script playback to match the pace of voice synthesis**<br>
  Synchronize the timing of script display with the reading speed of voice synthesis.<br>
  When this option is off, text in the balloon advances at its usual speed, and the voice follows along. When it is on, the ghost waits for the voice to catch up, reducing the mismatch between voice and text. (However, if synthesis takes a long time, the ghost's movements will also slow down.) This option is off by default.

## Voice synthesis advanced settings dialog (Settings button on the right)

This dialog opens when you click “Settings...” for a “LocalAPI-” or “CloudAPI-” option. Select the type of software or service you want to use, then enter the required information.<br>
All fields are optional except for the API key when using cloud voice synthesis. Enter only what you need and leave the other fields blank. Fields that are not used by the selected type will be grayed out and unavailable.

- **Type**<br>
  Select the voice synthesis software or service to use. Local software is available for LocalAPI options, and cloud services are available for CloudAPI options.
- **Voice ID / Style ID / Browse...**<br>
  Specify the voice to use. Click “Browse...” to retrieve a list of voices from the connected software and select one by name. You can also enter the ID directly if you know it.<br>
  For LocalAPI, “Browse...” cannot show the list unless the connected software is running (a buzzer will sound). Start the software before clicking it.<br>
  For Aivis Cloud API and OpenAI TTS, “Browse...” opens a webpage listing the voices in your browser instead of retrieving a list.
- **Host name / IP and port number**<br>
  For LocalAPI, specify the computer running the software you want to connect to. Leave this blank if the software is running on the same computer.
- **API key**<br>
  This is the key used to connect to a cloud service. Get it from the service's management page and paste it here.

### LocalAPI

- **VOICEVOX, VOICEVOX Nemo, SHAREVOX, AivisSpeech**<br>
  Click the Browse button to select a voice ID by character name. You can also enter the ID directly if you know it.<br>
  Leave the host name and port number blank if the software is running on the same PC.
- **COEIROINK v2**<br>
  Click the Browse button to select a voice ID and style ID by character name. You can also enter the IDs directly if you know them.<br>
  Enter a style name (such as “れいせい”) for the style ID. You can also enter the ID if you know it.<br>
  Leave the host name and port number blank if the software is running on the same PC.
- **Style-BERT-VITS2**<br>
  Click the Browse button to select a voice ID and style ID by character name. You can also enter the IDs directly if you know them.<br>
  Enter a style name for the style ID. You can also enter the ID if you know it.<br>
  Leave the host name and port number blank if the software is running on the same PC.<br>
  Start Server.bat (`server_fastapi.py`).
- **OpenAI TTS - Local (local API compatible)**<br>
  Enter the name of a text-to-speech AI model as the voice ID, such as “irodori-tts”.<br>
  Enter a style ID according to the compatible server's specifications. For example, with Irodori-TTS-Server, use the name of the reference audio WAV file in the voices folder, without the extension.<br>
  Leave the host name blank if the software is running on the same PC. The port number depends on the service. For example, for Irodori-TTS-Server, use 8088.

### CloudAPI

- **Aivis Cloud API**<br>
  Copy the “Model UUID” and enter it as the voice ID. Note: This is not the Speaker UUID.<br>
  The style ID is listed on the voice details page.<br>
  A pitch of 0 is recommended. Other values are said to reduce synthesis speed.<br>
  You can get an API key from [this dashboard](https://hub.aivis-project.com/cloud-api/dashboard). Paste it into the API key field.
- **OpenAI TTS - Cloud (cloud API or compatible service)**<br>
  Enter the name of a text-to-speech AI model as the voice ID, such as “gpt-4o-mini-tts” or “tts-1”.<br>
  Enter a name listed in the “Voice options” section of [this documentation](https://developers.openai.com/api/docs/guides/text-to-speech#voice-options) as the style ID. For example: “marin” or “cedar”.<br>
  You can get an API key from [this dashboard](https://platform.openai.com/account/api-keys). Paste it into the API key field.<br>
  If you use a compatible service, set the host name. Leave this blank when using OpenAI Text-to-speech.

## Buttons at the bottom

- **Help**<br>
  Opens the help page for the current page in the Preferences dialog (that is, this page).<br>
  The “?” button at the top right of the dialog does the same thing.
- **Close**<br>
  Closes the Preferences dialog.<br>
  The “×” button at the top right of the dialog does the same thing.
