from django.db import models


class HeDaoTao(models.Model):
    tenHeDaoTao = models.CharField(max_length=100)

# Khóa nhập học
class KhoaHoc(models.Model):
    namKhoaHoc = models.CharField(max_length=100)

# Năm học
class NamHoc(models.Model):
    namHoc = models.CharField(max_length=100)

class Khoa(models.Model):
    tenKhoa = models.CharField(max_length=100)
    
class NganhDaoTao(models.Model):
    khoa = models.ForeignKey(Khoa, on_delete = models.CASCADE)
    heDaoTao = models.ForeignKey(HeDaoTao, on_delete = models.CASCADE)
    tenNganhDaoTao = models.CharField(max_length=100)

class Lop(models.Model):
    heDaoTao = models.ForeignKey(HeDaoTao, on_delete = models.CASCADE)
    nganhDaoTao = models.ForeignKey(NganhDaoTao, on_delete = models.CASCADE)
    khoaHoc = models.ForeignKey(KhoaHoc, on_delete = models.CASCADE)
    khoa = models.ForeignKey(Khoa, on_delete = models.CASCADE)
    lop = models.CharField(max_length=100)
    
class SinhVien(models.Model):
    maSV = models.CharField(max_length=10)
    hoTen = models.CharField(max_length=100)
    ngaySinh = models.DateField(blank=True, null=True)
    queQuan = models.CharField(max_length=100)
    lop = models.ForeignKey(Lop, on_delete = models.CASCADE)
    trangThai = models.BooleanField(blank=True)

class DanhMucThuChi(models.Model):
    tenKhoan = models.CharField(max_length=100)
    isKhoanThu = models.BooleanField(blank=True)
    isKhoanChi = models.BooleanField(blank=True)
    isKhoanThuNhapHoc = models.BooleanField(blank=True)
    isHocPhi = models.BooleanField(blank=True)
    isThuTrucTuyen = models.BooleanField(blank=True)
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class ThietLapMucHocPhi(models.Model):
    heDaoTao = models.CharField(max_length=100)
    namHoc = models.CharField(max_length=100)
    tenNganh = models.CharField(max_length=100)
    khoa = models.CharField(max_length=100)
    lop = models.CharField(max_length=100)
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    isNganhHai = models.BooleanField(blank=True)
    isHocLai = models.BooleanField(blank=True)
    isMonGDTC = models.BooleanField(blank=True)
    isChatLuongCao = models.BooleanField(blank=True)
    isMienGiam = models.BooleanField(blank=True)
    hocKy = models.BooleanField(blank=True)
    tinhChat = models.CharField(max_length=100)
    heSo = models.IntegerField(blank=True)
    soTien = models.BigIntegerField(blank=True)
    
class KeHoachThu(models.Model):
    khoaHoc = models.ForeignKey(KhoaHoc, on_delete = models.CASCADE)
    dotThu = models.IntegerField()
    nganhDaoTao = models.ForeignKey(NganhDaoTao, on_delete = models.CASCADE)
    khoanThu = models.ForeignKey(DanhMucThuChi, on_delete = models.CASCADE)
    trangThai = models.BooleanField(blank=True, null=True)
    soTien = models.BigIntegerField()
    ngayBatDau = models.DateField(blank=True, null=True)
    ngayKetThuc = models.DateField(blank=True, null=True)
    noiDung = models.TextField()

class KhoanThuNhapHoc(models.Model):
    dotNhapHoc = models.IntegerField()
    khoaHoc = models.ForeignKey(KhoaHoc, on_delete = models.CASCADE)
    khoanThu = models.ForeignKey(DanhMucThuChi, on_delete = models.CASCADE)
    nganhDaoTao = models.ForeignKey(NganhDaoTao, on_delete = models.CASCADE)
    soTien = models.BigIntegerField()


    
class KhoanThuHocPhi(models.Model):
    sinhVien = models.ForeignKey(SinhVien, on_delete = models.CASCADE)
    mucHocPhi = models.ForeignKey(ThietLapMucHocPhi, on_delete = models.CASCADE)
    hanNop = models.DateField(blank=True, null=True)
    noiDungThu = models.CharField(max_length=100,blank=True, null=True)
    ghiChu = models.CharField(max_length=100,blank=True, null=True)
    maSoThue = models.CharField(max_length=10)
    soTienMienGiam = models.BigIntegerField()
    soTien = models.BigIntegerField()
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    trangThai = models.BooleanField(blank=True)

class ChiTraHocPhi(models.Model):
    sinhVien = models.ForeignKey(SinhVien, on_delete = models.CASCADE)
    khoanThuHocPhi = models.OneToOneField(KhoanThuHocPhi, on_delete=models.CASCADE)
    soPhieu = models.CharField(max_length=100,blank=True, null=True)
    noiDungChi = models.CharField(max_length=100,blank=True, null=True)
    ghiChu = models.CharField(max_length=100,blank=True, null=True)
    soTienDaNop = models.BigIntegerField()
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Payment_VNPay(models.Model):
    order_id = models.IntegerField(default=0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    order_desc = models.CharField(max_length=200,null=True, blank=True)
    vnp_TransactionNo = models.CharField(max_length=200,null=True, blank=True)
    vnp_ResponseCode = models.CharField(max_length=200,null=True, blank=True)