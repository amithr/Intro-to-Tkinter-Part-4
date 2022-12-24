import tkinter as tk
from tkinter import *
import re

root = tk.Tk()
root.geometry("600x100")  # Size of the window 
root.title("Validation Example")  # Adding a title

def validate_email(email_input):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email_input) and email_input.isalpha):
        email_validation_label.config(text="")
        submit_button.config(state='active')  
        return True        
    else:
        email_validation_label.config(text="Email invalid", foreground="red")
        submit_button.config(state='disabled') 
        return False  

def validate_name(name_input):
    # Accepts multiword names
    # No special symbols or numbers
    regex = "^[\-'a-zA-Z ]+$"
    if(re.search(regex,name_input)):
        name_validation_label.config(text="")
        submit_button.config(state='active')
        return True
    else:
        name_validation_label.config(text="Name invalid", foreground="red")
        submit_button.config(state='disabled') 
        return False
   
email_valid = root.register(validate_email)
email_validation_label = tk.Label(root)
email_validation_label.grid(row=2, column=2, pady=10)

email_label=tk.Label(root,text='Email')
email_label.grid(row=1,column=1,padx=5,pady=10)
# focus, focusin, focusout, key, all, none
# focus tried to validate whenever field gains or loses focus
email_field = Entry(root,validate='focus',validatecommand=(email_valid,'%P'))
email_field.grid(row=1,column=2,padx=10)


name_valid = root.register(validate_name)
name_validation_label = tk.Label(root)
name_validation_label.grid(row=2, column=4, pady=10)

name_label=tk.Label(root,text='Name')
name_label.grid(row=1,column=3,padx=5, pady=10)
name_field = tk.Entry(root, validate='focus', validatecommand=(name_valid, '%P'))
name_field.grid(row=1,column=4, padx=10)


submit_button = tk.Button(root,text='Submit')
submit_button.grid(row=1,column=5)

root.mainloop()  # Keep the window open