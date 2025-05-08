import customtkinter as ctk
import pyshorteners

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x500")
root.title("URL Shortener")

main_frame = ctk.CTkFrame(master=root, corner_radius=10,border_width=2)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

header_label = ctk.CTkLabel(master=main_frame, text="URL Shortener", font=("Bahnschrift Bold", 40)).pack(pady=10)

long_url = ctk.CTkEntry(master=main_frame, placeholder_text="  Your URL",fg_color="black", width=330, height=40, font=("Helvetica", 15,"bold"))
long_url.pack(pady=10)

generate_button = ctk.CTkButton(main_frame, text="Generate Short URL", width=100, height=20, font=("Helvetica", 15,"bold"))
generate_button.pack(pady=10)

short_url_frame = ctk.CTkFrame(master = main_frame, corner_radius=10,fg_color="black",width=20)
short_url_frame.pack(pady=30,fill="x",padx=10)

short_url_label = ctk.CTkLabel(master=short_url_frame, text="Shortened URL will appear here..", font=("Helvetica", 15,"bold"))
short_url_label.pack(pady=10)

root.mainloop()