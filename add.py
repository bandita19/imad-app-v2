import sqlite3
from tkinter import messagebox
from tkinter import *
import valid_demo

con = sqlite3.connect('recipes.db')

def back(root,s):
	root.deiconify()
	s.destroy()

def add(u,name,type):
	def store(u):
		flag=False
		#print(" in store error")
		e=e9.get("1.0","end-1c")
		if e8.get()=="" or e=="" :				#Condition to check Empty Fields
			messagebox.showinfo("ERROR3","Each Field is Mandatory")
			flag=True

		else:
			#print(e1.get(),type(e1.get()))
			if valid_demo.checkcuisine(e8.get())==1 or valid_demo.checkcuisine(e)==1:
				#print("validation")
				messagebox.showinfo("ERROR5","OOOPS!! Text Too Small!!!")
				flag=True

			elif valid_demo.checkcuisine(e8.get())==4:
				messagebox.showinfo("ERROR5","NOOOO!!! Enter a String only!!!")
				flag=True

			else:
				c = con.cursor()
				res=c.execute('''select recipe_name from recipe_database''')				#Fetch Date and Time from DB
				res=c.fetchall()
				resu=c.execute("select * from indian;")
				resu=c.fetchall()
				for row in res:
					#print(row)
					#ee=e.get()
					if row[0].upper()==e8.get().upper():
						cuis=var1.get()
						#r=c.execute("select recipe_name from ;")
						r = c.execute("select recipe_name from '"+cuis+"';")
						r = c.fetchall()
						for nm in r:
							if nm[0].lower()==e8.get().lower():
								flag=True
								messagebox.showinfo("ERROR2","This Recipe Already Exists in the cuisine:"+var1.get().upper()+"")
								break
						'''if r==[]:
							break
						
						elif var2.get()==r[0][0]:
							flag=True
							messagebox.showinfo("ERROR2","This Recipe Already Exists in the cuisine"+"var1.get()")
							break'''	
						
				if flag==False:
					print(var2.get())
					c.execute("insert into recipe_database (recipe_name, recipe_desc,feedback,count) values ( ?,?,?,? );",(e8.get(),e,0,0))
					con.commit()
					c.execute("insert into "+var1.get()+" (recipe_name, category) values ( ?,? );",(e8.get(),var2.get()))
					con.commit()
					#res=c.execute("select * from "+var1.get()+";")
					res=c.execute("select category from indian;")
					resul=c.execute("select recipe_name from recipe_database;")
					res=c.fetchall()
					resul=c.fetchall()
					print("cuisine")
					print(res)
					#print("database")
					#print(resul)
					#print("ok")
					messagebox.showinfo("Success","Succesfully Added")
					con.commit()
					u.deiconify()
					b.destroy()
					
	b=Toplevel(u)
	b.minsize(1520,820)
	#print("into add")
	b.title("Adding recipies")
	b.configure(background="thistle1")
	l9=Label(b,font="Bold 15",fg="thistle1",bg="purple4",text="SIGNED IN AS "+type.upper()+":"+name.upper()+"",height=2,width=160,anchor=W).place(x=0,y=0)
	l1=Label(b,font="Bold 15",fg="purple4",bg="thistle1",text="Select your desired cuisine : ").place(x=600,y=200)
	l2=Label(b,font="Bold 15",fg="purple4",bg="thistle1",text="Select your desired category  : ").place(x=600,y=300)
	l3=Label(b,font="Bold 15",fg="purple4",bg="thistle1",text="Enter recipe name : ").place(x=600,y=400)
	l4=Label(b,font="Bold 15",fg="purple4",bg="thistle1",text="Enter recipe description : ").place(x=600,y=500)

	cuisine=["indian","italian","thai","chinese"]
	category=["Main Course","Starters","Desserts"]
	e8=Entry(b)
	e8.place(x=900,y=400)
	e9=Text(b,height=10,width=40)
	e9.place(x=900,y=500)
	#e3=Entry(n)
	#e4=Entry(n)

	'''var1=StringVar(b)
	var1.set(cuisine[0])
	var2=StringVar(b)
	var2.set(category[0])
	w1=apply(OptionMenu, (b,var1) + tuple(cuisine))
	w2=apply(OptionMenu, (b,var2) + tuple(category))'''
	var1=StringVar()
	var2=StringVar()

	var1.set(cuisine[0])
	var2.set(category[0])

	w1=OptionMenu(b,var1,*cuisine).place(x=900,y=200)
	w2=OptionMenu(b,var2,*category).place(x=900,y=300)


	print("befor store function")
	b1=Button(b,width=20,height=2,relief=GROOVE,bg="purple4",fg="thistle1",text="Add",command=lambda : store(u)).place(x=700,y=600)
	b2=Button(b,width=20,height=2,relief=GROOVE,bg="purple4",fg="thistle1",text="Back",command=lambda : back(u,b)).place(x=700,y=670)
	#u.withdraw()
	b.mainloop()
