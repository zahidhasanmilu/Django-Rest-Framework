from .import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('post/', views.student_post),
]
