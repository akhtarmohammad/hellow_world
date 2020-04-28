from django.urls import path
from .views import homePageVeiw
urlpatterns=[
    path('',homePageVeiw,name='home')
]
