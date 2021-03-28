from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('abc',views.app1,name='app1'),
]