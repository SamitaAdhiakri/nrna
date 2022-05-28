from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('about/<str:pk>/', views.aboutDetail, name="about"),

    path('project/', views.project, name="project"),
    path('project/<str:pk>/', views.projectDetail, name="project"),

    path('teams/', views.team, name="teams"),


    path('events/', views.event, name="events"),
    path('events/<str:pk>/', views.eventDetail, name="events"),

    path('news/', views.news, name="news"),
    path('news/<str:pk>/', views.newsDetail, name="news"),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),

    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),

]
