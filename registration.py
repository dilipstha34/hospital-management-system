from pydoc import text
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from turtle import title

# Registration class is for patient registration window

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.minsize(1100, 650)
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

        ############functions ###############
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno ("Member Registration Form", "Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
                return

        # reset button function
        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt.config(state = DISABLED)

        # this function is for reset button which will ask user if he wants to add new record or not

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel("member Registration Form", "You want to add as new Recod")
            if reeesetbtt:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
            return

        def Reference_number():
            ranumber = random.randint(1000, 9999)
            randomRef = str(ranumber)
            Ref.set(randomRef)

        # TITLE 
        title = Label(self.root, text = "Member Registration Form", font = ("monotype corsiva", 30, "bold"), bd = 5,
                     relief = GROOVE, bg = "#E6005C", fg = "#000000")
        title.pack(side=TOP, fill = X)

        # member frame
        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "#001a66")
        Manage_Frame.place(relx = 0.015, rely = 0.135, relwidth = 0.345, relheight = 0.84)

        Manage_Frame.grid_columnconfigure(0, weight = 1)
        Manage_Frame.grid_columnconfigure(1, weight = 1)

        ######### text, label, comboboxes in manage frame #########
        Cus_title = Label (Manage_Frame, text = "Customer Details", font = ("arail", 20, "bold"), bg = "#001a66",fg = "white")
        Cus_title.grid(row =0, columnspan = 2, pady = 8)

        member_datelbl = Label(Manage_Frame, text = "Date", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_datelbl.grid(row = 1, column = 0, pady = 6, padx = 12, sticky = "w")

        member_datetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Date_of_Registration, width = 20)
        member_datetxt.grid(row = 1, column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_reflbl = Label (Manage_Frame, text = "Reference ID", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_reflbl.grid(row = 2, column = 0, pady = 6, padx = 12, sticky = "w")

        member_reftxt = Entry(Manage_Frame, font=("arial", 15, "bold"), state=DISABLED, textvariable=Ref, width = 20)
        member_reftxt.grid(row = 2, column = 1, pady = 6, padx = 12, sticky = "ew")

        member_fnamelbl = Label(Manage_Frame, text = "First Name", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_fnamelbl.grid(row = 3, column = 0, pady = 6, padx = 12, sticky = "w")

        member_fnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Firstname, width = 20)
        member_fnametxt.grid(row = 3, column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_lnamelbl = Label(Manage_Frame, text = "Last Name", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_lnamelbl.grid(row = 4, column = 0, pady = 6, padx = 12, sticky = "w")

        member_lnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Lastname, width = 20)
        member_lnametxt.grid(row = 4, column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_mobilelbl = Label(Manage_Frame, text = "Mobile No.", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_mobilelbl.grid(row = 5, column = 0, pady = 6, padx = 12, sticky = "w")

        member_mobiletxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Mobile_no, width = 20)
        member_mobiletxt.grid(row = 5 , column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_addresslbl = Label(Manage_Frame, text = "Address", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_addresslbl.grid(row = 6, column = 0, pady = 6, padx = 12, sticky = "w")

        member_addresstxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Address, width = 20)
        member_addresstxt.grid(row = 6, column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_pincodelbl = Label(Manage_Frame, text = "Pin Code", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_pincodelbl.grid(row = 7, column = 0, pady = 6, padx = 12, sticky = "w")

        member_pincodetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable = Pincode, width = 20)
        member_pincodetxt.grid(row = 7, column = 1 , pady = 6, padx = 12, sticky = "ew")

        member_genderlbl = Label(Manage_Frame, text = "Gender", font = ("arial", 15, "bold"), bg = "#001a66", fg= "white")
        member_genderlbl.grid(row = 8, column = 0, pady = 6, padx = 12, sticky = "w")

        member_gendercmb = ttk.Combobox(Manage_Frame, text = var4, state = "readonly", font = ("arail", 15, "bold"), width = 19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row = 8, column = 1, pady = 6, padx = 12, sticky = "ew")

        member_id_prooflbl = Label(Manage_Frame, text = "ID Proof", font = ("arial", 15, "bold"), bg = "#001a66", fg = "white")
        member_id_prooflbl.grid(row = 9, column=0, pady = 6, padx = 12, sticky = "w")

        member_id_proofcmb = ttk.Combobox(Manage_Frame, text = "ID Proof", state = "readonly", font = ("arail", 15, "bold"), width= 19)
        member_id_proofcmb['values'] = ("","Citizen Card", "Passport", "Driving License", "Pan Card", "Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row = 9, column = 1, pady = 6, padx = 12, sticky = "ew")

        member_memtypelbl = Label(Manage_Frame, text = "Member Type", font = ("arial", 15, "bold"), bg= "#001a66", fg= "white")
        member_memtypelbl.grid(row = 10, column=0 ,pady = 6 , padx = 12, sticky = "w")

        member_memtypecmb = ttk.Combobox(Manage_Frame, text = var2, state = "readonly", font = ("arail", 15, "bold"), width= 19)
        member_memtypecmb ['values'] = ("", "Male", "Female", "Other")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row = 10, column = 1, pady = 6 ,padx = 12, sticky = "ew")

        member_paymentwithlbl = Label(Manage_Frame, text = "Payment", font = ("arial", 15, "bold"), bg= "#001a66", fg= "white")
        member_paymentwithlbl.grid(row = 11, column=0 ,pady = 6 , padx = 12, sticky = "w")

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text = var1, state = "readonly", font = ("arail", 15, "bold"), width= 19)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card", "Esewa", "Khalti")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row = 11, column = 1, pady = 6 ,padx = 12, sticky = "ew")

        member_membership = Checkbutton (Manage_Frame, text = "Membership Fees", variable = var5, onvalue = 1,
                                          offvalue = 0, font = ("arial", 15, "bold"), bg = "#001a66", fg = "white")
        member_membership.grid(row = 12, column = 0, pady = 6, padx = 12, sticky = "w")

        member_membershiptxt = Entry(Manage_Frame, font = ("arail", 15, "bold"), state = DISABLED, justify = RIGHT, 
                                     textvariable = Membership, width = 20)
        member_membershiptxt.grid(row =12, column = 1, pady = 6, padx = 12, sticky = "ew") 


        ########Detail Frame ##
        detail_frame = Frame (self.root, relief = RIDGE, bd = 4, bg = "#001a66")
        detail_frame.place(relx = 0.37, rely = 0.135, relwidth = 0.615, relheight = 0.84)

        detail_frame.grid_rowconfigure(1, weight = 1)
        detail_frame.grid_columnconfigure(0, weight = 1)
        detail_frame.grid_columnconfigure(1, weight = 1)
        detail_frame.grid_columnconfigure(2, weight = 1)
        detail_frame.grid_columnconfigure(3, weight = 1)

        detail_label = Label(detail_frame, font = ("arail", 11, "bold"), pady = 10, padx=2, width = 95,
        text = "Date\t Ref Id\t Firstname   Lastname     Mobile No     Address     PincodeGender     Membership",
        bg = "#001a66", fg = "white")

        detail_label.grid(row=0, column=0, columnspan=4)

        detail_labeltxt = Text(detail_frame, width= 92, height = 23, font = ("arial", 12))
        detail_labeltxt.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 5, sticky = "nsew")

        ########## we will add button in detail frame ################3
        receiptbtn = Button(detail_frame, padx = 10, bg="#ff9966", width = 18, bd = 5 ,
                             font =("arail", 12, "bold"), text = "Receipt", command = Reference_number)
        receiptbtn.grid ( row = 2 , column= 0, padx = 8, pady = 8)

        resetbtn = Button(detail_frame, padx = 10, bd = 5 , 
                          font =("arail", 12, "bold"), bg="#ff9966", width = 18, text = "Reset", command = reeesetbtt)
        resetbtn.grid(row = 2, column = 1, padx = 8, pady = 8)
        
        exitbtn = Button(detail_frame, padx = 10, bg="#ff9966", width = 18, text = "Exit", bd = 5, 
                         font = ("arail", 12, "bold"), command = exitbtt)
        exitbtn.grid(row = 2, column = 2, padx = 8, pady = 8)
            
# main function to run the program 

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()