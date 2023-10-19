import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

# conn.execute('CREATE TABLE student_(name TEXT, addr TEXT, city TEXT, pin TEXT)')
# conn.execute("INSERT INTO student_(name, addr, city, pin) VALUES (?,?,?,?)",('deep','kcl','nvs','396310') )
conn.execute("INSERT INTO student_(name, addr, city, pin) VALUES (?,?,?,?)",('A','kcl','nvs','396310') )
print ("Table created successfully")
conn.commit()
conn.close()