from tkinter import *
import os
'''import cuisines
import search_demo
import add
import signup
import update
import update
import login
import view
import remove_user
import aboutus
import request
'''
def home(root,s):
	root.deiconify()
	s.destroy()
def project1(root,r,name,type):
	l=Toplevel(root)
	l.minsize(800,600)
	l.title("RECIPE MANAGEMENT SYSTEM")
	
	
	#BACKGROUND
	background_img = PhotoImage(file="C://Users//Anaya//food1.png")
	#background_img1 = PhotoImage(file="C://Users//Anaya//food3.png")
	background_label = Label(l,image=background_img)
	background_label.pack(fill=BOTH , expand=True)
	l1=Label(l,font="Bold 15",fg="ghost white",bg="maroon",text="SIGNED IN AS "+type.upper()+" : "+name.upper()+"",height=2,width=160,anchor=W).place(x=0,y=750)

	#BUTTON
	#b1=Button(l, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	#b1.place(x=20, y=300)

	b2=Button(l, bg="MAROON", fg="GHOST WHITE", text='MY RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : cuisines.cuisines(l))
	b2.place(x=20, y=350)

	b3=Button(l, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : aboutus.aboutus(l))
	b3.place(x=20, y=400)

	#b4=Button(l, bg="MAROON",fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	#b4.place(x=20, y=450)

	b5=Button(l, bg="MAROON",fg="GHOST WHITE", text='SEARCH YOUR RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : search_demo.search(l))
	b5.place(x=600, y=650)

	b45=Button(l, bg="MAROON", fg="GHOST WHITE", text='SIGN OUT',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : home(r,l))
	b45.place(x=1170, y=150)
	if type=='user':
		b9=Button(l, bg="MAROON", fg="GHOST WHITE", text='ADMIN LOGIN',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : login.login(l,"admin"))
		b9.place(x=1170, y=200)

		#b7=Button(l, bg="MAROON", fg="GHOST WHITE", text='UPDATE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
		#b7.place(x=1170, y=400)
		b7=Button(l, bg="MAROON",fg="GHOST WHITE", text='ADD NEW RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : add.add(l,name,type))
		b7.place(x=600, y=650)
		
		

	if type=="admin":
		b6=Button(l, bg="MAROON", fg="GHOST WHITE", text='REMOVE THE RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : cuisines.cuisines1(l,0))
		b6.place(x=1170, y=300)
		b8=Button(l, bg="MAROON", fg="GHOST WHITE", text='UPDATE THE RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : cuisines.cuisines1(l,1))
		b8.place(x=1170, y=350)
		b111=Button(l, bg="MAROON",fg="GHOST WHITE", text='ADD NEW RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : add.add(l,name,type))
		b111.place(x=1170, y=400)
		b47=Button(l, bg="MAROON", fg="GHOST WHITE", text='ADD ANOTHER ADMIN',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : signup.signup(l,r,"admin"))
		b47.place(x=1170, y=200)
		b57=Button(l, bg="MAROON", fg="GHOST WHITE", text='VIEW USER',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : view.view(l))
		b57.place(x=1170, y=600)
		b67=Button(l, bg="MAROON", fg="GHOST WHITE", text='REMOVE USER',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : remove_user.remove(l))
		b67.place(x=1170, y=650)
		b97=Button(l, bg="MAROON", fg="GHOST WHITE", text='PENDING REQUESTS',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : request.request(l))
		b97.place(x=1170, y=550)
	root.withdraw()
	l.mainloop()
	
