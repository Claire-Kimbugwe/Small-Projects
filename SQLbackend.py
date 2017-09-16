#Quiz: Give that App a Backend
#The forum database has already been created for you. Your code will need to connect to it using
# psycopg2.connect("dbname=forum") and then perform select and insert operations on the posts table. 
# The existing GetAllPosts function returns all the entries from a list. So its database version should return all
# the entries from the posts table.And likewise, the existing AddPost function inserts an entry into a list.
# You do not need to provide the time column when you insert a post. The table is set up to already provide a timestamp.
# The existing GetAllPosts function sorts the posts using a Python sort function. When you implement this
# function using the database, can you avoid sorting in Python by doing it in SQL?

## Database connection
DB = [] ## Get posts from database. 
def GetAllPosts(): 
  '''
  Get all the posts from the database, sorted with the newest first. 
  Returns: A list of dictionaries, where each dictionary has a 'content'
  key pointing to the post content, 
  and 'time' key pointing to the time it was posted. 
  ''' 
  posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB] 
  posts.sort(key=lambda row: row['time'], reverse=True) 
  return posts ## Add a post to the database. 

def AddPost(content): 
  '''
  Add a new post to the database. Args: content: The text
  content of the new post. 
  '''
  t = time.strftime('%c', time.localtime()) 
  DB.append((t, content))

