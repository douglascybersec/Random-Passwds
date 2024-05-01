# Modules
import customtkinter 
from tkinter import*
import random
import string
import pyperclip
from CTkMessagebox import CTkMessagebox

# App appearance mode, settings & more
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("GreyLight.json")
 
# App settings
app = customtkinter.CTk()
app.title("Random PAssW0rd Generator")
app.geometry(f"{420}x{400}")
app.resizable(False, False)

# Fonts
font1 = customtkinter.CTkFont(family="Helvetica",size=16,weight="bold")
font2 = customtkinter.CTkFont(family="Montserrat",size=25,weight="bold")
font3 = customtkinter.CTkFont(family="Montserrat",size=20,weight="bold")
font4 = customtkinter.CTkFont(family="Helvetica",size=8,weight="bold")

# Frames
nameFrame = customtkinter.CTkFrame(app)
nameFrame.pack(side="top", expand=True, fill="both", padx=5, pady=5)

entryFrame = customtkinter.CTkFrame(app)
entryFrame.pack(expand=True, fill="both", padx=5, pady=5)

genFrame = customtkinter.CTkFrame(app)
genFrame.pack(side="bottom", expand=True, fill="both", padx=5, pady=5)

# AppName(label)
app.name = customtkinter.CTkLabel( master=nameFrame, text="Random PAssW0rd Generator", font=font2, wraplength=400, anchor="center")
app.name.pack(expand=True, fill="both")

# Spinbox
select = Spinbox(master=entryFrame, from_=8, to=32, state="normal")
select.grid(row=0, column=1, padx=10, pady=10, sticky="we" )
select.config(width=5, font=font1)
    
# Function ---> Generate password upon selection
def gen_pass(length, add_uppercase, add_numbers, add_extra_chars):
    
    if not (add_uppercase or add_numbers or add_extra_chars):
        
        # If not checked, no additions(default), length is 8, password is lowercase
        if length == 8:
            password_chars = string.ascii_lowercase
        else:
            
            # Otherwise, generate a password, in lowercase
            password_chars = string.ascii_lowercase * (length // len(string.ascii_lowercase)) + string.ascii_lowercase[:length % len(string.ascii_lowercase)]
    else:
        password_chars = string.ascii_lowercase
        if add_uppercase:
            password_chars += string.ascii_uppercase
        if add_numbers:
            password_chars += string.digits
        if add_extra_chars:
            password_chars += "!@#$%^&*()_+{}[]|\\:;\"',.<>/?"
    
    password = ''.join(random.choice(password_chars) for _ in range(length))
    return password

# Function ---> generate & Update PAsswd entry
def update_password_entry(event=None):
    
    # Get length from Spinbox
    length = int(select.get())
    
    # Check if checkboxes are checked too 
    add_uppercase = check_1.get()
    add_numbers = check_2.get()
    add_extra_chars = check_3.get()
    
    # Then, generate the password from gen_pass
    password = gen_pass(length, add_uppercase, add_numbers, add_extra_chars)
    
    # Activate the entry
    PAsswd.configure(state="normal")
    
    # Clear previous password
    PAsswd.delete(0, "end")
    
    # Insert a new one
    PAsswd.insert(0, password)
    
    # Deactivate
    PAsswd.configure(state="disabled")

# Function ---> Clear entry
def clear():
    PAsswd.configure(state="normal")
    PAsswd.delete(0, "end")
    PAsswd.configure(state="disabled")
  
# FUnction ---> Messagebox
def success():
    CTkMessagebox(title="Success", message="Password copied! Ready to use.", icon="check", width=300, height=100)

def error():
    CTkMessagebox(title="Error", message="Oops! Something went wrong.", icon="cancel", width=300, height=100)
      
# Function ---> Copy Password  
def copy():
    
    # Get the password
    password = PAsswd.get()
    
    # Copy if generated, show success, if not, the latter
    if password:
        pyperclip.copy(password)
        success()
    else:
        error()


# ---OTHER WIDGETS---
# entryFrame Labels
label_1 = customtkinter.CTkLabel(master=entryFrame, text="Password Length :", font=font3, padx=5, pady=5, anchor="w")
label_1.grid(row=0, column=0, sticky="wens")

# Check & toggle password values
check_1 = customtkinter.CTkCheckBox(master=entryFrame, text="Upper Case", font=font1)
check_1.grid(row=1, column=0, pady=10, padx=10, sticky="w")

check_2 = customtkinter.CTkCheckBox(master=entryFrame, text="Numbers", font=font1)
check_2.grid(row=2, column=0, pady=10, padx=10, sticky="w")

check_3 = customtkinter.CTkCheckBox(master=entryFrame, text="Extra Characters", font=font1)
check_3.grid(row=3, column=0, pady=10, padx=10, sticky="w")

# Buttons
Btn_1 = customtkinter.CTkButton(master=genFrame, text="Generate Password", corner_radius=20, font=font1, width=370, height=32, command=update_password_entry)
Btn_1.grid(row=0, column=0, padx=10, pady=10, sticky="we", columnspan=2)

# PAssw0rd output--CTkEntry
PAsswd = customtkinter.CTkEntry(master=genFrame, corner_radius=20, font=font1, justify="center", width=370, height=32,state="disabled")
PAsswd.grid(row=1, column=0, pady=10, padx=10, sticky="we", columnspan=2)

# Other buttons
Btn_2 = customtkinter.CTkButton(master=genFrame, text="Clear", corner_radius=20, font=font1, width=185, height=32, command=clear)
Btn_2.grid(row=2, column=0, padx=10, pady=5, sticky="we")

Btn_3 = customtkinter.CTkButton(master=genFrame, text="Copy", corner_radius=20, font=font1, width=185, height=32, command=copy)
Btn_3.grid(row=2, column=1, padx=10, pady=5, sticky="we")



# Run App
app.mainloop() 