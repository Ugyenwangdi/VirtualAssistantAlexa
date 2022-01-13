import speech_recognition as sr  # SpeechRecognition package to understand the speech
import pyttsx3  # To speak the text
import pywhatkit  # pywhatkit allows us to do searching in youtube and other fun
import datetime  # To use date and time
import wikipedia  # To use for searching online
import pyjokes  # To use jokes by in the program
# import webbrowser
# import time


listener = sr.Recognizer()  # create a recognizer which will understand the voice
engine = pyttsx3.init()  # Python text to speech initialize
voices = engine.getProperty('voices')  # Get all the voices
engine.setProperty('voice', voices[1].id)  # set it to second voice


def speak(text):
    engine.say(text)  # ask it to say the command
    engine.runAndWait()


def get_command():
    command = ''
    try:
        with sr.Microphone() as source:  # Use microphone
            print('Listening...')
            voice = listener.listen(source)  # lister to listen to the source and store as voice
            command = listener.recognize_google(voice)  # Converting the voice to text using google api
            command = command.lower()  # convert to lower case
            if 'alexa' in command:  # check if name 'alexa' is in command
                command = command.replace('alexa', '')  # Remove 'alexa' from command by replacing it with empty string
                print(command)

    except:
        pass

    return command  # return command that we are saying


def run_alexa():  # To start alexa
    command = get_command()  # Get command
    #
    # if 'alexa' in command:  # check if name 'alexa' is in command
    #     command = command.replace('alexa', '')  # Remove 'alexa' from command by replacing it with empty string
    #     print(command)

    if 'play' in command:  # To play music
        song = command.replace('play', '')  # remove play from the command
        speak('playing' + song)
        pywhatkit.playonyt(song)  # play it in youtube

    elif 'time' in command:  # To get the time
        time = datetime.datetime.now().strftime(
            '%I:%M %p')  # %H:%M for 24 hr format # Get the hours and mins from datetime and format it
        speak('Current time is ' + time)
        print(time)

    elif 'who is' in command:  # To use word wikipedia in command
        person = command.replace('who the hell is', '')  # replace who is with empty str in command
        try:
            info = wikipedia.summary(person, 1)  # search person and mention how many lines we want
            speak(info)  # speak the information
            print(info)

        except:
            speak('Couldn\'t find ' + person)

    elif 'drink' in command:
        speak('sorry, I have a headache ')
    #
    # elif 'are you single' in command:
    #     speak('I am in a relationship with wifi ')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)

    elif 'what is your name' in command:
        speak('My name is alexa')

    # elif 'write' in command:
    #     recognizer = sr.Recognizer()
    #     try:
    #         with sr.Microphone() as mic:
    #             recognizer.adjust_for_ambient_noise(mic, duration=0.3)
    #             audio = recognizer.listen(mic)
    #
    #             text = recognizer.recognize_google(audio)
    #             text.lower()
    #
    #             print('Recognized as: ')
    #             print(text)
    #
    #     except sr.UnknownValueError():
    #         run_alexa()

    # elif 'open youtube' in statement:
    #     webbrowser.open_new_tab("https://www.youtube.com")
    #     speak("youtube is open now")
    #     time.sleep(5)
    #
    # elif 'open google' in statement:
    #     webbrowser.open_new_tab("https://www.google.com")
    #     speak("Google chrome is open now")
    #     time.sleep(5)
    #
    # elif 'open gmail' in statement:
    #     webbrowser.open_new_tab("gmail.com")
    #     speak("Google Mail open now")
    #     time.sleep(5)

    else:  # Default
        # speak("Please say it again")
        run_alexa()


if __name__=='__main__':
    speak('Hello, How can I help you? ')
    while True:
        try:
            run_alexa()  # Run it continuously

        except sr.UnknownValueError():
            listener = sr.Recognizer()
            continue


#
# if __name__=='__main__':
#     while True:
#         speak('Hello, How can I help you? ')
#         statement = get_command()
#         if statement == 0:
#             continue
#
#         if 'alexa' in statement:
#             try:
#                 run_alexa()  # Run it continuously
#
#             except sr.UnknownValueError():
#                 listener = sr.Recognizer()
#                 continue
#         if 'bye' in statement:
#             speak('your personal assistant is shutting down,Good bye')
#             print('your personal assistant is shutting down,Good bye')
#             break
#
#
#
# When running this code on PyCharm, you might encounter an error regarding PyAudio and will have to download that library.
#
# And if the usual “pip install PyAudio” command doesn’t work, you will have to go with a workaround. First, install Pipwin and then use the command “Pipwin install PyAudio.”