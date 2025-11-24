import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

from gtts import gTTS
import pygame
import os
import google.generativeai as genai 
import time                           



try:
    pygame.mixer.init()
except Exception as e:
    print("Warning: pygame.mixer.init() failed on import:", e)


recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"


GEMINI_API_KEY = "AIzaSyCC7c5I9ZR_hnFxcZo2S3WVbWCWOFso_yM"


if GEMINI_API_KEY:
    try:
        
        genai.configure(api_key=GEMINI_API_KEY)
        
    except Exception as e:
        print("Warning: failed to configure genai:", e)

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    """
   
    Robust gTTS + pygame playback:
    - Waits for file to be written.
    - Ensures mixer is initialized.
    - Plays and blocks until playback finishes.
    - Cleans up temp file afterwards.
    
    """
    if not text:
        return

    temp_mp3 = "temp.mp3"
    try:
        
        tts = gTTS(text)
        tts.save(temp_mp3)

        
        for _ in range(20):
            if os.path.exists(temp_mp3) and os.path.getsize(temp_mp3) > 0:
                break
            time.sleep(0.05)

        
        if not pygame.mixer.get_init():
            try:
                pygame.mixer.init()
            except Exception as e:
                print("Failed to init pygame.mixer:", e)

      
        pygame.mixer.music.load(temp_mp3)
        pygame.mixer.music.play()

        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print("TTS/playback error:", e)
    finally:
        
        try:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
        except Exception:
            pass
        try:
            if os.path.exists(temp_mp3):
                os.remove(temp_mp3)
        except Exception:
            pass

def aiProcess(command):
    """
    Uses Google Gemini (via google.generativeai) to generate a short response.
    Adjust model name if needed (e.g. 'gemini-2.0-flash', 'gemini-2.1', etc.)
    """
    
    if not GEMINI_API_KEY:
        return "Gemini API key not configured."

    try:
        
        model = genai.GenerativeModel("gemini-2.0-flash")  
        resp = model.generate_content(
            command,
            generation_config={
                "max_output_tokens": 256
            }
        )
        
        if hasattr(resp, "text") and resp.text:
            return resp.text.strip()
        
        return str(resp)
        
    except Exception as e:
        print("Gemini API error:", e)
        return "Sorry, I couldn't reach the AI service."

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ", 1)
        if len(parts) > 1:
            song = parts[1].strip()
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak(f"I don't know the song {song}")
        else:
            speak("Tell me the song name after play.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            
            data = r.json()
            
            
            articles = data.get('articles', [])
            
            
            for article in articles:
                speak(article.get('title', 'No title'))
        else:
            speak("Couldn't fetch news right now.")

    else:
        
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
