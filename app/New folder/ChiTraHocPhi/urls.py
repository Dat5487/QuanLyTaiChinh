from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ChonSinhVien)),
   path('chonsinhvien', login_required(views.ChonSinhVien), name="chonSinhVien"),
   path('thanhtoan/<int:id>/', login_required(views.ThanhToan), name='thanhToan'),
]