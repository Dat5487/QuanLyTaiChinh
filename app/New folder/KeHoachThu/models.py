from django.db import models
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from DanhMucThuChi.models import DanhMucThuChi
from datetime import date

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
