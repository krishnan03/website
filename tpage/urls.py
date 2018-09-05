from django.conf.urls import url
from . import views
from django.urls import path

app_name='tpage'

urlpatterns = [
    path('', views.index, name='transactionPage'),
    #tpage/checkUserDetails
    path('', views.verifyuser, name='verifyUser'),

    path('addItem/', views.addToCart, name='addToCart'),
    path('closeTransaction/', views.closeTransaction, name='closeTransaction'),
]