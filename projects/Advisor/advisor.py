# Importing libraries
from tkinter.constants import DISABLED
import random
import requests
import tkinter as tk
from tkinter import messagebox

previous_advice_set = []

def advice():
    global previous_advice
    try:
        previous_advice = advice_text.get()
        res = requests.get("https://api.adviceslip.com/advice").json()
        advice_text.set(res["slip"]["advice"])
        previous_advice_set.append(advice_text.get())
        #print(previous_advice_set)
        if previous_advice:
            get_back_button.config(state = tk.NORMAL)
            clear_button.config(state = tk.NORMAL)
    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Error", "Failed to fetch advice. Please check your internet connection."
        )

def back_to_previous():
    global previous_advice

    if previous_advice:
        #current_advice = advice_text.get()
        #advice_text.set(previous_advice)
        previous_advice = previous_advice_set[random.randint(0,len(previous_advice_set))-1]
        advice_text.set(previous_advice)
    if not previous_advice:
        get_back_button.config(state=tk.DISABLED)

def clear_button_advice():
    previous_advice_set.clear()
    return advice()
# Create the main window
root = tk.Tk()
root.title("Random Advisor Application")

# Create and configure widgets
advice_text = tk.StringVar()
previous_advice = ""
advice_label = tk.Label(
    root, textvariable=advice_text, wraplength=400, font=("Arial", 14)
)
get_advice_button = tk.Button(root, text="Get Advice", command=advice)
get_back_button = tk.Button(root,text="Previous advice",command=back_to_previous,state=DISABLED)
clear_button = tk.Button(root,text="Restart",command = clear_button_advice,state =DISABLED )
# Pack widgets
advice_label.pack(side = 'top',pady= 40)
get_advice_button.pack(side = 'left',pady =10)
get_back_button.pack(side = 'left',pady =10)
clear_button.pack(side= 'right',pady =10)
# Initial advice fetching
advice()

# Run the main event loop
root.mainloop()
