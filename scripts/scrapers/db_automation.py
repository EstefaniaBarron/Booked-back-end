import sqlite3
import os

from itertools import chain

from DataBase.bookDataBase.singleBookData.models import Book
from DataBase.bookDataBase.singleBookData.models import Listing



bookTable="singleBookData_book"
listingTable = "singleBookData_listing"
connection = sqlite3.connect('/Users/nataliemohun/Documents/GitHub/Booked-back-end/DataBase/bookedDataBase/db.sqlite3')
c = connection.cursor()

singleBookKeys= ["ISBN", 
      "Title",
      "Author",
      "Binding",]

listingBookKeys =["isbn_id","price","book_store_id","link_url"]
    
    


"""
The database ISBN list that gets checked and updated after
each insertion
"""
DB_ISBN=[]

def parseBookObj(outputfile):
    bookFlagStart=[]
    bookFlagEnd=[]
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

          
def addBookObj(bookFlagStart,bookFlagEnd,file_lst):
    
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
    vals=[seq[i:i+8] for i in range(0,len(seq),8)]
            
    #print(vals)
    
    
    
    
    #vals = cleaned values 
    # ex:   "Hardcover"
    return vals
    

def printsingleBookTableSQL(c):
    query=("select * from "+bookTable)
    
    c.execute(query)
    
    rows=c.fetchall()
    
    # print(rows)
  
    for row in rows:
        for col in row:
            print(col,end=' ')
        print('\n')

        
def printlistingBookTableSQL(c):
    query=("select * from "+listingTable)
    
    c.execute(query)
    
    rows=c.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print('\n')
   

        
def getDB_ISBN():
    c.execute("SELECT ISBN FROM "+bookTable)
    DB_ISBN_List = c.fetchall()
    
    for x in DB_ISBN_List:
        x = str(x).replace('(', '"')
        x = str(x).replace(',)', '"')
        DB_ISBN.append(x)
        
    #print(DB_ISBN)
        
    return DB_ISBN

def checkISBNDuplicates(isbn, DB_ISBN):
    
    found = False
    
    #print("checking if ",isbn," is in: ",DB_ISBN)
    if isbn in DB_ISBN:
            #print("isbn: ",isbn," found in DB:\n",DB_ISBN)
            found = True
            #print(found)

    return found



def searchMappingSingleBook(vals):
    singleBookDictionary ={}
    #key= ISBN #value = entire book data 
    for i in range(len(vals)):
        isbn=vals[i][4]
        #print(isbn)
        singleBookDictionary[isbn]=vals[i]
        
    #print(singleBookDictionary,"\n")
    #print(singleBookDictionary.keys())
    return singleBookDictionary


def insertListings(vals,bookObject):
    
    #for i in vals:
        #print(i,"\n\n")

    #bookObject is single book django Object specific to the listings
        
    isbn=[]
    price=[]
    url=[]
    storeName=[]
    condition=[]
        
    for i in range(len(vals)):
        #each new iteration represents a new listing/linking to the passed in bookObject
        isbn.append(vals[i][4])
        price.append(vals[i][3])
        url.append(vals[i][5])
        storeName.append(vals[i][6])
        condition.append(vals[i][7])
        listingObject = "listing_"+str(i)
        #creating a new listing using the Book object
        #linking bookstore = single book object and isbn = single book object keys
        listingObject = Listing(book_store=bookObject,link_url=url[i],price=price[i],isbn=bookObject)
        listingObject.save()
        
    # listing key sequence =["isbn_id","price","book_store_id","link_url"]
    
        
    for i in range(0,len(vals)): 
         c.execute("INSERT INTO "+listingTable+"("+listingBookKeys[0]+","+listingBookKeys[1]+","
                   +listingBookKeys[2]+","+listingBookKeys[3]+")" 
                   +"VALUES("+isbn[i]+","+price[i]+","+storeName[i]+","+url[i]+")")
         connection.commit() 




def insertSingleBookDictionary(singleBookDictionary,vals):

    singleBook =[]
   
    
    for i in singleBookDictionary:
        #print(i,"\n\n",singleBookDictionary.get(i))
        singleBook.append(singleBookDictionary.get(i))
        



    #print(singleBook)
    
    binding=[]
    title=[]
    author=[]
    isbn=[]
   

    for i in range(len(singleBook)):
        isbn.append(singleBook[i][4])
        title.append(singleBook[i][1])
        author.append(singleBook[i][2])
        binding.append(singleBook[i][0])
        
        
   
    """
         singlebook key sequence:
         "ISBN", 
         "Title",
         "Author",
         "Binding",
     """
     #Globals of the table names
     #listingTable = singleBookData_listing
     #bookTable = singleBookData_book
  
    for i in range(0,len(singleBook)): 
        isbnToCheck = singleBook[i][4]
        
        
        
        
        #make sure ISBN is only entered once
        #get the list of databse ISBN from book table
        DB_ISBN=getDB_ISBN()
        if checkISBNDuplicates(isbnToCheck,DB_ISBN )==True:
            print("this book was already in the book table\n")
            continue

        #https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
        #book_store = models.ForeignKey(Book, related_name='available_at', on_delete=models.CASCADE)
        #create a new book object
        #per link book is reporter listing is article
        
        #bookObject = str("singleBook_"+str(i))
        #model object
        bookObject = Book(author=author[i],binding=binding[i],isbn=isbn[i],title=title[i])
        bookObject.save()
        print(bookObject.__sizeof__)
        

        if checkISBNDuplicates(isbnToCheck,DB_ISBN )==False:
            print("this is a new book to add to single book table\n")
            c.execute("INSERT INTO "+bookTable+"("+singleBookKeys[0]+","+singleBookKeys[1]+","
                   +singleBookKeys[2]+","+singleBookKeys[3]+")" 
                   +"VALUES("+isbn[i]+","+title[i]+","+author[i]+","+binding[i]+")")
            connection.commit() 
            #this was a new book so populate listings tables
            insertListings(vals,bookObject)
    
        


    
        

#main below



def driver(outputfile):


    #the table in db is booked_boook
    file_lst=[]
    bookFlagStart=[]
    bookFlagEnd=[]

    bookFlagStart,bookFlagEnd,file_lst=parseBookObj(outputfile)

    b=addBookObj(bookFlagStart, bookFlagEnd,file_lst)

    vals=getVals(b)
    
    singleBookDictionary = searchMappingSingleBook(vals)


    #calls insert listing so we avoid duplicate insertion of listings 
    insertSingleBookDictionary(singleBookDictionary,vals)


    #printSQL(c)
    #printsingleBookTableSQL(c)
    #printlistingBookTableSQL(c)


#testing 
#testing file below to test just uncomment driver
outputfile = "/Users/nataliemohun/Documents/GitHub/Booked-back-end/scripts/scrapers/search_outputs/The Great Gatsby_search_output.txt"
driver(outputfile)
