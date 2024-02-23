from .models import ThietLapMucHocPhi
from django import forms

class ThietLapMucHocPhiForm(forms.ModelForm):
    class Meta:
        model = ThietLapMucHocPhi
        fields = ['heDaoTao', 'namHoc', 'tenNganh','khoa','lop','hocKy','isNganhHai','isHocLai','isMienGiam','isMonGDTC','isChatLuongCao','tinhChat','heSo','soTien']