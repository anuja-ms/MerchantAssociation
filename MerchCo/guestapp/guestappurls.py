from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.login,name="login"),
    path('loginprocess/',views.loginprocess,name="loginprocess"),
    path('',views.index,name="index2"),
    path('register/',views.register,name="register"),
    path('register_process/',views.register_process,name="register_process"),
    path('registerfeepayment/<member_id>',views.registerfeepayment,name="registerfeepayment"),
]