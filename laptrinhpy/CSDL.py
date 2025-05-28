import sqlite3
import os
def connect_db():
    return sqlite3.connect("hotel.db")

def create_database():
    if not os.path.exists("hotel.db"): # kiem tra csdl chua tontai
        with connect_db()as conn:
            print(" tao co so du lieu hotel.db")
            create_tables()
    else:
        print(" co so du da ton tai, chi tao bang neu chua co")
        create_tables()
def create_tables():
    with connect_db() as conn:
        cursor= conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY AUTOINCREMENT,
                       room_number TEXT,
                       room_type TEXT,
                       price REAL)''')
        conn.commit()
    
#create_database()
def them_room(room_number,room_type,opricee):
    with connect_db()as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO rooms (room_number,room_type,price) VALUES (?, ?, ?)",(room_number,room_type,opricee))
        conn.commit()
#them_room("p102","thuong",500000)
#them_room("p103","Vip",1000000)
def sua_room(id,room_number):
    with connect_db()as conn:
        cursor=conn.cursor()
        cursor.execute("UPDATE rooms SET id = ? WHERE room_number = ?",(id,room_number))
        conn.commit()
#sua_room(1,"p201")
def xoa_roon(id):
    with connect_db() as conn:
        cursor=conn.cursor()
        cursor.execute("DELETE FROM rooms WHERE id = ? ",(id,))
        conn.commit()
#xoa_roon(2)
#xoa_roon(4)
def hien_thi_room():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rooms" )
        room= cursor.fetchall()
        conn.commit
        if room:
            print(" them phong hotel:")
            for i in room:
                print(f"- {i[0]} | ten room :{i[1]}|type:{i[2]}| Price:{i[3]}")
        else:
            print(" khong co phong nao :") 
#sua_room(2,"p201")
#hien_thi_room()               
def menu():
    while True:
        print("=== MENU ===")
        print("a. Thêm dữ liệu")
        print("b. Sửa thông tin")
        print("c. Xóa thông tin")
        print("d. Hiển thị các phòng có giá từ 500000 đến 1000000")

        cn = input("Chọn chức năng (a/b/c/d): ").lower()

        if cn == 'a':
            them_room()
        elif cn == 'b':
            sua_room()
        elif cn == 'c':
            xoa_roon()
        elif cn == 'd':
            hien_thi_room()
            break
        else:
            print("Lựa chọn không hợp lệ.\n")

# Chạy chương trình
menu()