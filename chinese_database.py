import sqlite3
import recipe1

def name():
    name = "Mango Pudding"
    return name
    


con = sqlite3.connect('recipes.db')
c = con.cursor()

c.execute('''drop table if exists chinese''')
con.commit()
c.execute('''create table chinese (recipe_name text not null primary key,category text)''')

c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Momos','Starters'))
c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Babycorn Chilly','Starters'))
c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Noodles','Main Course'))
c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Fried Rice','Main Course'))
c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Mooncake','Desserts'))
c.execute('''insert into chinese (recipe_name, category) values ( ?,? );''',('Mango Pudding','Desserts'))


con.commit()
result = c.execute("select * from chinese where recipe_name='"+name()+"';")
result = c.fetchall()
print(result)
print(len(result))
for item in result:
    print(type(item))
print(result[0][0])

