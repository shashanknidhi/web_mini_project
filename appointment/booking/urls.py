from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.book,name='book'), 
    path('login/',views.login,name='login'),
    path('login/auth_admin/',views.auth_admin, name='auth_admin')
]