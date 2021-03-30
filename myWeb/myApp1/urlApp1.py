from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name="base"),
    path('index',views.index,name="index"),
    path('all_question',views.questions_list,name="questions_list"),
    path('detail/<int:question_id>',views.detailView,name="detail_question"),
]