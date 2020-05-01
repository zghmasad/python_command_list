import pymysql

connection = pymysql.connect('localhost', 'root', '9125432834@Ali', 'ali')
cursor = connection.cursor()
# cursor.execute("CREATE database ali")

'''try:
    cursor.execute("create TABLE log (message VARCHAR(100) NOT NULL, id INT(6) NOT NULL)")
    connection.commit()
except:
    connection.rollback()
'''

# cursor.execute("drop TABLE log")
# connection.commit()
'''try:
    cursor.execute("Insert into log (message,id) values ('third log3',89)")
    connection.commit()
except:
    connection.rollback()
'''

'''try:
    cursor.execute("UPDATE log SET message = 'denise@my.com' WHERE id = 89")
    connection.commit()
except:
    connection.rollback()
'''

'''try:
    cursor.execute("DELETE FROM log WHERE id = 89")
    connection.commit()
except:
    connection.rollback()
'''

cursor.execute("select * from log")

data = cursor.fetchall()
for row in data:
    message, id = row
    print('row:', message, ' ', id)

print(cursor.description)
print(cursor.rowcount)
connection.close()
