from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #TOP PAGE
    path('', views.index_view, name='index'),
    path("login", views.login ,name="login"),
    path("logout", views.logout ,name="logout"),
    path("signup", views.signup ,name="signup"),

    #MY PAGE
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('answer/<int:pk>/<int:ans>', views.answer, name='answer'),
    path('answer/<int:pk>/post', views.post_answer, name='post_answer'),
    path('company/<int:pk>/post', views.post_company, name='post_company'),
    path('CompanyEsPage/<int:pk>/<int:comp>', views.CompanyEsPage, name='CompanyEsPage'),
    path('CompanyEsPost/<int:pk>/<int:comp>', views.CompanyESPost, name='CompanyESPost'),
    path('answer/<int:pk>/<int:ans>/delete', views.delete_answer, name='delete_answer'),
    path('Edit_answer/<int:pk>/<int:ans>',views.Edit_answer, name='Edit_answer'),
    path('Edit_ES/<int:pk>/<int:comp>/<int:es>',views.Edit_ES, name='Edit_ES'),

    #質問一覧のページ
    path('questions/<int:pk>/<>', views.questions, name='questions'),
    #ESを出した会社を管理するページ
    path('companies/<int:pk>/', views.companies, name='companies'),


    path('delete_ES/<int:pk>/<int:comp>/<int:es>', views.delete_ES, name='delete_ES'),


    path('wordcloud_test/<int:pk>/<int:ans>', views.wordcloud_test, name='wordcloud_test'),

    #企業削除ページ
    path('delete_company/<int:pk>/<int:comp>', views.delete_company, name='delete_company'),


]