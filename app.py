import tkinter as tk
import customtkinter
import cv2
import numpy as np
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWindow, ToplevelWarningWindow, ToplevelErrorWindow, ToplevelSuccessWindow
from topLevelRecyclingWindow import ToplevelRecyclingWindow
from topLevelAuthenticationWindow import ToplevelAuthenticationWindow
from recyclingSession import RecyclingSession
import ressources

customtkinter.set_default_color_theme("ressources/blue.json")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 600
        self.height = 600
        self.center_window()
        self.title('ReviveMate')

        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(1).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.toplevel_reycling_window = None
        self.toplevel_authentication_window = None
        self.warning_window = None
        img_auth = ImageTk.PhotoImage(Image.open("ressources/user.png").resize((50, 50), Image.ANTIALIAS))
        img_recycle = ImageTk.PhotoImage(Image.open("ressources/recycle.png").resize((50, 50), Image.ANTIALIAS))
        img_problem = ImageTk.PhotoImage(Image.open("ressources/problem.png").resize((50, 50), Image.ANTIALIAS)) 
        self.btn_auth = customtkinter.CTkButton(self, command=self.open_authentication_interface, text="Authenticate", image=img_auth, font=("Helveita", 20), compound="left", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_recycle = customtkinter.CTkButton(self, command=self.open_warning_window, text="Recycle", font=("Helveita", 20), image=img_recycle, compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", border_color="#000000", border_width=2, width=350, height=75, text_color="#000000", corner_radius=25)
        self.btn_problem = customtkinter.CTkButton(self, text="Report a problem", font=("Helveita", 20), image=img_problem, compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", width=350, height=75, corner_radius=25, text_color="#000000")
        self.btn_auth.place(relx=.5, rely=.52,anchor= 'center')
        self.btn_recycle.place(relx=.5, rely=.7,anchor= 'center')
        self.btn_problem.place(relx=.5, rely=.87,anchor= 'center')


    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))

    def open_warning_window(self):
        self.warning_window = ToplevelWarningWindow(warning=" Warning: Not authenticated", btn_ignore_txt="Start Recycling", btn_appreciate_txt="Authenticate", btn_ignore_command=self.open_reycling_interface, btn_appreciate_command=self.open_authentication_interface)
        self.warning_window.transient(self)
    
    def open_reycling_interface(self):
        ressources.startNewRecyclingSession()
        if self.warning_window is not None:
            self.warning_window.destroy()
        
        if self.toplevel_reycling_window is None or not self.toplevel_reycling_window.winfo_exists():
            self.toplevel_reycling_window = ToplevelRecyclingWindow()  # create window if its None or destroyed
        else:
            self.toplevel_reycling_window.focus()  # if window exists focus
    
    def open_authentication_interface(self):
        ressources.startNewRecyclingSession()
        if self.warning_window is not None:
            self.warning_window.destroy()
        if self.toplevel_authentication_window is None or not self.toplevel_authentication_window.winfo_exists():
            self.toplevel_authentication_window = ToplevelAuthenticationWindow()  # create window if its None or destroyed
        else:
            self.toplevel_authentication_window.focus()  # if window exists focus
    

        



#app = App()


#img_support = ImageTk.PhotoImage(Image.open("ressources/support.png").resize((30, 30), Image.ANTIALIAS))
#label_support = customtkinter.CTkLabel(app, text="Support 24/7 \n 20666369", font=("Helveita", 15), image=img_support, compound="left", width=200, height=50)



#label_support.pack(anchor="se")
#app.mainloop()

"""


def print_me():
    label["text"] = txt.get("1.0", "end")

def delete():
    listbox.delete((listbox.index(ACTIVE)))
frame1 = Frame(app, bg="blue")
btn = Button(frame1, command=print_me, text="click me", width="50", height="10", font="24", bg="black", fg="white", padx=20, pady=50)
frame2 = Frame(app, bg="red")
label = Label(frame2, text="suuiii", width="50", height="5", bg="green", fg="white", font="40")
frame3 = Frame(app, bg="green")
txt = Text(frame3, width="50", height="5", bg="white", fg="black", font="40")

txt.pack()
btn.pack()
label.pack()

btn2 = Button(app, text="btn2", bg="black", fg="white")
btn2.pack()
btn2.place(anchor=NW, width=100, height=100, bordermode=OUTSIDE)

#frame1.pack(side=TOP)
#frame2.pack(side=LEFT)
#frame3.pack(side=RIGHT)

#frame1.grid(column=1, row=1)
#frame2.grid(column=1, row=2)
#frame3.grid(column=1, row=3)



checkbtn = Checkbutton(app, text="Auto Save", font="14", command=print_me, state="disabled", onvalue=1, offvalue=0)
checkbtn.pack()

rdbtn1 = Radiobutton(app, text="Male", value=1)
rdbtn2 = Radiobutton(app, text="female", value=2)
rdbtn1.pack()
rdbtn2.pack()

listbox = Listbox(app)
listbox.insert(1, "OPT1")
listbox.insert(2, "OPT2")
listbox.insert(3, "OPT3")
listbox.pack()
btndel = Button(app, text="Delete", command=delete)
btndel.pack()


"""

#line = tk.Frame(self.toplevel_reycling_window, height=2, bg='gray')
#line.pack(fill='x', padx=10, pady=10)