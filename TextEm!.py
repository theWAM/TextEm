# TextEm!        12.25.18                                                =
# © Woody Allen Montilus 2018                                            =
#                                                                        =
# ========================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import imaplib
import email
import textPhonetest as tpt
import textfunctions as tf

def click_cancel():
    print("User pressed cancel")
    self.destroy()
    quit()

def run_TextEm(event):
    print("Running textPhonetest...")

    try:
        tpt.TextPhone(e_addy.get(), e_pwd.get(), e_to.get(), e_msg.get())
    except ValueError:
        tf.error()
    print("Message successfully sent!")

self = Tk()
self.grid()
self.geometry("+250+150")
self.title("TextEm!")

spacer_frame = ttk.Frame(self)
spacer_frame.grid(pady=10)

body_frame = ttk.Frame(self)
body_frame.grid(padx=20, pady=10)

header_div = ttk.Frame(body_frame)
header_div.grid()
Label(header_div, text = "Welcome to TextEm! (Gmail supported)", font = "System 16 bold").grid()
Label(header_div, text = "Recipient should be phone#@provideraddress, i.e. number@txt.att.net").grid()
Label(header_div, text = "Click Provider List for provider specific addresses").grid()

addy_div = ttk.Frame(body_frame)
addy_div.grid()

ttk.Label(addy_div, text = "Email Address:").grid(row = 1, column = 0, padx = 10, pady = 15)

e_addy = ttk.Entry(addy_div)
e_addy.grid(row = 1, column = 1, padx = 10, pady = 15)
e_addy.bind("<Return>", run_TextEm)
e_addy.focus()

pwd_div = ttk.Frame(body_frame)
pwd_div.grid()

ttk.Label(pwd_div, text = "Password:").grid(row = 2, column = 0, padx = 10, pady = 15)

e_pwd = ttk.Entry(pwd_div, show="*")
e_pwd.grid(row = 2, column = 1, padx = 10, pady = 15)
e_pwd.bind("<Return>", run_TextEm)

to_div = ttk.Frame(body_frame)
to_div.grid()

ttk.Label(to_div, text = "Recipient:").grid(row = 3, column = 0, padx = 10, pady = 15)

e_to = ttk.Entry(to_div)
e_to.grid(row = 3, column = 1, padx = 10, pady = 15)
e_to.bind("<Return>", run_TextEm)

msg_div = ttk.Frame(body_frame)
msg_div.grid()

m_label = ttk.Label(msg_div, text = "Message:").grid(row = 4, column = 0, padx = 10, pady = 15)

e_msg = ttk.Entry(msg_div)
e_msg.grid(row = 4, column = 1, padx = 10, pady = 15)
e_msg.bind("<Return>", run_TextEm)

btns = ttk.Frame(body_frame)
btns.grid(padx=10, pady=10)

ttk.Button(btns, text = "Provider List", command = tf.pvd_lst).grid()

self.protocol("WM_DELETE_WINDOW", click_cancel)
ttk.Button(btns, text = "Cancel", command = click_cancel).grid()

