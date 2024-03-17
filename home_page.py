from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import sys


class homePage:
    def __init__(self, window):
        self.window = window

        width = 1340
        height = 690
        x = 100
        y = 40
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # window Icon
        icon = PhotoImage(file='images/opening_logo.png')
        window.iconphoto(True, icon)
        window.title('Welcome')
        window.config(bg='#843812')

        def log_out():
            sys.exit(window.destroy())

        def production_inventory():
            window.destroy()
            os.system("python production_inventory.py")

        def production_log():
            window.destroy()
            os.system('python production_log.py')

        def question():
            messagebox.showinfo('Welcome!',
                                'We are now in the Home page. Here you could go to the other functions of the app.\n\n'
                                'If you press the Production Inventory button, you would then be directed to the Production Inventory recorder.\n'
                                'Wherein you could input the name, quantity of the product produced, and its price per piece, and it would instantly \n'
                                'calculate the total amount of the product.\n\n'
                                'Then, if you press the Production Log, you would be able to access all the past records saved, and you can change the files\n'
                                'contents as well.\n\n'
                                'And, if you press the Log out button, you would be logged out of the program and the program will stop\n\n'
                                'I hope you find this useful!')

        # Window Background
        bgImage = Image.open('images/home_page_bg.png').resize((1340, 690))
        bgPhoto = ImageTk.PhotoImage(bgImage)
        bgLabel = ttk.Label(window, image=bgPhoto)
        bgLabel.image = bgPhoto
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        # character
        tk.Label(text="Welcome!", fg="white", background="#843812",
                 font=("Helvetica", 20)).place(x=248, y=394)

        # Buttons
        home_label = tk.Label(window, text='Home', fg='#843812',bg='#FAEAC5' ,font=("", 16, "bold","underline"), border=17, width=10,)
        home_label.place(x=450, y=2)

        production_inventory = tk.Button(window, command=production_inventory, text='Production Inventory', bg='#843812', font=("", 16, "bold"), bd=0, fg='white', width=20, height=2,activebackground='#FAEAC5', activeforeground='#843812')
        production_inventory.place(x=607, y=1)

        production_log = tk.Button(window, command=production_log, text='Production Log', bg='#843812',font=("", 16, "bold"), bd=0, fg='white', width=20, height=2, activebackground='#FAEAC5', activeforeground='#843812')
        production_log.place(x=873, y=1)

        log_out = tk.Button(window, text='Log out', command=log_out, bg='#843812', font=("", 16, "bold"), bd=0, fg='white', width=15, height=2, activebackground='#FAEAC5', activeforeground='#843812')
        log_out.place(x=1139, y=1)

        help_button = tk.Button(text='?', command=question, font=("Helvetica", 17, "bold"), bd=0, bg='#FAEAC5',
                                fg='#843812', width=0, height=0, activebackground='#843812', activeforeground='#FAEAC5')
        help_button.place(x=10, y=1)

def page():
    window = Tk()
    homePage(window)
    window.mainloop()


if __name__ == '__main__':
    page()





