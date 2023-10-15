# importing the required modules
import tkinter as tk            
from tkinter import ttk                 
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# The function to update the list  
def list_update():  
    clear_list()  
    for password in passwords:  
        password_listbox.insert('end', password)   

# function to clear the list 
def clear_list():   
    password_listbox.delete(0, 'end') 

def generate_password_button():
    try:
        length = length_field.get()
        complexity = complex_field.get()
        if (length == "") or (complexity == ""):  
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            length = int(length)
            complexity = int(complexity)
            password = generate_password(length, complexity)
            passwords.append(password)
            list_update()  
            length_field.delete(0, 'end') 
            complex_field.delete(0, 'end') 
            
    except ValueError:
        messagebox.showinfo('Error', 'Please enter valid inputs.')

# function to close the application
def close():     
    guiWindow.destroy()  

 
# main function  
if __name__ == "__main__":  

    # creating an object of the Tk() class
    guiWindow = tk.Tk()  
    guiWindow.title("Password Generator")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#FAEBD7")  
  
    # defining an empty list
    passwords = []  
      
    header_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
    functions_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
    listbox_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
  
    # using the pack() method to place the frames in the application
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    header_label = ttk.Label(  
        header_frame,  
        text = "Password Generator",  
        font = ("Times New Roman", "30"),  
        background = "#FAEBD7",
        foreground = "#8B4513"  
    )  
    
    header_label.pack(padx = 20, pady = 20)  
   
    length_label = ttk.Label(  
        functions_frame,  
        text = "Enter the password length:",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )  

    length_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget 
    length_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#1a1818"  
    )   
    length_field.place(x = 30, y = 80)

    complex_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Complexity(1/2/3):",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )  

    complex_label.place(x = 30, y = 120)  
      
    complex_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#1a1818"  
    )   

    complex_field.place(x = 30, y = 160)
  
    generate_button = ttk.Button(  
        functions_frame,  
        text = "Generate Password ",  
        width = 24,  
        command = generate_password_button
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  

    # using the place() method to set the position of the buttons in the application 
    generate_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  

    # defining a list box using the tk.Listbox() widget
    password_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#4fbd4a",  
        selectforeground = "#FFFFFF"  
    )  

    password_listbox.place(x = 40, y = 40)  
   
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
