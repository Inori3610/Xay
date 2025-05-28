import sqlite3
import os
def connect_db():
    return sqlite3.connect("QLSV.db")

def create_database():
    if not os.path.exists("QLSV.db"): # kiem tra csdl chua tontai
        with connect_db()as conn:
            print(" tao co so du lieu QLSV.db")
            create_tables()
            
    else:
        print(" co so du da ton tai, chi tao bang neu chua co")
        create_tables()
def create_tables():
    with connect_db() as conn:
        cursor= conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Lop (id INTEGER PRIMARY KEY AUTOINCREMENT,ten_lop TEXT NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS Sinhvien (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                       ho_ten NEXT NOT NULL,ma_sv TEXT UNIQUE NOT NULL,
                       lop_id INTEGER,FOREIGN KEY (lop_id) REFERENCES Lop(id))''')
        
        conn.commit()
#create_database()
def them_lop(ten_lop):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(" INSERT INTO Lop (ten_lop) VALUES (?)",(ten_lop,))
        conn.commit
def them_sinh_vien(ho_ten, ma_sv, lop_id):
    with connect_db() as conn:
        cursor= conn.cursor()
        cursor.execute("INSERT INTO Sinhvien (ho_ten, ma_sv, lop_id) VALUES (?, ?, ?)",
                       (ho_ten, ma_sv, lop_id))
        conn.commit()
def hien_thi_lop():
    with connect_db()as conn:
        cursor = conn.cursor()
        cursor.execute(" SELECT * FROM Lop ")
        sinh_vien = cursor.fetchall()
        if sinh_vien:
            print(f" danh sach sinh vien lop:")
            for sv in sinh_vien:
                print(f"- {sv[0]} (Lop : {sv[1]})")
        else:
            print("khong co sunh vien trong lop nay.")
def hien_thi_sv():
    with connect_db()as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sinhvien ")
        sinh_vien= cursor.fetchall()
        if sinh_vien:
            print(f" danh sach sinh vien :")
            for sv in sinh_vien:
                print(f"- {sv[0]} (Masv: {sv[2]}) (Ten: {sv[1]}) (Malop: {sv[3]})")
        else:
            print(" khong co sinh vien nao trong lop nay.")
def sua_sinh_vien(ma_sv, ho_ten_moi):
    with connect_db()as conn:
        cursor=conn.cursor()
        cursor.execute("UPDATE Sinhvien SET ho_ten = ? WHERE ma_sv = ?",
                       (ho_ten_moi, ma_sv))
        conn.commit()
#sua_sinh_vien("sv01","giang mi xay")
#sua_sinh_vien("sv02"," vi van anh")
#hien_thi_sv()
def xoa_sinh_vien(ma_sv):
    with connect_db()as conn:
        cursor= conn.cursor()
        cursor.execute("DELETE FROM Sinhvien WHERE ma_sv = ?",(ma_sv,))
        conn.commit()
#xoa_sinh_vien("sv01")
#hien_thi_sv() 
def hien_thi_sinh_vien_cua_lop(ten_lop):
    with connect_db() as conn:
        cursor =conn.cursor()
        cursor.execute("SELECT Sinhvien.ho_ten, Sinhvien.ma_sv FROM "
                       "Sinhvien JOIN Lop ON Sinhvien.lop_id = Lop.id "
                       "WHERE Lop.ten_lop = ?", (ten_lop,))
        sinh_vien = cursor.fetchall()
        if sinh_vien:
            print(f"Danh sach sinh vien lop {ten_lop}:")
            for sv in sinh_vien:
                print(f"- {sv[0]} (Ma sv: {sv[1]})")
        else:
            print("khong co sinh vien nao trong lop nay")
#hien_thi_sinh_vien_cua_lop("CNTT01") 
#hien_thi_sv()
#hien_thi_lop()

