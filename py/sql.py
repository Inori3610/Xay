import sqlite3
from prettytable import PrettyTable
def book():
    conn=sqlite3.connect("book.db")
    #autoincrement la tu dong tang khi chen mot cuon sach moi thi chi so tang len
    query='''CREATE TABLE IF NOT EXISTS Book(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        price INTEGER NOT NULL
        )'''
    cursor=conn.cursor()
    cursor.execute(query)
    conn.close()
    
def insert(name,author,price):
    conn=sqlite3.connect("book.db")
    query='''INSERT INTO Book (name,author,price) VALUES (?, ?, ?)'''
    
    cursor=conn.cursor()
    cursor.execute(query,(name,author,price))
    conn.commit()
    conn.close()
def getAllbook(name):
    conn=sqlite3.connect("book.db")
    query='''SELECT * FROM Book WHERE name LIKE ?'''
    cursor=conn.cursor()
    bookList=cursor.execute(query, ('%'+name+'%',)).fetchall()
    conn.close()
    return bookList
def printbooklist(bookList):
    table=PrettyTable(["Mã sách","Tên sách","Tác giả","Giá bán"])
    for book in bookList:
        table.add_row(book)
    print(table)
    
if __name__ == "__main__":
    book()
    