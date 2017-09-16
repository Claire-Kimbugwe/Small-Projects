  
# connect to students data base and select students make sure
# that the student records are fetched in sorted order
# by student's name.


import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:" #print the words raw data
print rows        #prindts the rows fron db

# And let's loop over it too:
print        #empty line is printed
print "Student names:" #print enclosed words
for row in rows:   #iterate and print first column
  print "  ", row[0]

db.close() #close connecction to db
