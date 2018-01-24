from tkinter import *
from tkinter import messagebox
import sqlite3
import valid_demo
import indian
import italian
import thai
import chinese
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

def close(root):
	root.destroy()

def show(s,result):										
	i=2
	ans=Toplevel(s)
	ans.minsize(1520,820)
	ans.title("Your Chosen Recipe:")
	ans.configure(background="thistle1")
	l1=Label(ans,fg="purple4",bg="thistle1",font="Helvetica 30 bold",text="Your Recipe :) ")
	l1.place(x=600,y=10)
	l=Label(ans,fg="purple4",bg="thistle1",font="Helvetica 12 bold",text=result,padx=50)
	l.place(x=130,y=130)
	b=Button(ans,bg="purple4",fg="thistle1",width=30,height=3,relief=GROOVE,text="Close",command=lambda : close(ans))
	b.place(x=620,y=600)
	s.withdraw()
	ans.mainloop()


def recipenm():
        li=[]
        result = c.execute('''select recipe_name from recipe_database''')
        result = c.fetchall()
        for name in result:
                li.append(name[0])
        #print(len(li))
        return li
#recipenm()


def do(s,e1,e2,v1,root):
		if v1.get()==1:
			e2.configure(state='disabled')
			e2.update()
			if valid_demo.checkname(e1.get(),recipenm())==1:
				messagebox.showinfo("ERROR5","OOOPS!! Too small recipe_name!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif valid_demo.checkname(e1.get(),recipenm())==3:
				messagebox.showinfo("ERROR5","Sorry,Requested recipe is not available!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif valid_demo.checkname(e1.get(),recipenm())==4:
				messagebox.showinfo("ERROR5","OOOPS!!! Such recipe name is not valid!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif valid_demo.checkname(e1.get(),recipenm())==2:
				result = c.execute("select recipe_desc from recipe_database where recipe_name='"+e1.get()+"';")
				result = c.fetchall()
				show(s,result[0][0])
		elif v1.get()==2:
			e1.configure(state='disabled')
			e1.update()
			if valid_demo.checkcuisine(e2.get())==2:
				messagebox.showinfo("ERROR5","Sorry,Requested recipe is not available!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif valid_demo.checkcuisine(e2.get())==1:
				messagebox.showinfo("ERROR5","OOOPS!!! text is too small!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif e2.get().isalpha()==False:
				messagebox.showinfo("ERROR5","OOOPS!!! Such recipe name is not valid!!!")
				s.deiconify()
				e2.delete(0,'end')
				e1.delete(0,'end')
			elif valid_demo.checkcuisine(e2.get())==3:
				if e2.get()=="indian":
					indian.indian(s,root)
				elif e2.get()=="italian":
					italian.italian(s,root)
				elif e2.get()=="chinese":
					chinese.chinese(s,root)
				elif e2.get()=="thai":
					thai.thai(s,root)
		elif v1.get()!=2 and v1.get()!=1:
			messagebox.showinfo("ERROR1","No Fields Selected")
			s.deiconify()
			e2.delete(0,'end')
			e1.delete(0,'end')

def back(root,s):
	root.deiconify()
	s.destroy()

        
def disable(x,y):
        x.configure(state='disabled')
        x.update()
        y.configure(state='normal')
        y.update()
	
def search(root):
	s=Toplevel(root)
	s.title("recipe search")
	v1=IntVar()
	#v2=IntVar()
	s.minsize(850,500)
	s.configure(background="thistle1")
	#l1=Label(s,text="Search Form")
	e1=Entry(s,width=31)
	e2=Entry(s,width=31)
	e1.place(x=450,y=110)
        
	e2.place(x=450,y=160)
	#e1=Entry(s)
	#e1.grid(row=1,column=1)
	c1=Radiobutton(s,font="Bold 15",fg="black",bg="thistle1",text="Recipe Name :",variable=v1,value=1)
	c2=Radiobutton(s,font="Bold 15",fg="black",bg="thistle1",text="Cuisine Name :",variable=v1,value=2)
	c1.configure(command=lambda : disable(e2,e1))
	c2.configure(command=lambda : disable(e1,e2))
	'''
	if v1.get()==1:
		c1.configure(command = disable(e2))
	elif v1.get()==2:
		c2.configure(command = disable(e1))
	'''
	b1=Button(s,bg="purple4",fg="thistle1",width=20,height=2,relief=GROOVE,text="Search",command=lambda : do(s,e1,e2,v1,root))
	b2=Button(s,bg="purple4",fg="thistle1",width=20,height=2,relief=GROOVE,text="Back",command=lambda : back(root,s))
	b3=Button(s,bg="purple4",fg="thistle1",width=20,height=2,relief=GROOVE,text="Close",command=lambda : close(s))
	#l1.grid(row=0,column=1)
	c1.place(x=250,y=100)
		
	c2.place(x=250,y=150)
        
	
	#b1.grid(row=3,column=0)
	#b2.place(x=150,y=200)
	b1.place(x=250,y=280)
	b2.place(x=450,y=280)
	b3.place(x=350,y=400)
	s.mainloop()
