from tkinter import *
import os
import cuisines
import search_demo
import add
import remove
import update
import aboutus
import login


root = Tk()
root.minsize(1520,880)
root.title("RECIPE MANAGEMENT SYSTEM")


#BACKGROUND
background_img = PhotoImage(file="food1.png")
background_label = Label(root,image=background_img)
background_label.pack(fill=BOTH , expand=True)



#BUTTON
b1=Button(root, bg="MAROON",fg="GHOST WHITE", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
b1.place(x=20, y=300)

b2=Button(root, bg="MAROON", fg="GHOST WHITE", text='MY RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : cuisines.cuisines(root))
b2.place(x=20, y=350)

b3=Button(root, bg="MAROON", fg="GHOST WHITE", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : aboutus.aboutus(root))
b3.place(x=20, y=400)

#b4=Button(root, bg="MAROON",fg="GHOST WHITE", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
#b4.place(x=20, y=450)

b5=Button(root, bg="MAROON",fg="GHOST WHITE", text='SEARCH YOUR RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : search_demo.search(root))
b5.place(x=600, y=700)

b8=Button(root, bg="MAROON", fg="GHOST WHITE", text='USER LOGIN',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : login.login(root,"user"))
b8.place(x=1040, y=200)

b9=Button(root, bg="MAROON", fg="GHOST WHITE", text='ADMIN LOGIN',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=20,command=lambda : login.login(root,"admin"))
b9.place(x=1290, y=200)


root.mainloop()


