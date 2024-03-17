from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog
import datetime
import os

class production_inventory:
    def __init__(self, window):
        self.window = window
        window.config(bg='#FBF3CB')
        window.title('Production Inventory')

        # background
        bgImage = Image.open('images/product_inventoryBG.png').resize((1340, 690))
        bgphoto = ImageTk.PhotoImage(bgImage)
        bgLabel = ttk.Label(window, image=bgphoto)
        bgLabel.image = bgphoto
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)


        # Window Centering
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


        font = ("Helvetica", 18, "bold")

        # Text entries and Labels
        product_name = tk.Label(window, text='Product Name:', font=font, bg='#843812', fg='#FAEAC5')
        product_name.place(x=185, y=200)

        product_name_text = ttk.Entry(window, width=50)
        product_name_text.place(x=120, y=240)

        product_quantity = tk.Label(window, text='Product Quantity:', font=font, bg='#843812', fg='#FAEAC5')
        product_quantity.place(x=173, y=285)

        product_quantity_text = ttk.Entry(window, width=50)
        product_quantity_text.place(x=120, y=325)

        product_pricePer_Piece = tk.Label(window, text='Product Price Per Piece:', font=font, bg='#843812', fg='#FAEAC5')
        product_pricePer_Piece.place(x=135, y=370)

        product_pricePer_Piece = ttk.Entry(window, width=50)
        product_pricePer_Piece.place(x=120, y=410)

        product_dic = {}

        # Functions
        def clear_text():
            product_name_text.delete(0, END)
            product_quantity_text.delete(0, END)
            product_pricePer_Piece.delete(0, END)

        def display_text(event):
            select = tree.focus()
            if select:
                item_values = tree.item(select)['values']
                if item_values:
                    clear_text()
                    product_name_text.insert(0, item_values[0])
                    product_quantity_text.insert(0, item_values[1])
                    product_pricePer_Piece.insert(0, item_values[2])

        def calculate(quantity, price):
            total = quantity*price
            return total

        def total_production(total):
            sum=0
            for i in total:
                sum+=i
            return sum

        def clear():
            window.withdraw()
            answer = simpledialog.askstring('Confirmation', 'Do you want to clear the data? \nType Yes or No')

            if answer == None:
                window.deiconify()
                pass

            if answer.upper() == 'Yes'.upper():
                for item in tree.get_children():
                    item_val = tree.item(item)['values']
                    tree.delete(item)
                    del product_dic[str(item_val[0])]
                clear_text()
                window.deiconify()

            elif answer.upper() == 'NO':
                window.deiconify()
                pass

            else:
                messagebox.showerror('Error', 'Invalid Input')
                window.deiconify()

        def add():
            name_entry = product_name_text.get()
            try:
                quantity_entry = int(product_quantity_text.get())
                price_entry = int(product_pricePer_Piece.get())
            except ValueError:
                messagebox.showerror('Error', 'Product Quantity and Price must be integers')
                return

            if not (name_entry and quantity_entry and price_entry):
                messagebox.showerror('Error', 'Enter all Fields')
            elif name_entry in product_dic:
                messagebox.showerror('Error', 'Product already added')
                pass
            else:
                amount = calculate(quantity_entry, price_entry)
                tree.insert('', 'end', values=(name_entry, quantity_entry, price_entry, amount))
                product_dic.update({name_entry: [quantity_entry, price_entry, amount]})

                clear_text()

        def update():
            name_entry = product_name_text.get()
            selected_item = tree.focus()

            if not selected_item:
                messagebox.showerror('Error', 'Choose an entry to update')
                return

            item_val = tree.item(selected_item)['values']
            original_name = str(item_val[0])

            if name_entry != original_name:
                for val in tree.get_children():
                    item_value = tree.item(val)['values']
                    if str(item_value[0]) == name_entry:
                        messagebox.showerror('Error', 'The product has already been added')
                        return
                    else:
                        pass
            else:
                pass

            try:
                quantity_entry = int(product_quantity_text.get())
                price_entry = int(product_pricePer_Piece.get())
            except ValueError:
                messagebox.showerror('Error', 'Product Quantity and Price must be integers')
                return

            amount = calculate(quantity_entry, price_entry)
            if not (name_entry and quantity_entry and price_entry):
                messagebox.showerror('Error', 'Enter all Fields')
                return

            if original_name != name_entry:
                del product_dic[original_name]

            tree.delete(selected_item)
            tree.insert('', 'end', values=(name_entry, quantity_entry, price_entry, amount))
            product_dic[name_entry] = [quantity_entry, price_entry, amount]
            messagebox.showinfo('Successfully updated', 'Entry successfully updated')

        def delete():
            window.withdraw()
            answer = simpledialog.askstring('Confirmation', 'Do you want to delete this entry? \nType Yes or No')
            window.deiconify()

            if answer.upper() == 'Yes'.upper():
                selected_item = tree.focus()
                if not selected_item:
                    messagebox.showerror('Error', 'Choose an entry to delete')
                else:
                    item_values = tree.item(selected_item)['values']
                    tree_name = str(item_values[0])
                    tree.delete(selected_item)
                    del product_dic[tree_name]
                    messagebox.showinfo('Successfully deleted', 'Entry successfully deleted')

            elif answer.upper() == 'NO':
                pass
            else:
                messagebox.showerror('Error', 'Invalid Input')


        def save():
            window.withdraw()
            answer = simpledialog.askstring('Confirmation','Do you want to save the data into a text file? \nType Yes or No.')

            if answer == None:
                window.deiconify()
                pass

            if answer.upper() == 'YES':
                entries = tree.get_children()
                all_val = []
                final_total = []
                for item in entries:
                    item_values = tree.item(item)['values']
                    quantity = item_values[1]
                    price = item_values[2]
                    amount = quantity * price
                    final_total.append(amount)

                for item in entries:
                    item_values = tree.item(item)['values']
                    all_val.append(item_values)

                current_date = datetime.date.today()
                total_calc = total_production(final_total)
                file_path = f'Production_Records/record{current_date}.txt'

                if os.path.exists(file_path):
                    messagebox.showerror('Error', 'Todays record has already been made. \nEdit the contents of the file in the Production Log.')
                    window.deiconify()
                else:
                    with open(file_path, 'w') as file:
                        header = '{:<30} {:<20} {:<30} {:<30}\n'.format('NAME', 'QUANTITY', 'PRICE PER PIECE', 'TOTAL')
                        file.write(header)
                        for value in all_val:
                            line = '{:<30} {:<20} {:<30} {:<30}\n'.format(*value)
                            file.write(line)
                        file.write("\n\n\n============================================================================================================================================\n")
                        file.write(f"Total Amount Produced: {total_calc}")
                        messagebox.showinfo('File Saved', f"Data saved successfully to {file_path}")
                        window.deiconify()

            elif answer.upper() == 'NO':
                window.deiconify()
                pass
            else:
                messagebox.showerror('Error', 'Invalid Input')
                window.deiconify()

        def home_page():
            confirmation = simpledialog.askstring('Confirmation', 'Are you sure you want to go back?\nYour entries would not be saved,\nand it would be lost. Type yes or no.')
            if confirmation == None:
                pass
            if confirmation.upper() == 'YES':
                window.destroy()
                os.system('python home_page.py')
            elif  confirmation.upper() == 'NO':
                pass
            else:
                messagebox.showerror('Error', 'Invalid input.')

        def question():
            messagebox.showinfo('Functions',
                                'We are now in the Production Inventory window. Here, you could create records of the production made within the day and everything would be recorded for you.\n\n'
                                'Here, you would need to input the name, quantity, and the price per piece of the product. Then the total amount produced for each product would then be provided for you.\n\n'
                                'Add - this button allows you to add data within the table.\n\n'
                                'Update - this button allows you to change your previous entries. You would have to select an entry in the table then proceed to the editin go fteh data\n\n'
                                'Save - his allows you to save a text file record of all your entries along with a overall total of all the entries for easy calculation of the days production\n\n'
                                'Clear - this enables you to clear the the treeview as well sa the data collected and start over.\n However you will ever be able to get the previuosly entered entries ever again\n\n'
                                'Delete - this enables you to delete selected entries from the treeview.\n\n'
                                'Back- this allows you to go back to he Home Page.')

        # Buttons
        add_button = tk.Button(text="Add", command=add, font=font, bd=0, bg='#FAEAC5', fg='#843812', width=7, height=1, activebackground='#843812', activeforeground='#FAEAC5')
        add_button.place(x=90, y=470)

        delete_button = tk.Button(text="Delete", command=delete, font=font, bd=0, bg='#FAEAC5', fg='#843812', width=7,height=1, activebackground='#843812', activeforeground='#FAEAC5')
        delete_button.place(x=220, y=470)

        update_button = tk.Button(text="Update", command=update, font=font, bd=0, bg='#FAEAC5', fg='#843812', width=7, height=1, activebackground='#843812', activeforeground='#FAEAC5')
        update_button.place(x=350, y=470)

        save_button = tk.Button(text="Save", command=save, font=font, bd=0, bg='#FAEAC5', fg='#843812', width=7, height=1, activebackground='#843812', activeforeground='#FAEAC5')
        save_button.place(x=150, y=550)

        clear_button = tk.Button(text="Clear", command=clear, font=font, bd=0, bg='#FAEAC5', fg='#843812', width=7,height=1, activebackground='#843812', activeforeground='#FAEAC5')
        clear_button.place(x=290, y=550)

        back_button = tk.Button(text='< Back', command=home_page, font=("Helvetica", 15, "bold"), bd=0, bg='#FAEAC5',fg='#843812', width=0, height=0, activebackground='#843812', activeforeground='#FAEAC5')
        back_button.place(x=10, y=1)

        help_button = tk.Button(text='?', command=question, font=("Helvetica", 17, "bold"), bd=0, bg='#FAEAC5',
                                fg='#843812', width=0, height=0, activebackground='#843812', activeforeground='#FAEAC5')
        help_button.place(x=1300, y=1)

        # Treeview widget
        style = ttk.Style(window)
        style.theme_use('clam')
        style.map('Treeview', background=[('selected', '#DDBB6B')])

        tree = ttk.Treeview(window, height=27)
        tree['columns'] = ('Name', 'Quantity', 'Price', 'Total' )

        tree.column('#0', width=0, stretch=tk.NO)
        tree.column('Name', anchor=tk.CENTER, width=170)
        tree.column('Quantity', anchor=tk.CENTER, width=170)
        tree.column('Price', anchor=tk.CENTER, width=170)
        tree.column('Total', anchor=tk.CENTER, width=170)

        tree.heading('Name', text='Name')
        tree.heading('Quantity', text='Quantity')
        tree.heading('Price', text='Price')
        tree.heading('Total', text='Total')

        tree.place(x=585, y=79)
        tree.bind("<<TreeviewSelect>>", display_text)

def page():
    window = tk.Tk()
    production_inventory(window)
    window.mainloop()

if __name__=='__main__':
    page()

