import sqlite3
import os


from itertools import chain



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
    
    numBooks=int(len(bookFlagStart)/2)
    
    books=[]
    for i in range(0,numBooks):
        books.append(file_lst[bookFlagStart[i]:bookFlagEnd[i]-1])
      
    
    book =[]
    for i in books:
        j = str(i)
        #print(j)
        book.append(j)
        
    #print(book)
    
    
    b =[[]]
    
    b=[book[i::9] for i in range(9)]
    
    
    
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
    vals=[seq[i:i+6] for i in range(0,len(seq),6)]
            
    
    #for i in vals:
        #for j in i:
            #print(j)
    
    #vals = cleaned values   
    return vals
    
  

    """
    @todo: 
        parse output file to format for sqldb and pass into insertBook function 
        [{"binding": "Paperback", 
        "title": "The Great Gatsby: The Only Authorized Edition", 
        "author": "F. Scott Fitzgerald", 
        "price": "$17.00", 
        "isbn": "9780743273565", 
        "url": "https://www.prince-books.com/book/9780743273565"}, 
        {"binding": "Hardcover", "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald", 
        "price": "$12.99", 
        "isbn": "9781509826360", 
        "url": "https://www.prince-books.com/book/9781509826360"}]
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


        
def insert(vals):
    
    
    connection = sqlite3.connect('/Users/nataliemohun/Documents/GitHub/Booked-back-end/DataBase/bookedDataBase/db.sqlite3')
    
    
    c = connection.cursor()
    
     
    
    keys= ["ISBN", 
          "Title",
          "Binding",
          "Author",
          "Price",
          "LinkUrl"]
    
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
    for i in range(len(vals)):
        b.append(vals[i][0])
        t.append(vals[i][1])
        a.append(vals[i][2])
        p.append(vals[i][3])
        isbn.append(vals[i][4])
        u.append(vals[i][5])

    bookTable="singleBookData_book"
        
    #print(b,t,a,p,isbn,u)
    
    #print(len(vals))
    
    
    
    for i in range(0,len(vals)):
        print("VALUES("+isbn[i]+","+t[i]+","+a[i]+","+b[i]+","+p[i]+","+u[i]+")")
        
        c.execute("INSERT INTO "+bookTable+"("+keys[0]+","+keys[1]+","+keys[2]+","
                  +keys[3]+","+keys[4]+","+keys[5]+") VALUES("
                  +isbn[i]+","+t[i]+","+a[i]+","+b[i]+","+p[i]+","+u[i]+")")
        connection.commit() 
    
    

   

    
    
    connection.close()
    
        

#main below




#the table in db is booked_boook
outputfile = 'scrapers/outputfile'
file_lst=[]
bookFlagStart=[]
bookFlagEnd=[]

bookFlagStart,bookFileEnd,file_lst=parseBookObj(outputfile)

#get list of books
#a matrix
b=addBookObj(bookFlagStart, bookFileEnd,file_lst)

vals=getVals(b)
insert(vals)


