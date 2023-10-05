import customtkinter
from PIL import Image, ImageTk

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_attributes('-type', 'splash')
        self.width = width
        self.height = height
        self.center_window()
        background_image = ImageTk.PhotoImage(Image.open("ressources/bg1.png").resize((550, 350), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))
    
class ToplevelErrorWindow(ToplevelWindow):
    def __init__(self, label_txt="error", btn_quit_txt="Quit", btn_retry_text="retry", btn_quit_command=None, btn_retry_command=None, *args, **kwargs):
        super().__init__(width=550, height=350, *args, **kwargs)
        img_error = ImageTk.PhotoImage(Image.open("ressources/warning(2).png").resize((50, 50), Image.ANTIALIAS))
        self.label = customtkinter.CTkLabel(self, text=label_txt, image=img_error, font=("Helveita", 28), compound="left", width=250, height=100, text_color="#FF7779")
        self.label.place(relx=.5, rely=.4,anchor= 'center')

        self.frame = customtkinter.CTkFrame(self, bg_color="#FFFFFF")
        self.frame.place(relx=.5, rely=.65, anchor= 'center')
        self.btn_quit = customtkinter.CTkButton(self.frame, command=btn_quit_command, text=btn_quit_txt, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_quit.pack(side='left')
        self.btn_retry = customtkinter.CTkButton(self.frame, command=btn_retry_command, text=btn_retry_text, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_retry.pack(side='right', padx=30)

class ToplevelWarningWindow(ToplevelWindow):
    def __init__(self, warning="Warning", btn_ignore_txt="yes", btn_appreciate_txt="no", btn_ignore_command=None, btn_appreciate_command=None, *args, **kwargs):
        super().__init__(width=550, height=350, *args, **kwargs)
        img_warning = ImageTk.PhotoImage(Image.open("ressources/warning(1).png").resize((50, 50), Image.ANTIALIAS))
        self.label = customtkinter.CTkLabel(self, text=warning, image=img_warning, font=("Helveita", 28), compound="left", width=250, height=100, text_color="#000000")
        self.label.place(relx=.5, rely=.4,anchor= 'center')

        self.frame = customtkinter.CTkFrame(self)
        self.frame.place(relx=.5, rely=.65, anchor= 'center')
        self.btn_ignore = customtkinter.CTkButton(self.frame, command=btn_ignore_command, text=btn_ignore_txt, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_ignore.pack(side='left')
        self.btn_appreciate = customtkinter.CTkButton(self.frame, command=btn_appreciate_command, text=btn_appreciate_txt, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_appreciate.pack(side='right', padx=30)
        

class ToplevelSuccessWindow(ToplevelWindow):
    def __init__(self, label_txt="Success", btn_txt="OK", btn_command=None, *args, **kwargs):
        super().__init__(width=550, height=350, *args, **kwargs)
        img_success = ImageTk.PhotoImage(Image.open("ressources/check.png").resize((50, 50), Image.ANTIALIAS))
        self.label = customtkinter.CTkLabel(self, text=label_txt, image=img_success, font=("Helveita", 28), compound="left", width=250, height=100, text_color="#00A300")
        self.label.place(relx=.5, rely=.4, anchor= 'center')

        self.btn_ok = customtkinter.CTkButton(self, command=btn_command, text=btn_txt, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_ok.place(relx=.5, rely=.65, anchor= 'center')

class RecyclingErrorWindow(ToplevelWindow):
    def __init__(self, label_txt="Error", btn_txt="OK", btn_command=None, *args, **kwargs):
        super().__init__(width=550, height=350, *args, **kwargs)
        img_error = ImageTk.PhotoImage(Image.open("ressources/warning(2).png").resize((50, 50), Image.ANTIALIAS))
        self.label = customtkinter.CTkLabel(self, text=label_txt, image=img_error, font=("Helveita", 28), compound="left", width=250, height=100, text_color="#FF7779")
        self.label.place(relx=.5, rely=.4, anchor= 'center')

        self.btn_ok = customtkinter.CTkButton(self, command=btn_command, text=btn_txt, font=("Helveita", 20), compound="left", hover_color="#89CFF0", fg_color="#89CFF0", bg_color="#FFFFFF", border_color="#000000", border_width=2, width=150, text_color="#000000", height=75, corner_radius=25)
        self.btn_ok.place(relx=.5, rely=.65, anchor= 'center')