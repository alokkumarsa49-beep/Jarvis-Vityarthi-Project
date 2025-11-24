1. Problem Statement

Modern computer users perform many repetitive tasks such as opening websites, searching for information, checking news, and controlling applications manually. These tasks can be time-consuming and require constant user interaction.
There is a need for a hands-free, voice-controlled assistant that can efficiently perform actions, respond intelligently, and simplify the user’s digital workflow.
The goal of this project is to develop Jarvis, an AI-powered voice assistant capable of recognizing voice commands, performing system actions, fetching real-time information, and generating context-aware responses using advanced AI models.

2. Scope of the Project

The project includes the following scope:

Implementing speech recognition for command detection.

Creating a voice wake system triggered by the keyword “Jarvis”.

Opening frequently used websites via voice commands.

Integrating a music library system to play predefined songs.

Fetching real-time news using the NewsAPI service.

Generating intelligent conversational responses using Google Gemini AI.

Providing text-to-speech output using gTTS + pygame.

Ensuring smooth audio playback and error handling.

Running continuously with a simple command interface.

Out of Scope (not included in this version):

Full natural conversational memory

Smart home device control

Custom desktop automation (file handling, app launching)

Offline speech recognition

3. Target Users

The primary users of this project include:

Students — who want a simple assistant to browse, search, or gather information hands-free.

Tech enthusiasts — interested in exploring voice AI automation.

General computer users — who want a faster way to open websites, get news, and interact with AI without typing.

Developers — who want a customizable base for building advanced AI assistants.

4. High-Level Features
4.1 Voice Activation

Wake word detection using the keyword “Jarvis”.

4.2 Voice Command Recognition

Detects user speech and interprets commands.

4.3 Website Automation

Opens Google, YouTube, Facebook, LinkedIn, and more.

4.4 Music Playback

Plays predefined songs using a user-created music library.

4.5 Real-Time News

Fetches top headlines from Indian news sources via NewsAPI.

4.6 AI Response Generation

Uses Gemini 2.0 Flash to generate intelligent, natural responses for general queries.

4.7 Text-to-Speech Output

Converts responses to speech using gTTS.

Plays audio reliably using pygame.

4.8 Continuous Listening Mode

Runs in a loop and stays active until manually stopped.
