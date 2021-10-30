from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,"JudgeSystemApp/main.html")

def index(request):
    return render(request,"JudgeSystemApp/index.html")

def login_register(request):
    return render(request,"JudgeSystemApp/login_register.html")

def Problem(request):
    return render(request,"JudgeSystemApp/Problem.html")

def Profile(request):
    return render(request,"JudgeSystemApp/Profile.html")







