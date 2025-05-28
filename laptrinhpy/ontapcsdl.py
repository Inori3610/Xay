import sqlite3
conn = sqlite3.connect("QLNS.db")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Chucvu (Macv TEXT PRIMARY KEY, Tencv TEXT,Tienphucap Float) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Nhanvien(Manv INTEGER  PRIMARY KEY,Hoten TEXT, Ngaysinh DATETIME,Macv TEXT , Luong FLOAT,FOREIGN KEY (Macv) REFERENCES Chucvu(Macv)  )''')
CV=[('cv1','CEO','1000000'),
         ('cv2','PGD','800000'),
         ('cv3','TP','600000'),
         ('cv4','kt','400000'),
         ('cv5','PKD','300000'),]
cursor.executemany("INSERT OR REPLACE INTO Chucvu VALUES(?,?,?)", CV)
NV=[(1,'Nguyen Van A',12/2/1999,'cv4',6000000),
    (2,'Hoang Thi B',25/4/1999,'cv5',7000000),
    (3,'Cao BA D',19/9/1990,'cv1',20000000),
    (4,'Pham THi E',20/4/1998,'cv3',10000000),
    (5,'Nguyen Ngoc G',27/6/1989,'cv2',15000000)
]
cursor.executemany("INSERT OR REPLACE INTO Nhanvien VALUES(?,?,?,?,?)",NV)
query='''
    SELECT 
        cv.Tencv AS "TEN CHUC VU",
        nv.Hoten AS "TEN NHAN VIEN",
        nv.Luong AS "LUONG",
        cv.Tienphucap AS "PHU CAP",
        COALESCE(nv.Luong, 0) + cv.Tienphucap AS "TONG LUONG"
    FROM Chucvu cv 
    LEFT JOIN Nhanvien nv ON cv.Macv = nv.Macv
    ORDER BY cv.Macv
'''
cursor.execute(query)
rows=cursor.fetchall()
col1=15
col2=14
col3=15
col4=14
col5=15
tieude=f"{'Chuc Vu':<{col1}}|{'Ten Nhan Vien':<{col2}}|{'Luong':<{col3}}|{'Phu Cap':<{col4}}|{'Tong luong':<{col5}}"
dorong=f"{'-'*col1}-|{'-'*col2}=|{'-'*col3}-|{'-'*col4}=|{'-'*col5}"
for Chucvu,tennv,luong,phucap, tong in rows:
    print(f"{Chucvu:<{col1}}|{tennv:<{col2}}|{luong:<{col3}}|{phucap:<{col4}}|{tong:<{col5}}")
cursor.close






