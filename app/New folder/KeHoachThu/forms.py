from .models import KeHoachThu
from django import forms

class KeHoachThuForm(forms.ModelForm):
    class Meta:
        model = KeHoachThu
        fields = ['khoaHoc', 'dotThu','khoanThu','nganhDaoTao','soTien','ngayBatDau','ngayKetThuc','noiDung']

