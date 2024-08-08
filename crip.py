import customtkinter as ctk

def add_task():
    task = entry.get()
    label = ctk.CTkLabel(scroll_frame, text=task)
    label.pack()
    entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("500x450")
root.title("countdown timer")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

## creating widgtes
title_label = ctk.CTkLabel(root, text="Countdown Timer", font=("Arial", 24),
    text_color="white", corner_radius=10) 
title_label.pack(pady=20, padx=10)

scroll_frame = ctk.CTkScrollableFrame(root, width=400, height=300)
scroll_frame.pack(pady=10, padx=20)

entry = ctk.CTkEntry(scroll_frame, placeholder_text="Enter task")
entry.pack(fill="x")


btn = ctk.CTkButton(root, text="add", font=("Arial", 24),
                    width=500, command=add_task)
btn.pack(pady=10, padx=20)





root.mainloop()