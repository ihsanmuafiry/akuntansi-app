
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('tambahcabang/', views.addBranch, name='addBranch'),
    path('cabang/<str:pk>/', views.branch, name='branch'),

    path('akun/', views.account, name='account'),
    path('tambahakun/', views.addAccount, name='addAccount'),
    path('ubahakun/<str:pk>/', views.updateAccount.as_view(), name='updateAccount'),
    path('hapusakun/<str:pk>/', views.deleteAccount.as_view(), name='deleteAccount'),

    path('tambahjurnal/<str:pk>/', views.addTrans, name='addTrans'),
    path('ubahjurnal/<str:pk>/', views.updateTrans.as_view(), name='updateTrans'),
    path('hapusjurnal/<str:pk>/', views.deleteTrans.as_view(), name='deleteTrans'),

]
