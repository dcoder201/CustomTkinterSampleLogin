# Importing customtkinter module
import customtkinter
from PIL import Image, ImageTk

# Set appearance mode
from _testcapi import test_Z_code

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Define windows size for display
root = customtkinter.CTk()
root.geometry("600x400")


def login():
    print("Successfully Logged in")


# Set frame
frame = customtkinter.CTkFrame(master=root,width=600,height=600)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Set Login label
topLabel = customtkinter.CTkLabel(master=frame, text="Modern Login UI", text_font=("roboto",20))
topLabel.pack(padx=12, pady=30)

# Set user field
userEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Username",width=160)
userEntry.pack(padx=18, pady=20)

# Set password field
passEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Password",width=160, show="*")
passEntry.pack(padx=18, pady=5)

# Set Login button
loginButton = customtkinter.CTkButton(master=frame, text="Login", width=100, corner_radius=25, hover_color="green", command=login())
loginButton.pack(padx=18, pady=20)

# Set Check box
radioButton = customtkinter.CTkCheckBox(master=frame,width=20, height=20, text="Remember me", text_color="grey")
radioButton.pack(padx=15, pady=5)



root.mainloop()




