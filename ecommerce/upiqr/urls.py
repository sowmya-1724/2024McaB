from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrcode_form, name='qrcode_form'),
    path('generate_qrcode/', views.generate_qrcode, name='generate_qrcode'),
]