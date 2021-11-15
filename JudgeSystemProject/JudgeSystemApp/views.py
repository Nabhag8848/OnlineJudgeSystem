from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import array as arr

def main(request):
    return render(request,"JudgeSystemApp/main.html")

def index(request):
    return render(request,"JudgeSystemApp/index.html")

def login(request):
    form = UserCreationForm()
    
    context = {'form':form}
    return render(request,"JudgeSystemApp/login.html" , context) 

def register(request):
    form = UserCreationForm()
    
    context = {'form':form}
    return render(request,"JudgeSystemApp/register.html" , context)

def Problem(request):
    
    return render(request,"JudgeSystemApp/Problem.html")

def Profile(request):
    return render(request,"JudgeSystemApp/Profile.html")

def questionsList(request):
  
    lists = arr.array('i', [1, 2, 3 , 4,5,6,7,8,9,10])
    
    return render(request,"JudgeSystemApp/questionsList.html" , {'lists':lists})







