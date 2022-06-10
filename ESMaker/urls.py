from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path("login", views.login ,name="login"),
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('answer/<int:pk>/<int:ans>', views.answer, name='answer'),
]