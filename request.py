import sqlite3
from tkinter import *
from tkinter import messagebox

def back(root,s):
	root.deiconify()
	s.destroy()
	
con = sqlite3.connect('recipes.db')
p = con.cursor()
def request(root):
	def store(a,b,g):
		p.execute("select user from request_table")
		res=p.fetchall()
		#print(res)
		for row in res:
			if row[0]==a:
				p.execute("update user set status ='enable' where username='"+a+"'")
				con.commit()
				p.execute("delete from request_table where user='"+a+"'")
				con.commit()
				messagebox.showinfo("SUCCESS","Successfully Updated!!")
				request(g)
				#g.withdraw()
	g=Toplevel(root)
	g.title("Request")
	g.minsize(600,600)
	g.configure(background="darkolivegreen1")
	p.execute("select user from request_table;")
	result1=p.fetchall()
	a=StringVar()
	b=StringVar()
	l=len(result1)
	#print(result1)
	i=50
	j=20
	for user in result1:
		#print(user[0])
		Radiobutton(g,bg="dark green",fg="darkolivegreen1",variable=a,value=user[0],text="Accept",font=(None,12)).place(x=i+150,y=j)
		l1=Label(g,font="Bold 15",fg="darkolivegreen1",bg="dark green",text=user[0]).place(x=i,y=j)
		#print(a.get())		
		j+=50
	j=20
	for user in result1:
		Radiobutton(g,bg="dark green",fg="darkolivegreen1",variable=b,value=user[0],text="Pending",font=(None,12)).place(x=i+300,y=j)
		j+=50
	#print(a.get())
	#print(b.get())
	b1=Button(g,bg="MAROON",fg="WHITE",relief=RAISED,text="BACK",font="Bold 10",height=1,width=10,command=lambda : back(root,g)).place(x=250,y=500)
	b2=Button(g,bg="DEEP SKY BLUE",fg="BLACK", text='Update',font="Bold 10",relief = RAISED,height=1,width=10,command=lambda : store(a.get(),b.get(),root)).place(x=350,y=500)
	
	
	root.withdraw()
	g.mainloop()
