import smtplib
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import socket
from ttkthemes import ThemedStyle
import pyttsx3
import random

def sendEmail():
	engine = pyttsx3.init()
	engine.setProperty('volume', 0.9)
	# engine.setProperty("rate", 50) 


	file_path = None
	with open("userdata\\GUM.bd", "r") as file:
		line1 = file.readline()
		line2 = file.readline()
		line3 = file.readline()
		line4 = file.readline()
		line5 = file.readline()
		line6 = file.readline()
		line7 = file.readline()
	def attachFile():
		# file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
		def globalVar():
			global file_path
			file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])

		globalVar()
		
		return file_path

	def send_email(): # subject, message, to_email, attachment_path=None

		try:
			from_email = f"{line6}"
			# import base64
			encoded_text = f"{line7}"
			# = base64.b64encode(passcode.encode())
			# passcode = base64.b64decode(encoded_text).decode()
			password = encoded_text# passcode

			msg = MIMEMultipart()
			msg['From'] = from_email_entry.get()
			msg['To'] = to_email_entry.get()
			msg['Subject'] = subject_email_entry.get()

			body = message_entry.get("1.0", tk.END)
			msg.attach(MIMEText(body, 'plain'))

			attachment_path = file_path
			if attachment_path:
			    with open(attachment_path, "rb") as attachment:
			        part = MIMEApplication(attachment.read())
			    part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
			    msg.attach(part)

			server = smtplib.SMTP('smtp.example.com', 587)  # Use your email provider's SMTP server and port
			server.starttls()
			server.login(from_email, password)
			text = msg.as_string()
			server.sendmail(from_email, to_email_entry.get(), text)
			server.quit()

			messagebox.showinfo("Email Sent", f"{line1}, your Email has been sent successfully to {to_email_entry.get()}")
			engine.say(random.choice([f"{line1}, I've Sent the email through", "sent it", "done"]))
			engine.runAndWait()
		except socket.gaierror:
			engine.say("I can't send mails without an Internet Connection")
			engine.runAndWait()
		except:
			engine.say("An error occured, try again")
			engine.runAndWait()


	sendMailRoot = tk.Tk()
	sendMailRoot.title("Alex - Send Mails")
	alexIcon = ("MEDIA\\alex-icon-new.ico")
	sendMailRoot.iconbitmap(alexIcon)
	style = ThemedStyle(sendMailRoot)
	style.set_theme("arc")

	sendMailRootMenu = tk.Menu(sendMailRoot)
	sendMailRoot.config(menu=sendMailRootMenu)

	file_menu2 = tk.Menu(sendMailRootMenu, tearoff=0)
	file_menu2.add_command(label="Exit", command=lambda:sendMailRoot.destroy)

	sendMailRootMenu.add_cascade(label="File", menu=file_menu2)

	file_menu3 = tk.Menu(sendMailRootMenu, tearoff=0)
	file_menu3.add_separator()
	contentA = """

	alexMail
	Version build: v1.02
	© Bluvid. All rights reserved.

	The alexMail is a simple and easy-to-use app that allows you to send email messages without all the bells and whistles of a traditional email client. Just enter the recipient's email address, your message, and click send. That's it!

	The alexMail is perfect for anyone who needs to send a quick email but doesn't want to deal with a complicated interface. It's also a great option for people who don't have a regular email account.

	Features:

	Simple and easy-to-use interface
	No need to create an account
	Send email messages to any email address
	Supports attachments

	"""
	file_menu3.add_command(label="About", command=lambda:messagebox.showinfo("About alexMail", f"{contentA}"))

	sendMailRootMenu.add_cascade(label="Help", menu=file_menu3)

	tk.Label(sendMailRoot, text="Send Mails", font=("Roboto", 30)).pack(pady=30)
	tk.Label(sendMailRoot, text="to send mails, make sure you've\ndisabled '' in gmail settings").pack(pady=5)


	# From
	tk.Label(sendMailRoot, text="From:", font=("Roboto", 10, "bold")).pack()
	from_email_entry = ttk.Entry(sendMailRoot, width=40)
	from_email_entry.insert(0, f"{line6}")
	from_email_entry.pack(pady=3)

	# To
	tk.Label(sendMailRoot, text="To:", font=("Roboto", 10, "bold")).pack()
	to_email_entry = ttk.Entry(sendMailRoot, width=40)
	to_email_entry.pack(pady=3)

	# Subject
	tk.Label(sendMailRoot, text="Subject:", font=("Roboto", 10, "bold")).pack()
	subject_email_entry = ttk.Entry(sendMailRoot, width=40)
	subject_email_entry.pack(pady=3)

	# Message
	tk.Label(sendMailRoot, text="Message:", font=("Roboto", 10, "bold")).pack()
	message_entry = tk.Text(sendMailRoot, height=15, width=50)
	message_entry.pack(pady=3)

	# Attach files
	attachFileBt = ttk.Button(sendMailRoot, text="Attach Files", width=40, command=attachFile)
	attachFileBt.pack(pady=3)

	# Send Button
	sendBt = ttk.Button(sendMailRoot, text="Send", width=40, command=send_email)
	sendBt.pack(pady=3)

	sendMailRoot.mainloop()

	# if __name__ == "__main__":
	#     subject = "Test Email"
	#     message = "This is a test email sent from Python."
	#     to_email = "recipient@example.com"
	#     attachment_path = "C:\\dummy.txt"  # Optional
	    
	#     send_email(subject, message, to_email, attachment_path)
	#     print("Email sent successfully!")

# sendEmail()