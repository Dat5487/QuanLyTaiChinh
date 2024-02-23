from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ListKhoanThuHocPhi)),
   path('listkhoanthuhocphi', login_required(views.ListKhoanThuHocPhi), name="listKhoanThuHocPhi"),
   path('listkhoanthuhocphi/', login_required(views.ListKhoanThuHocPhi), name="listKhoanThuHocPhi"),
   path('listsinhvien/<int:id>/', login_required(views.ListSinhVien), name="listSinhVien"),
   path('listsinhvien/<int:id>', login_required(views.ListSinhVien), name="listSinhVien"),
   path('newkhoanthuhocphi/<int:id>/', login_required(views.NewKhoanThuHocPhi), name='newKhoanThuHocPhi'),
   path('addkhoanthuhocphi/<int:id>/', login_required(views.AddKhoanThuHocPhi), name='addKhoanThuHocPhi'),

   path('xemcackhoanthu/<int:id>/', login_required(views.XemCacKhoanThuCuaSV), name='xemCacKhoanThuSV'),
   path('<int:id>/detail/', login_required(views.XemKhoanThuHocPhi), name='xemKhoanThuHocPhi'),
   path('<int:id>/delete/', login_required(views.XoaKhoanThuHocPhi), name='xoaKhoanThuHocPhi'),
   path('<int:id>/update/', login_required(views.SuaKhoanThuHocPhi), name='suaKhoanThuHocPhi'),

]