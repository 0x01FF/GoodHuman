import sqlite3


DB = sqlite3.connect("goodhuman.db")
CUR = DB.cursor()

#CUR.execute("DROP TABLE rewards")
#CUR.execute("DROP TABLE tasks")
CUR.execute("SELECT group_id FROM members")
print(CUR.fetchall())


