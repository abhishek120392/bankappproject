from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^banks_in_city/', views.bankInCity, name='bankInCity'),
    url(r'^bank_details/', views.bankdetails, name='bankdetails'),
]