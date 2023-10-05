import tkinter as tk

root = tk.Tk()

background_image=tk.PhotoImage(file = "ressources/money.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()