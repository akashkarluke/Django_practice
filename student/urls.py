from django.urls import path
from student import views

urlpatterns = [
    path('hello/', views.wish),
    path('student/', views.student_list),
    path('student1/', views.student_detail),
    path('student1/<int:pk>', views.student_detail),
]
