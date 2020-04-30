from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk

todo_list_reader_mode = open("todos.txt", "r")


# configure window
win = Tk()
win.geometry("600x600")
win.title("Simple TODO")
win.configure(bg="#e7e7e7")
win.iconbitmap("resources/icon.ico")

def add_to_todo_list():
    todo_list_write_mode = open("todos.txt", "a")
    supported_input = todo_text_entry.get()
    todo_cat = cat_select_box.get()
    if len(supported_input) == 0 and len(todo_cat) == 0:
        msg.showerror("გაფრთხილება", "გთხოვთ შეიყვანეთ ყველა ველი")
    else:
        msg.showinfo("success", "ჩანაწერი წარმატებით დაემატა")
        todo_list_write_mode.write(supported_input + "\n")
        list_items = main_todo_list.cget("text") + supported_input + "\n"
        main_todo_list.config(text=list_items)

    print(supported_input)




main_image = Image.open('resources/logo.png')
main_image.resize((80,80), )
logo = ImageTk.PhotoImage(main_image)
Label(win, image=logo).pack()


nb = Notebook(win)
nb.pack(side='top', expand=1, fill='both', padx=10, pady=10)

tab1 = Frame(nb)
nb.add(tab1, text="შესრულებულები", underline=0)


# tab2 = Frame(nb)
# nb.add(tab2, text="შეუსრულებლები", underline=0)

tab3 = Frame(nb)
nb.add(tab3, text="დამატება", underline=0)

nb.select(tab1)
nb.enable_traversal()



# first tab items
main_todo_list = Label(tab1, text=todo_list_reader_mode.read())
main_todo_list.pack()


# last tab items
todo_text_entry = Entry(tab3)
todo_text_entry.pack(pady="30")
Radiobutton(tab3, text="მნიშვნელოვანია", value=1).pack()
Radiobutton(tab3, text="არ არის მნიშვნელოვანია", value=2).pack()

cat_select_box = Combobox(tab3, values=["გართობა", "სამსახური", "დასვენება", "რამე"])
cat_select_box.pack()

Button(tab3, text="დამატება", command=add_to_todo_list).pack(pady="10")



win.mainloop()
