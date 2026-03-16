import customtkinter as ctk


def show_error_popup(parent, message):
    popup = ctk.CTkToplevel(parent)
    popup.title("ERROR")
    popup.geometry("400x180")
    popup.resizable(False, False)
    popup.configure(fg_color="#000000")
    popup.transient(parent)
    popup.grab_set()

    popup.update_idletasks()
    x = popup.winfo_screenwidth() // 2 - popup.winfo_width() // 2
    y = popup.winfo_screenheight() // 2 - popup.winfo_height() // 2
    popup.geometry(f"+{x}+{y}")

    main_frame = ctk.CTkFrame(popup, fg_color="#000000")
    main_frame.pack(fill="both", expand=True, padx=30, pady=25)

    error_label = ctk.CTkLabel(
        main_frame,
        text=message,
        font=ctk.CTkFont(size=14),
        text_color="white",
        wraplength=340
    )
    error_label.pack(pady=(0, 25))

    ok_button = ctk.CTkButton(
        main_frame,
        text="OK",
        font=ctk.CTkFont(size=14, weight="bold"),
        height=40,
        fg_color="#c93535",
        hover_color="#a12828",
        text_color="white",
        command=popup.destroy
    )
    ok_button.pack(ipadx=30)
