import customtkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.resizable(0, 0)
root.title("login")

def login():
    username = username_entery.get()
    password = password_entery.get()

    if username == "" and password == "":
        messagebox.showinfo("", "blank not allowed")


    elif username == "tetris" and password == "1234567890":
        root.destroy()


    else:
        messagebox.showerror("", "incorrect username or password ")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 28))
label.pack(pady=12, padx=10)

username_entery = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username_entery.pack(pady=12, padx=10)

password_entery = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entery.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

# ========= show/hide password ===========
def show():
    hide_button = Button(frame, image=hide_image, command=hide, activebackground="black", background="#1F1F1F", width=30, height=30,bd=0)
    hide_button.place(x=400, y=190)
    password_entery.configure(show="")

def hide():
    show_button = Button(frame, image=show_image, command=show, activebackground="black", background="#1F1F1F", width=30, height=30, bd=0)
    show_button.place(x=400, y=190)
    password_entery.configure(show="*")

show_image = Image.open("images/show1.png").resize((30, 30))
show_image = ImageTk.PhotoImage(show_image)

hide_image = Image.open("images/hide1.png").resize((30, 30))
hide_image = ImageTk.PhotoImage(hide_image)


show_button = Button(frame, image=show_image, command=show, activebackground="black", background="#1F1F1F", width=30, height=30, bd=0)
show_button.place(x=400, y=190)

root.mainloop()