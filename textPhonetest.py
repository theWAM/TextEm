import tkinter as tk
from tkinter import ttk
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import imaplib
import email

class TextPhone:

    def __init__(self, addy, pwd, to, message):

        s = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
        s.starttls()
        
        try:
            s.login(addy, pwd)

            print("Email successfully authenticated...")

            msg = MIMEMultipart()

            msg['From'] = addy
            msg['To'] = to

            msg.attach(MIMEText(message, 'plain'))

            s.send_message(msg)
    
            print("Message sending...")
            
        except Exception as e:
            print("Failed email authentication")
            
            priv = tk.Tk()
            priv.title("ERROR")

            ttk.Label(priv, text = "We couldn't let you into your account! Enter your address and password again").grid()
            ttk.Button(priv, text = "OK", command = priv.destroy).grid()

            priv.mainloop()



