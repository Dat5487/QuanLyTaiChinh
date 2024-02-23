from django.urls import path
from . import views
from .views import logout_view
urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', logout_view, name='logout'),
]