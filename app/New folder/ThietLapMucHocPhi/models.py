from django.db import models

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
