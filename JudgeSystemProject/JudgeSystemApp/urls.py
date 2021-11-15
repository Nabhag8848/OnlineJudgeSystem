from django.urls import path
from .import views

urlpatterns=[
    path('',views.main,name="main"),
    path('index/',views.index,name="index"),
    path('Problem/',views.Problem,name="Problem"),
    path('Profile/',views.Profile,name="Profile"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),

    path('questionsList/',views.questionsList,name="questionsList"),


   

]


