import sqlite3
con= sqlite3.connect('recipes.db')
p=con.cursor()
p.execute('''drop table if exists user''')

con.commit()

p.execute('''create table user (name text not null, gender text, username text not null,password text,confirm_password text,status text)''')

p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name1','male','username1','123456','123456','enable'))
p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name2','female','username2','123456','123456','enable' ))
p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name3','male','username3','123456','123456','enable' ))
p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name4','female','username4','123456','123456','enable' ))
p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name5','male','username5','123456','123456','enable' ))
p.execute('''insert into user (name, gender,username,password,confirm_password,status) values (?,?,?,?,?,?);''',('name6','male','username6','123456','123456','enable' ))
con.commit()



p.execute('''select * from user''')
result=p.fetchall()
print(result)

p.execute('''drop table if exists admin''')

con.commit()

p.execute('''create table admin (name text not null, gender text, username text not null,password text,confirm_password text)''')

p.execute('''insert into admin (name, gender,username,password,confirm_password) values (?,?,?,?,?);''',('Manish','male','manish','123456','123456' ))
p.execute('''insert into admin (name, gender,username,password,confirm_password) values (?,?,?,?,?);''',('Bandita','female','bandita','123456','123456' ))
p.execute('''insert into admin (name, gender,username,password,confirm_password) values (?,?,?,?,?);''',('Robin','male','robin','123456','123456' ))
p.execute('''insert into admin (name, gender,username,password,confirm_password) values (?,?,?,?,?);''',('Eakshitha','female','eakshitha','123456','123456' ))

con.commit()

p.execute('''drop table if exists request_table''')

con.commit()

p.execute('''create table request_table (user text not null,status not null)''')

con.commit()
