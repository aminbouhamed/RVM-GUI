import customtkinter
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWindow, ToplevelWarningWindow, ToplevelErrorWindow, ToplevelSuccessWindow
from topLevelRecyclingWindow import ToplevelRecyclingWindow
import ressources

class ToplevelAuthenticationWindow(ToplevelWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(600, 600, *args, **kwargs)
        self.center_window()
        self.toplevel_success_window = None
        self.toplevel_error_window = None

        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(2).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        img_scan = ImageTk.PhotoImage(Image.open("ressources/scan.png").resize((250, 250), Image.ANTIALIAS))
        self.label_bottle = customtkinter.CTkLabel(self, text="", image=img_scan, font=("Helveita", 20), compound="left", width=250, height=100, fg_color="#FFFFFF", text_color="#000000")
        self.label_bottle.place(relx=.5, rely=.45,anchor= 'center') 

        img_qrcode = ImageTk.PhotoImage(Image.open("ressources/qr-code.png").resize((50, 50), Image.ANTIALIAS))
        self.btn_qrcode_auth = customtkinter.CTkButton(self, command=self.qrcode_authentication, text="QR Code Authentication", image=img_qrcode, font=("Helveita", 20), compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_qrcode_auth.place(relx=.5, rely=.80,anchor= 'center')
        self.btn_quit = customtkinter.CTkButton(self, command=self.destroy, text="Quit", font=("Helveita", 20), compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", border_color="#000000", border_width=2, width=250, text_color="#000000", height=75, corner_radius=25)
        self.btn_quit.place(relx=.5, rely=.93,anchor= 'center')   
   
    def qrcode_authentication(self):
        qrcode = ressources.currentRecyclingSession.authentication.scan_QRCode()
        if (qrcode != None):
            authentication = ressources.currentRecyclingSession.authentication.authenticate(qrcode)
            if (authentication):
                self.open_success_window()
            else:
                self.open_error_window(label_txt=" Invalid credentials.")
        else:
            self.open_error_window(label_txt=" QR Code scan failed")

    
    def open_success_window(self):
        if self.toplevel_success_window is None or not self.toplevel_success_window.winfo_exists():
            self.toplevel_success_window = ToplevelSuccessWindow(label_txt=" Authentication setup successfully.", btn_txt="Start Recycling", btn_command=self.startRecycling)  # create window if its None or destroy
            self.toplevel_success_window.transient(self)
        else:
            self.toplevel_success_window.focus()  # if window exists focus i
    
    def open_error_window(self, label_txt):
        if self.toplevel_error_window is None or not self.toplevel_error_window.winfo_exists():
            self.toplevel_error_window = ToplevelErrorWindow(label_txt=label_txt, btn_quit_command=self.quit, btn_retry_command=self.retry)  # create window if its None or destroy
            self.toplevel_error_window.transient(self)
        else:
            self.toplevel_error_window.focus()  # if window exists focus i
    
    def startRecycling(self):
        self.toplevel_success_window.destroy()
        self.destroy()
        ToplevelRecyclingWindow()
    
    def quit(self):
        self.toplevel_error_window.destroy()
        self.destroy()
    
    def retry(self):
        self.toplevel_error_window.destroy()