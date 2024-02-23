from .models import ChiTraHocPhi
from django import forms

class ChiTraHocPhiForm(forms.ModelForm):
    class Meta:
        model = ChiTraHocPhi
        fields = ['sinhVien', 'khoanThuHocPhi', 'soPhieu','noiDungChi','ghiChu','soTienDaNop']