import random
import time
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from turtle import title

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")

        # Taking live date time
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        ### this var1,2,3,4,5 are for combobox
        var1 = StringVar()
        var2= StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar() # we will keep this as int bcuz we will keep here numerical value

        Membership = StringVar()
        Membership.set("0") # when membeship checkbox is unclicked or reset has been done it will automatically set as 0


        # TITLE 
        title = Label(self.root, text = "Member Registration Form", font = ("monotype corsiva", 30, "bold"), bd = 5,
                     relief = GROOVE, bg = "#E6005C", fg = "#000000")
        title.pack(side=TOP, fill = X)

        # member frame
        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "#001a66")
        Manage_Frame.place(x = 20, y = 100, width=450, height = 638)

        ######### text, label, comboboxes in manage frame #########
        Cus_title = Label (Manage_Frame, text = "Customer Details", font = ("arail", 20, "bold"), bg = "#001a66",fg = "white")
        Cus_title.grid(row =0, columnspan = 2, pady = 5)

        member_datelbl = Label(Manage_Frame, text = "Date", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_datelbl.grid(row = 1, column = 0, pady = 5, padx = 10, sticky = "w")

        member_datetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Date_of_Registration)
        member_datetxt.grid(row = 1, column = 1 , pady = 5, padx = 10, sticky = "w")

        member_reflbl = Label (Manage_Frame, text = "Reference ID", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_reflbl.grid(row = 2, column = 0, pady = 5, padx = 10, sticky = "w")

        member_reftxt = Entry(Manage_Frame, font=("arial", 15, "bold"), state=DISABLED, textvariable=Ref)
        member_reftxt.grid(row = 2, column = 1, pady = 5, padx = 10, sticky = "w")

        member_fnamelbl = Label(Manage_Frame, text = "First Name", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_fnamelbl.grid(row = 3, column = 0, pady = 5, padx = 10, sticky = "w")

        member_fnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Firstname)
        member_fnametxt.grid(row = 3, column = 1 , pady = 5, padx = 10, sticky = "w")

        member_lnamelbl = Label(Manage_Frame, text = "Last Name", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_lnamelbl.grid(row = 4, column = 0, pady = 5, padx = 10, sticky = "w")

        member_lnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Lastname)
        member_lnametxt.grid(row = 4, column = 1 , pady = 5, padx = 10, sticky = "w")

        member_mobilelbl = Label(Manage_Frame, text = "Mobile No.", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_mobilelbl.grid(row = 5, column = 0, pady = 5, padx = 10, sticky = "w")

        member_mobiletxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Mobile_no)
        member_mobiletxt.grid(row = 5 , column = 1 , pady = 5, padx = 10, sticky = "w")

        member_addresslbl = Label(Manage_Frame, text = "Address", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_addresslbl.grid(row = 6, column = 0, pady = 5, padx = 10, sticky = "w")

        member_addresstxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Address)
        member_addresstxt.grid(row = 6, column = 1 , pady = 5, padx = 10, sticky = "w")

        member_pincodelbl = Label(Manage_Frame, text = "Pin Code", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_pincodelbl.grid(row = 7, column = 0, pady = 5, padx = 10, sticky = "w")

        member_pincodetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Pincode)
        member_pincodetxt.grid(row = 7, column = 1 , pady = 5, padx = 10, sticky = "w")

        member_genderlbl = Label(Manage_Frame, text = "Gender", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_genderlbl.grid(row = 8, column = 0, pady = 5, padx = 10, sticky = "w")

        member_gendercmb = ttk.Combobox(Manage_Frame, text = var4, state = "readonly", font = ("arail", 15, "bold"), width = 19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0) # when nothing it will be set as empty which we have given at index 6
        member_gendercmb.grid(row = 8, column = 1, pady = 5, padx = 10, sticky = "w")

        ########Detail Frame ##
        detail_frame = Frame (self.root, relief = RIDGE, bg = "#001a66")
        detail_frame.place(x=500, y = 100, width = 828, height = 630)
            

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()