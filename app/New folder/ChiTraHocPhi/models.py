from django.db import models
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from KhoanThuHocPhi.models import KhoanThuHocPhi


from ThongTin.models import SinhVien

class ChiTraHocPhi(models.Model):
    sinhVien = models.ForeignKey(SinhVien, on_delete = models.CASCADE)
    khoanThuHocPhi = models.OneToOneField(KhoanThuHocPhi, on_delete=models.CASCADE)
    soPhieu = models.CharField(max_length=100,blank=True, null=True)
    noiDungChi = models.CharField(max_length=100,blank=True, null=True)
    ghiChu = models.CharField(max_length=100,blank=True, null=True)
    soTienDaNop = models.BigIntegerField()
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)