from tkinter import *
import sqlite3

def back(root,s):
	root.deiconify()
	s.destroy()
	
def view(root):
	i=3
	con=sqlite3.connect("recipes.db")
	result = con.execute('''select name,gender,username,status from user ''')
	v=Toplevel(root)
	v.title("Meeting Scheduler")
	v.minsize(380,200)
	v.configure(background="cadetblue1")
	
	#l=Label(v,text="Show Schedule")
	lt1=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text=" Name ").grid(row=1,column=0)
	lt2=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text=" Gender ").grid(row=1,column=1)
	lt3=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text=" Username ").grid(row=1,column=2)
	lt4=Label(v,fg="blue4",bg="cadetblue1",font="Helvetica 20 bold",text=" Status ").grid(row=1,column=3)
	for name,gender,username,status in result:
		l1=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=name).grid(row=i,column=0)
		l2=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=gender).grid(row=i,column=1)
		l3=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=username).grid(row=i,column=2)
		l4=Label(v,font="Bold 15",fg="black",bg="cadetblue1",text=status).grid(row=i,column=3)
		i+=1
	b1=Button(v,compound=LEFT,width=10,height=1,bg="blue4",fg="cadetblue1",relief=GROOVE,text="Back",font="Bold 15",command=lambda : back(root,v))
	#i1=Label(v,width=10,height=1,bg="cadetblue1",text="").grid(row=i+1,column=0)
	#i2=Label(v,width=10,height=2,bg="cadetblue1",text="").grid(row=i+1,column=2)
	#i3=Label(v,width=10,height=2,bg="cadetblue1",text="").grid(row=i+1,column=3)
	#l.grid(row=0,column=1)
	#t1.pack()
	b1.grid(row=i+1,column=1)
	#b1.place(anchor=S)
	root.withdraw()
	v.mainloop()
	#root.destroy()
