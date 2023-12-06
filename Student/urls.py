from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_form/', views.student_form, name='student_form'),
    path('student/', views.student_data, name='student_data'),
    path('contact/', views.contact, name='contact'),
    path('edit_student/', views.editStundet, name='edit_student'),

]
