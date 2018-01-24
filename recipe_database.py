import sqlite3
import tkinter
import recipe1

def name():
    name = "Malai_Kulfi"
    return name
    


con = sqlite3.connect('recipes.db')
c = con.cursor()

c.execute('''drop table if exists recipe_database''')
con.commit()
c.execute('''create table recipe_database (recipe_name text not null, recipe_desc text, feedback int, count int)''')

c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Momos',recipe1.momos(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Babycorn',recipe1.babycorn(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Noodles',recipe1.chinese_noodles(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Fried Rice',recipe1.fried_rice(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Mooncake',recipe1.mooncake(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Mango Pudding',recipe1.mango_pudding(),0,0 ))



c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Spring Roll',recipe1.thai_spring_roll(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Crab Corn Cake',recipe1.thai_crab_corn_cake(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Rice',recipe1.thai_rice(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Barbecue Sea Bass',recipe1.barbecue_see_bass(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Kanom Chan',recipe1.kanom_chan(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Takos',recipe1.thai_takos(),0,0 ))



c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Pizza',recipe1.italian_pizza(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Pasta',recipe1.italian_pasta(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Bolognese Stuffed',recipe1.bolognese_stuffed(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Bobs Braciole',recipe1.bobs_braciole(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Panna Cotta',recipe1.panna_cotta(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Creamcake',recipe1.italian_creamcake(),0,0 ))



c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Samosa',recipe1.samosa(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Pakoda',recipe1.pakoda(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Butter Chicken',recipe1.butter_chicken(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Butter Panner',recipe1.butter_panner(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Gulab Jamun',recipe1.gulab_jamun(),0,0 ))
c.execute('''insert into recipe_database (recipe_name, recipe_desc, feedback, count) values ( ?,?,?,? );''',('Malai Kulfi',recipe1.malai_kulfi(),0,0 ))


con.commit()
#result = c.execute("select recipe_desc from recipe_database where recipe_name='"+name()+"';")
result=c.execute('''select recipe_name from recipe_database''')
result = c.fetchall()
#print(len(result))
'''for item in result:
    print(type(item))
print(result[0][0])
'''
