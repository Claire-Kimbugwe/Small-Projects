##  
# connect to students data base and select students make sure
# that the student records are fetched in sorted order
# by student's name.


import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students") #connect to db
c = db.cursor()  #cursor used to run querries
query = "select name, id from students order by name;"  #query
c.execute(query) #executes query
rows = c.fetchall() #use cursor to fetch the results(rows)

# First, what data structure did we get?
print "Row data:" #print the words raw data
print rows        #prindts the rows fron db

# And let's loop over it too:
print        #empty line is printed
print "Student names:" #print enclosed words
for row in rows:   #iterate and print first column
  print "  ", row[0]

db.close() #close connecction to db
