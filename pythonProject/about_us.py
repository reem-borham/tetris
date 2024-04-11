from customtkinter import *


window = CTk()
window.geometry("700x350")
window.title("about us")
window._set_appearance_mode("dark")

label1 = CTkLabel(master=window, text="Team Names ", fg_color="dodgerblue4", text_color="white", font=("bold", 40), corner_radius=20, pady=20, padx=20)
label1.place(x=210, y=20)

label1 = CTkLabel(master=window, text="Reem Khaled Ali   ID:231000165 ", fg_color="transparent", text_color="#FF69B4", font=("bold", 30))
label1.place(x=90, y=120)

label1 = CTkLabel(master=window, text="Basem Magdy   ID:231000682 ", fg_color="transparent", text_color="#1C86EE", font=("bold", 30))
label1.place(x=90, y=160)

label1 = CTkLabel(master=window, text="Youssef Mohamed Yacoub   ID:231000016 ", fg_color="transparent", text_color="#00CD66", font=("bold", 30))
label1.place(x=90, y=200)

label1 = CTkLabel(master=window, text="Mahmoud Khairy  ID:231000686 ", fg_color="transparent", text_color="#FF9912", font=("bold", 30))
label1.place(x=90, y=240)

window.mainloop()