import pickle
class customer:
    def __init__(self):
        self.makh=""
        self.tenkh=""
        self.diachi=""
        self.sdt=""
        self.soluong=0
        self.dongia=0.0
    def input(self):
        self.makh=input("Nhập mã khách hàng :")
        self.tenkh=input("Nhập tên khách hàng :")
        self.diachi=input(" Nhập địa chỉ :")
        self.sdt=input(" Nhập số điện thoại :")
        self.soluong=int(input(" Nhập số lượng :"))
        self.dongia=float(input("Nhập đơn giá :"))
    def output(self):
        print("ma kh",self.makh)
        print("ten kh",self.tenkh)
        print("dia chi",self.diachi)
        print("sdt",self.sdt)
        print("so luong",self.soluong)
        print("don gia",self.dongia)
class VIPCustom(customer):
    def __init__(self):
        super().__init__()
        self.mucchietkhau=""
    def input(self):
        super().input()
        self.mucchietkhau=int(input("Nhập mức chiết khấu:"))
    def output(self):
        super().output()
        print("muc chiet khau",self.mucchietkhau,"%")
        print("tong tien",self.Tongtien())
    def chietkhau(self):
        return self.soluong*self.dongia*self.mucchietkhau /100
    def Tongtien(self):
        return(self.dongia*self.soluong)-self.chietkhau()
def ghi(name,dsVip):
    with open(name,"wb")as f:
        pickle.dump(dsVip,f)
def doc(name):
    with open(name,"rb")as f:
        return pickle.load(f)
def main():
    ds=[]
    n=int(input("Nhập số lượng khách Vip :"))
    for i in range(n):
        print(f"\n Nhập thông tin khách Vip {i+1}:")
        vip=VIPCustom()
        vip.input()
        ds.append(vip)
    ghi("D:\\ds.dat",ds)
    print("\n Danh sach da diuoc ghi vao tep: D\\ds.dat")
    dsVip=doc("D:\\ds.dat")
    sum=0
    for vip in dsVip:
        print("     ")
        vip.output()
    for vip in dsVip:
        sum+=vip.Tongtien()
    print("")
    print("Tong doanh thu:",sum)
if __name__ == "__main__":
    main()