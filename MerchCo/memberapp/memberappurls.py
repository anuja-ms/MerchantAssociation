from django.urls import path
from . import views
urlpatterns=[
    
    path('index/',views.index,name="index1"),
    path('deposite/',views.deposite,name="deposite"),
    
    path('loanreq/',views.loanreq,name="loanreq"),
    path('deposite_process/',views.deposite_process,name="deposite_process"),
    path('loanreq_process/',views.loanreq_process,name="loanreq_process"),
    path('welfareview/',views.welfareview,name="welfareview"),
    path('welfarepayment/<id>',views.welfarepayment,name="welfarepayment"),
    path('payment_process',views.payment_process,name="payment_process"),
    path('notificationview/',views.notificationview,name="notificationview"),
    path('viewloanreq/',views.viewloanreq,name="viewloanreq"),
    path('loantransaction/<id>', views.loantransaction, name="loantransaction"),
    path('loanpayment_process/', views.loanpayment_process, name="loanpayment_process"),
    path('loanpayment/<id>',views.loanpayment,name="loanpayment"),
    path('viewpayments/',views.viewpayments,name="viewpayments"),
    path('profile/',views.profile,name="profile"),
    path('edit_member/<member_id>',views.edit_member,name="edit_member"),
    path('fillunit',views.fillunit,name="fillunit"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
]