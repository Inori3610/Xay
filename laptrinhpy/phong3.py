import pickle
class Phong:
    def __init__(self):
        self.tenphong=""
        self.giaphong=""
    def tinhtien(self):
        self.songay=""
        return self.giaphong*self.songay
class Thuephong(Phong):
    def __init__(self):
        super().__init__()
        self.tenkhachhang=""
        self.loaiphong=""
    def tinhtien(self):
        tongtien = super().tinhtien()
        if self.loaiphong == "vip":
            return tongtien * 1.1
        return tongtien
def nhap_danh_sach_kh(ds_kh):
    n= int(input("Nhập số lượng khách hàng thuê phòng :"))
    for i in range(n):
        print (f"Nhập thông tin khách hang thứ {i+1}")
        them(ds_kh)
def them(ds_kh):
    tenkhachhang=input("Nhap ten khach hang:")
    tenphong=input("Nhap ten phong :")
    loaiphong=input("Nhap loai phong:")
    giaphong=float(input("Nhap gia phong:"))
    kh=(tenkhachhang,tenphong,loaiphong,giaphong)
    ds_kh.append(kh)
    print("da them thanh cong")

   