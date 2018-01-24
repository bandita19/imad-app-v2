import sqlite3
import recipe1

def name():
    name = "Creamcake"
    return name
    


con = sqlite3.connect('recipes.db')
c = con.cursor()

c.execute('''drop table if exists italian''')
con.commit()
c.execute('''create table italian (recipe_name text not null primary key,category text)''')

c.execute('''insert into italian(recipe_name, category) values ( ?,? );''',('Pizza','Starters'))
c.execute('''insert into italian (recipe_name, category) values ( ?,? );''',('Pasta','Starters'))
c.execute('''insert into italian (recipe_name, category) values ( ?,? );''',('Bolognese Stuffed','Main Course'))
c.execute('''insert into italian (recipe_name, category) values ( ?,? );''',('Bobs Braciole','Main Course'))
c.execute('''insert into italian (recipe_name, category) values ( ?,? );''',('Panna Cotta','Desserts'))
c.execute('''insert into italian (recipe_name, category) values ( ?,? );''',('Creamcake','Desserts'))


con.commit()
result = c.execute("select * from italian where recipe_name='"+name()+"';")
result = c.fetchall()
print(result)
print(len(result))
for item in result:
    print(type(item))
print(result[0][0])

