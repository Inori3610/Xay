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
        
    def timsach(self):
        name=input()
        if(self.title== name):
            print(" sach can tim la:")
            print(f"id:{self.id}| tiêu đề:{self.title}| tác giả:{self.author}| năm:{self.year}")
        else:
            print(" khong tim thay sach:")
            
ds_sach=[]
n=int(input(" Nhap danh sach thu vien :"))
for i in range(n):
    print(f" nhap thong tin thu vien {i+1}:")
    tv= thuvien()
    tv.thongtin()
    ds_sach.append(tv)
# hien thi
print(" danh sach da them:")
for thuvien in ds_sach:
    thuvien.hienthi()
#timsach
print(" nhap ten sach can tim:")
for thuvien in ds_sach:
    tv.timsach()

    
    
    

