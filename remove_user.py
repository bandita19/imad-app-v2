from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("recipes.db")
c=con.cursor()

def back(root,s):
	root.deiconify()
	s.destroy()

def delete(a,root,v):
	#print(a)
	a=str(a)
	if a!='0':
		c.execute("update user set status=? where username=?",("disable",a))
		con.commit()
		messagebox.showinfo("Success","Succesfully Deleted")
		v.destroy()								#Update the Result 
		remove(root)							#after delete operation
	else:
		messagebox.showinfo("ERROR4","Nothing is Selected")
		
def remove(root):
	i=2
	a=StringVar()
	result = con.execute('''select name,gender,username from user where status="enable"''')
	#v.deiconify()
	
	v=Toplevel(root)
	v.deiconify()
	v.title("remove user")
	v.configure(background="cadetblue1")
	lt1=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text="Name").grid(row=1,column=1)
	lt2=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text="Gender").grid(row=1,column=2)
	lt3=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text="Username").grid(row=1,column=3)

	for name,gender,username in result:					#Show Entries in Database
		Radiobutton(v,bg="cadetblue1",variable=a,value=username).grid(row=i,column=0)	#Radiobutton assigned to each entry
		l1=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=name).grid(row=i,column=1)
		l2=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=gender).grid(row=i,column=2)
		l3=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=username).grid(row=i,column=3)
		i+=1

	b1=Button(v,width=10,height=1,relief=GROOVE,bg="blue4",fg="cadetblue1",font="Bold 15",text="Delete",command=lambda : delete(a.get(),root,v))
	b2=Button(v,width=10,height=1,relief=GROOVE,bg="blue4",fg="cadetblue1",font="Bold 15",text="Back",command=lambda : back(root,v))
	b1.grid(row=i+1,column=1)
	b2.grid(row=i+1,column=3)
	#root.withdraw()
	v.mainloop()
