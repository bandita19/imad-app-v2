import sqlite3
import recipe1

def name():
    name = "Spring Roll"
    return name
    


con = sqlite3.connect('recipes.db')
c = con.cursor()

c.execute('''drop table if exists thai''')
con.commit()
c.execute('''create table thai (recipe_name text not null primary key,category text)''')

c.execute('''insert into thai(recipe_name, category) values ( ?,? );''',('Spring Roll','Starters'))
c.execute('''insert into thai (recipe_name, category) values ( ?,? );''',('Crab Corn Cake','Starters'))
c.execute('''insert into thai (recipe_name, category) values ( ?,? );''',('Thai Rice','Main Course'))
c.execute('''insert into thai (recipe_name, category) values ( ?,? );''',('Barbecue Sea Bass','Main Course'))
c.execute('''insert into thai (recipe_name, category) values ( ?,? );''',('Kanom Chan','Desserts'))
c.execute('''insert into thai (recipe_name, category) values ( ?,? );''',('Tako','Desserts'))


con.commit()
result = c.execute("select * from thai where recipe_name='"+name()+"';")
result = c.fetchall()
print(result)
print(len(result))
for item in result:
    print(type(item))
print(result[0][0])

