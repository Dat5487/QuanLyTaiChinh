from django.shortcuts import render, redirect
from django.urls import reverse
from .models import KhoanThuNhapHoc
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import KhoanThuNhapHocForm
from django.contrib.auth.decorators import login_required
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop
from DanhMucThuChi.models import DanhMucThuChi

@login_required
def ListKhoanThuNhapHoc(request):
   alertContent = request.GET.get('alertContent')
   listKhoanThuNhapHoc = KhoanThuNhapHoc.objects.all().order_by('-id')
   return render(request, 'listKhoanThuNhapHoc.html', {'listKhoanThuNhapHoc': listKhoanThuNhapHoc, 'alertContent': alertContent})


@login_required
def NewKhoanThuNhapHoc(request):
    cacKhoaHoc = KhoaHoc.objects.all().order_by('-id')
    cacTenNganh = NganhDaoTao.objects.all().order_by('-id')
    cacKhoanThu = DanhMucThuChi.objects.filter(isKhoanThuNhapHoc = True).order_by('-id')
    if request.method == 'POST':
        form = KhoanThuNhapHocForm(request.POST)
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('listKhoanThuNhapHoc') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = KhoanThuNhapHocForm()
    return render(request, 'newKhoanThuNhapHoc.html', {'form': form, 'cacKhoaHoc': cacKhoaHoc,'cacTenNganh': cacTenNganh,'cacKhoanThu': cacKhoanThu})


@login_required
def SuaKhoanThuNhapHoc(request, id):
    khoanThuNhaphoc = get_object_or_404(KhoanThuNhapHoc, id=id)
    cacKhoaHoc = KhoaHoc.objects.all().order_by('-id')
    cacTenNganh = NganhDaoTao.objects.all().order_by('-id')
    cacKhoanThu = DanhMucThuChi.objects.filter(isKhoanThuNhapHoc = True).order_by('-id')
    if request.method == 'POST':
        khoanThuNhaphoc.khoaHoc =  get_object_or_404(KhoaHoc, id=request.POST.get('khoaHoc'))
        khoanThuNhaphoc.dotNhapHoc = request.POST.get('dotNhapHoc')
        khoanThuNhaphoc.khoanThu = get_object_or_404(DanhMucThuChi, id=request.POST.get('khoanThu'))
        khoanThuNhaphoc.nganhDaoTao = get_object_or_404(NganhDaoTao, id=request.POST.get('nganhDaoTao'))
        khoanThuNhaphoc.soTien = request.POST.get('soTien')
        khoanThuNhaphoc.save()
        alert_content = 'Sửa'
        url = reverse('listKhoanThuNhapHoc') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        khoanThuNhapHoc = KhoanThuNhapHoc.objects.get(id=id)
        form = KhoanThuNhapHocForm()


    return render(request, 'suaKhoanThuNhaphoc.html', {'form': form,'khoanThuNhapHoc': khoanThuNhapHoc,'cacKhoaHoc': cacKhoaHoc,'cacTenNganh': cacTenNganh,'cacKhoanThu': cacKhoanThu})

@login_required
def XoaKhoanThuNhapHoc(request, id):
    khoanThuNhapHoc = get_object_or_404(KhoanThuNhapHoc, id=id)

    if request.method == 'POST':
        khoanThuNhapHoc.delete()
        alert_content = 'Xóa'
        url = reverse('listKhoanThuNhapHoc') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaKhoanThuNhaphoc.html', {'khoanThuNhapHoc': khoanThuNhapHoc})