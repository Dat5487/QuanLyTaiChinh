from django.db import models
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from ThietLapMucHocPhi.models import ThietLapMucHocPhi
from ThongTin.models import SinhVien

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