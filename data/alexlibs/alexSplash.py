import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

NetworkStat = "nil"
def splashScreen():
	splashScreenWin = tk.Tk()
	splashScreenWin.title("Alex - Virtual Assistant")
	splashScreenWin.geometry("450x350")
	splashScreenWin.overrideredirect(True)
	splashScreenWin.config(bg="#081734")
	splashScreenWin.tk_setPalette(background='#081734')
	splashScreenWin.resizable(width=False, height=False)
	style = ThemedStyle(splashScreenWin)
	style.set_theme("arc")

	# alexIcon = ("MEDIA\\alex-icon.ico")
	# splashScreenWin.iconbitmap(alexIcon)

	def closeSplash():
		splashScreenWin.destroy()

	splashScreenWin.after(10000, closeSplash)

	tk.Label(splashScreenWin, text="\n", bg="#081734").pack()

	splashImg = tk.PhotoImage(file="MEDIA\\alex-dark.png")
	splashImgLb = tk.Label(splashScreenWin, image=splashImg, bg="#081734")
	splashImgLb.pack(pady=20)

	# with open("data\\versionInfo.bd", "r") as file:
	versionInfo = "v2" #file.readline()

	# lb1 = tk.Label(splashScreenWin, text="Preparing libraries & modules......optimizing interface", fg="white", bg="#081734", font=("Roboto", 10))
	# lb1.pack()
	# lb1.after(9000, lambda:lb1.destroy())

	# lb2 = tk.Label(splashScreenWin, text=f"Fetching input resources........checking for network connection\nNetwork status: {NetworkStat}", fg="white", bg="#081734", font=("Roboto", 10))
	# lb2.pack()
	# lb2.after(2000, lambda:lb2.destroy())

	# lb3 = tk.Label(splashScreenWin, text="Leveraging resources.......Launching", fg="white", bg="#081734", font=("Roboto", 10))
	# lb3.pack()
	# lb3.after(6000, lambda:lb3.destroy())

	loadbar = ttk.Progressbar(splashScreenWin, length=200)
	loadbar.pack(pady=30)

	loadbar.start()

	lb = tk.Label(splashScreenWin, text=f"alex {versionInfo}\n© 2022 Bluvid\n\n", fg="white", bg="#081734", font=("Roboto", 9))
	lb.pack(pady=30)

	splashScreenWin.mainloop()

splashScreen()