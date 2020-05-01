## Recognition_Module

#### Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc. To use these install required libraries or modules.


### Speech Input Using a Microphone and Translation of Speech to Text

Allow Adjusting for Ambient Noise: Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
Speech to text translation: This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.

### Translation of Speech to Text:

First, we need to import the library and then initialize it using init() function. This function may take 2 arguments.

  > init(driverName string, debug bool)

  drivername: [Name of available driver] sapi5 on Windows | nsss on MacOS
  debug: to enable or disable debug output

After initialization, we will make the program speak the text using say() function.

This method may also take 2 arguments.

  > say(text unicode, name string)

  text: Any text you wish to hear.
  name: To set a name for this speech. (optional)

Finally, to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().

##### Python Speech Recognition module:
  
  > pip install speechrecognition

##### Install pyaudio by executing the following command

  > pip install pyaudio



### Convert Text to Speech in Python using win32com.client:

There are several APIs available to convert text to speech in python. One of such APIs available in the python library commonly known as win32com library. It provides a bunch of methods to get excited about and one of them is the Dispatch method of the library. Dispatch method when passed with the argument of SAPI.SpVoice It interacts with the Microsoft Speech SDK to speak what you type in from the keyboard.

##### Installation

To install the win32com.client module , open terminal and write

  > python -m pip install pywin32

This works on Windows platform. Now we are all set to write a sample program that converts text to speech.



### Convert Text to Speech in Python:

There are several APIs available to convert text to speech in python. One of such APIs is the Google Text to Speech API commonly known as the gTTS API. gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.

The gTTS API supports several languages including English, Hindi, Tamil, French, German and many more. The speech can be delivered in any one of the two available audio speeds, fast or slow. However, as of the latest update, it is not possible to change the voice of the generated audio.

##### Installation

To install the gTTS API, open terminal and write

  > pip install gTTS



### Text to Speech by using pyttsx3:

pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. Engine instance. it is a very easy to use tool which converts the entered text into speech.

The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.

It supports three TTS engines :

  sapi5 – SAPI5 on Windows
  nsss – NSSpeechSynthesizer on Mac OS X
  espeak – eSpeak on every other platform

##### Installataion

To install the pyttsx3 module, first of all, you have to open the terminal and write

  > pip install pyttsx3



### Text To Speech using pyttsx module
pyttsx is a cross-platform text to speech library which is platform independent. The major advantage of using this library for text-to-speech conversion is that it works offline. However, pyttsx supports only Python 2.x. Hence, we will see pyttsx3 which is modified to work on both Python 2.x and Python 3.x with the same code.



### Text-To-Speech changing voice in Python
There are several APIs available to convert text to speech in python. One such APIs is the Python Text to Speech API commonly known as the pyttsx3 API. pyttsx3 is a very easy to use tool which converts the text entered, into audio.

##### Installation

To install the pyttsx3 API, open terminal and write

  > pip install pyttsx3
  
This library is dependent on win32 for which we may get an error while executing the program. To avoid that simply install pypiwin32 in your environment.

  > pip install pypiwin32

Some of the important functions available in pyttsx3 are:

  pyttsx3.init([driverName : string, debug : bool]) – Gets a reference to an engine instance that will use the given driver. If the requested driver is already in use by another engine instance, that engine is returned. Otherwise, a new engine is created.
  
  getProperty(name : string) – Gets the current value of an engine property.
  
  setProperty(name, value) – Queues a command to set an engine property. The new property value affects all utterances queued after this command.
  
  say(text : unicode, name : string) – Queues a command to speak an utterance. The speech is output according to the properties set before this command in the queue.
  
  runAndWait() – Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.
