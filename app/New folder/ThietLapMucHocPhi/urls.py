from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(views.ListMucHocPhi)),
   path('index', login_required(views.ListMucHocPhi), name="index"),
   path('index/', login_required(views.ListMucHocPhi), name="index"),
   path('newmuchocphi/', login_required(views.NewMucHocPhi), name='newMucHocPhi'),
   path('<int:id>/update/', login_required(views.SuaMucHocPhi), name='suaMucHocPhi'),
   path('<int:id>/delete/', login_required(views.XoaMucHocPhi), name='xoaMucHocPhi'),
]