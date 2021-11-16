from django.urls import path
from .import views

urlpatterns=[
    path('',views.main,name="main"),
    path('index/',views.index,name="index"),
    path('Problem/<str:lang>/<str:poll_id>/',views.Problem,name="Problem"),
    path('Profile/',views.Profile,name="Profile"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('explore/',views.explore,name= "explore"),

    path('questionsList/<str:poll_id>/',views.questionsList,name="questionsList"),


   

]


