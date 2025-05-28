#cursor mo co so du lieu
import sqlite3
from prettytable import PrettyTable
conn=sqlite3.connect(("qlbh.db"))
cursor=conn.cursor()
#create table
cursor.execute(''' CREATE TABLE Sanpham (Masp TEXT PRIMARY KEY ,
               Tensp TEXT,
               Soluong INTEGER)''')
cursor.execute(''' CREATE TABLE Hoadon (
    Mahd INTEGER PRIMARY KEY,
    Masp TEXT,
    Soluong INTEGER,
    FOREIGN KEY (Masp) REFERENCES Sanpham(Masp))''')
# insert 5 records into Sanpham
products=[
    ('sp1','but',30),
    ('sp2','vo',20),
    ('sp3','tay',50),
    ('sp4','thuoc',20),
    ('sp5','keo',100)
]
cursor.executemany('INSERT INTO Sanpham VALUES (?, ?, ?)', products)
# Insert 5 recor into Hoadon
invoices=[
    (1,'sp1',20),
    (2,'sp2',10),
    (3,'sp3',5),
    (4,'sp1',5),
    (5,'sp5',2)
]
cursor.executemany('INSERT INTO Hoadon VALUES (?, ?, ?)', invoices)
#Query to
#coalesce thay the gia tri null bang o
query='''SELECT ROW_NUMBER() OVER (ORDER BY sp.Masp) AS "STT",
                sp.Tensp AS "Tên sản phẩm",
                sp.Soluong AS " Số lượng nhập",
                COALESCE(SUM(hd.Soluong),0) AS " Số lượng bán",
                sp.Soluong - COALESCE(SUM(hd.Soluong),0) AS " Số lượng tồn"
        FROM Sanpham sp
        LEFT JOIN Hoadon hd ON sp.Masp = hd.Masp
        GROUP BY sp.Masp, sp.Tensp, sp.Soluong '''
cursor.execute(query)
#fetch
#rows=table
rows= cursor.fetchall()
#print results
table=PrettyTable(["STT","Tên sản phẩm","Số lượng nhập","Số lượng bán","Số lượng tồn"])
for row in rows:
    table.add_row(row)

print(table)
conn.commit()
conn.close()