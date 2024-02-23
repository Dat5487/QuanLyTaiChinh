from .models import DanhMucThuChi
from django import forms

class DanhMucThuChiForm(forms.ModelForm):
    class Meta:
        model = DanhMucThuChi
        fields = ['tenKhoan', 'isKhoanThu', 'isKhoanChi','isKhoanThuNhapHoc','isHocPhi','isThuTrucTuyen']