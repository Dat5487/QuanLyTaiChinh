from app.models import *
from django import forms

class ChiTraHocPhiForm(forms.ModelForm):
    class Meta:
        model = ChiTraHocPhi
        fields = ['sinhVien', 'khoanThuHocPhi', 'soPhieu','noiDungChi','ghiChu','soTienDaNop']

class DanhMucThuChiForm(forms.ModelForm):
    class Meta:
        model = DanhMucThuChi
        fields = ['tenKhoan', 'isKhoanThu', 'isKhoanChi','isKhoanThuNhapHoc','isHocPhi','isThuTrucTuyen']

class KeHoachThuForm(forms.ModelForm):
    class Meta:
        model = KeHoachThu
        fields = ['khoaHoc', 'dotThu','khoanThu','nganhDaoTao','soTien','ngayBatDau','ngayKetThuc','noiDung']

class KhoanThuHocPhiForm(forms.ModelForm):
    class Meta:
        model = KhoanThuHocPhi
        fields = ["sinhVien","mucHocPhi","hanNop","noiDungThu","ghiChu","maSoThue","soTienMienGiam","soTien"]

class BatchKhoanThuHocPhiForm(forms.ModelForm):
    class Meta:
        model = KhoanThuHocPhi
        fields = ["mucHocPhi","hanNop","noiDungThu","ghiChu","maSoThue","soTienMienGiam","soTien"] 

class KhoanThuNhapHocForm(forms.ModelForm):
    class Meta:
        model = KhoanThuNhapHoc
        fields = ['khoaHoc', 'dotNhapHoc','khoanThu','nganhDaoTao','soTien']

class ThietLapMucHocPhiForm(forms.ModelForm):
    class Meta:
        model = ThietLapMucHocPhi
        fields = ['heDaoTao', 'namHoc', 'tenNganh','khoa','lop','hocKy','isNganhHai','isHocLai','isMienGiam','isMonGDTC','isChatLuongCao','heSo','soTien']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']

class PaymentForm(forms.Form):
    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)