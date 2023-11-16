import firstTime
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle
import random as ra
import webbrowser
import socket
from tkinter import messagebox
import speech_recognition as sr
import os
# from PyDictionary import PyDictionary
import requests
import datetime
from data.alexlibs import COMBO as cb
from collections import Counter
import threading
import time
from datetime import datetime
from tkinter.font import Font
import json
from datetime import timedelta
from win10toast import ToastNotifier
import subprocess
import statistics
import re
import pyttsx3
# import bividCalculation as bc
from data.alexlibs import bividSearch as bs
from data.alexlibs import bividVoice as bv
from data.alexlibs import alexSplash
from data.alexlibs import alexNotes
from data.alexlibs import alexEmail
import nltk
from nltk.corpus import wordnet
import CheckUpdatee

# Download WordNet data (only needed once)
try:
    nltk.download("wordnet")
except TimeoutError:
    engine.say("Internet Connection is weak or not working, try reconnecting to another network")
    engine.runAndWait()

# USEFUL GLOBAL VARIABLES

# 1.) Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
# engine.setProperty('rate', 10)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# 2.) 
Answer = ""
# def globalVar(variableToMakeGlobal):
#     global Answer
#     Answer = variableToMakeGlobal
# 3.)
with open("userdata\\GUM.bd", "r") as GUM_File__:
    NameNew = GUM_File__.readline()

NameNew = NameNew.replace('\n', '')
UserName = NameNew

# 5.)
greeting = [f"Hello {UserName}!", f"Hi {UserName}!", f"Hey! {UserName}", f"Greetings! {UserName}", f"Heya! {UserName}",
    "Hiya!", f"Hi there {UserName}!", f"Hi hi! {UserName}", f"Hola {UserName}!", f"Sup {UserName}!", "Howdy!", f"Hey {UserName}!", "Hey there!", f"Aloha {UserName}!", f"Hello there {UserName}!", f"Heya {UserName}!", f"Hey {UserName}!",
    "Hi, nice to see\nyou again!", f"Hello {UserName},\nhow's your day?", f"Hello {UserName}", f"Hi {UserName}", f"Hey {UserName}", "Yo", f"Sup {UserName}", f"Greetings {UserName}", "Hola", "Heya", "Aloha", f"Heyo {UserName}"]

# 6.)
Current_Time = datetime.now().strftime("%H:%M")
Current_Date = datetime.now().strftime("%Y-%m-%d")

def startRecents():
    with open("data\\store.bd", "r") as writing_recent_file:
        Recent = writing_recent_file.readline()

    if Recent == "":
        pass
    else:
        do_tasks_label.destroy()
        foreground_color_scheme = ["lime", "lightblue", "orange", "purple", "yellow"]
        background_color_scheme = ["green", "blue", "red", "pink", "indigo"]
        tk.Button(recent_Frame, text=Recent, fg=ra.choice(foreground_color_scheme), bg=ra.choice(background_color_scheme),border=0).pack(pady=10)

# 8.) 
VAName = "Alex"

# 9.)
toaster = ToastNotifier()

# 10.)
def waitAndSay(word_to_say):
    TextToSay = word_to_say
    def sayText():
        engine.say(TextToSay)
        engine.runAndWait()

    homeWin.after(2000, sayText)

# START OF BIVID
homeWin = tk.Tk()
homeWin.title("Alex - Virtual Assistant")
homeWin.geometry("600x650")
homeWin.resizable(width=False, height=False)
alexIcon = ("data\\alexlibs\\MEDIA\\alex-icon-new.ico")
homeWin.iconbitmap(alexIcon)
# 11.)
style = ThemedStyle(homeWin)
style.set_theme("arc")
# alexSplash.splashScreen()
MIC_IMG = tk.PhotoImage(file="data\\alexlibs\\MEDIA\\icons8-micro-50.png")
MIC_IMG_RED = tk.PhotoImage(file="data\\alexlibs\\MEDIA\\icons8-micro-50-red.png")
def listen():
    def is_connected():
        try:
            # Connect to a well-known host (like Google's DNS server)
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            pass
        return False

    # Check for internet connection
    if is_connected():
        # Initializing the recognizer
        recognizer = sr.Recognizer()

        # Record audio from the microphone
        with sr.Microphone() as source:
            print("Say something...")
            engine.say(ra.choice(["Say something...", "I'm listening", f"{UserName}, say something"]))
            engine.runAndWait()
            audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API for speech recognition
            textVoice = recognizer.recognize_google(audio)
            bv.processUserVoice(textVoice)
            print("User Input [Voice]: ", textVoice)
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say(ra.choice(["Try that again...", "Didn't quite get that", f"{UserName}, I don't seem to get what you said, please speak again"]))
            engine.runAndWait()
        except sr.RequestError as e:
            print("Error making the request; {0}".format(e))
            engine.say(ra.choice(["something's wrong", "an error occurred, try using text", f"{UserName}, something's wrong, try that again"]))
            engine.runAndWait()
    else:
        waitAndSay(word_to_say=ra.choice([f"connect to the internet so I can better understand your speech", "I'm not Connected, so I can't understand your voice.", f"sorry {UserName}, it's just text based commands for now, try Connecting to the Internet"]))


homeWin.after(300000, listen)
# thread1 = threading.Thread(target=listen)

# thread1.start()
# thread1.join()

