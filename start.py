from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os
import sys

root = Tk()
root.config(bg='#FBF3CB')
image_open = Image.open('images/opening_logo.png')
photo = ImageTk.PhotoImage(image_open)
bgLabel = ttk.Label(root, image=photo)
bgLabel.image = photo
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# window Icon
icon = PhotoImage(file='images/opening_logo.png')
root.iconphoto(True, icon)
root.title('Welcome')
root.config(bg='#843812')

height = 560
width = 540
x = 500
y = 120
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#FBF3CB')

progress_label = Label(root, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='#B7441E')
progress_label.place(x=200, y=490)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=450)

exit_btn = Button(text='x', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"), fg='#B7441E')
exit_btn.place(x=490, y=0)


def exit_window():
    sys.exit(root.destroy())

def top():
    root.destroy()
    os.system("python home_page.py")

i = 0

def load():
    global i
    if i <= 10 :
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 5
    else:
        top()

load()
root.mainloop()