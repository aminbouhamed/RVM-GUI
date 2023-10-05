import customtkinter
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWindow, ToplevelWarningWindow, ToplevelErrorWindow, ToplevelSuccessWindow
from couponWindow import CouponWindow
import ressources

class CheckoutWindow(ToplevelWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(600, 600, *args, **kwargs)
        self.center_window()
        self.success_window = None
        self.error_window = None
        self.couponWindow = None
        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(2).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        img_coupon = ImageTk.PhotoImage(Image.open("ressources/promo-code.png").resize((50, 50), Image.ANTIALIAS))
        self.btn_coupon = customtkinter.CTkButton(self, command=self.print_coupon, text=" PRINT COUPON " , image=img_coupon, font=("Helveita", 20), compound="left", bg_color="#FFFFFF", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_coupon.place(relx=.5, rely=.3, anchor= 'center') 

        img_redeem = ImageTk.PhotoImage(Image.open("ressources/booking.png").resize((50, 50), Image.ANTIALIAS))
        self.btn_redeem = customtkinter.CTkButton(self, command=self.redeem_recompense, text=" USE MY ACCOUNT" , image=img_redeem, font=("Helveita", 20), compound="left", bg_color="#FFFFFF", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_redeem.place(relx=.5, rely=.7, anchor= 'center')

        if not ressources.currentRecyclingSession.authentication.is_authenticated:
            self.btn_redeem.configure(state="disabled")
          
    def print_coupon(self):
        self.destroy()
        self.couponWindow = CouponWindow()

    def redeem_recompense(self):
        response = ressources.currentRecyclingSession.persistRecyclingSession()
        if response.status_code==200:
            self.success_window = ToplevelSuccessWindow(btn_command=self.startRecycling)
        else:
            self.error_window = ToplevelErrorWindow(btn_quit_command=self.quit, btn_retry_command=self.retry)
    
    def startRecycling(self):
        self.success_window.destroy()
        self.destroy()
    
    def quit(self):
        self.error_window.destroy()
        self.destroy()
    
    def retry(self):
        self.error_window.destroy()
