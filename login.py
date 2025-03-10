from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
from subprocess import call


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import dashboard

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        frame = Frame(self.root)
        frame.place(x=610, y=160, width=340, height=450)

        get_str = Label(frame, text="ADMIN LOGIN", font=("Vijaya", 24, "bold"), fg="navy")
        get_str.place(x=60, y=100)

        username = Label(frame, text="Username", font=("FreesiaUPC", 15, "bold"), fg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("IrisUPC", 12))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("FreesiaUPC", 15, "bold"), fg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("IrisUPC", 12), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login, font=("Leelawadee", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)  

    def login(self):
        if self.txtuser.get() == "Srinivasan" and self.txtpass.get() == "srini789":
            messagebox.showinfo("Successful", "Login successful")
            self.root.destroy()
            call(['python', 'dashboard.py'])  # Open dashboard window
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()







if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()



    

                      