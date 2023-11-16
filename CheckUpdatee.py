import socket
import requests
import time
import os
import tkinter as tk
import shutil
from tkinter import ttk, messagebox
import webbrowser
import subprocess
from ttkthemes import ThemedStyle


def runUpdateDialog():
	def checkUpdate():
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
			def startUpdate():	
				progressBr.start()

				pBARlB.config(text="18% - Removing older app files")

				os.remove("Alex.exe")
				os.remove("data/brain-nlp.json")
				os.remove("data/brain-nlp-response.json")
				os.remove("data/versionInfo.bd")
				os.remove("data/alexlibs/alexEmail.py")
				os.remove("data/alexlibs/alexNotes.py")
				os.remove("data/alexlibs/bividVoice.py")
				os.remove("data/alexlibs/COMBO.py")
				os.remove("CheckUpdatee.py")
				os.remove("Alex.py")
				# os.remove("")
				

				brain__ = "https://bluvid.000webhostapp.com/others/updateFile/alexex/brain-nlp.json"
				brain__response = "https://bluvid.000webhostapp.com/others/updateFile/alexex/brain-nlp-response.json"
				email__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/alexEmail.py"
				note__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/alexNotes.py"
				voice__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/bividVoice.py"
				update__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/CheckUpdatee.py"
				combo__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/COMBO.py"
				versionInfo = "https://bluvid.000webhostapp.com/others/updateFile/alexex/versionInfo.bd"
				alex__app = "https://bluvid.000webhostapp.com/others/updateFile/alexex/Alex.py"

				directoryData = "/data"
				directoryDataAlexLibs = "/data/alexlibs"
				mainDir = "/"

				os.mkdir(directoryData)
				os.mkdir(directoryDataAlexLibs)
				os.mkdir(mainDir)




				# Brain
				response_brain = requests.get(brain__)

				with open(os.path.join(directoryData, "brain-nlp.json"), "wb") as brain:
					brain.write(response_brain.content)


				# Brain Response
				response_brain_response = requests.get(brain__response)

				with open(os.path.join(directoryData, "brain-nlp-response.json"), "wb") as brain_response:
					brain_response.write(response_brain_response.content)

				# Email App
				emailResp = requests.get(email__app)

				with open(os.path.join(directoryDataAlexLibs, "alexEmail.py"), "wb") as email:
					email.write(emailResp.content)

				# Note App
				noteResp = requests.get(note__app)

				with open(os.path.join(directoryDataAlexLibs, "alexNotes.py"), "wb") as note:
					note.write(noteResp.content)

				pBARlB.config(text="25% - Downloading update files")
				# Voice App
				voiceResp = requests.get(voice__app)

				with open(os.path.join(directoryDataAlexLibs, "bividVoice.py"), "wb") as voice:
					voice.write(voiceResp.content)


				# Update App
				updateResp = requests.get(update__app)

				with open(os.path.join(mainDir, "CheckUpdatee.py"), "wb") as update:
					update.write(updateResp.content)


				# Combo App
				comboResp = requests.get(combo__app)

				with open(os.path.join(directoryDataAlexLibs, "COMBO.py"), "wb") as combo:
					combo.write(comboResp.content)


				# Version Info
				versionResp = requests.get(versionInfo)

				with open(os.path.join(directoryData, "versionInfo.bd"), "wb") as version:
					version.write(versionResp.content)

				pBARlB.config(text="60% - Downloading update files")
				# Alex
				alexResp = requests.get(alex__app)

				with open(os.path.join(mainDir, "Alex.py"), "wb") as alex:
					alex.write(alexResp.content)

				pBARlB.config(text="70% - Installing update files")

				
				pBARlB.config(text="75%  - Packaging application")

				subprocess.run("pyinstaller -p . --onefile Alex.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				statusButton = tk.Button(app, text="Updated. View Update features →", command=lambda:webbrowser.open("https://bluvid.000webhostapp.com/others/updateFile/changelogs.html")).pack()

				progressBr.stop()
		else:
			statusText.config(text="No internet", fg="red")
			messagebox.showwarning("No internet", "Internet connection is needed for update")

	def instPy():
		subprocess.run("Python\\python-3.11.4-amd64.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		messagebox.showinfo("Python install", "Python is required for running of Alex, please wait while python installs when done, close the update dialog and start the dialog again.")

	app = tk.Tk()
	app.title("Alex - Check for updates")
	app.geometry("500x600")
	app.resizable(height=False, width=False)
	alexIcon = ("MEDIA\\alex-icon-new.ico")
	app.iconbitmap(alexIcon)

	style = ThemedStyle(app)
	style.set_theme("arc")

	ttk.Label(app, text="Update Alex", font=("Roboto", 30)).pack(pady=10)

	Lb = ttk.Label(app, text="Tap Update to check for updates")
	Lb.pack(pady=5)

	pBARlB = ttk.Label(app, text="0%").pack(pady=5)

	progressBr = ttk.Progressbar(app, length=200)
	# progressBr.set(0)

	progressBr.pack(pady=30)

	appBt = ttk.Button(app, text="Check for updates →", width=40, command=checkUpdate, state="disabled")
	appBt.pack(pady=10)

	statusText = tk.Label(app, text="")
	statusText.pack(pady=10)

	def checkPython():
		if shutil.which("python"):
			statusText.config(text="Python installed, proceed with update!", fg="green")
			appBt.config(state="enabled")
		else:
			messagebox.showerror("Python Not Installed", "Please install")

	checkPython()

	chkPyBt = ttk.Button(app, text="Install Python. No internet connection required!", command=instPy)
	chkPyBt.pack(pady=30)

	app.mainloop()