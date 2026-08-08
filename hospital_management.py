import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()


class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitle = Label(self.frame, text="Hospital Management System", font=("Arial", 40, "bold"), bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.LoginFrame1 = Frame(self.frame, bd=10, width=1000, height=300, relief="groove")
        self.LoginFrame1.grid(row=1, column=0, pady=10)

        self.LoginFrame2 = Frame(self.frame, bd=10, width=1000, height=300, relief="groove")
        self.LoginFrame2.grid(row=2, column=0, pady=15)

        self.LoginFrame3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.LoginFrame3.grid(row=3, column=0, pady=5)

        self.button_reg = Button(self.LoginFrame3, text="Patient Registration Window", font=("arial", 15, "bold"), command=self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_Hosp = Button(self.LoginFrame3, text="Hospital Management Window", font=("arial", 15, "bold"), command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Dr_appt = Button(self.LoginFrame3, text="Doctor Appointment Window", font=("arial", 15, "bold"), command=self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=0, column=2, padx=10, pady=10)

        self.button_med_stock = Button(self.LoginFrame3, text="Medicine Stock Window", font=("arial", 15, "bold"), command=self.Medicine_window)
        self.button_med_stock.grid(row=0, column=3, padx=10, pady=10)

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)

    def Medicine_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)


class windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")
        self.master.geometry("1350x750+0+0")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.title = Label(self.frame, text="Patient Management System", font=("Arial", 35, "bold"), bd=10, relief="sunken")
        self.title.pack(pady=20)


class windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.title = Label(self.frame, text="Hospital Management System", font=("Arial", 35, "bold"), bd=10, relief="sunken")
        self.title.pack(pady=20)


class windows4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Appointment System")
        self.master.geometry("1350x750+0+0")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.title = Label(self.frame, text="Doctor Appointment System", font=("Arial", 35, "bold"), bd=10, relief="sunken")
        self.title.pack(pady=20)


class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine Management System")
        self.master.geometry("1350x750+0+0")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.title = Label(self.frame, text="Medicine Management System", font=("Arial", 35, "bold"), bd=10, relief="sunken")
        self.title.pack(pady=20)


if __name__ == "__main__":
    main()