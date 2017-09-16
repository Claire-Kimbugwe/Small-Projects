
# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
# 

import sqlite3

db = sqlite3.connect("testdb") #connect to databse
c = db.cursor() #caall the curser
c.execute("insert into balloons values ('blue', 'water') ") #use curser to execute query
db.commit() #saves changes
db.close() #disconnect database
