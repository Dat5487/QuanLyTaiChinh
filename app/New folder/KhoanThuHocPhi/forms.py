from .models import KhoanThuHocPhi
from django import forms

class KhoanThuHocPhiForm(forms.ModelForm):
    class Meta:
        model = KhoanThuHocPhi
        fields = ["sinhVien","mucHocPhi","hanNop","noiDungThu","ghiChu","maSoThue","soTienMienGiam","soTien"]

class BatchKhoanThuHocPhiForm(forms.ModelForm):
    class Meta:
        model = KhoanThuHocPhi
        fields = ["mucHocPhi","hanNop","noiDungThu","ghiChu","maSoThue","soTienMienGiam","soTien"] 