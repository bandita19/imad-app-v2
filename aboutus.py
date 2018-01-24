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

	
def aboutus(root):
	i=3
	v=Toplevel(root)
	v.title("cuisine")
	#v.minsize(1450,1080)
	v.minsize(1360,768)
	#BACKGROUND
	background_img = PhotoImage(file="C://Users//Anaya//about.png")
	#background_img1 = PhotoImage(file="C://Users//Anaya//indian.png")
	#background_img2 = PhotoImage(file="C://Users//Anaya//italian.png")
	#background_img3 = PhotoImage(file="C://Users//Anaya//chinese.png")
	#background_img4 = PhotoImage(file="C://Users//Anaya//thai.png")
	background_label = Label(v,image=background_img)
	background_label.pack(expand=True)
	
	
	#BUTTON
	b1=Button(v, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root,v))
	b1.place(x=600, y=700)
	

	root.withdraw()
	v.mainloop()