# Settings
def trigger_settings():
    settingWin = tk.Tk()
    settingWin.title("Alex: Settings & Personalization")
    settingWin.geometry("500x400")
    alexIcon = ("data\\alexlibs\\MEDIA\\alex-icon-new.ico")
    settingWin.iconbitmap(alexIcon)
    settingWin.resizable(width=False, height=True)


    # Initializing the Scrollbar
    settingCanvas = tk.Canvas(settingWin)
    scroll_y = ttk.Scrollbar(settingWin, command=settingCanvas.yview)
    scroll_y.pack(side="right", fill="y")

    WindowFrame = tk.Frame(settingCanvas) # settingCanvas

    settingCanvas.create_window((0, 0), window=WindowFrame, anchor="nw")
    # settingCanvas.update_idletasks()
    # settingCanvas.configure(yscrollcommand=scroll_y.set)


    # User-Data
    def getUserData():
        Name = name_box.get() # John Doe
        Age = age_box.get() # 23
        Address = home_address.get() # 21 Hillary Street, Clinton Close, Der Bay
        City = city.get() # Liverpool
        Country = country.get() # England
        Email = email.get() # johndoe23@email.com
        EmailPassword = emailPassword.get() #*********
        import base64
        # EmailPassword = base64.b64encode(EmailPassword.encode())
        Telephone = telephone.get() # 123456789

        GUM = (Name + " aged " + Age + " resides at " + Address + ", " + City + ", " + Country + ". " + Name + " can be contacted by both Email & Telephone. Email: " + Email + " & Telephone: " + Telephone) # Generate User Model - GUM
        print(GUM)
        GUM_File = open("userdata\\GUM.bd", "w")
        GUM_File.write(f"{Name}\n{Age}\n{Address}\n{City}\n{Country}\n{Email}\n{EmailPassword}\n{Telephone}")
        GUM_File.close()

    section1 = tk.Label(WindowFrame, text="You & Your Data", font=Font(family="Roboto", size=80, weight="bold"))
    section1.pack(pady=30)

    name_box_label = tk.Label(WindowFrame, text="Adjust the way you want to be addressed")
    name_box_label.pack()
    name_box = ttk.Entry(WindowFrame, width=20)
    name_box.insert(0, UserName)
    name_box.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Edit")
    edit_button.pack()

    age_box_label = tk.Label(WindowFrame, text="Add Age")
    age_box_label.pack()
    age_box = ttk.Entry(WindowFrame, width=20)
    age_box.insert(0, "")
    age_box.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    home_address_label = tk.Label(WindowFrame, text="Add Home Address")
    home_address_label.pack()
    home_address = ttk.Entry(WindowFrame, width=20)
    home_address.insert(0, "")
    home_address.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    city_label = tk.Label(WindowFrame, text="Add City")
    city_label.pack()
    city = ttk.Entry(WindowFrame, width=20)
    city.insert(0, "")
    city.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    country_label = tk.Label(WindowFrame, text="Add Country")
    country_label.pack()
    country = ttk.Entry(WindowFrame, width=20)
    country.insert(0, "")
    country.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    email_label = tk.Label(WindowFrame, text="Add Email")
    email_label.pack()
    email = ttk.Entry(WindowFrame, width=20)
    email.insert(0, "")
    email.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    emailPassword_label = tk.Label(WindowFrame, text="Add Email")
    emailPassword_label.pack()
    emailPassword = ttk.Entry(WindowFrame, width=20)
    emailPassword.insert(0, "")
    # emailPassword.replace("", *)
    emailPassword.pack()
    edit_Password_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_Password_button.pack()

    telephone_label = tk.Label(WindowFrame, text="Add Telephone Number")
    telephone_label.pack()
    telephone = ttk.Entry(WindowFrame, width=20)
    telephone.insert(0, "")
    telephone.pack()
    edit_button = ttk.Button(WindowFrame, command=getUserData, text="Add")
    edit_button.pack()

    seperater = tk.Label(WindowFrame, text="____________________________________________________________________________________________________________________________")
    seperater.pack()


    # Personalisation
    # section2 = tk.Label(WindowFrame, text="Personalization", font=Font(family="Roboto", size=80, weight="bold"))
    # section2.pack()
    # tk.Label(WindowFrame, text="Change View").pack()

    # miniView = ttk.Button(WindowFrame, text="Mini View")
    # miniView.pack(pady=5)

    # productiveView = ttk.Button(WindowFrame, text="Productive View")
    # productiveView.pack(pady=5)

    # desktopView = ttk.Button(WindowFrame, text="Desktop View")
    # desktopView.pack(pady=5)

    # seperater = tk.Label(WindowFrame, text="____________________________________________________________________________________________________________________________")
    # seperater.pack()


    # Others
    section3 = tk.Label(WindowFrame, text="Others", font=Font(family="Roboto", size=80, weight="bold"))
    section3.pack()

    tk.Label(WindowFrame, text="Usage & Handling of your data").pack()

    tk.Label(WindowFrame, text="Handling the data you provide to alex\nwhile stressing data privacy is crucial.\nAlex follows these principles to ensure\nyour data is kept safe:\n1.) Data Minimization: Collect only the\nnecessary data for the assistant's\nfunctioning.\n2.) Anonymization: Remove personally identifiable\ninformation if not needed.\n3.) Data Encryption: Store sensitive data in\nencrypted form.\n4.) User Consent: Obtain clear and informed consent\nfor data collection.\n5.) Transparency: Clearly communicate how data will\nbe used.\n6.) Regular Auditing: Regularly review and update\nprivacy practices.").pack()

    WindowFrame.update_idletasks()
    settingCanvas.config(scrollregion=settingCanvas.bbox("all"))

    settingCanvas.pack(fill='both', expand=True, side='left')
    # scroll_y.pack(fill='y', side='right')

    # WindowFrame.pack() # side=tk.LEFT

    settingWin.mainloop()

def internetStatusCheck():

    def is_connected():
        try:
            # Connect to a well-known host (like Google's DNS server)
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            pass
        return False

    # Check for internet connection
    if is_connected():
        internetStatusCheckLb.destroy()
        # internetStatusGood = tk.Label(homeWin, text="Connected", bg="lime", fg="black", font=Font(family="Roboto", size=10, weight="bold"))
        # internetStatusGood.pack(anchor="se")
        MIC_BUTTON = tk.Button(homeWin, image=MIC_IMG, command=listen, border=0)
        MIC_BUTTON.pack(anchor="s", side="bottom")
        # homeWin.after(1000, internetStatusCheck)
    else:
        internetStatusCheckLb.destroy()
        internetStatusBad = tk.Label(homeWin, text="Not Connected", bg="red", fg="white", font=Font(family="Roboto", size=10, weight="bold"))
        internetStatusBad.pack(anchor="s", side="bottom")
        # MIC_BUTTON = tk.Button(homeWin, image=MIC_IMG_RED, command=listen, border=0)
        # MIC_BUTTON.pack(anchor="s", side="bottom")
        # homeWin.after(1000, internetStatusCheck)
    

internetStatusCheckLb = tk.Label(homeWin, text="Internet Status", bg="blue", fg="white", font=Font(family="Roboto", size=10, weight="bold"))
internetStatusCheckLb.pack(anchor="se")

internetStatusCheck()
# app_logo = tk.PhotoImage(file="data\\alexlibs\\MEDIA\\alex-light.png")
app_logo_label = tk.Label(homeWin, text="alex", font=("Britannic Bold", 40, "bold"), fg="#081734")
app_logo_label.pack(side="top", anchor="nw")

hamburger = tk.PhotoImage(file="MEDIA\\icons8-xbox-menu-50.png")
trigger_settings = tk.Button(homeWin, image=hamburger, border="0", command=trigger_settings)
trigger_settings.pack(side="top", anchor="ne")

#Time
def update_time():
    current_time = datetime.now().strftime("%H:%M")
    time_label.config(text=current_time, font=Font(family="Roboto", size=40, weight="bold"))
    homeWin.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Label to display the time
time_label = tk.Label(homeWin, text="", font=("Helvetica", 24), fg="#081734")
time_label.pack(side="top")

# Initial call to update_time to start the time display
update_time()

def removeWelcomeText():
    welcomeText.destroy()

# Welcome Text
roboto_bold_font = Font(family="Roboto", size=20)
welcomeText = tk.Label(homeWin, text=(ra.choice(greeting)).replace("\n", " "), font=roboto_bold_font)
welcomeText.pack(pady=10)

welcomeText.after(5000, removeWelcomeText)

# Initializing the Scrollbar
chatCanvas = tk.Canvas(homeWin, border=1, width=False)
scroll_y = tk.Scrollbar(homeWin, bg="lightblue", command=chatCanvas.yview, border=0)
scroll_y.pack(side="right", fill="y")

# Chat Frame
chat_Frame = tk.Frame(chatCanvas, bg="#081734")
chatCanvas.create_window((0, 0), window=chat_Frame)
# chat_Frame.pack(anchor="center", fill=tk.BOTH)

# Create a label to display the imageb
# bg_Frame = tk.Label(chat_Frame, image=imageCF)
# bg_Frame.place(relwidth=1, relheight=1)
tk.Label(chat_Frame, text="                                Chat                               ", bg="#081734", fg="white", font=("Roboto", 20)).pack(anchor="center")
start_chat_message = tk.Label(chat_Frame, text=ra.choice(["+ Start a conversation", "Chats would show up here"]), fg="white", bg="#081734")
start_chat_message.pack(pady=250)

searchFrame = tk.Frame(homeWin)
searchFrame.pack(side=tk.BOTTOM)


tasking_bar = ttk.Entry(searchFrame, width=50)
tasking_bar.insert(0, "")
tasking_bar.pack(side=tk.LEFT)



suggestFrame = ttk.Frame(homeWin)
suggestFrame.pack(anchor="s", side="bottom")


# BUT_IMG = tk.PhotoImage(file="data\\alexlibs\\MEDIA\\icons8-go-50.png")



