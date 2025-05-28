import sqlite3
import os
def employees_db():
    return sqlite3.connect("company.db")

def create_database():
    if not os.path.exists("company.db"): # kiem tra csdl chua tontai
        with employees_db()as conn:
            print(" tao co so du lieu hotel.db")
            create_tables()
    else:
        print(" co so du da ton tai, chi tao bang neu chua co")
        create_tables()
def create_tables():
    with employees_db() as conn:
        cursor= conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        salary float)''')
        conn.commit()
#create_database()
def them_employees(name,salary):
    with employees_db()as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO employees (name,salary) VALUES (?, ?)",(name,salary))
        conn.commit()
#them_employees("nam",110000)
#them_employees("xay",230000)
#them_employees("hung",400000)
def hien_thi_employess():
    with employees_db()as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees" )
        name=cursor.fetchall()
        conn.commit
        if name:
            print(" them employees:")
            for i in name:
                print(f"-id: {i[0]} | name :{i[1]}|salary:{i[2]}")
        else:
            print(" khong co  :") 
hien_thi_employess()
def update(id,name):
    with employees_db() as conn:
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET id = ? WHERE name = ?",(id,name))
        conn.commit()
#update(1,"nam")