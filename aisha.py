{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pyaudio'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-31-0f921c65e5f8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mspeech_recognition\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpyttsx3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'sapi5'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pyaudio'"
     ]
    }
   ],
   "source": [
    "import pyttsx3\n",
    "import datetime\n",
    "import speech_recognition as sr\n",
    "import pyaudio\n",
    "\n",
    "engine = pyttsx3.init('sapi5')\n",
    "voices = engine.getProperty('voices')\n",
    "#print(voices[1].id)\n",
    "engine.setProperty('voice',voices[1].id)\n",
    "\n",
    "def speak(audio):\n",
    "    engine.say(audio)\n",
    "    engine.runAndWait()\n",
    "    \n",
    "    \n",
    "def wishMe():\n",
    "    hour =int(datetime.datetime.now().hour)\n",
    "    if hour>=0 and hour<12:\n",
    "        speak(\"Good Morning!\")\n",
    "    \n",
    "    elif hour>=12 and hour<18:\n",
    "        speak(\"Good Afternoon!\")\n",
    "    \n",
    "    else:\n",
    "        speak(\"Good Evening!\")\n",
    "    \n",
    "    speak(\"I am Aisha sir. Please tell me how may I help you\")\n",
    "    \n",
    "def takeCommand():\n",
    "    #it takes microphone input from user and returns string output\n",
    "    r = sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        print(\"Listening...\")\n",
    "        r.pause_threshold = 1    #to increase a pause\n",
    "        audio = r.listen(source)\n",
    "    \n",
    "    try:\n",
    "        print(\"Recognizing...\")\n",
    "        query = r.recognize_google(audio, Language='en-in')\n",
    "        print(f\"User said: {query}\\n\")\n",
    "        \n",
    "    except Exception as e:\n",
    "        #print(e)   #if you want to don't show error on console remove this \n",
    "        print(\"Say that again please...\")\n",
    "        return \"None\"\n",
    "    return query\n",
    "if __name__ ==\"__main__\":\n",
    "    wishMe()\n",
    "    takeCommand()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
