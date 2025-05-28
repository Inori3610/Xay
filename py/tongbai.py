def hieu(a,b):
    return a - b
if __name__ =="__main__" :
    n1 = float(input("nhap so thu nhat:"))
    n2 = float(input("nhap so thu nhat:"))
    print(f" hieu cua hai so la:{hieu(n1,n2)}")
my_list=[1,"chao",3.14,[2,4,6]]
print(my_list[3])

numbers=[10,20,30,40,50]
for num in  numbers:
    print(num)
    
for index,value in enumerate(numbers):
    print(f" vi tri {index}:{value}")
    
i=0
while i<len(numbers):
    print(numbers)
    i+=1

import list
result = list.hieu(20,10)
print(f"hieu cua 20 va 10 la :{result}")

def Fibanocci(n):
    if n <=2:
        return [2]
    F = [2, 3]
    
    while len(F) <= n:
        next_value = F[len(F) - 1] + F[len(F) - 2]
        F.append(next_value)
    return F

print(" sau  so dau tien:")
print( Fibanocci(5))

def fibanocci(n):
    F=[2,3]
    for i in range (2,n):
        F.append(F[-1]+F[-2])
    return F
n=6
F=fibanocci(n)
max1=max(F)
min1=min(F)
result=fibanocci(n)
print(f" fibanocci thu {n} :",result)
print( "fibanocci max :",max1 )
print( "fibanocci min :",min1 )

## tinh chat bao dong
class calculator:
    def __init__(self,num1,num2):
       self.__num1=num1 #private
       self.__num2=num2
    def get_num(self):
        return self.__num1 + self.__num2
ca=calculator(5,7)
print(" tong hai so:",ca.get_num())
# tinh ke thua va da hinh
class cha:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def ca_sa(self):
        return self.base_salary
    def display(self):
        print(f"{self.name}-luong:{self.ca_sa()} vnd")
class con(cha):
    def __init__(self,name,base_salary,position_allowance):
        super().__init__(name,base_salary)
        self.position_allowance=position_allowance
    def ca_sa(self):
        return self.base_salary+ self.position_allowance
amin=con("nguyen van a",8000000,2000000)
amin.display()
#
from abc import ABC,abstractmethod
class cha(ABC):
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    @abstractmethod
    def ca_sa(self):
       pass
    def display(self):
       print(f"{self.name}-luong:{self.ca_sa()} vnd")
class con(cha):
    def __init__(self,name,base_salary,position_allowance):
        super().__init__(name,base_salary)
        self.position_allowance=position_allowance
    def ca_sa(self):
        return self.base_salary+ self.position_allowance
amin=con("nguyen van a",8000000,2000000)
amin.display()

#bai tap
class thuvien:
    def __init__(self,id,title,author,year):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
TV=thuvien("136","python","giang mi xay","2004")
print("id:",TV.id)
print("title:",TV.title)
print("author:",TV.author)
print("year :",TV.year)

# bai tu hoc:
ds=[]
while True:
    print(" nhap danh sach menu:")
    print("1.nhap danh sach hoc sinh:")
    print("2.in danh sach hoc sinh:")
    print("3.xoa danh sach hoc sinh:")
    print("4.thoat chuong trinh:")
    
    hs=input()
    if hs=="4":
        break
    if hs=="1":
        value=input("moi nahp ten hoc sinh :")
        ds.append(value)
    if hs=="2":
        print("so luong hoc sinh da co",len(ds))
        for index,sv in enumerate(ds):
            print("hoc sinh thu{} ten{}".format(index+1,sv))    
    if hs=="3":
        print(" xoa danhs sach hoc sinh:")

#class thu vien
class thuvien:
    def __init__(self):
        self.id=""
        self.title=""
        self.author=""
        self.year=""
    def thongtin(self):
        self.id= int(input(" nhập id :"))
        self.title=input("nhập tiêu đề:")
        self.author=input("nhập tác giả:")
        self.year=int(input(" nhâp năm:"))
    def hienthi(self):
        print(f"id:{self.id}| tiêu đề:{self.title}| tác giả:{self.author}| năm:{self.year}")
class Book(thuvien):
    def __init__(self):
        super().__init__()
        self.id=""
    def thongtin(self):
        super().thongtin()
        self.id=input(" nhap sach:")
    def hienthi(self):
        super().hienthi()
        print(f" idid: {self.id}| tiêu đề:{self.title}|tác giả:{self.author}| năm:{self.year}")
ds_sach=[]
n=int(input(" Nhap danh sach thu vien :"))
for i in range(n):
    print(f" nhap thong tin thu vien {i+1}:")
    tv= Book()
    tv.thongtin()
    ds_sach.append(tv)
##lam viec voi tep
# ghi tep: write()
# chen du lieu vao cuoi tap: append()

def tinh_tong_so_chan(ten_tep="D:\\so_chan.txt"):
    tong=0
    with open(ten_tep,"r",encoding="utf-8") as file:
        content= file.read().strip()
        if content:
            for num in content.split():
                tong=tong+int(num)
            print(f" noi dung tep:{content}")
            print(f" tong cac so chan :{tong}")
        else:
            print("tep khong co san")
##
def ghi_so_chan(mang,ten_tep="D:\\so_chan.txt"):
    so_chan=""
    with open(ten_tep,"w", encoding="utf-8") as file:
        for so in mang :
            if int(so) % 2 == 0:
                so_chan += so +" "
        file.write(so_chan)
    print(" da ghi cac so chan vao tep!")
ma=["1", "2" ,"3", "4", "5", "6", "7", "8"]
ghi_so_chan(ma)
def tinh_tong_so_chan(ten_tep="D:\\so_chan.txt"):
    tong=0
    with open(ten_tep,"r",encoding="utf-8") as file:
        content= file.read().strip()
        if content:
            for num in content.split():
                tong=tong+int(num)
            print(f" noi dung tep:{content}")
            print(f" tong cac so chan :{tong}")
        else:
            print("tep khong co san")
tinh_tong_so_chan()

#ZeroDivisionError: loi khong doan duoc
#Exception : loi doan duoc
"""
file_name="sochan.txt"
mang=[2,4,6,7,9]
with open(file_name, "wb")as f:
    for i in mang:
        if int(i)%2==0:
            f.write(repr(i).encode())
            
# doc tep va tim so nguyen
with open(file_name,"rb")as f:
    for i in f.read():
        print(" mang doc tu file:"+chr(i)+" ") """
"""def kiem_tra_tuoi(tuoi):
    if tuoi<0:
        raise ValueError(" Tuoi khong the am ")
    print(f" tuoi cua ban:{tuoi}")
try:
    tuoi=int(input(" nhap vao tuoi:"))
    kiem_tra_tuoi(tuoi)
except ValueError as e:
    print(f" loi:{e}")"""
    
    
    