import tkinter as tk
from tkinter import *
import re

my_w = tk.Tk()
my_w.geometry("500x100")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

def validate(u_input):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,u_input) and u_input.isalpha):
        validation_label.config(text="")
        print(True)
        submit_button.config(state='active')  
        return True        
    else:
        validation_label.config(text="Name or email invalid", foreground="red")
        print(False)
        submit_button.config(state='disabled') 
        return False  
   
my_valid = my_w.register(validate)

validation_label = tk.Label(my_w)
validation_label.grid(row=2, column=2)

email_label=tk.Label(my_w,text='Email')
email_label.grid(row=1,column=1,padx=5,pady=20)
email_field = Entry(my_w,validate='focusout',validatecommand=(my_valid,'%P'))
email_field.grid(row=1,column=2,padx=10)


name_label=tk.Label(my_w,text='Name')
name_label.grid(row=1,column=3,padx=5,pady=20)
label_field = tk.Entry(my_w,width=10)
label_field.grid(row=1,column=4)


submit_button = tk.Button(my_w,text='Submit')
submit_button.grid(row=1,column=5)

my_w.mainloop()  # Keep the window open