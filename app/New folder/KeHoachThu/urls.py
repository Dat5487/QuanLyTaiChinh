from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ListKeHoachThu)),
   path('listKeHoachThu', login_required(views.ListKeHoachThu), name="listKeHoachThu"),
   path('listKeHoachThu/', login_required(views.ListKeHoachThu), name="listKeHoachThu"),
   path('<int:id>/detail/', login_required(views.XemKeHoachThu), name='xemKeHoachThu'),
   path('newKeHoachThu/', login_required(views.NewKeHoachThu), name='newKeHoachThu'),
   path('<int:id>/update/', login_required(views.SuaKeHoachThu), name='suaKeHoachThu'),
   path('<int:id>/delete/', login_required(views.XoaKeHoachThu), name='xoaKeHoachThu'),
]