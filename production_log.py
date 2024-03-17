from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os


class production_log():
    def __init__(self, window):
        self.window = window
        self.file_path = ""

        #Window Centering
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


        def open_file():
            file_name = filedialog.askopenfilename(initialdir='Production_Records', title='Open file', filetypes=(("Text Files",'*.txt'),))
            self.file_path = file_name
            filename = open(file_name,'r')
            text = filename.read()
            text_box.delete(1.0, END)
            text_box.insert(END, text)
            window.deiconify()


        def save_change():
            window.withdraw()
            answer = simpledialog.askstring('Confirmation', 'Do you want to save the changes in the file? \nType yes or no.')

            if answer == None:
                window.deiconify()
                pass

            if answer and answer.upper() == 'YES':
                with open(self.file_path, 'w') as file:
                    file.write(text_box.get("1.0", END))
                    messagebox.showinfo('Successful', 'File successfully saved')
                    text_box.delete(1.0, END)
                    window.deiconify()

            elif answer.upper() == 'NO':
                window.deiconify()
                pass

            else:
                messagebox.showerror('Error', 'Invalid Input')
                window.deiconify()

        def home_page():
            window.destroy()
            os.system('python home_page.py')

        def question():
            messagebox.showinfo('Functions',
                                'We are now in the Production Log window. Here, you could access and edit previuosly saved logs/records.\n\n'
                                'Open - this button allows you to open a file from the record book.\n\n'
                                'Save - this button allows you to save the changes you have made in the text box into the file it self.\n\n'
                                'Back - this allows you to go back to the Home Page.')

        font = ("Helvetica", 18, "bold")
        font2 = ("Helvetica", 23, "bold")

        text_box = tk.Text(window, width=140, height=33)
        text_box.place(x=107,y=50)

        open_button = tk.Button(text="Open", command=open_file, font=font2, bd=0, bg='#FAEAC5', fg='#843812', width=12, height=1,activebackground='#843812', activeforeground='#FAEAC5')
        open_button.place(x=368, y=603)

        save_button = tk.Button(text="Save", command=save_change, font=font2, bd=0, bg='#FAEAC5', fg='#843812', width=12,height=1,activebackground='#843812', activeforeground='#FAEAC5')
        save_button.place(x=690, y=603)

        back_button = tk.Button(text='< Back', command=home_page, font=("Helvetica", 15, "bold"), bd=0, bg='#FAEAC5',
                                fg='#843812', width=0, height=0, activebackground='#843812', activeforeground='#FAEAC5')
        back_button.place(x=10, y=1)

        help_button = tk.Button(text='?', command=question, font=("Helvetica", 17, "bold"), bd=0, bg='#FAEAC5', fg='#843812', width=0, height=0, activebackground='#843812', activeforeground='#FAEAC5')
        help_button.place(x=1300, y=1)


def page():
    window = tk.Tk()
    production_log(window)
    window.mainloop()

if __name__=='__main__':
    page()







