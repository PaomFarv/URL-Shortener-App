import customtkinter as ctk
import pyshorteners
import pyperclip

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

def url_shortener():
    generate_button.configure(state="disabled", text="Working...")
    root.after(100, perform_shortening)  # Delay slightly to let UI update

def perform_shortening():
    shorten = pyshorteners.Shortener() 
    long_url_value = long_url.get()

    if long_url_value:
        try:
            short_url = shorten.tinyurl.short(long_url_value)
            short_url_label.configure(text=short_url, text_color="white")
            copy_button.pack(side="right", padx=10, pady=10)
            copy_button.configure(command=copy_url)
        except Exception:
            short_url_label.configure(text="Error: Invalid URL", text_color="red")
    else:
        short_url_label.configure(text="Please enter a URL", text_color="red")
    
    generate_button.configure(state="normal", text="Generate Short URL")


def copy_url():
    short_url = short_url_label.cget("text")
    
    if short_url and short_url != "Shortened URL will appear here..":
        pyperclip.copy(short_url)
        copy_button.configure(text="Copied!", text_color="green")
    else:
        copy_button.configure(text="Copy", text_color="black")

def reset_fields():
    long_url.delete(0, ctk.END)
    short_url_label.configure(text="Shortened URL will appear here..", text_color="grey")
    copy_button.pack_forget()
    copy_button.configure(text="Copy", text_color="black")

def paste():
    long_url.insert("end", pyperclip.paste())

root = ctk.CTk()
root.geometry("450x500")
root.title("URL Shortener")
root.configure(fg_color="black")

main_frame = ctk.CTkFrame(master=root, corner_radius=10,border_width=2,fg_color="#202020")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

header_label = ctk.CTkLabel(master=main_frame, text="URL Shortener", font=("Bahnschrift Bold", 40)).pack(pady=10)

entry_frame = ctk.CTkFrame(master=main_frame, fg_color="black", corner_radius=10)
entry_frame.pack(pady=20, padx=20, fill="x")

long_url = ctk.CTkEntry(master=entry_frame, placeholder_text="  Your URL",fg_color="black", font=("Helvetica", 15,"bold"),border_width=0,width=250)
long_url.pack(fill="x",pady=10,padx=10,side="left")

paste_button = ctk.CTkButton(master=entry_frame, text="Paste", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black",command=paste)
paste_button.pack(side="right", padx=10, pady=10)

generate_button = ctk.CTkButton(main_frame, text="Generate Short URL", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black",command=url_shortener)
generate_button.pack(pady=10)

short_url_frame = ctk.CTkFrame(master = main_frame, corner_radius=10,fg_color="black")
short_url_frame.pack(pady=25,fill="x",padx=20)

short_url_label = ctk.CTkLabel(master=short_url_frame, text="Shortened URL will appear here..", font=("Helvetica", 17,"bold"),text_color="grey")
short_url_label.pack(side="left", padx=10, pady=10)

copy_button = ctk.CTkButton(master=short_url_frame, text="Copy", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black",command=copy_url)
copy_button.pack_forget()

reset_button = ctk.CTkButton(master=main_frame, text="Reset", width=100, height=30, font=("Helvetica", 15,"bold"),fg_color="White",text_color="black",command=reset_fields)
reset_button.pack(pady=10)

author_mark = ctk.CTkLabel(master=main_frame, text="Coded by PaomFarv <3", font=("Bahnschrift Bold", 12))
author_mark.pack(side="bottom", pady=10)

root.mainloop()