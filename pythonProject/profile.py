import customtkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("450x600")
root.resizable(0, 0)
root.title("Profile")


# ============ profile image ================
def upload_profile_picture():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.bmp;*.gif")])
    if file_path:
        prof_Img = Image.open(file_path).resize((200, 200))
        photo = customtkinter.CTkImage(prof_Img, size=(130, 130))
        prof_Img_label = customtkinter.CTkLabel(master=root, text="", image=photo, bg_color='transparent')
        prof_Img_label.image = photo
        prof_Img_label.place(y=40, x=160)
        profile_pic_label.lift()

prof_Img = Image.open("images/ProfileIcon.png").resize((200, 200))
photo = customtkinter.CTkImage(prof_Img, size=(130, 130))
prof_Img_label = customtkinter.CTkLabel(master=root, text="", image=photo, bg_color='transparent')
prof_Img_label.image = photo
prof_Img_label.place(y=40, x=160)

profile_icon = Image.open("images/uploadIcon.png").resize((40, 40))
profile_icon = ImageTk.PhotoImage(profile_icon)
profile_pic_label = Label(root, image=profile_icon, cursor='hand2')
profile_pic_label.bind('<Button-1>', lambda event: upload_profile_picture())
profile_pic_label.place(y=220, x=420)


profile_icon = Image.open("images/uploadIcon.png").resize((40, 40))
profile_icon = ImageTk.PhotoImage(profile_icon)
profile_pic_label = Label(root, image=profile_icon, cursor='hand2')
profile_pic_label.bind('<Button-1>', lambda event: upload_profile_picture())
profile_pic_label.place(y=220, x=420)



# =============name label ================

label1 = customtkinter.CTkLabel(master=root, text="tetris", font=("Roboto", 28))
label1.place(x=190, y=180)

# =============== Achievements label ================

label2 = customtkinter.CTkLabel(master=root, text="Achievements", font=("Roboto", 28))
label2.place(x=20, y=290)
achievement1_text = "Novice Achievements:\n"
achievement1_text2= "Clear 10 lines in a single game and Score 500 points in a single game"
Achievement1 = customtkinter.CTkLabel(master=root, text=f"{achievement1_text}{achievement1_text2}",
                                    fg_color="#27408B", width=250, height=40,
                                    corner_radius=10, anchor="center", wraplength=0)
Achievement1.place(x=10, y=340)

achievement2_text = "Intermediate Achievements:\n"
achievement2_text2 = "* Achieve a total score of 1,000 points across all games \n * Clear 50 lines in a single game"
Achievement2 = customtkinter.CTkLabel(master=root, text=f"{achievement2_text}{achievement2_text2}",
                                    fg_color="#27408B", width=430, height=40,
                                    corner_radius=10, anchor="center", wraplength=0)
Achievement2.place(x=10, y=390)

achievement3_text = "Expert Achievements:\n"
achievement3_text2 = "*  Achieve a total score of 5,000 points across all games \n *  Clear 100 lines in a single game"
Achievement3 = customtkinter.CTkLabel(master=root, text=f"{achievement3_text}{achievement3_text2}",
                                    fg_color="#27408B", width=430, height=40,
                                    corner_radius=10, anchor="center", wraplength=0)
Achievement3.place(x=10, y=450)

# ================ score label ==================
score_img = customtkinter.CTkImage(Image.open("images/scoreicon.png"))
score_label = customtkinter.CTkLabel(master=root, text="highest score", font=("Roboto", 14),
                                    fg_color="#636363", corner_radius=10, anchor="w", wraplength=90,
                                    image=score_img, compound="left", padx=10)
score_label.place(x=10, y=240)

# ============= trophy number label ==============
trophy_img = customtkinter.CTkImage(Image.open("images/trophy.png"))
trophy_num_label = customtkinter.CTkLabel(master=root, text="numders of \n trophy", font=("Roboto", 14),
                                   fg_color="#636363", corner_radius=10, anchor="w",
                                   image=trophy_img, compound="left", padx=5)
trophy_num_label.place(x=170, y=240)


# ============= time played label ===============
time_icon = customtkinter.CTkImage(Image.open("images/time icon.png"))
time_played_label = customtkinter.CTkLabel(master=root,text="Time played", font=("Roboto", 14), fg_color="#636363", corner_radius=10,
                                         anchor="w", image=time_icon, compound="left", padx=5)
time_played_label.place(x=310, y=240)

root.mainloop()