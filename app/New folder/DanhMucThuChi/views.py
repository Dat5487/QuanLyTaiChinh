from django.shortcuts import render, redirect
from django.urls import reverse
from .models import DanhMucThuChi
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import DanhMucThuChiForm
from django.contrib.auth.decorators import login_required

@login_required
def ListDanhMucThuChi(request):
   alertContent = request.GET.get('alertContent')
   ListDanhMucThuChi = DanhMucThuChi.objects.all().order_by('-ngayThem')
   return render(request, 'listDanhMucThuChi.html', {'ListDanhMucThuChi': ListDanhMucThuChi, 'alertContent': alertContent})

@login_required
def NewDanhMucThuChi(request):
    if request.method == 'POST':
        form = DanhMucThuChiForm(request.POST)
        data_copy = request.POST.copy()
        loaiKhoan = request.POST.get('loaiKhoan')
        print(loaiKhoan)
        if(int(loaiKhoan) == 1):
            data_copy['isKhoanThu'] = True
            data_copy['isKhoanChi'] = False
        else:
            data_copy['isKhoanThu'] = False
            data_copy['isKhoanChi']  = True 
        data_copy['isKhoanThuNhapHoc'] = request.POST.get('isKhoanThuNhapHoc') 
        data_copy['isHocPhi'] = request.POST.get('isHocPhi') 
        data_copy['isThuTrucTuyen'] = request.POST.get('isThuTrucTuyen') 
        form.data = data_copy
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('listDanhMucThuChi') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = DanhMucThuChiForm()
    return render(request, 'newDanhMucThuChi.html', {'form': form})

@login_required
def SuaDanhMucThuChi(request, id):
    danhMucThuChi = get_object_or_404(DanhMucThuChi, id=id)
    
    if request.method == 'POST':
        danhMucThuChi.tenKhoan = request.POST.get('tenKhoan')
        loaiKhoan = request.POST.get('loaiKhoan')
        if(int(loaiKhoan) == 1):
            danhMucThuChi.isKhoanThu = 1
            danhMucThuChi.isKhoanChi = 0
        else:
            danhMucThuChi.isKhoanThu = 0
            danhMucThuChi.isKhoanChi = 1

        danhMucThuChi.isKhoanThuNhapHoc = request.POST.get('isKhoanThuNhapHoc')
        danhMucThuChi.isHocPhi = request.POST.get('isHocPhi')
        danhMucThuChi.isThuTrucTuyen = request.POST.get('isThuTrucTuyen')
        danhMucThuChi.save()

        alert_content = 'Sửa'
        url = reverse('listDanhMucThuChi') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        danhMucThuChi = DanhMucThuChi.objects.get(id=id)
        form = DanhMucThuChiForm()

    return render(request, 'suaDanhMucThuChi.html', {'form': form,'danhMucThuChi': danhMucThuChi})

@login_required
def XoaDanhMucThuChi(request, id):
    danhMucThuChi = get_object_or_404(DanhMucThuChi, id=id)

    if request.method == 'POST':
        danhMucThuChi.delete()
        alert_content = 'Xóa'
        url = reverse('listDanhMucThuChi') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaDanhMucThuChi.html', {'danhMucThuChi': danhMucThuChi})