import pyttsx3
import tkinter as tk
from tkinter import ttk, filedialog
from datetime import timedelta
from datetime import datetime
import subprocess
import re
from tkinter import messagebox
import random as ra
import socket
from data.alexlibs import alexEmail
from data.alexlibs import alexNotes
import webbrowser
import datetime
import threading
import json
import time

engine = pyttsx3.init()

# Set properties (optional)
# engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

with open("userdata\\GUM.bd", "r") as GUM_File__:
    NameNew = GUM_File__.readline()

NameNew = NameNew.replace('\n', '')
UserName = NameNew

Current_Time = datetime.datetime.now().strftime("%H:%M")
Current_Date = datetime.datetime.now().strftime("%Y-%m-%d")


def checkConnection():

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
        def processUserVoice(userSTT):
            userInput = userSTT
            user_input = userInput
            print("User Input: " + userInput)
            with open("brain-nlp.json") as NLPFile:

                conversation_dict = json.load(NLPFile)
            
            with open("brain-nlp-response.json") as NLPFile2:

                response_dict = json.load(NLPFile2)
            user_input = userInput

            if 'and' in userInput:
                userInput = ((((str(userInput.replace("and", "").split()).replace("['", "")).replace("', '", "\n")).replace("']", "")))
                user_input = userInput.lower()
                user_input_N = user_input
            else:
                user_input = userInput.lower()
                user_input_N = user_input

            
            if 'how to' in user_input:
                if "how to" in user_input:
                    user_input = user_input.replace("how to ", "")
                    bs.howToSearch(user_input)
                else:
                    bs.normalSearch(user_input, search_engine="google")

            def get_response(input_text):
                def errorProcessing():
                    with open("learned.bd") as learnFile2:
                        data = learnFile2.read()

                    # Tokenize words (split by non-word characters)
                    commonWords = re.findall(r'\w+', data.lower())

                    # Count the occurrences of each word
                    word_count = Counter(commonWords)

                    # Get the most common word
                    most_common_word = user_input #word_count.most_common(1)[0]
                    # print(f"The most common word is '{most_common_word[0]}' with {most_common_word[1]} occurrences.")

                    with open("brain-nlp.json") as NLPFile:

                        conversation_dict = json.load(NLPFile)
                    
                    with open("brain-nlp-response.json") as NLPFile2:

                        response_dict = json.load(NLPFile2)

                    
                    for conversationTag, convKeyword in conversation_dict.items():
                        for convKw in convKeyword:
                            # print(convKw)
                            # Load JSON file into a dictionary
                            with open('brain-nlp.json', 'r') as file:
                                File = json.load(file)

                            # Add a new item
                            # new_item = {'word': f'{most_common_word[0]}'}
                            File['learnt error'] = f'{most_common_word}'

                            # Write the updated dictionary back to the JSON file
                            with open('brain-nlp.json', 'w') as file:
                                json.dump(File, file, indent=4)

                            print("Successfully added!")

                    if f"{most_common_word} is" in user_input:
                        meaning_of_error = (f"{most_common_word} is").replace(f"{most_common_word} is", "")

                        with open('brain-nlp-response.json', 'r') as file:
                            respFile = json.load(file)

                            # Add a new item
                            # new_item = {'word': f'{short_answer}'}
                            respFile['learnt error'] = [f'Well {most_common_word} is {meaning_of_error}', f'According to you, {most_common_word} is {meaning_of_error}', f'{meaning_of_error}']

                        # Write the updated dictionary back to the JSON file
                        with open('brain-nlp-response.json', 'w') as file:
                            json.dump(respFile, file, indent=4)

                        query = "Your question goes here"
                        short_answer = get_short_answer(most_common_word)
                        with open('brain-nlp-response.json', 'r') as file:
                            respFile = json.load(file)

                        # Add a new item
                        # new_item = {'word': f'{short_answer}'}
                        respFile['learnt error'] = [f'{short_answer}', f'{short_answer}', f'{short_answer}']

                        # Write the updated dictionary back to the JSON file
                        with open('brain-nlp-response.json', 'w') as file:
                            json.dump(respFile, file, indent=4)

                        # print(short_answer)
                    else:
                        with open('brain-nlp-response.json', 'r') as file:
                            respFile = json.load(file)

                        # Add a new item
                        # new_item = {'word': f'{most_common_word[0]}'}
                        respFile['learnt error'] = [f'What is {most_common_word}?', f'Explain {most_common_word}', f'I dont seem to know {most_common_word}, what is it?']

                        # Write the updated dictionary back to the JSON file
                        with open('brain-nlp-response.json', 'w') as file:
                            json.dump(respFile, file, indent=4)
                            
                        # print(short_answer)
                                    
                    learnUserError()
                    usertext_Label = tk.Label(chat_Frame, text=userInput, bg="white", fg="black", font=("Roboto", 10))
                    usertext_Label.pack(anchor="nw")
                    
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
                    with open("userdata\\GUM.txt", "r") as userData:
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
                        with open("comboApps.json") as ComApp:
                            ComApp_dict = json.load(ComApp)

                        for appTag, appPath in ComApp_dict.items():
                            if (f"load {appTag}") == user_input:
                                with open("combolist.bd", "r") as CBFile:
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
                    with open("combolist.bd", "r") as CBFile:
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

                for key, values in conversation_dict.items():
                    for value in values:
                        print("Value: " + value)
                        if value in conversation_dict['AlexNyze']:
                            try:
                                AlexNyze()
                            except Exception as e:
                                response_Label = tk.Label(chat_Frame, text=f"{e}\nTry Opening it from the 'Tools'", bg="orange", fg="white", font=("Roboto", 10))
                                response_Label.pack(anchor="se", pady=5)

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

                                        generateRecent("Reminder", setReminder)
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

                                        generateRecent("Reminder", setReminder)
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

                                        generateRecent("Reminder", setReminder)
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

                                        generateRecent("Reminder", setReminder)
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

                                        generateRecent(f"Alarm - {tuned_user_input}", setReminder)
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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
                                    definition = wordDictionary.meaning(wordToDefine)

                                    response_Label = tk.Label(chat_Frame, text=definition, bg="green", fg="black", font=("Roboto", 10))
                                    response_Label.pack(anchor="se", pady=5)

                                    # Text to be converted to speech
                                    response_Voiced = (definition.replace("\n", " "))
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

                                generateRecent(f"Launch {app_to_open}", doThis)
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

                                generateRecent(f"Open {app_to_open}", doThis)
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
                                generateRecent(f"Start {app_to_open}", doThis)

                            elif "music" in user_input:
                                def doThis():
                                    app_name = "Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"  # Groove Music's package family name

                                    try:
                                        subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                                    except Exception as e:
                                        print("An error occurred:", e)
                                doThis()
                                generateRecent("Media", doThis)
                            elif "movie" in user_input:
                                def doThis():
                                    app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                                    try:
                                        subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                                    except Exception as e:
                                        print("An error occurred:", e)
                                doThis()
                                generateRecent("Media", doThis)
                            elif "tv" in user_input:
                                def doThis():
                                    app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                                    try:
                                        subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                                    except Exception as e:
                                        print("An error occurred:", e)
                                doThis()
                                generateRecent("Media", doThis)
                            elif "video app" in user_input:
                                def doThis():
                                    app_name = "Microsoft.MoviesAndTV_"  # Movies & TV package family name

                                    try:
                                        subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                                    except Exception as e:
                                        print("An error occurred:", e)
                                doThis()
                                generateRecent("Media", doThis) 
                            elif "videos" in user_input:
                 
                                def doThis():
                                    app_name = "Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo"  # Groove Music's package family name

                                    try:
                                        subprocess.run(["start", "shell:AppsFolder\\" + app_name], shell=True)
                                    except Exception as e:
                                        print("An error occurred:", e)
                                doThis()
                                generateRecent("Media", doThis)
                        

                        print("Value: " + value)


                        print("Value: " + value)
                        # refined_text = re.search(r'\b{}\b'.format(value.lower()), input_text.lower())
                        if value in input_text:
                            from tkinter.font import Font
                            #  or re.search(r'\b{}\b'.format(value.lower()), input_text.lower())
                            # User Text
                           
                            
                            # Bivid Response
                            sm_resp = [(response_dict[key][0]), (response_dict[key][1]), (response_dict[key][2])]
                            
                            # Text to be converted to speech
                            response_Voiced = (ra.choice(sm_resp).replace("\n", " "))

                            # Convert text to speech
                            engine.say(response_Voiced)

                            # Wait for speech to finish
                            engine.runAndWait()
                            return response_dict[key][0]  # Only return the first response

                return errorProcessing()

            # Bot Inner-mind Response 😂
            response = get_response(user_input)
    else:
        engine.say("Not Connected, it's just text based commands for now")
        engine.runAndWait()
    

# internetStatusCheck()