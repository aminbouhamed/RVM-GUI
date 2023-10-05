import customtkinter
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWindow, ToplevelWarningWindow, RecyclingErrorWindow
from checkoutWindow import CheckoutWindow
from detect import object_detection, volume_brand_classification
import cv2
import ressources

class ToplevelRecyclingWindow(ToplevelWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(600, 600, *args, **kwargs)
        self.center_window()

        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(2).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.recycling_error_window = None
        
        self.frame = customtkinter.CTkFrame(self)
        
        self.frame.pack(pady=100)

        recyclingSession = ressources.currentRecyclingSession
        img_bottle = ImageTk.PhotoImage(Image.open("ressources/water.png").resize((50, 50), Image.ANTIALIAS))
        self.label_bottle = customtkinter.CTkLabel(self.frame, text=" X " + str(recyclingSession.bottleCount), image=img_bottle, font=("Helveita", 20), compound="left", width=250, height=100, fg_color="#FFFFFF", text_color="#000000")
        self.label_bottle.pack(side='left')

        img_can = ImageTk.PhotoImage(Image.open("ressources/soda-can.png").resize((50, 50), Image.ANTIALIAS))
        self.label_can = customtkinter.CTkLabel(self.frame, text=" X " + str(recyclingSession.canCount), image=img_can, font=("Helveita", 20), compound="left", width=250, height=100, fg_color="#FFFFFF", text_color="#000000")
        self.label_can.pack()

        img_money = ImageTk.PhotoImage(Image.open("ressources/money.png").resize((50, 50), Image.ANTIALIAS))
        self.btn_total_recompense = customtkinter.CTkButton(self, command=self.open_checkout_window, text=" Total: " + str(recyclingSession.total_recompense) + " $", image=img_money, font=("Helveita", 20), compound="left", bg_color="#FFFFFF", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_total_recompense.place(relx=.5, rely=.52, anchor= 'center')
            
        img_recycle = ImageTk.PhotoImage(Image.open("ressources/recycle.png").resize((50, 50), Image.ANTIALIAS))
        self.btn_recycle = customtkinter.CTkButton(self, command=self.recycle , text="Recycle", font=("Helveita", 20), image=img_recycle, compound="left", bg_color="#FFFFFF", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_recycle.place(relx=.5, rely=.7, anchor= 'center')

        self.btn_quit = customtkinter.CTkButton(self, command=self.destroy, text="Quit", font=("Helveita", 20), compound="left", bg_color="#FFFFFF", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_quit.place(relx=.5, rely=.85,anchor= 'center')
    
    def open_error_interface(self, warning):
        self.toplevel_warning_window = None
        if self.toplevel_warning_window is None or not self.toplevel_warning_window.winfo_exists():
            self.toplevel_warning_window = ToplevelWarningWindow(warning)  # create window if its None or destroy
        else:
            self.toplevel_warning_window.focus()  # if window exists focus window
    
    def open_checkout_window(self):
        self.checkout_window = None
        if self.checkout_window  is None or not self.checkout_window .winfo_exists():
            self.checkout_window  = CheckoutWindow()  # create window if its None or destroy
        else:
            self.toplevel_warning_window.focus()  # if window exists focus window
    
    def retry(self):
        self.recycling_error_window.destroy()
    
    def recycle(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        img_path = 'img.jpg'
        cv2.imwrite(img_path, frame)
        cam.release()
        img = cv2.imread(img_path)
        _, img_encoded = cv2.imencode('.jpg', img)
        img_file = {'img': ('img.jpg', img_encoded.tobytes(), 'img/jpeg')}
        
        bottle = 0.0
        cup = 1.0

        detected_objects = object_detection(img_file).json()
        print(detected_objects)

        if len(detected_objects) == 0:
            self.recycling_error_window = RecyclingErrorWindow(label_txt=" Foreign object detected", btn_command=self.retry)
            self.recycling_error_window.transient(self)
        elif cup in detected_objects:
            self.open_error_interface(' Please remove cup')
        else:
            if bottle in detected_objects:
                ressources.currentRecyclingSession.bottleCount+=1
                self.label_bottle.configure(text=" X " + str(ressources.currentRecyclingSession.bottleCount))
            else:
                ressources.currentRecyclingSession.canCount+=1
                self.label_can.configure(text=" X " + str(ressources.currentRecyclingSession.canCount))
            
            ressources.currentRecyclingSession.update_total_recompense()
            self.btn_total_recompense.configure(text=" Total: " + str(ressources.currentRecyclingSession.total_recompense))

            recyclableItem = volume_brand_classification(img_file).json()
            print(recyclableItem)
            
            if recyclableItem in ressources.currentRecyclingSession.recyclableItemList.keys():
                ressources.currentRecyclingSession.recyclableItemList[recyclableItem] = ressources.currentRecyclingSession.recyclableItemList[recyclableItem] + 1
            else:
                ressources.currentRecyclingSession.recyclableItemList[recyclableItem] = 1

            print(ressources.currentRecyclingSession.recyclableItemList)