import sqlite3
from tkinter import *
from tkinter import messagebox
import signup
import project1

con = sqlite3.connect('recipes.db')
p = con.cursor()

#print("inside")
def request(a,h,v):
	
	p.execute("insert into request_table(user,status) values (?,?);",(a,'pending' ))
	con.commit() 
	messagebox.showinfo("ERROR3","Your Request is sent")
	v.deiconify()
	h.withdraw()
	
def request_page(a,v):
	h=Toplevel(v)
	h.title("request")
	h.minsize(400,400)
	h.configure(background="darkolivegreen1")
	l=Label(h,fg="dark green",bg="darkolivegreen1",font="Helvetica 15 bold",text="Your account is diactivated!!\n Kindly request to activate").place(x=0,y=0)
	
	#BUTTON
	b=Button(h, bg="dark green",fg="darkolivegreen1", text='REQUEST',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : request(a,h,v)).place(x=180,y=300)
	
	
def home(root,s):
	root.deiconify()
	s.destroy()

def login(root,name):

	def store1(v,root,name):
		if e1.get()=="" or e2.get()=="":				#Condition to check Empty Fields
			messagebox.showinfo("ERROR3","Each Field is Mandatory")
			e2.delete(0,'end')
			e1.delete(0,'end')
			
		else:
                       
			res=[]
			p.execute('''select username from admin''')
			result=p.fetchall()
			for row in result:
				if row[0]==e1.get():
					p.execute("select password from admin where username='"+e1.get()+"';")
					result1=p.fetchall()
					name1=e1.get()
					if result1[0][0]==e2.get():
						messagebox.showinfo("Success","Logged In Successfully")
						e1.delete(0,'end')
						e2.delete(0,'end')
						project1.project1(v,root,name1,name)
						break
					else:
						messagebox.showinfo("ERROR","Your Password doesn't match")
						e2.delete(0,'end')
						e1.delete(0,'end')
						
			else:
				messagebox.showinfo("ERROR","Username does not exist")
				v.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
				
                                

	def store(v,root,name):
		
		if e1.get()=="" or e2.get()=="":				#Condition to check Empty Fields
			messagebox.showinfo("ERROR3","Each Field is Mandatory")
		
		else:
			res=[]
			p.execute("select username from user;")
			result=p.fetchall()
			#print(result)
			#print(len(result))       
			for row in result:
				#print("inside for")
				#print(row)
				#print(row[0])
				#print(e1.get())
				if row[0]==e1.get():
					p.execute("select status from user where username='"+e1.get()+"';")
					re=p.fetchall()
					#print("inside if",re)
					if re[0][0]=="enable":
						
						p.execute("select password from user where username='"+e1.get()+"';")
						result1=p.fetchall()
						#print(result1[0][0])
						#print(e2.get())
						if result1[0][0]==e2.get():
							messagebox.showinfo("Success","Logged In Successfully")
							x=e1.get()
							e2.delete(0,'end')
							e1.delete(0,'end')
							project1.project1(v,root,x,name)
							break
						else:
							messagebox.showinfo("ERROR","Password Does'nt match")
							e2.delete(0,'end')
							e1.delete(0,'end')
							break
							#if c==len(result):
					else:
						req=p.execute("select user from request_table;")
						req=p.fetchall()
						#print("request")
						#print(req)
						for row in req:
							#print(row)
							if e1.get()==row[0]:
								messagebox.showinfo("ERROR","Your request id still pending")
								e2.delete(0,'end')
								e1.delete(0,'end')
								break
						else:
							#print("else")
							request_page(e1.get(),v)
							break
						break
			else:
				messagebox.showinfo("ERROR","Username does not exist")
				v.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
		
	v=Toplevel(root)
	v.title("log in")
	v.minsize(1520,1000)
	v.configure(background="darkolivegreen1")
	l3=Label(v,fg="dark green",bg="darkolivegreen1",font="Helvetica 30 bold",text="LOGIN").place(x=660,y=50)
	
	#BUTTON
	b1=Button(v, bg="dark green",fg="darkolivegreen1", text='BACK',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root,v))
	b1.place(x=660, y=500)
      
	l1=Label(v,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Username  : ")
	l2=Label(v,font="Bold 15",fg="dark green",bg="darkolivegreen1",text="Password  : ")
	e1=Entry(v)
	e2=Entry(v,show="*")
	l1.place(x=580, y=250) 
	l2.place(x=580, y=300)
	e1.place(x=720, y=250)
	e2.place(x=720, y=300)
       
	
	if name=="user":
		b5=Button(v, bg="dark green",fg="darkolivegreen1", text='LOGIN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : store(v,root,name))
		b5.place(x=660, y=380)
		b6=Button(v, bg="darkolivegreen1",fg="dark green", text='New User? Sign Up Here.',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : signup.signup(v,root,"user"))
		b6.place(x=620, y=430)
	else:
		b5=Button(v, bg="dark green",fg="darkolivegreen1", text='LOGIN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : store1(v,root,name))
		b5.place(x=660, y=380)
	
	root.withdraw()
	v.mainloop()
              

        
