from django.urls import path
from app.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', home),

   path('chonbaocao/', login_required(ChonBaoCao), name="chonBaoCao"),

   path('chonsinhvien/', login_required(ChonSinhVien), name="chonSinhVien"),
   path('thanhtoan/<int:id>/', login_required(ThanhToan), name='thanhToan'),

   path('listdanhmucthuchi/', login_required(ListDanhMucThuChi), name="listDanhMucThuChi"),
   path('danhmucthuchi/newdanhmucthuchi/', login_required(NewDanhMucThuChi), name='newDanhMucThuChi'),
   path('danhmucthuchi/<int:id>/update/', login_required(SuaDanhMucThuChi), name='suaDanhMucThuChi'),
   path('danhmucthuchi/<int:id>/delete/', login_required(XoaDanhMucThuChi), name='xoaDanhMucThuChi'),

   path('listKeHoachThu/', login_required(ListKeHoachThu), name="listKeHoachThu"),
   path('kehoachthu/<int:id>/detail/', login_required(XemKeHoachThu), name='xemKeHoachThu'),
   path('kehoachthu/newKeHoachThu/', login_required(NewKeHoachThu), name='newKeHoachThu'),
   path('kehoachthu/<int:id>/update/', login_required(SuaKeHoachThu), name='suaKeHoachThu'),
   path('kehoachthu/<int:id>/delete/', login_required(XoaKeHoachThu), name='xoaKeHoachThu'),

   path('listkhoanthuhocphi/', login_required(ListKhoanThuHocPhi), name="listKhoanThuHocPhi"),
   path('khoanthuhocphi/listsinhvien/<int:id>/', login_required(ListSinhVien), name="listSinhVien"),
   path('khoanthuhocphi/newkhoanthuhocphi/<int:id>/', login_required(NewKhoanThuHocPhi), name='newKhoanThuHocPhi'),
   path('khoanthuhocphi/addkhoanthuhocphi/<int:id>/', login_required(AddKhoanThuHocPhi), name='addKhoanThuHocPhi'),
   path('khoanthuhocphi/xemcackhoanthu/<int:id>/', login_required(XemCacKhoanThuCuaSV), name='xemCacKhoanThuSV'),
   path('khoanthuhocphi/<int:id>/detail/', login_required(XemKhoanThuHocPhi), name='xemKhoanThuHocPhi'),
   path('khoanthuhocphi/<int:id>/delete/', login_required(XoaKhoanThuHocPhi), name='xoaKhoanThuHocPhi'),
   path('khoanthuhocphi/<int:id>/update/', login_required(SuaKhoanThuHocPhi), name='suaKhoanThuHocPhi'),

   path('listKhoanThuNhapHoc/', login_required(ListKhoanThuNhapHoc), name="listKhoanThuNhapHoc"),
   path('khoanthunhaphoc/newKhoanThuNhapHoc/', login_required(NewKhoanThuNhapHoc), name='newKhoanThuNhapHoc'),
   path('khoanthunhaphoc/<int:id>/update/', login_required(SuaKhoanThuNhapHoc), name='suaKhoanThuNhapHoc'),
   path('khoanthunhaphoc/<int:id>/delete/', login_required(XoaKhoanThuNhapHoc), name='xoaKhoanThuNhapHoc'),

   path('login/', login_page, name='login'),
   path('logout/', logout_view, name='logout'),

   path('listmuchocphi/', login_required(ListMucHocPhi), name="listMucHocPhi"),
   path('muchocphi/newmuchocphi/', login_required(NewMucHocPhi), name='newMucHocPhi'),
   path('muchocphi/<int:id>/update/', login_required(SuaMucHocPhi), name='suaMucHocPhi'),
   path('muchocphi/<int:id>/delete/', login_required(XoaMucHocPhi), name='xoaMucHocPhi'),


   path('pay', index, name='index'),
   path('payment', payment, name='payment'),
   path('payment_ipn', payment_ipn, name='payment_ipn'),
   path('payment_return', payment_return, name='payment_return'),
   path('query', query, name='query'),
   path('refund', refund, name='refund'),

]