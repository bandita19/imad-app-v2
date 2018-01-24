import sqlite3
import recipe1

def name():
    name = "malai_kulfi"
    return name
    


con = sqlite3.connect('recipes.db')
c = con.cursor()

c.execute('''drop table if exists indian''')
con.commit()
c.execute('''create table indian (recipe_name text not null primary key,category text)''')

c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Samosa','Starters'))
c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Pakoda','Starters'))
c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Butter Chicken','Main Course'))
c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Butter Panner','Main Course'))
c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Gulab Jamun','Desserts'))
c.execute('''insert into indian (recipe_name, category) values ( ?,? );''',('Malai Kulfi','Desserts'))


con.commit()
#result = c.execute("select * from indian where recipe_name='"+name()+"';")
result = c.execute("select * from indian")
result=c.fetchall()
print(result)

#result = c.fetchall()
#print(result)
