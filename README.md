Jarvis Voice Assistant (Python)

Jarvis is a Python-based voice assistant capable of recognizing voice commands, opening websites, playing music, fetching news, and generating responses using Google Gemini AI.
It uses SpeechRecognition, gTTS, pygame, and google-generativeai for powerful voice interaction.

🚀 Features
<br><br/>

Voice Wake Word Detection → Activates when you say "Jarvis"
<br><br/>

Voice Commands:
<br><br/>

Open websites (Google, YouTube, Facebook, LinkedIn)
<br><br/>

Play predefined songs using musicLibrary.py
<br><br/>

Read top news headlines (via NewsAPI)
<br><br/>

AI-Generated Responses using Gemini 2.0 Flash

Text-to-Speech using gTTS + pygame

Error handling for stable audio playback

Continuous listening loop

📁 Project Structure
project/
<br><br/>
│── main.py
<br><br/>
│── musicLibrary.py
<br><br/>
│── README.md


musicLibrary.py should contain something like:

music = {
    "song name": "youtube_link",
    ...
}

🛠️ Installation
1. Install Dependencies

Run:

pip install speechrecognition pyttsx3 pygame gtts requests google-generativeai pyaudio


Note:

On some systems, installing pyaudio may require additional setup.

🔧 Configuration
1. Add your Gemini API key

Replace:

GEMINI_API_KEY = "YOUR_API_KEY_HERE"

2. Add your NewsAPI key

Set:

newsapi = "<Your NewsAPI Key>"


You can get one from: https://newsapi.org/

▶️ How to Run

Run the script:

python main.py


Jarvis will start and say:

Initializing Jarvis...

🎤 How to Use

The assistant listens continuously.

Say "Jarvis"

Speak your command. Examples:

Website commands

“Open Google”

“Open YouTube”

“Open LinkedIn”

Music

“Play perfect”

“Play shape of you”

News

“Tell me the news”

AI Query

Anything else you say is processed via Gemini AI, for example:

“What is quantum computing?”

“Tell me a joke”

“Explain black holes”

🧠 How AI Response Works

Jarvis sends your message to Google Gemini:

model = genai.GenerativeModel("gemini-2.0-flash")
resp = model.generate_content(command)


Returned text is spoken back using the custom speak() function.

🔊 TTS System

The project uses:

gTTS → generates speech audio

pygame → plays the audio reliably

Auto-cleanup removes temporary audio files

⚠️ Notes & Troubleshooting
1. Microphone Issues?

Check if your system recognizes the microphone:

python -m speech_recognition

2. PyAudio Installation Error

On Windows, install:

pip install pipwin
pipwin install pyaudio

3. Audio playback errors

Make sure your system audio output device is working.

📄 License

This project is open-source. You may modify and use it freely for personal projects.
