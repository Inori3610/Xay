import pickle #Doc va ghi voi objecct hieu qua
from prettytable import PrettyTable
class hocsinh:
    def __init__(self):
        self.hoten=""
        self.ngaysinh=""
        self.diemtoan=0.0
        self.diemvan=0.0
    def input(self):
        self.hoten= input(" nhap ho ten :")
        self.ngaysinh=input("nhap ngay sinh (dd/mm/yyy):")
        self.diemtoan=float(input("nhap diem toan:"))
        self.diemvan=float(input(" nhap diem van:"))
    def output(self):
        print(f"ho ten :{self.hoten}|ngay sinh:{self.ngaysinh}|toan:{self.diemtoan}| Van:{self.diemvan}")
        
class chuyenvan(hocsinh):
    def __init__(self):
        super().__init__()
        self.lop=""
    def input(self):
        super().input()
        self.lop=input(" Nhap lop chuyên văn:")
    def output(self):
        super().output()
        print(f"lop: {self.lop}")
        print(f"diem trung binh:{self.diemtb():.2f}")
        print(f"xep loai: {self.xeploai()}")
    def diemtb(self):
        return(self.diemvan*2+self.diemtoan)/3
    def xeploai(self):
        dtb=self.diemtb()
        if dtb<5:
            return "kém"
        elif dtb < 6.5:
            return "trung bình"
        elif dtb <7.5:
            return "khá"
        elif dtb <9:
            return "giỏi"
        else:
            return "xuất sắc"
def ghi(name,dssv):
    with open(name, "wb")as f:
        pickle.dump(dssv, f)
def doc(name):
    with open(name, "rb")as f:
        return pickle.load(f)
def main():
    ds_hocsinh=[]
    n=int(input("Nhập số lượng hoc sinh chuyên văn:"))
    for i in range(n):
        print(f" Nhập thông tin học sinh {i+1}:")
        hs= chuyenvan()
        hs.input()
        ds_hocsinh.append(hs)
    ghi("D:\\ds.dat",ds_hocsinh)
    print("\nDanh sách hs đã được ghi vào tep:D:\\ds.dat")
    #Đọc va ghi ra 
    dssv=doc("D:\\ds.dat")
    for hs in dssv:
        if  hs.xeploai() in ["giỏi","xuất sắc"]:
            hs.output()
            print(" - " * 40 ) 

if __name__ == "__main__":
    main()     
        
     
        

