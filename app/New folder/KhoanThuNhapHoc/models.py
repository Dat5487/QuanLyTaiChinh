from django.db import models
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from DanhMucThuChi.models import DanhMucThuChi

class KhoanThuNhapHoc(models.Model):
    dotNhapHoc = models.IntegerField()
    khoaHoc = models.ForeignKey(KhoaHoc, on_delete = models.CASCADE)
    khoanThu = models.ForeignKey(DanhMucThuChi, on_delete = models.CASCADE)
    nganhDaoTao = models.ForeignKey(NganhDaoTao, on_delete = models.CASCADE)
    soTien = models.BigIntegerField()

