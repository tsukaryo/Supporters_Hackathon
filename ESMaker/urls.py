from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path("login", views.login ,name="login"),
    path("logout", views.logout ,name="logout"),
    path("signup", views.signup ,name="signup"),
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('answer/<int:pk>/<int:ans>', views.answer, name='answer'),
    path('answer/<int:pk>/post', views.post_answer, name='post_answer'),
    path('answer/<int:pk>/<int:ans>/delete', views.delete_answer, name='delete_answer'),
]