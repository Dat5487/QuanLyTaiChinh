from django.shortcuts import render, redirect
from django.urls import reverse
from .models import KeHoachThu
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import KeHoachThuForm
from django.contrib.auth.decorators import login_required
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from DanhMucThuChi.models import DanhMucThuChi

@login_required
def ListKeHoachThu(request):
   alertContent = request.GET.get('alertContent')
   listKeHoachThu = KeHoachThu.objects.all().order_by('-id')
   return render(request, 'listKeHoachThu.html', {'listKeHoachThu': listKeHoachThu, 'alertContent': alertContent})

@login_required
def NewKeHoachThu(request):
    cacKhoaHoc = KhoaHoc.objects.all().order_by('-id')
    cacNganhDaoTao = NganhDaoTao.objects.all().order_by('-id')
    cacKhoanThu = DanhMucThuChi.objects.filter(isKhoanThu = True).order_by('-id')
    cacHeDaoTao = HeDaoTao.objects.all().order_by('-id')
    if request.method == 'POST':
        form = KeHoachThuForm(request.POST)
        data_copy = request.POST.copy()
        data_copy['soTien'] = data_copy['soTien'].replace(",", "") 
        form.data = data_copy
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('listKeHoachThu') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = KeHoachThuForm()
    return render(request, 'newKeHoachThu.html', {'form': form, 'cacHeDaoTao': cacHeDaoTao, 'cacKhoanThu': cacKhoanThu,'cacKhoaHoc': cacKhoaHoc,'cacNganhDaoTao': cacNganhDaoTao})

@login_required
def SuaKeHoachThu(request, id):

    keHoachThu = get_object_or_404(KeHoachThu, id=id)
    cacKhoaHoc = KhoaHoc.objects.all().order_by('-id')
    cacNganhDaoTao = NganhDaoTao.objects.all().order_by('-id')
    cacKhoanThu = DanhMucThuChi.objects.filter(isKhoanThu = True).order_by('-id')
    cacHeDaoTao = HeDaoTao.objects.all().order_by('-id')
    if request.method == 'POST':
        keHoachThu.khoaHoc =  get_object_or_404(KhoaHoc, id=request.POST.get('khoaHoc'))
        keHoachThu.khoanThu = get_object_or_404(DanhMucThuChi, id=request.POST.get('khoanThu'))
        keHoachThu.nganhDaoTao = get_object_or_404(NganhDaoTao, id=request.POST.get('nganhDaoTao'))
        keHoachThu.soTien = request.POST.get('soTien').replace(",", "")
        keHoachThu.dotThu = request.POST.get('dotThu')
        keHoachThu.ngayBatDau = request.POST.get('ngayBatDau')
        keHoachThu.ngayKetThuc = request.POST.get('ngayKetThuc')
        keHoachThu.noiDung = request.POST.get('noiDung')
        keHoachThu.save()
        alert_content = 'Sửa'
        url = reverse('listKeHoachThu') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        keHoachThu = KeHoachThu.objects.get(id=id)
        form = KeHoachThuForm()


    return render(request, 'suaKeHoachThu.html', {'form': form,'keHoachThu': keHoachThu,'cacHeDaoTao': cacHeDaoTao,'cacKhoaHoc': cacKhoaHoc,'cacNganhDaoTao': cacNganhDaoTao,'cacKhoanThu': cacKhoanThu})

@login_required
def XoaKeHoachThu(request, id):
    keHoachThu = get_object_or_404(KeHoachThu, id=id)
    soTien = format(keHoachThu.soTien, ",.0f")
    if request.method == 'POST':
        keHoachThu.delete()
        alert_content = 'Xóa'
        url = reverse('listKeHoachThu') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaKeHoachThu.html', {'keHoachThu': keHoachThu, 'soTien': soTien})

@login_required
def XemKeHoachThu(request, id):
    keHoachThu = get_object_or_404(KeHoachThu, id=id)
    soTien = format(keHoachThu.soTien, ",.0f")
    return render(request, 'xemKeHoachThu.html', {'keHoachThu': keHoachThu, 'soTien': soTien})