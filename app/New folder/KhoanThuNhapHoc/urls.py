from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ListKhoanThuNhapHoc)),
   path('listKhoanThuNhapHoc', login_required(views.ListKhoanThuNhapHoc), name="listKhoanThuNhapHoc"),
   path('listKhoanThuNhapHoc/', login_required(views.ListKhoanThuNhapHoc), name="listKhoanThuNhapHoc"),
   path('newKhoanThuNhapHoc/', login_required(views.NewKhoanThuNhapHoc), name='newKhoanThuNhapHoc'),
   path('<int:id>/update/', login_required(views.SuaKhoanThuNhapHoc), name='suaKhoanThuNhapHoc'),
   path('<int:id>/delete/', login_required(views.XoaKhoanThuNhapHoc), name='xoaKhoanThuNhapHoc'),
]