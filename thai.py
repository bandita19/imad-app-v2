from tkinter import *
import maincourse
import starters
import aboutus
import dessert
	
def home(root,s):
	root.deiconify()
	s.destroy()
	
def back(v,c):
	v.deiconify()
	c.destroy()
	
def thai(root,root1):
	i=3
	c=Toplevel(root)
	c.title("thai")
	c.minsize(1360,768)
	#BAckground
	background_img = PhotoImage(file="C://Users//Anaya//thai1.png")
	background_img1 = PhotoImage(file="C://Users//Anaya//thai_maincourse.png")
	background_img2 = PhotoImage(file="C://Users//Anaya//thai_starter.png")
	background_img3 = PhotoImage(file="C://Users//Anaya//thai_dessert.png")
	background_label = Label(c,image=background_img)
	background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON
	b1=Button(c, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root1,c))
	b1.place(x=20, y=300)

	b2=Button(c, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : aboutus.aboutus(root1))
	b2.place(x=20, y=350)

	#b3=Button(c, bg="MAROON", fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
	#b3.place(x=20, y=400)
	
	b10=Button(c, bg="MAROON", fg="GHOST WHITE", text='BACK',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : back(root,c))
	b10.place(x=20, y=400)

	
	
	
	
	
	#b4=Button(c, image=background_img1, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=200, command=lambda : maincourse.maincourse(c,root,root1,"thai"))
	b4=Button(c, image=background_img1, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=250, command=lambda : maincourse.maincourse(c,root,root1,"thai"))
	b4.place(x=530,y=150)
	b4.image=background_img1
	
	#b5=Button(c, image=background_img2, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=200, command=lambda : staters.starters(c,root,root1,"thai"))
	b5=Button(c, image=background_img2, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=250, command=lambda : starters.starters(c,root,root1,"thai"))
	b5.place(x=1100,y=150)
	b5.image=background_img2
	
	#b6=Button(c, image=background_img3, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=200, command=lambda : dessert.dessert(c,root,root1,"thai"))
	b6=Button(c, image=background_img3, fg="GHOST WHITE",pady=0.5,relief = FLAT,height=150,width=250, command=lambda : dessert.dessert(c,root,root1,"thai"))
	b6.place(x=830,y=420)
	b6.image=background_img3
	
	root.withdraw()
	root.mainloop()
	
