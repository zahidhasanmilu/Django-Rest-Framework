from .import views
from django.urls import path

urlpatterns = [
    path('', views.students_info),
    path('<int:id>/', views.student_info, name='student_info'),
    path('post/', views.student_post),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student_info),

]
