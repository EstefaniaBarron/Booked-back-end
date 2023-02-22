import sqlite3

sqliteConnection = sqlite3.connect('db.sqlite3')
cursor = sqliteConnection.cursor()

#the table in db is booked_boook

def parseOutput(file):
    """
    @todo: 
        parse output file to format for sqldb and pass into insertBook function 
    """
def printSQL(cursor):
    query="select * from booked_book"
    
    cursor.execute(query)
    
    rows=cursor.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
   
    cursor.close()

def insertBook():
    try:
        #values need to be unique to the book insertions 
        sqlite_insert_query =sqlite_insert_query = """INSERT INTO booked_book
                          (id, title, author_name, binding, price,link) 
                           VALUES 
                          (3,'Emma','Jane Austen','paperback',8.99,'www.test.com')"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Insertion complete", cursor.rowcount)
    

    except sqlite3.Error as error:
        print("Insertion Error:", error)
    finally:
        if sqliteConnection:
            #print and close
            printSQL(cursor)
            print("The SQLite connection is closed")



#insertBook()

