from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ThietLapMucHocPhi
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ThietLapMucHocPhiForm
from django.contrib.auth.decorators import login_required
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop, NamHoc

@login_required
def ListMucHocPhi(request):
   alertContent = request.GET.get('alertContent')
   ListMucHocPhi = ThietLapMucHocPhi.objects.all().order_by('-ngayThem')
   return render(request, 'index.html', {'ListMucHocPhi': ListMucHocPhi, 'alertContent': alertContent})

@login_required
def NewMucHocPhi(request):
    cacHeDaoTao = HeDaoTao.objects.all().order_by('-id')
    cacNamHoc = NamHoc.objects.all().order_by('-id')
    cacNganhDaoTao = NganhDaoTao.objects.all().order_by('-id')
    cacKhoa= Khoa.objects.all().order_by('-id')
    cacLop = Lop.objects.all().order_by('-id')
    if request.method == 'POST':
        form = ThietLapMucHocPhiForm(request.POST)
        data_copy = request.POST.copy()
        data_copy['soTien'] = data_copy['soTien'].replace(",", "") 
        data_copy['isNganhHai'] = request.POST.get('isNganhHai')
        data_copy['isHocLai'] = request.POST.get('isHocLai')
        data_copy['isMienGiam'] = request.POST.get('isMienGiam')
        form.data = data_copy
        if form.is_valid():
            form.save()
            alert_content = 'Thêm'
            url = reverse('index') + f'?alertContent={alert_content}'
            return redirect(url)
    else:
        form = ThietLapMucHocPhiForm()
    return render(request, 'newMucHocPhi.html', {'form': form, 'cacHeDaoTao': cacHeDaoTao,'cacNganhDaoTao': cacNganhDaoTao,'cacKhoa': cacKhoa,'cacLop': cacLop,'cacNamHoc': cacNamHoc})

@login_required
def SuaMucHocPhi(request, id):
    mucHocPhi = get_object_or_404(ThietLapMucHocPhi, id=id)
    soTien = format(mucHocPhi.soTien, ",.0f")

    if request.method == 'POST':
        mucHocPhi.heDaoTao = request.POST.get('heDaoTao')
        mucHocPhi.namHoc = request.POST.get('namHoc')
        mucHocPhi.tenNganh = request.POST.get('tenNganh')
        mucHocPhi.khoa = request.POST.get('khoa')
        mucHocPhi.lop = request.POST.get('lop')
        mucHocPhi.hocKy = request.POST.get('hocKy')
        mucHocPhi.isNganhHai = request.POST.get('isNganhHai')
        mucHocPhi.isHocLai = request.POST.get('isHocLai')
        mucHocPhi.isMienGiam = request.POST.get('isMienGiam')
        mucHocPhi.isChatLuongCao = request.POST.get('isChatLuongCao')
        mucHocPhi.isMonGDTC = request.POST.get('isMonGDTC')
        mucHocPhi.tinhChat = request.POST.get('tinhChat')
        mucHocPhi.heSo = request.POST.get('heSo')
        mucHocPhi.soTien = request.POST.get('soTien').replace(",", "")

        mucHocPhi.save()
        alert_content = 'Sửa'
        url = reverse('index') + f'?alertContent={alert_content}'
        return redirect(url)
    else:
        mucHocPhi = ThietLapMucHocPhi.objects.get(id=id)
        form = ThietLapMucHocPhiForm()

    cacHeDaoTao = HeDaoTao.objects.all().order_by('-id')
    cacNamHoc = NamHoc.objects.all().order_by('-id')
    cacNganhDaoTao = NganhDaoTao.objects.all().order_by('-id')
    cacKhoa= Khoa.objects.all().order_by('-id')
    cacLop = Lop.objects.all().order_by('-id')
    return render(request, 'suaMucHocPhi.html', {'form': form,'mucHocPhi': mucHocPhi, 'cacHeDaoTao': cacHeDaoTao,'cacNamHoc': cacNamHoc,'cacNganhDaoTao': cacNganhDaoTao,'cacKhoa': cacKhoa,'cacLop': cacLop,'soTien': soTien})

@login_required
def XoaMucHocPhi(request, id):
    mucHocPhi = get_object_or_404(ThietLapMucHocPhi, id=id)
    soTien = format(mucHocPhi.soTien, ",.0f")
    if request.method == 'POST':
        mucHocPhi.delete()
        alert_content = 'Xóa'
        url = reverse('index') + f'?alertContent={alert_content}'
        return redirect(url)

    return render(request, 'xoaMucHocPhi.html', {'mucHocPhi': mucHocPhi,'soTien': soTien})