import sqlite3
import os


from itertools import chain


outputfile="/Users/nataliemohun/Documents/GitHub/Booked-back-end/scripts/scrapers/search_outputs/The_great_gatsby_search_output.txt"
bookTable="singleBookData_book"
connection = sqlite3.connect('/Users/nataliemohun/Documents/GitHub/Booked-back-end/DataBase/bookedDataBase/db.sqlite3')
c = connection.cursor()

keys= ["ISBN", 
      "Title",
      "Author",
      "Binding",
      "Price",
      "LinkUrl",
      "BookStore"]

"""
The database ISBN list that gets checked and updated after
each insertion
"""
DB_ISBN=[]

def parseBookObj(outputfile):
    f=open(outputfile,'r')
    file_lst=f.read()
    charCount=0

    for letter in file_lst:
        charCount+=1
        
        #the char num to index out book objs
        if letter =='{':
            bookFlagStart.append(charCount)
            
        if letter =='}':
            bookFlagEnd.append(charCount)
        
    return bookFlagStart,bookFlagEnd,file_lst

          
def addBookObj(bookFlagStart,bookFileEnd,file_lst):
    
    numBooks=int(len(bookFlagStart))
    
    books=[]
    for i in range(0,numBooks):
        books.append(file_lst[bookFlagStart[i]:bookFlagEnd[i]-1])
      
    
    book =[]
    for i in books:
        j = str(i)
        book.append(j)
    
    
    
    b =[[]]
    
    #create book matrix [book[bookData]]
    b=[book[i::numBooks] for i in range(numBooks)]
    #print(b)
    
    
    return b



def getVals(b):
    
    d=[[]]
    #numB == rows
    numB=len(b)
    #print(numB)
    v=[]
 
    #print(str(v).split(','))
    #b=[b[i::9] for i in range(9)]
    f = list(chain.from_iterable(b))
    for i in f:
        v+=(str(i).split(','))
    

    flag ='": '
    c=[]
    for i in v:
        c+=str(i).split(flag)
    seq=c[1::2]  
    vals=[seq[i:i+7] for i in range(0,len(seq),7)]
            
    """
    for i in vals:
        for j in i:
            print(j)
    """
    
    #vals = cleaned values 
    # ex:   "Hardcover"
    return vals
    

def printSQL(c):
    query=("select * from "+bookTable)
    
    c.execute(query)
    
    rows=c.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print('\n')
   

        
def getDB_ISBN(vals):
    c.execute("SELECT ISBN FROM "+bookTable)
    DB_ISBN_List = c.fetchall()
    
    for x in DB_ISBN_List:
        x = str(x).replace('(', '"')
        x = str(x).replace(',)', '"')
        DB_ISBN.append(x)
        
    print(DB_ISBN)
        
    return DB_ISBN

def checkISBNDuplicates(isbn, DB_ISBN):
    
    found = False
    
    print("checking if ",isbn," is in: ",DB_ISBN)
    if isbn in DB_ISBN:
            print("isbn: ",isbn," found in DB:\n",DB_ISBN)
            found = True
            print(found)

    return found
        
def insert(vals):
    

    
    """
    uncomment for blank databases insertino/naming of columns   
    for i in range(0,len(keys)):
        query="ALTER TABLE b ADD "+keys[i]+" VARCHAR(100)"
        c.execute(query) 
        conn.commit()
    """
    
    
    b=[]
    t=[]
    a=[]
    p=[]
    isbn=[]
    u=[]
    s=[]
    for i in range(len(vals)):
        isbn.append(vals[i][4])
        print(vals[i][4])
        t.append(vals[i][1])
        a.append(vals[i][2])
        b.append(vals[i][0])
        p.append(vals[i][3])
        u.append(vals[i][5])
        s.append(vals[i][6])

    print(isbn)
    """
        key sequence:
        "ISBN", 
        "Title",
        "Author",
        "Binding",
        "Price",
        "LinkUrl",
        "BookStore"
    """
    for i in range(0,len(vals)):
        isbnToCheck = vals[i][4]
        DB_ISBN=getDB_ISBN(vals)
        if checkISBNDuplicates(isbnToCheck,DB_ISBN )==True:
            continue      
       
        c.execute("INSERT INTO "+bookTable+"("+keys[0]+","+keys[1]+","
                  +keys[2]+","+keys[3]+","+keys[4]+","+keys[5]+","+keys[6]+")" 
                  +"VALUES("+isbn[i]+","+t[i]+","+a[i]+","+b[i]+","+p[i]+","+u[i]+","+s[i]+")")
        connection.commit() 
    

    
        

#main below




#the table in db is booked_boook
file_lst=[]
bookFlagStart=[]
bookFlagEnd=[]

bookFlagStart,bookFileEnd,file_lst=parseBookObj(outputfile)

b=addBookObj(bookFlagStart, bookFileEnd,file_lst)

vals=getVals(b)
getDB_ISBN(vals)
insert(vals)

#printSQL(c)


