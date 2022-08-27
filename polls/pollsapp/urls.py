from django.urls import path,include
from pollsapp import views

urlpatterns = [
    
    path('',views.home,name = 'index'),
    path('question/<str:pk>/',views.question_detail,name = 'question_detail'),
    path('result/<str:pk>/',views.result,name = 'result'),
    path('add_poll',views.polls_add,name = 'add_poll'),
    path('delete_poll/<str:pk>/',views.polls_delete,name = 'delete_poll'),

]
