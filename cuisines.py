from tkinter import *
import indian
import chinese
import thai
import italian
import remove
import update
	
def home(root,s):
	root.deiconify()
	s.destroy()

def cuisines2(root):
	i=3
	v=Toplevel(root)
	v.title("cuisine")
	#v.minsize(1500,1080)
	v.minsize(1360,768)
	#BACKGROUND
	background_img = PhotoImage(file="C://Users//Anaya//test.png")
	background_img1 = PhotoImage(file="C://Users//Anaya//indian.png")
	background_img2 = PhotoImage(file="C://Users//Anaya//italian.png")
	background_img3 = PhotoImage(file="C://Users//Anaya//chinese.png")
	background_img4 = PhotoImage(file="C://Users//Anaya//thai.png")
	background_label = Label(v,image=background_img)
	background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON
	b1=Button(v, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root,v))
	b1.place(x=20, y=300)

	b2=Button(v, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	b2.place(x=20, y=350)

	#b3=Button(v, bg="MAROON", fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	#b3.place(x=20, y=400)

	
	
	#b4=Button(v, image=background_img1, fg="GHOST WHITE",bg="MAROON",text='INDIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : indian.indian(v,root))
	b4=Button(v,  image=background_img1, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update_db.update_db(root,"indian"))
	b4.place(x=550,y=180)
	b4.image=background_img1
	
	#b5=Button(v, image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : italian.italian(v,root))
	b5=Button(v,  image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update_db.update_db(root,"italian"))
	b5.place(x=1130,y=180)
	b5.image=background_img2
	
	#b6=Button(v, image=background_img3, fg="GHOST WHITE",bg="MAROON",text='CHINESE',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : chinese.chinese(v,root))
	b6=Button(v,  image=background_img3, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update_db.update_db(root,"chinese"))
	b6.place(x=550,y=450)
	b6.image=background_img3
	
	#b7=Button(v, image=background_img4, fg="GHOST WHITE",bg="MAROON",text='THAI',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : thai.thai(v,root))
	b7=Button(v,  image=background_img4, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update_db.update_db(root,"thai"))
	b7.place(x=1130,y=450)
	b7.image=background_img1
	

	root.withdraw()
	v.mainloop()



	
def cuisines1(root,a):
	v=Toplevel(root)
	v.title("cuisine")
	#v.minsize(1450,1080)
	v.minsize(1360,768)
	#BACKGROUND
	background_img = PhotoImage(file="C://Users//Anaya//test.png")
	background_img1 = PhotoImage(file="C://Users//Anaya//indian.png")
	background_img2 = PhotoImage(file="C://Users//Anaya//italian.png")
	background_img3 = PhotoImage(file="C://Users//Anaya//chinese.png")
	background_img4 = PhotoImage(file="C://Users//Anaya//thai.png")
	if a==0:#remove
		background_label = Label(v,image=background_img)
		background_label.pack(fill=BOTH , expand=True)

	elif a==1:#update
		background_label = Label(v,image=background_img)
		background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON
	b1=Button(v, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root,v))
	b1.place(x=20, y=300)

	b2=Button(v, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	b2.place(x=20, y=350)

	b3=Button(v, bg="MAROON", fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	b3.place(x=20, y=400)

	
	if a==0:
	#b4=Button(v, image=background_img1, fg="GHOST WHITE",bg="MAROON",text='INDIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : indian.indian(v,root))
		b4=Button(v,  image=background_img1, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : remove.remove(root,"indian"))
		b4.place(x=550,y=180)
		b4.image=background_img1
		
		b5=Button(v,  image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : remove.remove(root,"italian"))
		b5.place(x=1130,y=180)
		b5.image=background_img2
	
	#b6=Button(v, image=background_img3, fg="GHOST WHITE",bg="MAROON",text='CHINESE',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : chinese.chinese(v,root))
		b6=Button(v,  image=background_img3, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : remove.remove(root,"chinese"))
		b6.place(x=550,y=450)
		b6.image=background_img3
	
	#b7=Button(v, image=background_img4, fg="GHOST WHITE",bg="MAROON",text='THAI',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : thai.thai(v,root))
		b7=Button(v,  image=background_img4, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : remove.remove(root,"thai"))
		b7.place(x=1130,y=450)
		b7.image=background_img1
		
	elif a==1:
	#b4=Button(v, image=background_img1, fg="GHOST WHITE",bg="MAROON",text='INDIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : indian.indian(v,root))
		b4=Button(v,  image=background_img1, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update.remove(root,"indian"))
		b4.place(x=550,y=180)
		b4.image=background_img1
	
	#b5=Button(v, image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : italian.italian(v,root))
		b5=Button(v,  image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update.remove(root,"italian"))
		b5.place(x=1130,y=180)
		b5.image=background_img2
	
	#b6=Button(v, image=background_img3, fg="GHOST WHITE",bg="MAROON",text='CHINESE',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : chinese.chinese(v,root))
		b6=Button(v,  image=background_img3, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update.remove(root,"chinese"))
		b6.place(x=550,y=450)
		b6.image=background_img3
	
	#b7=Button(v, image=background_img4, fg="GHOST WHITE",bg="MAROON",text='THAI',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : thai.thai(v,root))
		b7=Button(v,  image=background_img4, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : update.remove(root,"thai"))
		b7.place(x=1130,y=450)
		b7.image=background_img1
	

	root.withdraw()
	v.mainloop()
	
def cuisines(root):
	i=3
	v=Toplevel(root)
	v.title("cuisine")
	#v.minsize(1450,1080)
	v.minsize(1360,768)
	#BACKGROUND
	background_img = PhotoImage(file="C://Users//Anaya//test.png")
	background_img1 = PhotoImage(file="C://Users//Anaya//indian.png")
	background_img2 = PhotoImage(file="C://Users//Anaya//italian.png")
	background_img3 = PhotoImage(file="C://Users//Anaya//chinese.png")
	background_img4 = PhotoImage(file="C://Users//Anaya//thai.png")
	background_label = Label(v,image=background_img)
	background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON
	b1=Button(v, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root,v))
	b1.place(x=20, y=300)

	b2=Button(v, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	b2.place(x=20, y=350)

	#b3=Button(v, bg="MAROON", fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	#b3.place(x=20, y=400)

	
	
	#b4=Button(v, image=background_img1, fg="GHOST WHITE",bg="MAROON",text='INDIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : indian.indian(v,root))
	b4=Button(v,  image=background_img1, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : indian.indian(v,root))
	b4.place(x=550,y=180)
	b4.image=background_img1
	
	#b5=Button(v, image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : italian.italian(v,root))
	b5=Button(v,  image=background_img2, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : italian.italian(v,root))
	b5.place(x=1130,y=180)
	b5.image=background_img2
	
	#b6=Button(v, image=background_img3, fg="GHOST WHITE",bg="MAROON",text='CHINESE',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : chinese.chinese(v,root))
	b6=Button(v,  image=background_img3, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : chinese.chinese(v,root))
	b6.place(x=550,y=450)
	b6.image=background_img3
	
	#b7=Button(v, image=background_img4, fg="GHOST WHITE",bg="MAROON",text='THAI',pady=0.5,relief = FLAT,height=150,width=500, command=lambda : thai.thai(v,root))
	b7=Button(v,  image=background_img4, fg="GHOST WHITE",bg="MAROON",text='ITALIAN',pady=0.5,relief = FLAT,height=150,width=250, command=lambda : thai.thai(v,root))
	b7.place(x=1130,y=450)
	b7.image=background_img1
	

	root.withdraw()
	v.mainloop()

