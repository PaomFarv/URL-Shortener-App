import customtkinter as ctk
import pyshorteners

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("450x500")
root.title("URL Shortener")

main_frame = ctk.CTkFrame(master=root, corner_radius=10,border_width=2)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

header_label = ctk.CTkLabel(master=main_frame, text="URL Shortener", font=("Bahnschrift Bold", 40)).pack(pady=10)

long_url = ctk.CTkEntry(master=main_frame, placeholder_text="  Your URL",fg_color="black",height=40, font=("Helvetica", 15,"bold"),border_width=0)
long_url.pack(fill="x",pady=10,padx=20)

generate_button = ctk.CTkButton(main_frame, text="Generate Short URL", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black")
generate_button.pack(pady=10)

short_url_frame = ctk.CTkFrame(master = main_frame, corner_radius=10,fg_color="black")
short_url_frame.pack(pady=25,fill="x",padx=20)

short_url_label = ctk.CTkLabel(master=short_url_frame, text="Shortened URL will appear here..", font=("Helvetica", 17,"bold"),text_color="grey")
short_url_label.pack(side="left", padx=10, pady=10)

copy_button = ctk.CTkButton(master=short_url_frame, text="Copy", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black")
copy_button.pack_forget()
#copy_button.pack(side="right", padx=10, pady=10)

reset_button = ctk.CTkButton(master=main_frame, text="Reset", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black")
reset_button.pack(pady=10)

author_mark = ctk.CTkLabel(master=main_frame, text="Coded by PaomFarv <3", font=("Bahnschrift Bold", 12))
author_mark.pack(pady=50)

root.mainloop()