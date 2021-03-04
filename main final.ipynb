from tkinter import*
from tkinter import ttk
#Registeration
from PIL import Image,ImageTk 
from tkinter import messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # bg image 
        self.bg=ImageTk.PhotoImage(file="images/b22.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        self.left=ImageTk.PhotoImage(file="images/right.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
        #=== Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=50,y=30)
         # -----row 1
        title=Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_fname.place(x=50,y=130,width=250)
        
        title=Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_lname.place(x=370,y=130,width=250)
        
         # -----row 2
        contact=Label(frame1,text="Contact No.",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_contact.place(x=50,y=200,width=250)
        
        title=Label(frame1,text="Email",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_email.place(x=370,y=200,width=250)
         
            #----Row 3 
        self.ques=Label(frame1,text="Security Question",font=("times new roman",20,"bold"),bg="white",fg="gray")
        self.ques.place(x=50,y=240)
        
        
        
        self.cmb_ques=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)
        self.cmb_ques['values']=("select","Your Pet Name","Your Birth Place","Your Best Friends Name")
        self.cmb_ques.place(x=50,y=270,width=250)
        self.cmb_ques.current(0)
        
        ans=Label(frame1,text="Answer",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_ans=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_ans.place(x=370,y=270,width=250)
        
        
         # -----row 2
        password=Label(frame1,text="Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_pass=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_pass.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_cpass.place(x=370,y=340,width=250)
         
            
        #-----register button
        self.var_chk=IntVar()
        
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable= self.var_chk,bg="white",onvalue=1,offvalue=0,font=("times new roman",12)).place(x=50,y=380)
        
        self.btn_img=ImageTk.PhotoImage(file="images/20-203659_buy-now-button-png-register-now-yellow-button.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        
        btn_login=Button(self.root,text="Sigin In",font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180)
        
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or  self.txt_pass.get()=="" or self.cmb_ques.get()=="select" or self.txt_cpass.get()=="" or self.txt_ans.get()=="" or self.txt_email.get()=="" :
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        elif( self.txt_pass.get()!= self.txt_cpass.get()):
            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our T&C",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values (%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             
                             self.cmb_ques.get(),
                             self.txt_ans.get(),
                             self.txt_pass.get()                            
                           ))
                
                con.commit()
                con.close()
                messagebox.showinfo("Sucess","Registered Successfuly",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"error due to{str(es)}",parent=self.root)  
            
            
    
        
root=Tk()
obj=Register(root)
root.mainloop()
