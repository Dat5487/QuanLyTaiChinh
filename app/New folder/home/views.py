from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ThongTin.models import HeDaoTao, NganhDaoTao, Khoa, KhoaHoc, Lop, NamHoc
from ThongTin.models import SinhVien
from KhoanThuHocPhi.models import KhoanThuHocPhi
from ThietLapMucHocPhi.models import ThietLapMucHocPhi
from django.db.models import Sum

@login_required
def home(request):
    soLuongChuaNop = KhoanThuHocPhi.objects.filter(trangThai=0).count()
    soLuongDaNop = KhoanThuHocPhi.objects.filter(trangThai=1).count()
    soTienChuaNop = KhoanThuHocPhi.objects.filter(trangThai=0).aggregate(Sum('soTien'))['soTien__sum']
    soTienDaNop = KhoanThuHocPhi.objects.filter(trangThai=1).aggregate(Sum('soTien'))['soTien__sum']
    return render(request, 'home.html', {'soLuongChuaNop': soLuongChuaNop,'soLuongDaNop': soLuongDaNop,'soTienChuaNop': soTienChuaNop,'soTienDaNop': soTienDaNop })

