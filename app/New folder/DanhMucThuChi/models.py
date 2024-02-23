from django.db import models

class DanhMucThuChi(models.Model):
    tenKhoan = models.CharField(max_length=100)
    isKhoanThu = models.BooleanField(blank=True)
    isKhoanChi = models.BooleanField(blank=True)
    isKhoanThuNhapHoc = models.BooleanField(blank=True)
    isHocPhi = models.BooleanField(blank=True)
    isThuTrucTuyen = models.BooleanField(blank=True)
    ngayThem = models.DateTimeField(auto_now_add=True, blank=True, null=True)
