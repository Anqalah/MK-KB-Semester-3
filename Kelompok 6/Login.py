from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Admin!")
root.geometry("200x100")

username = "admin"
password = "admin"

def login():
    user = e1.get()
    pas = e2.get()

    if(username == user and password == pas):
        messagebox.showinfo("Login Berhasil", "Selamat login berhasil")
    else:
        messagebox.showwarning("Login gagal", "Maaf username atau password yang anda masukkan salah")

label = Label(root, text="Login Admin")
label.pack()

e1 = Entry(root)
e1.pack()
e1.insert(0, "")

e2 = Entry(root)
e2.pack()
e2.insert(0, "")

tombol = Button(root, text="Login", command=login)
tombol.pack()

root.mainloop()