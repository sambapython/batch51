import sqlite3
db_name="db1.sqlite3"
def get_con():
	con = sqlite3.connect(db_name)
	return con, con.cursor()
def create_table():
	con,cur=get_con()
	cur.execute("create table vm(id int, username varchar(60),password varchar(60),ip varchar(60))")
