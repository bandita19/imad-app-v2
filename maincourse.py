from tkinter import *
import sqlite3
from tkinter import messagebox
#import tkMesssageBox
import recipe_database
import aboutus

con=sqlite3.connect("recipes.db")
c=con.cursor()
li=[]

def close(root):
	root.destroy()
def home(root,s):
		root.deiconify()
		s.destroy()
def back(c,m):
		c.deiconify()
		m.destroy()
		
def rating(ans,g,rname,a,s,result):
	if a==1 or a==2 or a==3 or a==4 or a==5:
		c.execute("select feedback,count from recipe_database where recipe_name='"+rname+"';")
		con.commit()
		res=c.fetchall()
		#print(res)
		f=res[0][0]+a
		#print("f",f)
		co=res[0][1]+1
		#print("c",co)
		c.execute("update recipe_database set feedback=? where recipe_name=?",(int(f),rname))
		con.commit()
		c.execute("update recipe_database set count=? where recipe_name=?",(int(co),rname))
		con.commit()
		c.execute("select feedback,count from recipe_database where recipe_name='"+rname+"';")
		con.commit()
		result1=c.fetchall()
		#print(result1)
		messagebox.showinfo("Success","Thanks for your feedback!!")
		g.withdraw()
		ans.withdraw()
		show(s,result,rname)
		
	else:
		messagebox.showinfo("ERROR","Select an option to submit your feedback!!")
		

	
def feedback(ans,rname,s,result):
			g=Toplevel(ans)
			g.minsize(520,520)
			g.title("Feedback:")
			g.configure(background="papaya whip")
			a=IntVar()
			r1=Radiobutton(g,variable=a,value=1,bg="papaya whip").place(x=20,y=20)
			r2=Radiobutton(g,variable=a,value=2,bg="papaya whip").place(x=20,y=50)
			r3=Radiobutton(g,variable=a,value=3,bg="papaya whip").place(x=20,y=80)
			r4=Radiobutton(g,variable=a,value=4,bg="papaya whip").place(x=20,y=110)
			r5=Radiobutton(g,variable=a,value=5,bg="papaya whip").place(x=20,y=140)
			l1=Label(g,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="1 star").place(x=70,y=20)
			l2=Label(g,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="2 star").place(x=70,y=50)
			l3=Label(g,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="3 star").place(x=70,y=80)
			l4=Label(g,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="4 star").place(x=70,y=110)
			l5=Label(g,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="5 star").place(x=70,y=140)
			b1=Button(g,bg="maroon",fg="papaya whip",width=30,height=3,relief=GROOVE,text="SUBMIT",command=lambda : rating(ans,g,rname,a.get(),s,result)).place(x=100,y=400)
			#ans.withdraw()
			g.mainloop()
			
		
def show(s,result,rname):
	
	#i=2
	ans=Toplevel(s)
	ans.minsize(1520,820)
	ans.title("Your Chosen Recipe:")
	ans.configure(background="papaya whip")
	c.execute("select feedback,count from recipe_database where recipe_name='"+rname+"';")
	con.commit()
	res=c.fetchall()
	#print(res)
	f=res[0][0]
	#print("f",f)
	co=res[0][1]
	#print("count",co)
	if co==0:
		l4=Label(ans,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="RATING: 0 STARS").place(x=200,y=600)
	else:
		l4=Label(ans,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text="RATING: "+str(float(f)/float(co))+"STARS").place(x=200,y=600)
	l1=Label(ans,fg="maroon",bg="papaya whip",font="Helvetica 30 bold",text="Your Recipe :) ")
	l1.place(x=600,y=10)

	l=Label(ans,fg="maroon",bg="papaya whip",font="Helvetica 12 bold",text=result,padx=50)
	l.place(x=130,y=130)
	b=Button(ans,bg="maroon",fg="papaya whip",width=30,height=3,relief=GROOVE,text="CLOSE",command=lambda : close(ans))
	b.place(x=620,y=600)
	b=Button(ans,bg="maroon",fg="papaya whip",width=30,height=3,relief=GROOVE,text="FEEDBACK",command=lambda : feedback(ans,rname,s,result)).place(x=1000,y=600)
	ans.mainloop()
        
def display(m,name,type):
		result = c.execute("select recipe_desc from recipe_database where recipe_name='"+name+"';")
		result = c.fetchall()
		if result==[]:
			messagebox.showinfo("ERROR3","Choose any one recipe!!")
		else:
			show(m,result[0][0],name)
		
def maincourse(root,root1,root2,type):
        a=StringVar()
        result = c.execute("select recipe_name from "+type+" where category='Main Course'")
        result = c.fetchall()
        #print(result)
        #print(result)
        m=Toplevel(root)
        m.title("main course")
        m.minsize(1450,1080)
        m.configure(background="papaya whip")
        j=200
        i=0
        for item in result:
                r=Radiobutton(m,variable=a,value=item[0],bg="papaya whip")
                b11=Label(m, bg="maroon",fg="burlywood2", text=item[0] ,font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
                b11.place(x=500,y=j)
                r.place(x=450,y=j)
                j+=150
                #print(name,type(name))
				
        #BUTTON
        b1=Button(m, bg="maroon",fg="burlywood2", text='HOME',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : home(root2,m))
        b1.place(x=20, y=300)

        b2=Button(m, bg="maroon", fg="burlywood2", text='ABOUT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : aboutus.aboutus(root2))
        b2.place(x=20, y=350)

        #b3=Button(m, bg="maroon", fg="burlywood2", text='CONTACT US',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30)
        #b3.place(x=20, y=400)
	
        b10=Button(m, bg="maroon", fg="burlywood2", text='BACK',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : back(root,m))
        b10.place(x=20, y=400)
		

        b10=Button(m, bg="maroon", fg="burlywood2", text='SHOW RECIPE',font="Bold 15",pady=0.5,relief = FLAT,height=1,width=30,command=lambda : display(m,a.get(),type))
        b10.place(x=600, y=600)
        root.withdraw()
        root.mainloop()

