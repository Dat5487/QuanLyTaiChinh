from .models import KhoanThuNhapHoc
from django import forms

class KhoanThuNhapHocForm(forms.ModelForm):
    class Meta:
        model = KhoanThuNhapHoc
        fields = ['khoaHoc', 'dotNhapHoc','khoanThu','nganhDaoTao','soTien']

        