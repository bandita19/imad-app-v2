from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("recipes.db")

def back(root,s):
	root.deiconify()
	s.destroy()

def delete(a,root,v,cuisine):
	#print("delete")
	#print(a)
	#a=str(a)
	if a!='':
		c=con.cursor()
		print(a)
		c.execute("delete from recipe_database where recipe_name='"+a+"';")
		c.execute("delete from '"+cuisine+"' where recipe_name='"+a+"';")
		con.commit()
		messagebox.showinfo("Success","Succesfully Deleted")
		v.destroy()								#Update the Result 
		remove(root,cuisine)							#after delete operation
	else:
		messagebox.showinfo("ERROR4","Nothing is Selected")
		
def remove(root,cuisine):
	i=120
	a=StringVar()
	c=con.cursor()
	li=[]
	result = c.execute("select recipe_name from '"+cuisine+"';")
	result = c.fetchall()
	'''for item in result
		print(item[1])
		l1.append(item1)'''
	con.commit()
	v=Toplevel(root)
	v.title("Recipe Names")
	v.minsize(850,550)
	v.configure(background="thistle1")
	lt1=Label(v,fg="purple4",bg="thistle1",font="Helvetica 20 bold",text="Recipes available in this cuisine : ").place(x=250,y=50)
	#e1=Entry(f,width=31).place(x=150,y=50)
	#lt2=Label(f,fg="thistle1",bg="purple4",font="Helvetica 20 bold",text="Time").grid(row=1,column=2)
	#lt3=Label(f,fg="thistle1",bg="purple4",font="Helvetica 20 bold",text="Name").grid(row=1,column=3)
	#lt4=Label(f,fg="thistle1",bg="purple4",font="Helvetica 20 bold",text="Topic").grid(row=1,column=4)

	for item in result:	#Show Entries in Database
		r1=Radiobutton(v,bg="thistle1",variable=a,value=item[0]).place(x=100,y=i)	#Radiobutton assigned to each entry
		#print(a.get())
		l=Label(v,font="Bold 15",fg="purple4",bg="thistle1",text=item[0]).place(x=200,y=i)
		#l2=Label(v,font="Bold 15",fg="black",bg="powder blue",text=time).grid(row=i,column=2)
		#l3=Label(v,font="Bold 15",fg="black",bg="powder blue",text=project).grid(row=i,column=3)
		#l4=Label(v,font="Bold 15",fg="black",bg="powder blue",text=topic).grid(row=i,column=4)
		i+=40

	b1=Button(v,width=10,height=1,relief=GROOVE,bg="purple4",fg="thistle1",font="Bold 15",text="Delete",command=lambda : delete(a.get(),root,v,cuisine)).place(x=200,y=500)
	b2=Button(v,width=10,height=1,relief=GROOVE,font="Bold 15",bg="purple4",fg="thistle1"
	,text="Back",command=lambda : back(root,v)).place(x=400,y=500)
	#b1.grid(row=i+1,column=1)
	#b2.grid(row=i+1,column=3)
	#e.Entry(f)
	#e.place(300,50)
	root.withdraw()
	v.mainloop()
