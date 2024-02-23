from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ChiTraHocPhiForm
from django.contrib.auth.decorators import login_required
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from ThongTin.models import SinhVien
from KhoanThuHocPhi.models import KhoanThuHocPhi
from ThietLapMucHocPhi.models import ThietLapMucHocPhi

# Create your views here.
@login_required
def ChonSinhVien(request):
    listSinhVien = SinhVien.objects.all()
    if request.method == 'POST':
            maSV = request.POST.get('sinhVien')
            return redirect('thanhToan', maSV)
    else:
        return render(request, 'chonSinhVien.html', {'listSinhVien': listSinhVien})

@login_required
def ThanhToan(request,id):
    sinhVien = get_object_or_404(SinhVien, id=id)
    listKhoanThuHocPhi = KhoanThuHocPhi.objects.filter(sinhVien = sinhVien).order_by('-id')
    if request.method == 'POST':
        form = ChiTraHocPhiForm(request.POST)
        data_copy = request.POST.copy()
        data_copy['soTienDaNop'] = data_copy['soTienDaNop'].replace(",", "") 
        form.data = data_copy

        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('listSinhVien', args=[id]) + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = ChiTraHocPhiForm()
    return render(request, 'thanhToan.html', {'form': form, 'listKhoanThuHocPhi': listKhoanThuHocPhi, 'sinhVien': sinhVien, 'idSV': id})

