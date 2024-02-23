from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ListDanhMucThuChi)),
   path('listdanhmucthuchi', login_required(views.ListDanhMucThuChi), name="listDanhMucThuChi"),
   path('listdanhmucthuchi/', login_required(views.ListDanhMucThuChi), name="listDanhMucThuChi"),
   path('newdanhmucthuchi/', login_required(views.NewDanhMucThuChi), name='newDanhMucThuChi'),
   path('<int:id>/update/', login_required(views.SuaDanhMucThuChi), name='suaDanhMucThuChi'),
   path('<int:id>/delete/', login_required(views.XoaDanhMucThuChi), name='xoaDanhMucThuChi'),
]