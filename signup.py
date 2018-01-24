import sqlite3
from tkinter import messagebox
from tkinter import *
import valid
con = sqlite3.connect('recipes.db')
p = con.cursor()
                
def home(root,s):
		root.deiconify()
		s.destroy()
def back(v,c):
		v.deiconify()
		c.destroy()
			
def signup(root,root1,name):
		def store(value,c,name,root1):
			#print("hello")
			#print(name)
			flag=False
			if e1.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="":				#Condition to check Empty Fields
				messagebox.showinfo("ERROR3","Each Field is Mandatory")
			else:
				if valid.checkname(e1.get())==False:
					messagebox.showinfo("ERROR5","Name cannot have any special character or number")
				elif value!=1 and value!=2:
					messagebox.showinfo("Please,Select Your Gender!")
				elif valid.checkusername(e3.get())==False:
					messagebox.showinfo("Username Not Valid","Username Must Be An Identifier")
				elif valid.checkpassword(e4.get())==False:
					messagebox.showinfo("\nPassword Should Be Minumum Of 6 Digit")
				elif valid.checkconfirm_password(e4.get(),e5.get())==False:
					messagebox.showinfo("ERRROR3","The Password Doesn't Match With The Above Password")
				else:
					p.execute("select username from '"+name+"';")
					result=p.fetchall()
					print(result)
					#con.commit()
					for row in result:																#Check if Similar Date and Time Exists
								if row[0]==e3.get():
									flag==True
									messagebox.showinfo("ERROR2","Username Already Exists")
									break
								if flag==False:
									if m.get()==1:
										str_gender="Male"
									else:
										str_gender="Female"
                                                #Add New Entry to Datab
								if name=="admin":
									p.execute("insert into '"+name+"' (name,gender,username,password,confirm_password) values ( ?,?,?,?,? )",(e1.get(),str_gender,e3.get(),e4.get(),e5.get()))
									con.commit()
									p.execute("insert into user (name,gender,username,password,confirm_password) values ( ?,?,?,?,? )",(e1.get(),str_gender,e3.get(),e4.get(),e5.get()))
									con.commit()
									messagebox.showinfo("Success","Succesfully Signed In")
								else:
										p.execute("insert into '"+name+"' (name,gender,username,password,confirm_password) values ( ?,?,?,?,? )",(e1.get(),str_gender,e3.get(),e4.get(),e5.get()))
										con.commit()

										messagebox.showinfo("Success","Succesfully Signed In")
                                                
										p.execute('''select name from user''')
										result=p.fetchall()
										print(result)
										#con.commit()
										root1.deiconify()
										c.destroy()
										break           
							
                                

					
        
		c=Toplevel(root)
		c.title("signup")
		c.minsize(1520,820)
		c.configure(background="darkolivegreen1")
		m = IntVar()
		#background_img = PhotoImage(file="C:\\Users\\HP\\Desktop\\New folder\\eem1.png")
		#background_label = Label(c,image=background_img)
		#background_label.pack(fill=BOTH , expand=True)
	#BUTTON
        
		b10=Button(c, bg="dark green", fg="darkolivegreen1", text='BACK',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : back(root,c))
		b10.place(x=670, y=600)
		b11=Button(c, bg="dark green",fg="darkolivegreen1", text='SIGN IN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda :store(m.get(),c,name,root1))
		b11.place(x=670, y=550)
		l=Label(c,font="Bold 30",fg="dark green",bg="darkolivegreen1",text="SIGN UP").place(x=650,y=50)
		l1=Label(c,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Name  : ")
		l2=Label(c,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Gender  : ")
		l3=Label(c,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="UserName  : ")
		l4=Label(c,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Password  : ")
		l5=Label(c,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Confirm Password : ")
		
		b2=Radiobutton(c, text="male",bg="darkolivegreen1",font=(None, 12), variable=m , value=1)
		b3=Radiobutton(c, text="female", bg="darkolivegreen1",font=(None, 12),variable=m ,value=2)
		b2.place(x=750, y=280)
		b3.place(x=850, y=280)
		
		l1.place(x=600, y=230)
		l2.place(x=600, y=280)
		l3.place(x=600, y=330)
		l4.place(x=600, y=410)
		l5.place(x=600, y=460)
        
		e1=Entry(c)
		e3=Entry(c)
		e4=Entry(c,show="*")
		e5=Entry(c,show="*")
		
		e1.place(x=800, y=230)
		e3.place(x=800, y=330)
		e4.place(x=800, y=410)
		e5.place(x=800, y=460)
		
		root.withdraw()
		#root1.withdraw()
		c.mainloop()
		return c

        
