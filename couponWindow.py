import customtkinter as ctk
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWindow, ToplevelWarningWindow, ToplevelErrorWindow, ToplevelSuccessWindow
import ressources

class CouponWindow(ToplevelWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(600, 600, *args, **kwargs)
        self.center_window()

        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(2).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = ctk.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.label_title = ctk.CTkLabel(self, font=("Helveita", 28), text="History", text_color="#000000")
        self.label_title.pack(padx=10, pady=(125, 25))

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=500, height=320)
        self.scrollable_frame.pack()
        
        for recyclableItem in ressources.currentRecyclingSession.recyclableItemList.keys():
            label = ctk.CTkLabel(self.scrollable_frame, text=str(recyclableItem) + " X " + str(ressources.currentRecyclingSession.recyclableItemList[recyclableItem]), font=("Helveita", 20), text_color="#000000")
            label.pack()
        
        self.label_total = ctk.CTkLabel(self.scrollable_frame, text="Total: " + " = " + str(ressources.currentRecyclingSession.total_recompense), font=("Helveita", 25), text_color="#000000")
        self.label_total.pack()
        
        self.btn_quit = ctk.CTkButton(self, command=self.destroy, text="Quit", font=("Helveita", 20), compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", border_color="#000000", border_width=2, width=250, text_color="#000000", height=75, corner_radius=25)
        self.btn_quit.place(relx=.5, rely=.93,anchor= 'center')  

        