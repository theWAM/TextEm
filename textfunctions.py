import tkinter as tk
from tkinter import ttk
from tkinter import *

def pvd_lst():
    ATT = "@txt.att.net"
    TMOBILE = "@tmomail.net"
    VERIZON ="@vtext.com"
    SPRINT = "@messaging.sprintpcs.com"
    VGMOBILE = "@vmobl.com"
    METROPCS = "@mymetropcs.com"

    pop = tk.Tk()
    pop.title("Provider List")

    ttk.Label(pop, text = "Provider List", font = "System 14 bold").grid(padx = 10, pady = 10)

    ttk.Label(pop, text = "Copy recipient provider and paste after their #").grid(padx = 10, pady = 10)

    labels_frame = ttk.Frame(pop)
    labels_frame.grid(padx = 10, pady = 10)

    ttk.Label(labels_frame, text = "AT&T:").grid(row = 0, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "T-Mobile:").grid(row = 1, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Verizon:").grid(row = 2, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Sprint:").grid(row = 3, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Virgin Mobile:").grid(row = 4, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "MetroPCS:").grid(row = 5, column = 0, padx= 10)

    ttk.Label(labels_frame, text = ATT).grid(row = 0, column = 1)
    ttk.Label(labels_frame, text = TMOBILE).grid(row = 1, column = 1)
    ttk.Label(labels_frame, text = VERIZON).grid(row = 2, column = 1)
    ttk.Label(labels_frame, text = SPRINT).grid(row = 3, column = 1)
    ttk.Label(labels_frame, text = VGMOBILE).grid(row = 4, column = 1)
    ttk.Label(labels_frame, text = METROPCS).grid(row = 5, column = 1)

    ttk.Button(pop, text = "OK", command = pop.destroy).grid()

    pop.mainloop()


def error():
    error = tk.Tk()
    error.title("ERROR")

    er_frame = ttk.Frame(error)
    er_frame.grid(padx=20, pady=10)
    popup.geometry("+450+250")

    label = ttk.Label(pop_frame, text = "Uh oh! Something went wrong! Try again!")
    label.grid()

    b1_frame = ttk.Frame(pop_frame)
    b1_frame.grid(pady = 10)
    b1 = ttk.Button(pop_frame, text = "OK", default = "active", command = popup.destroy)
    b1.grid()

def popup():
    popup = tk.Tk()
    popup.title("Success!")

    pop_frame = ttk.Frame(popup)
    pop_frame.grid(padx=20, pady=10)
    popup.geometry("+450+250")

    label = ttk.Label(pop_frame, text = "Sent! Would you like to send another message?")
    label.grid()

    b_frame = ttk.Frame(pop_frame)
    b_frame.grid(pady = 10)

    b1 = ttk.Button(b_frame, text = "Yes!", command = popup.destroy)
    b1.grid()
    
    b2 = ttk.Button(b_frame, text = "No, I'm done", default = "active", command = quit)
    b2.grid()

    popup.mainloop()