def processUserInput():
    # userInput = u
    def saveUserPattern():
        user = tasking_bar.get()
        with open("data\\learned.bd", "a") as learnFile:
            learnFile.write(user + "\t" + "\n")

    saveUserPattern()

    start_chat_message.destroy()
    userInput = tasking_bar.get()
    # userInput =
    print("User Input: " + userInput)

    with open("data\\brain-nlp.json") as NLPFile:

        conversation_dict = json.load(NLPFile)
    
    with open("data\\brain-nlp-response.json") as NLPFile2:

        response_dict = json.load(NLPFile2)


    # conversDictToJson = json.dumps(conversation_dict)
    # responsDictToJson = json.dumps(response_dict)

    # NLPFile = open("data\\brain-nlp.json", "a")
    # NLPFile.write(conversDictToJson)
    # NLPFile.close()

    # NLPFile2 = open("data\\brain-nlp-response.json", "a")
    # NLPFile2.write(responsDictToJson)
    # NLPFile2.close()

    if 'and' in userInput:
        userInput = ((((str(userInput.replace("and", "").split()).replace("['", "")).replace("', '", "\n")).replace("']", "")))
        user_input = userInput.lower()
        user_input_N = user_input
    else:
        user_input = (userInput.lower()).replace("\n", " ")
        user_input_N = user_input

    
    if 'how to' in user_input:
        if "how to" in user_input:
            user_input = user_input.replace("how to ", "")
            bs.howToSearch(user_input)
        else:
            bs.normalSearch(user_input, search_engine="google")

    # bs.normalSearch(user_input, search_engine="google")

    def get_response(input_text):
        def errorProcessing():
            def learnUserError():

                # learnt_response = "hey"

                with open("data\\learned.bd") as learnFile2:
                    data = learnFile2.read()

                # Tokenize words (split by non-word characters)
                commonWords = re.findall(r'\w+', data.lower())

                # Count the occurrences of each word
                word_count = Counter(commonWords)

                # Get the most common word
                most_common_word = user_input #word_count.most_common(1)[0]
                # print(f"The most common word is '{most_common_word[0]}' with {most_common_word[1]} occurrences.")

                with open("data\\brain-nlp.json") as NLPFile:

                    conversation_dict = json.load(NLPFile)
                
                with open("data\\brain-nlp-response.json") as NLPFile2:

                    response_dict = json.load(NLPFile2)

                
                for conversationTag, convKeyword in conversation_dict.items():
                    for convKw in convKeyword:
                        # print(convKw)
                        # Load JSON file into a dictionary
                        with open('data\\brain-nlp.json', 'r') as file:
                            File = json.load(file)

                        # Add a new item
                        # new_item = {'word': f'{most_common_word[0]}'}
                        File['learnt error'] = f'{most_common_word}'

                        # Write the updated dictionary back to the JSON file
                        with open('data\\brain-nlp.json', 'w') as file:
                            json.dump(File, file, indent=4)

                        print("Successfully added!")

                if f"{most_common_word} is" in user_input:
                    meaning_of_error = (f"{most_common_word} is").replace(f"{most_common_word} is", "")

                    with open('data\\brain-nlp-response.json', 'r') as file:
                        respFile = json.load(file)

                    # Add a new item
                    # new_item = {'word': f'{short_answer}'}
                    respFile['learnt error'] = [f'Well {most_common_word} is {meaning_of_error}', f'According to you, {most_common_word} is {meaning_of_error}', f'{meaning_of_error}']

                    # Write the updated dictionary back to the JSON file
                    with open('data\\brain-nlp-response.json', 'w') as file:
                        json.dump(respFile, file, indent=4)

                def is_connected():
                    try:
                        # Connect to a well-known host (like Google's DNS server)
                        socket.create_connection(("8.8.8.8", 53))
                        return True
                    except OSError:
                        pass
                    return False

                # Check for internet connection
                if is_connected():
                    def get_short_answer(query):
                        url = f"https://api.duckduckgo.com/?q={query}&format=json"
                        response = requests.get(url)
                        data = response.json()
                        if 'AbstractText' in data:
                            return data['AbstractText']
                        else:
                            return "No short answer found."

                    query = "Your question goes here"
                    short_answer = get_short_answer(most_common_word)
                    with open('data\\brain-nlp-response.json', 'r') as file:
                        respFile = json.load(file)

                    # Add a new item
                    # new_item = {'word': f'{short_answer}'}
                    respFile['learnt error'] = [f'{short_answer}', f'{short_answer}', f'{short_answer}']

                    # Write the updated dictionary back to the JSON file
                    with open('data\\brain-nlp-response.json', 'w') as file:
                        json.dump(respFile, file, indent=4)

                    # print(short_answer)
                else:
                    with open('data\\brain-nlp-response.json', 'r') as file:
                        respFile = json.load(file)

                    # Add a new item
                    # new_item = {'word': f'{most_common_word[0]}'}
                    respFile['learnt error'] = [f'What is {most_common_word}?', f'Explain {most_common_word}', f'I dont seem to know {most_common_word}, what is it?']

                    # Write the updated dictionary back to the JSON file
                    with open('data\\brain-nlp-response.json', 'w') as file:
                        json.dump(respFile, file, indent=4)
                        
                    # print(short_answer)
                            
            learnUserError()
            # User Text
            usertext_Label = tk.Label(chat_Frame, text=userInput, bg="#081734", fg="white", font=("Roboto", 10))
            usertext_Label.pack(anchor="nw")
            
            # Alex Response
            response_Label = tk.Label(chat_Frame, text=(ra.choice(["Didn't quite get that!\nI'll search the web for you", "Opening the web", "The Web might produce\naccurate results", f"Searching the web\nfor {input_text}"])), bg="orange", fg="white", font=("Roboto", 10))

            response_Label.pack(anchor="se", pady=5)
            # Text to be converted to speech
            response_Voiced = (ra.choice(["Didn't quite get that!\nI'll search the web for you", "Opening the web", "The Web might produce\naccurate results", f"Searching the web\nfor {input_text}"]))

            # Convert text to speech
            engine.say(response_Voiced)

            # Wait for speech to finish
            engine.runAndWait()

            def search_on_search_engine(query, search_engine="google"):
                search_query = query.replace(" ", "+")
                
                if search_engine == "google":
                    url = f"https://www.google.com/search?q={search_query}"
                elif search_engine == "bing":
                    url = f"https://www.bing.com/search?q={search_query}"
                elif search_engine == "duckduckgo":
                    url = f"https://duckduckgo.com/?q={search_query}"
                else:
                    raise ValueError("Unsupported search engine")
                
                webbrowser.open(url)

            search_query = input_text

            # Choose a search engine: "google", "bing", or "duckduckgo"
            search_engine = "google"

            search_on_search_engine(search_query, search_engine)

        if "find" in user_input_N:
            print("Validating Search2")
            
            def search_file(file_name, search_path):
                for root, dirs, files in os.walk(search_path):
                    if file_name in files:
                        return os.path.join(root, file_name)
                return None

            file_name_to_search = user_input_N.replace("find ", "")
            search_directory = "C:\\"

            found_path = search_file(file_name_to_search, search_directory)

            if found_path:
                response_Label = tk.Label(chat_Frame, text=ra.choice([f"Found {file_name_to_search}, Opening", "Found, Opening"]), bg="green", fg="white", font=("Roboto", 10))
                response_Label.pack(anchor="se", pady=5)
                subprocess.run(f"explorer {found_path}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                engine.say(ra.choice([f"Found {file_name_to_search}, Opening", "Found, Opening"]))
                engine.runAndWait()
            else:
                response_Label = tk.Label(chat_Frame, text=ra.choice([f"Sorry, no matches of {file_name_to_search} found", f"Nope, I Didn't find {file_name_to_search}"]), bg="orange", fg="white", font=("Roboto", 10))
                response_Label.pack(anchor="se", pady=5)
                engine.say(ra.choice([f"Sorry, no matches of {file_name_to_search} found", f"Nope, I Didn't find {file_name_to_search}"]))
                engine.runAndWait()

        if "my location" in user_input:
            with open("userdata\\GUM.bd", "r") as userData:
                line1 = userData.readline()
                line2 = userData.readline()
                line3 = userData.readline()
                line4 = userData.readline()
                line5 = userData.readline()
                line6 = userData.readline()
                line7 = userData.readline()

            userLocation = (line3 + " " + line4 + " " + line5).replace("\n", "")

            def locateUser(location):
                refinedLocation = location.replace(" ", "+")
                link = f"https://www.google.com/maps/search/{refinedLocation}/@6.5993602,3.1016324,10z/data=!3m1!4b1?entry=ttu"
                webbrowser.open(link)

            locateUser(location=userLocation)
            engine.say(ra.choice([f"{UserName}, here's your location: {userLocation}", "Here", f"According to your data, its...........{userLocation}"]))
            engine.runAndWait()

        if "search for" in user_input_N:
            def search_file(file_name, search_path):
                for root, dirs, files in os.walk(search_path):
                    if file_name in files:
                        return os.path.join(root, file_name)
                return None

                file_name_to_search = user_input_N.replace("search for ", "")
                search_directory = "C:\\"

                found_path = search_file(file_name_to_search, search_directory)

                if found_path:
                    response_Label = tk.Label(chat_Frame, text=ra.choice([f"Found {file_name_to_search}, Opening", "Found, Opening"]), bg="green", fg="white", font=("Roboto", 10))
                    subprocess.run(f"explorer {found_path}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                    response_Label.pack(anchor="se", pady=5)
                    engine.say(ra.choice([f"Found {file_name_to_search}, Opening", "Found, Opening"]))
                    engine.runAndWait()
                else:
                    response_Label = tk.Label(chat_Frame, text=ra.choice([f"Sorry, no matches of {file_name_to_search} found", f"Nope, I Didn't find {file_name_to_search}"]), bg="orange", fg="white", font=("Roboto", 10))
                    response_Label.pack(anchor="se", pady=5)
                    engine.say(ra.choice([f"Sorry, no matches of {file_name_to_search} found", f"Nope, I Didn't find {file_name_to_search}"]))
                    engine.runAndWait()

        if "say this" in user_input:

            text_to_speak = user_input.replace("say this ", "")
            engine.say(text_to_speak)
            engine.runAndWait()

            response_Label = tk.Label(chat_Frame, text=f"Said: '{text_to_speak}'", bg="green", fg="white", font=("Roboto", 10))
            response_Label.pack(anchor="se", pady=5)

        if 'combo' == user_input:
            cb.ComboApp()
            engine.say(ra.choice(["Launching combo app ", "Opening", "Opening combo"]))
            engine.runAndWait()

        if "load" in user_input:
            if "load" in user_input:
                with open("data\\comboApps.json") as ComApp:
                    ComApp_dict = json.load(ComApp)

                for appTag, appPath in ComApp_dict.items():
                    if (f"load {appTag}") == user_input:
                        with open("data\\combolist.bd", "r") as CBFile:
                            app1 = CBFile.readline()
                            app2 = CBFile.readline()
                            app2 = app2.replace("',)", "")
                            app3 = CBFile.readline()
                            # app4 = CBFile.readline()
                            # app5 = CBFile.readline()

                        subprocess.run(f'"{app1}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                        subprocess.run(f'"{app2}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                        subprocess.run(f'"{app3}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                return appTag
            else:
                engine.say(ra.choice([f"sorry {UserName} Couldn't find combo with the name {appTag}", "no combo's found with that name, try creating a new combo with that name", f"sorry {UserName}, i've searched and found no combo saved with that name"]))
                engine.runAndWait()

        if "load last combo" == user_input:
            engine.say(ra.choice([f"loading last combo {UserName}", f"{UserName}, sit back and relax while i load your last combo", "Opening last combo"]))
            engine.runAndWait()
            with open("data\\combolist.bd", "r") as CBFile:
                app1 = CBFile.readline()
                app2 = CBFile.readline()
                app2 = app2.replace("',)", "")
                app3 = CBFile.readline()
                # app4 = CBFile.readline()
                # app5 = CBFile.readline()

            subprocess.run(f'"{app1}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            subprocess.run(f'"{app2}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            subprocess.run(f'"{app3}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            # subprocess.run(f'"{app4}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            # subprocess.run(f'"{app5}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            

        if user_input in conversation_dict['Exit App']:
            engine.say([f"Goodbye {UserName}", "Closing"])
            engine.runAndWait()
            homeWin.destroy()

        if user_input in conversation_dict['Shutdown']:
            subprocess.run("shutdown /s", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        if user_input in conversation_dict['AlexNotes']:
            alexNotes.NoteApp()

        if user_input in conversation_dict['Emails']:
            alexEmail.sendEmail()

        if user_input in conversation_dict['AlexNyze']:
            try:
                AlexNyze()
            except Exception as e:
                response_Label = tk.Label(chat_Frame, text=f"{e}\nTry Opening it from the 'Tools'", bg="orange", fg="white", font=("Roboto", 10))
                response_Label.pack(anchor="se", pady=5)

        for key, values in conversation_dict.items():
            for value in values:
                print("Value: " + value)
                # if value in conversation_dict['AlexNotes']:
                #     alexNotes.NoteApp()

                # if value in conversation_dict['Emails']:
                #     alexEmail.sendEmail()

                if value in conversation_dict['translate text']:
                    if "french" in user_input:
                        try:
                            translator = Translator(to_lang="fr")  # Translate to French
                            text_to_translate = user_input.replace("translate this to french", "")

                            translated_text = translator.translate(text_to_translate)
                            response_Label = tk.Label(chat_Frame, text=translated_text, bg="green", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                            # print("Translated:", translated_text)
                        except Exception:
                            response_Label = tk.Label(chat_Frame, text=ra.choice(["Please connect to the internet for\ntranslation features", f"{UserName}, i can't translate without the internet"]), bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "spanish" in user_input:
                        try:
                            translator = Translator(to_lang="sp")  # Translate to French
                            text_to_translate = user_input.replace("translate this to spanish", "")

                            translated_text = translator.translate(text_to_translate)
                            response_Label = tk.Label(chat_Frame, text=translated_text, bg="green", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                            # print("Translated:", translated_text)
                        except Exception:
                            response_Label = tk.Label(chat_Frame, text=ra.choice(["Please connect to the internet for\ntranslation features", f"{UserName}, i can't translate without the internet"]), bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "latin" in user_input:
                        try:
                            translator = Translator(to_lang="lt")  # Translate to French
                            text_to_translate = user_input.replace("translate this to latin", "")

                            translated_text = translator.translate(text_to_translate)
                            response_Label = tk.Label(chat_Frame, text=translated_text, bg="green", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                            # print("Translated:", translated_text)
                        except Exception:
                            response_Label = tk.Label(chat_Frame, text=ra.choice(["Please connect to the internet for\ntranslation features", f"{UserName}, i can't translate without the internet"]), bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "english" in user_input:
                        try:
                            translator = Translator(to_lang="en")  # Translate to French
                            text_to_translate = user_input.replace("translate this to english", "")

                            translated_text = translator.translate(text_to_translate)
                            response_Label = tk.Label(chat_Frame, text=translated_text, bg="green", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                            # print("Translated:", translated_text)
                        except Exception:
                            response_Label = tk.Label(chat_Frame, text=ra.choice(["Please connect to the internet for\ntranslation features", f"{UserName}, i can't translate without the internet"]), bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                if value in conversation_dict['Reminder & Alarms']:
                    """
                    😂😂😂Just testing Docstrings
                    """
                    
                    if "set a reminder to" in user_input:
                        tuned_user_input = user_input.replace("set a reminder to", "")
                        class ReminderApp:
                            def __init__(self, alarmBox):
                                self.alarmBox = alarmBox
                                self.alarmBox.title("Reminders & Alarms")

                                self.label = tk.Label(alarmBox, text="Set Reminder:")
                                self.label.pack()

                                self.reminder_entry = ttk.Entry(alarmBox)
                                self.reminder_entry.insert(0, f"{tuned_user_input}")
                                self.reminder_entry.pack()

                                ttk.Label(alarmBox, text="How many mins from now").pack()
                                self.reminder_time_inquire = ttk.Entry(alarmBox)
                                self.reminder_time_inquire.insert(0, "1")
                                self.reminder_time_inquire.pack()

                                self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
                                self.set_button.pack()

                            def set_reminder(self):
                                def setReminder():
                                    reminder_text = self.reminder_entry.get()
                                    if reminder_text:
                                        current_time = datetime.now()

                                        reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                                        threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
                                setReminder()

                                # generateRecent("Reminder", setReminder)
                            def wait_and_show_reminder(self, reminder_time, reminder_text):
                                while datetime.now() < reminder_time:
                                    time.sleep(1)
                                
                                toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
                                messagebox.showinfo(f"{tuned_user_input}", reminder_text)
                                

                                
                        if __name__ == "__main__":
                            alarmBox = tk.Tk()
                            app = ReminderApp(alarmBox)
                            alarmBox.mainloop()



                    elif "set a reminder for" in user_input:
                        tuned_user_input = user_input.replace("set a reminder for", "")
                        class ReminderApp:
                            def __init__(self, alarmBox):
                                self.alarmBox = alarmBox
                                self.alarmBox.title("Reminders & Alarms")

                                self.label = tk.Label(alarmBox, text="Set Reminder:")
                                self.label.pack()

                                self.reminder_entry = ttk.Entry(alarmBox)
                                self.reminder_entry.insert(0, f"{tuned_user_input}")
                                self.reminder_entry.pack()

                                ttk.Label(alarmBox, text="How many mins from now").pack()
                                self.reminder_time_inquire = ttk.Entry(alarmBox)
                                self.reminder_time_inquire.insert(0, "1")
                                self.reminder_time_inquire.pack()

                                self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
                                self.set_button.pack()

                            def set_reminder(self):
                                def setReminder():
                                    reminder_text = self.reminder_entry.get()
                                    if reminder_text:
                                        current_time = datetime.now()

                                        reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                                        threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
                                setReminder()

                                # generateRecent("Reminder", setReminder)
                            def wait_and_show_reminder(self, reminder_time, reminder_text):
                                while datetime.now() < reminder_time:
                                    time.sleep(1)

                                toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
                                messagebox.showinfo(f"{tuned_user_input}", reminder_text)

                                
                        if __name__ == "__main__":
                            alarmBox = tk.Tk()
                            app = ReminderApp(alarmBox)
                            alarmBox.mainloop()

                    elif "set reminder to" in user_input:
                        tuned_user_input = user_input.replace("set reminder to", "")
                        class ReminderApp:
                            def __init__(self, alarmBox):
                                self.alarmBox = alarmBox
                                self.alarmBox.title("Reminders & Alarms")

                                self.label = tk.Label(alarmBox, text="Set Reminder:")
                                self.label.pack()

                                self.reminder_entry = ttk.Entry(alarmBox)
                                self.reminder_entry.insert(0, f"{tuned_user_input}")
                                self.reminder_entry.pack()

                                ttk.Label(alarmBox, text="How many mins from now").pack()
                                self.reminder_time_inquire = ttk.Entry(alarmBox)
                                self.reminder_time_inquire.insert(0, "1")
                                self.reminder_time_inquire.pack()

                                self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
                                self.set_button.pack()

                            def set_reminder(self):
                                def setReminder():
                                    reminder_text = self.reminder_entry.get()
                                    if reminder_text:
                                        current_time = datetime.now()

                                        reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                                        threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
                                setReminder()

                                # generateRecent("Reminder", setReminder)
                            def wait_and_show_reminder(self, reminder_time, reminder_text):
                                while datetime.now() < reminder_time:
                                    time.sleep(1)
                                
                                toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
                                messagebox.showinfo(f"{tuned_user_input}", reminder_text)

                                
                        if __name__ == "__main__":
                            alarmBox = tk.Tk()
                            app = ReminderApp(alarmBox)
                            alarmBox.mainloop()


                    elif "set reminder for" in user_input:
                        tuned_user_input = user_input.replace("set reminder for", "")
                        class ReminderApp:
                            def __init__(self, alarmBox):
                                self.alarmBox = alarmBox
                                self.alarmBox.title("Reminders & Alarms")

                                self.label = tk.Label(alarmBox, text="Set Reminder:")
                                self.label.pack()

                                self.reminder_entry = ttk.Entry(alarmBox)
                                self.reminder_entry.insert(0, f"{tuned_user_input}")
                                self.reminder_entry.pack()

                                ttk.Label(alarmBox, text="How many mins from now").pack()
                                self.reminder_time_inquire = ttk.Entry(alarmBox)
                                self.reminder_time_inquire.insert(0, "1")
                                self.reminder_time_inquire.pack()

                                self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
                                self.set_button.pack()

                            def set_reminder(self):
                                def setReminder():
                                    reminder_text = self.reminder_entry.get()
                                    if reminder_text:
                                        current_time = datetime.now()

                                        reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                                        threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
                                setReminder()

                                # generateRecent("Reminder", setReminder)
                            def wait_and_show_reminder(self, reminder_time, reminder_text):
                                while datetime.now() < reminder_time:
                                    time.sleep(1)

                                toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
                                messagebox.showinfo(f"{tuned_user_input}", reminder_text)

                                
                        if __name__ == "__main__":
                            alarmBox = tk.Tk()
                            app = ReminderApp(alarmBox)
                            alarmBox.mainloop()

                    elif "set an alarm for" in user_input:
                        tuned_user_input = user_input.replace("set an alarm for", "")
                        class ReminderApp:
                            def __init__(self, alarmBox):
                                self.alarmBox = alarmBox
                                self.alarmBox.title("Reminders & Alarms")

                                self.label = tk.Label(alarmBox, text="Set Reminder:")
                                self.label.pack()

                                self.reminder_entry = ttk.Entry(alarmBox)
                                self.reminder_entry.insert(0, f"{tuned_user_input}")
                                self.reminder_entry.pack()

                                ttk.Label(alarmBox, text="How many mins from now").pack()
                                self.reminder_time_inquire = ttk.Entry(alarmBox)
                                self.reminder_time_inquire.insert(0, "1")
                                self.reminder_time_inquire.pack()

                                self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
                                self.set_button.pack()

                            def set_reminder(self):
                                def setReminder():
                                    reminder_text = self.reminder_entry.get()
                                    if reminder_text:
                                        current_time = datetime.now()

                                        reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                                        threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
                                setReminder()

                                # generateRecent(f"Alarm - {tuned_user_input}", setReminder)
                            def wait_and_show_reminder(self, reminder_time, reminder_text):
                                while datetime.now() < reminder_time:
                                    time.sleep(1)
                                
                                toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
                                messagebox.showinfo(f"{tuned_user_input}", reminder_text)


                                
                        if __name__ == "__main__":
                            alarmBox = tk.Tk()
                            app = ReminderApp(alarmBox)
                            alarmBox.mainloop()


                # Calculations
                if value in conversation_dict['Simple Arithimetic(+ & -)']:
                    print("Analyzing + & -")
                    if "+" in user_input:
                        # Addition
                        problem = user_input
                        problem_LH = re.split("[+]", problem)
                        number_of_values = len(problem_LH)
                        if number_of_values == 2:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            Answer = str(num1 + num2)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            #a globalVar(Answer)


                        elif number_of_values == 3:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            Answer = str(num1 + num2 + num3)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 4:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            Answer = str(num1 + num2 + num3 + num4)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 5:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            Answer = str(num1 + num2 + num3 + num4 + num5)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 6:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            Answer = str((num1 + num2 + num3 + num4 + num5 + num6))
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 7:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 8:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 9:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 10:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 11:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            
                            
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 12:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 13:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            
                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 14:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])

                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 15:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])

                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 16:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])

                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 17:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])

                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16 + num17)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 18:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])
                            num18 = int(problem_LH[17])

                            Answer = str(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16 + num17 + num18)
                            Answer_list = f"Here's the solution: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        # print(Answer)

                    elif "-" in user_input:
                        # Subtraction
                        problem = user_input
                        problem_LH = re.split("[-]", problem)
                        number_of_values = len(problem_LH)
                        if number_of_values == 2:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            Answer = str(num1 - num2)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            #a globalVar(Answer)


                        elif number_of_values == 3:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            Answer = str(num1 - num2 - num3)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 4:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            Answer = str(num1 - num2 - num3 - num4)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 5:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            Answer = str(num1 - num2 - num3 - num4 - num5)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 6:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            Answer = str((num1 - num2 - num3 - num4 - num5 - num6))
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 7:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 8:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 9:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 10:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 11:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            
                            
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 12:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 13:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            
                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 14:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])

                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 15:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])

                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 16:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])

                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15 - num16)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 17:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])

                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15 - num16 - num17)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 18:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])
                            num18 = int(problem_LH[17])

                            Answer = str(num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15 - num16 - num17 - num18)
                            Answer_list = f"It'll give: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)

                if value in conversation_dict['Simple Arithimetic(* & /)']:
                    print("Analyzing * & /")
                    if "*" in user_input:
                        # Multiplication
                        problem = user_input
                        problem_LH = re.split("[*]", problem)
                        number_of_values = len(problem_LH)
                        if number_of_values == 2:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            Answer = str(num1 * num2)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            #a globalVar(Answer)


                        elif number_of_values == 3:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            Answer = str(num1 * num2 * num3)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 4:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            Answer = str(num1 * num2 * num3 * num4)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 5:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            Answer = str(num1 * num2 * num3 * num4 * num5)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 6:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            Answer = str((num1 * num2 * num3 * num4 * num5 * num6))
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 7:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 8:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 9:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 10:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 11:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            
                            
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 12:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 13:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            
                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 14:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])

                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 15:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])

                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 16:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])

                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15 * num16)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 17:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])

                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15 * num16 * num17)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 18:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])
                            num18 = int(problem_LH[17])

                            Answer = str(num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15 * num16 * num17 * num18)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)

                    elif "/" in user_input:
                        # Division
                        problem = user_input
                        problem_LH = re.split("[/]", problem)
                        number_of_values = len(problem_LH)
                        if number_of_values == 2:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            Answer = str(num1 / num2)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            #a globalVar(Answer)


                        elif number_of_values == 3:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            Answer = str(num1 / num2 / num3)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 4:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            Answer = str(num1 / num2 / num3 / num4)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 5:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            Answer = str(num1 / num2 / num3 / num4 / num5)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 6:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            Answer = str((num1 / num2 / num3 / num4 / num5 / num6))
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 7:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 8:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 9:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 10:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 11:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            
                            
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 12:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 13:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            
                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 14:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])

                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 15:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])

                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 16:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])

                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15 / num16)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 17:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])

                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15 / num16 / num17)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)
                        elif number_of_values == 18:
                            num1 = int(problem_LH[0])
                            num2 = int(problem_LH[1])
                            num3 = int(problem_LH[2])
                            num4 = int(problem_LH[3])
                            num5 = int(problem_LH[4])
                            num6 = int(problem_LH[5])
                            num7 = int(problem_LH[6])
                            num8 = int(problem_LH[7])
                            num9 = int(problem_LH[8])
                            num10 = int(problem_LH[9])
                            num11 = int(problem_LH[10])
                            num12 = int(problem_LH[12])
                            num13 = int(problem_LH[13])
                            num14 = int(problem_LH[13])
                            num15 = int(problem_LH[14])
                            num16 = int(problem_LH[15])
                            num17 = int(problem_LH[16])
                            num18 = int(problem_LH[17])

                            Answer = str(num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15 / num16 / num17 / num18)
                            Answer_list = f"Answer is: {Answer}"
                            response_Label = tk.Label(chat_Frame, text=(Answer_list), bg="lightblue", fg="black", font=("Roboto", 10, "bold"))
                            response_Label.pack(anchor="se", pady=5)
                            # globalVar(Answer)

                if value in conversation_dict['english dictionary']:
                    if "define" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("define", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                            
                        except ModuleNotFoundError:

                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                            response_Label.pack(anchor="se", pady=5)

                    if "Define" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("define", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                            
                        except ModuleNotFoundError:

                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "DEFINE" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("define", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                            
                        except ModuleNotFoundError:

                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "explain" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("explain", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                            
                        except ModuleNotFoundError:

                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "Explain" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("explain", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                            
                        except ModuleNotFoundError:

                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)
                    if "EXPLAIN" in user_input:
                        try:
                            wordToDefine = (user_input.lower()).replace("explain", "")
                            definition = wordnet.synsets(wordToDefine)

                            # Display meanings/definitions of the word from different synsets
                            for synset in synsets:
                                print(f"Definition from {definition.name()}: {definition.definition()}")

                            response_Label = tk.Label(chat_Frame, text=definition.definition(), bg="green", fg="black", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                            # Text to be converted to speech
                            response_Voiced = ((definition.definition()).replace("\n", " "))
                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()

                        except NameError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)                          
                        
                        except ModuleNotFoundError:
                            response_Label = tk.Label(chat_Frame, text="An error has occurred\nStart me again and wait\nfor me to properly load my\nlibraries.", bg="red", fg="white", font=("Roboto", 10))
                            response_Label.pack(anchor="se", pady=5)

                if value in conversation_dict['Open apps']:
                    print("Validating this one")
                    app_to_open = value
                    print("(O)Open this app: " + app_to_open)
                    if "launch" in user_input:
                        app_to_open = user_input.replace("launch", " ")
                        def doThis():
                            print("(I)Open this app: " + app_to_open)
                            # Example command: lists the files and folders in the current directory

                            try:
                                result = subprocess.run(app_to_open, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                                if result.returncode == 0:
                                    print("Command output:", result.stdout)
                                else:
                                    print("Command error:", result.stderr)
                            except Exception as e:
                                print("An error occurred:", e)

                        doThis()

                        # generateRecent(f"Launch {app_to_open}", doThis)
                    elif "open" in user_input:
                        app_to_open = user_input.replace("open", " ")
                        def doThis():
                            
                            # Example command: lists the files and folders in the current directory

                            try:
                                result = subprocess.run(app_to_open, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                                if result.returncode == 0:
                                    print("Command output:", result.stdout)
                                else:
                                    print("Command error:", result.stderr)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()

                        # generateRecent(f"Open {app_to_open}", doThis)
                    elif "start" in user_input:
                        app_to_open = user_input.replace("start", " ")
                        def doThis():
                            
                            # Example command: lists the files and folders in the current directory

                            try:
                                result = subprocess.run(app_to_open, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                                if result.returncode == 0:
                                    print("Command output:", result.stdout)
                                else:
                                    print("Command error:", result.stderr)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent(f"Start {app_to_open}", doThis)

                    elif "music" in user_input:
                        def doThis():
                            app_name = "Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"  # Groove Music's package family name

                            try:
                                subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent("data\\alexlibs\\Media", doThis)
                    elif "movie" in user_input:
                        def doThis():
                            app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                            try:
                                subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent("data\\alexlibs\\Media", doThis)
                    elif "tv" in user_input:
                        def doThis():
                            app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                            try:
                                subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent("data\\alexlibs\\Media", doThis)
                    elif "video app" in user_input:
                        def doThis():
                            app_name = "Microsoft.MoviesAndTV_"  # Movies & TV package family name

                            try:
                                subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent("data\\alexlibs\\Media", doThis) 
                    elif "videos" in user_input:
         
                        def doThis():
                            app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                            try:
                                subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                            except Exception as e:
                                print("An error occurred:", e)
                        doThis()
                        # generateRecent("data\\alexlibs\\Media", doThis)
                

                print("Value: " + value)
                # refined_text = re.search(r'\b{}\b'.format(value.lower()), input_text.lower())
                
                if value in input_text:
                    from tkinter.font import Font
                    #  or re.search(r'\b{}\b'.format(value.lower()), input_text.lower())
                    # User Text
                    usertext_Label = tk.Label(chat_Frame, text=userInput, bg="white", fg="black", font=("Roboto", 10))
                    usertext_Label.pack(anchor="se")
                    
                    # Alex Response
                    sm_resp = [(response_dict[key][0]), (response_dict[key][1]), (response_dict[key][2])]
                    response_Label = tk.Label(chat_Frame, text=(ra.choice(sm_resp)), bg="black", fg="white", font=("Roboto", 10))
                    response_Label.pack(anchor="nw", pady=5)
                    # Text to be converted to speech
                    response_Voiced = (ra.choice(sm_resp).replace("\n", " "))

                    # Convert text to speech
                    engine.say(response_Voiced)

                    # Wait for speech to finish
                    engine.runAndWait()
                    return response_dict[key][0]  # Only return the first response
                # if userInput in conversation_dict['bad words']:
                #     # Alex Response
                #     sm_resp = [(response_dict[key][0]), (response_dict[key][1]), (response_dict[key][2])]
                #     response_Label = tk.Label(chat_Frame, text=(ra.choice(sm_resp)), bg="redfuck", fg="black", font=("Roboto", 10))
                #     response_Label.pack(anchor="se", pady=5)
                #     # Text to be converted to speech
                #     response_Voiced = (ra.choice(sm_resp).replace("\n", " "))

                #     # Convert text to speech
                #     engine.say(response_Voiced)

                #     # Wait for speech to finish
                #     engine.runAndWait()

        return errorProcessing()

    # Bot Inner-mind Response 😂
    response = get_response(user_input)
    # print("Bot:", response)
go_button = ttk.Button(searchFrame, text="Go ▶", command=processUserInput)
go_button.pack(side=tk.RIGHT)
def AlexNote():
    alexNotes.NoteApp()

def AlexMail():
    alexEmail.sendEmail()

def AlexNyze():
    anzRt = tk.Tk()
    anzRt.title("AlexNyze™")
    anzRt.geometry("600x400")

    
    def alexNyzeData():
        data1 = int(entry1.get())
        data2 = int(entry2.get())
        data3 = int(entry3.get())
        data4 = int(entry4.get())
        data5 = int(entry5.get())
        data6 = int(entry6.get())
        data7 = int(entry7.get())
        data8 = int(entry8.get())
        data9 = int(entry9.get())
        data10 = int(entry10.get())
        dataList = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

        mean = str(statistics.mean(dataList))
        dataMean.config(text="Mean: "+ mean)

        median = str(statistics.median(dataList))
        dataMedian.config(text="Median: "+ median)

        rangee = str((max(dataList)) - (min(dataList)))
        dataRange.config(text="Range: "+ rangee)

        mode = str(statistics.mode(dataList))
        dataMode.config(text="Mode: "+ mode)

        std = str(statistics.stdev(dataList))
        dataSD.config(text="Standard Deviation: "+ std)

        engine.say("from your data, basic insights that can be drawn are the Mean, median, mode, range and Standard Deviation")
        engine.runAndWait()


    tk.Label(anzRt, text="AlexNyze™", font=("Roboto", 20)).pack(pady=30)
    tk.Label(anzRt, text="Powerful data analyzing tool").pack(pady=5)

    # Create a Canvas widget
    anzCanvas = tk.Canvas(anzRt)
    anzCanvas.pack(side="left", fill="both", expand=True)

    # Create a Scrollbar widget and attach it to the Canvas
    scrollbar = ttk.Scrollbar(anzRt, command=anzCanvas.yview)
    scrollbar.pack(side="right", fill="y")
    anzCanvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    anzFrame = tk.Frame(anzCanvas)
    anzCanvas.create_window((0, 0), window=anzFrame, anchor="n")

    # Add content to the Frame
    
    entry1 = ttk.Entry(anzFrame)
    entry1.insert(0, "0")
    entry1.pack()

    entry2 = ttk.Entry(anzFrame)
    entry2.insert(0, "0")
    entry2.pack()

    entry3 = ttk.Entry(anzFrame)
    entry3.insert(0, "0")
    entry3.pack()

    entry4 = ttk.Entry(anzFrame)
    entry4.insert(0, "0")
    entry4.pack()

    entry5 = ttk.Entry(anzFrame)
    entry5.insert(0, "0")
    entry5.pack()

    entry6 = ttk.Entry(anzFrame)
    entry6.insert(0, "0")
    entry6.pack()

    entry7 = ttk.Entry(anzFrame)
    entry7.insert(0, "0")
    entry7.pack()

    entry8 = ttk.Entry(anzFrame)
    entry8.insert(0, "0")
    entry8.pack()

    entry9 = ttk.Entry(anzFrame)
    entry9.insert(0, "0")
    entry9.pack()

    entry10 = ttk.Entry(anzFrame)
    entry10.insert(0, "0")
    entry10.pack()

    anzBt = ttk.Button(anzFrame, text="AlexNyze data", command=alexNyzeData)
    anzBt.pack(pady=3)

    insightsFrame = tk.Frame(anzFrame)
    insightsFrame.pack(anchor="s")

    dataMean = tk.Label(insightsFrame, text="Mean: -")
    dataMean.pack()

    Median = tk.Label(insightsFrame, text="data\\alexlibs\\Median: -")
    Median.pack()

    dataMode = tk.Label(insightsFrame, text="Mode: -")
    dataMode.pack()

    dataRange = tk.Label(insightsFrame, text="Range: -")
    dataRange.pack()

    dataSD = tk.Label(insightsFrame, text="Standard Deviation: -")
    dataSD.pack()

    # Configure the Canvas scrolling region
    anzFrame.update_idletasks()
    anzCanvas.config(scrollregion=anzCanvas.bbox("all"))

    anzRt.mainloop()

engine.say((ra.choice(greeting)).replace("\n", " "))
engine.runAndWait()

txt1 = "send an email"
txt2 = "setup a combo"
txt3 = "who is sundar pichai"
txt4 = "set a reminder for\nme to go to bed"


def doSuggest1():
    engine.say("Opening email dialog")
    engine.runAndWait()
    AlexMail()

def doSuggest2():
    engine.say("Opening combo dialog")
    engine.runAndWait()
    engine.runAndWait()
    cb.ComboApp()

def doSuggest3():
    query = txt3.replace("who is\n", "")
    engine.say(f"Searching for {query}")
    engine.runAndWait()
    webbrowser.open(f"https://www.google.com/search?q={query}")

def doSuggest4():
    engine.say("Sure thing, just specify the duration")
    engine.runAndWait()
    tuned_user_input = txt4.replace("set reminder for\n", "")
    class ReminderApp:
        def __init__(self, alarmBox):
            self.alarmBox = alarmBox
            self.alarmBox.title("Reminders & Alarms")
            self.style = ThemedStyle(alarmBox)
            self.style.set_theme("arc")

            self.label = ttk.Label(alarmBox, text="Set Reminder:")
            self.label.pack()

            self.reminder_entry = ttk.Entry(alarmBox)
            self.reminder_entry.insert(0, f"{tuned_user_input}")
            self.reminder_entry.pack()

            ttk.Label(alarmBox, text="How many mins from now").pack()
            self.reminder_time_inquire = ttk.Entry(alarmBox)
            self.reminder_time_inquire.insert(0, "1")
            self.reminder_time_inquire.pack()

            self.set_button = ttk.Button(alarmBox, text="Okay", command=self.set_reminder)
            self.set_button.pack()

        def set_reminder(self):
            def setReminder():
                reminder_text = self.reminder_entry.get()
                if reminder_text:
                    current_time = datetime.now()

                    reminder_time = current_time + timedelta(minutes=(int(self.reminder_time_inquire.get())))  # Set a reminder for 1 minute from now

                    threading.Thread(target=self.wait_and_show_reminder, args=(reminder_time, reminder_text)).start()
            setReminder()

            # generateRecent("Reminder", setReminder)
        def wait_and_show_reminder(self, reminder_time, reminder_text):
            while datetime.now() < reminder_time:
                time.sleep(1)
            
            toaster.show_toast(f"{UserName}, your reminder to:", reminder_text)
            messagebox.showinfo(f"{tuned_user_input}", reminder_text)

            
    if __name__ == "__main__":
        alarmBox = tk.Tk()
        app = ReminderApp(alarmBox)
        alarmBox.mainloop()

suggestedButtons1 = ttk.Button(suggestFrame, text=f"{txt1}", command=doSuggest1).grid(column=1, row=1)

suggestedButtons2 = ttk.Button(suggestFrame, text=f"{txt2}", command=doSuggest2).grid(column=2, row=1)

suggestedButtons3 = ttk.Button(suggestFrame, text=f"{txt3}", command=doSuggest3).grid(column=3, row=1)

suggestedButtons4 = ttk.Button(suggestFrame, text=f"{txt4}", command=doSuggest4).grid(column=4, row=1)

# Menubar
def dummy_command():
    print("Menu item clicked")

homeWinMenu = tk.Menu(homeWin)
homeWin.config(menu=homeWinMenu)

file_menu2 = tk.Menu(homeWinMenu, tearoff=0)
file_menu2.add_command(label="Combo", command=lambda:cb.ComboApp())
file_menu2.add_command(label="Voice", command=lambda:bv.checkConnection())
file_menu2.add_command(label="AlexNyze", command=AlexNyze)
file_menu2.add_command(label="AlexNotes", command=AlexNote)
file_menu2.add_command(label="Send Mails", command=AlexMail)
file_menu2.add_separator()
file_menu2.add_command(label="Settings", command=trigger_settings)

homeWinMenu.add_cascade(label="Tools", menu=file_menu2)

file_menu3 = tk.Menu(homeWinMenu, tearoff=0)
file_menu3.add_command(label="Website", command=lambda:webbrowser.open("https://bluvid.000webhostapp.com"))
file_menu3.add_command(label="Documentation", command=lambda:webbrowser.open("https://bluvid.000webhostapp.com/others/alex.html"))
file_menu3.add_command(label="Developer", command=lambda:webbrowser.open("https://bluvid.000webhostapp.com/others/developer.html"))
file_menu3.add_command(label="Update", command=lambda:CheckUpdatee.runUpdateDialog())
file_menu3.add_separator()
with open("data\\aboutAlex.bd", "r") as filee:
    contentA = filee.read()
file_menu3.add_command(label="About", command=lambda:messagebox.showinfo("About Alex", f"{contentA}"))

homeWinMenu.add_cascade(label="Help", menu=file_menu3)

# Search Bar (Task Bar)
# roboto_font = Font(family="Roboto", size=10, weight="normal")
# tasking_bar_label = tk.Label(homeWin, text=ra.choice(["Type in something", "How can I assist you?", "What are we doing today?", "How may I be of assistance?"]), font=roboto_font)
# tasking_bar_label.pack()

# Seperater
seperater = tk.Label(homeWin, text="____________________________________________________________________________________________________________________________")
# seperater.pack()

# Recent Task
# recent_Frame = tk.Frame(homeWin)
# recent_Frame.pack(pady=50)

# recent_image = tk.PhotoImage(file="data\\alexlibs\\MEDIA\\recent.png")
# recent_label = tk.Label(recent_Frame, image=recent_image, border="0")
# recent_label.pack()

# do_tasks_label = tk.Label(recent_Frame, text="Recent activities you've done would show up here!", font=("Roboto", 8))
# do_tasks_label.pack(pady=20)
startRecents()


def smartTalk(): #builtResponse
    sm_resp = [f"Hey {UserName}, why not try\n'recommend snacks for me'", "Wanna do basic calculations,\nwhy not try '23100+16200'", f"{UserName} If you're stuck, you can type 'help'\nto see the range of things I can do", f"{UserName}, Wanna listen to some soothing bass? You can try 'play music'"]
    response_Label = tk.Label(chat_Frame, text=(ra.choice(sm_resp)), bg="purple", fg="white", font=("Roboto", 10))
    response_Label.pack(anchor="se", pady=5)
    # Text to be converted to speech
    response_Voiced = (ra.choice(sm_resp).replace("\n", " "))

    # Convert text to speech
    engine.say(response_Voiced)

    # Wait for speech to finish
    engine.runAndWait()
    # homeWin.after(ra.choice([300000, 500000, 600000]), smartTalk)

def learnUserPattern():

    # learnt_response = "hey"

    with open("data\\learned.bd") as learnFile2:
        data = learnFile2.read()

    # Tokenize words (split by non-word characters)
    commonWords = re.findall(r'\w+', data.lower())

    # Count the occurrences of each word
    word_count = Counter(commonWords)
    # print(word_count)
    # Get the most common word
    most_common_word = word_count.most_common(1)[0]
    print(most_common_word[0])
    # print(f"The most common word is '{most_common_word[0]}' with {most_common_word[1]} occurrences.")

    with open("data\\brain-nlp.json") as NLPFile:

        conversation_dict = json.load(NLPFile)
    
    with open("data\\brain-nlp-response.json") as NLPFile2:

        response_dict = json.load(NLPFile2)

    
    for conversationTag, convKeyword in conversation_dict.items():
        for convKw in convKeyword:
            # print(convKw)
            # Load JSON file into a dictionary
            with open('data\\brain-nlp.json', 'r') as file:
                File = json.load(file)

            # Add a new item
            # new_item = {'word': f'{most_common_word[0]}'}
            File['most occuring word'] = f'{most_common_word[0]}'

            # Write the updated dictionary back to the JSON file
            with open('data\\brain-nlp.json', 'w') as file:
                json.dump(File, file, indent=4)

            print("Successfully added!")

    def is_connected():
        try:
            # Connect to a well-known host (like Google's DNS server)
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            pass
        return False

    # Check for internet connection
    if is_connected():
        try:
            def get_short_answer(query):
                url = f"https://api.duckduckgo.com/?q={query}&format=json"
                response = requests.get(url)
                data = response.json()
            if 'AbstractText' in data:
                return data['AbstractText']
            else:
                return "No short answer found."

            query = "Your question goes here"
            short_answer = get_short_answer(most_common_word)
            with open('data\\brain-nlp-response.json', 'r') as file:
                respFile = json.load(file)

            # Add a new item
            new_item = {'word': f'{short_answer}'} # requests.exceptions.SSLError
            respFile['most occuring word'] = [f'Well {most_common_word} means {short_answer}', f'{most_common_word} is {short_answer}', f'{most_common_word} means {short_answer}', f'Well {most_common_word} is {short_answer}']

            # Write the updated dictionary back to the JSON file
            with open('data\\brain-nlp-response.json', 'w') as file:
                json.dump(respFile, file, indent=4)

            # print(short_answer)
        except requests.exceptions.SSLError as e:
            engine.say("Internet Connection is weak or not working, try reconnecting to another network")
            engine.runAndWait()
    else:
        with open('data\\brain-nlp-response.json', 'r') as file:
            respFile = json.load(file)

        # Add a new item
        # new_item = {'word': f'{most_common_word[0]}'}
        respFile['most occuring word'] = [f'{most_common_word[0]}?', f'{most_common_word[0]}?', f'{most_common_word[0]}?' ]

        # Write the updated dictionary back to the JSON file
        with open('data\\brain-nlp-response.json', 'w') as file:
            json.dump(respFile, file, indent=4)
            
        # print(short_answer)


                
learnUserPattern()
def prepareUserData():
    with open("userdata\\GUM.bd", "r") as userData:
        line1 = userData.readline()
        line2 = userData.readline()
        line3 = userData.readline()
        line4 = userData.readline()
        line5 = userData.readline()
        line6 = userData.readline()
        line7 = userData.readline()

    userLocation = (line3 + " " + line4 + " " + line5).replace("\n", "")
    try:    
        userAge = int(line2)
    except ValueError:
        # firstTime.firstTimeT()
        engine.say("yOU HAVE TO FILL IN THE DETAILS IN THE FIRSTIME SCREEN")
        engine.runAndWait()

prepareUserData()
# learnUserPattern()
# smartTalk()
homeWin.after(500000, smartTalk)

# recent_activity = tk.Button(recent_Frame, text="RecentText", font=("Roboto", 10), bg="white", fg=ra.choice(["blue", "red", "lightblue", "orange", "green", "lime"]), border="0", width="50")
# recent_activity.pack(pady=20) # Template for recent activities when they're created.

chat_Frame.update_idletasks()
chatCanvas.config(scrollregion=chatCanvas.bbox("all"))
chatCanvas.pack(fill=tk.BOTH, expand=True)
# chat_Frame.pack(anchor="center")



# homeWin.after(1000, internetStatusCheck)
homeWin.mainloop()