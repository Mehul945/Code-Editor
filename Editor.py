import tkinter as tk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.commondialog import Dialog
def dark():
    name.config(bg='black',insertbackground='white', fg='white')

def light():
    name.config(bg='white',insertbackground='black', fg='black')

def blue():
    name.config(bg='blue',insertbackground='white', fg='white')

f = None

def save_as():
    global f
    f = asksaveasfile(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                      ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if f != None:
        f.write(name.get("1.0", "end-1c"))


def save():
    global f
    if f != None:
        f.write(name.get("1.0", "end-1c"))

def open_file():
    global f
    f = askopenfile(initialfile='Untitled.txt', defaultextension=".txt", \
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")], mode='w+')
    if f != None:
        text=f.read()
        name.insert("end",text)
        del text

win = tk.Tk()
win.geometry("720x480")
win.title("Mehul's App")
menu = tk.Menu(win)
theme = tk.Menu(menu, tearoff=False)
theme.add_command(label="Dark", command=dark)
theme.add_command(label="Light", command=light)
theme.add_command(label="Blue", command=blue)
theme.add_separator()
fileMenu = tk.Menu(menu, tearoff=False)
fileMenu.add_command(label="open file", command=open_file)
fileMenu.add_command(label="save", command=save)
fileMenu.add_command(label="save as", command=save_as)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=win.quit)

menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Theme", menu=theme)
tk.Label(win, text="Mehul's App", font=('italic', 25), height=1,
         fg='black', width=100, bg='cyan', pady=10).pack(side='top')


scrl=tk.Scrollbar(win,orient='vertical')
name = tk.Text(win, font=("alrial", 18), width=85)
scrl.config(command=name.yview)

name.configure(yscrollcommand=scrl.set)
name.pack(side='bottom')
scrl.pack(side='right',fill='y')
win.config(menu=menu)
k=0
def show(key):
    global k
    if (key.keycode!=17 | key.keycode!=83) | k>=100:
        k=0
    else:
        k+=key.keycode
    if k==100:
        save()

win.bind("<KeyRelease>",show)
win.mainloop()

