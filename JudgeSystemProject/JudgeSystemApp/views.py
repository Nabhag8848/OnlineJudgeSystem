from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import array as arr

from .models import CPPQuestions, CQuestions, JAVAQuestions, PYTHONQuestions

# from .models import CQuestions

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

def Problem(request ,lang, poll_id):
    if lang == 'C':
        lists = CQuestions.objects.get(heading = poll_id)
        
                
    elif lang == 'CPP':
        lists = CPPQuestions.objects.get(heading = poll_id)


    elif lang == 'JAVA':
        lists = JAVAQuestions.objects.get(heading = poll_id)


    elif lang == 'PYTHON':
        lists = PYTHONQuestions.objects.get(heading = poll_id)
       
    
    
    list = {'lists': lists}
    return render(request,"JudgeSystemApp/Problem.html" ,list)

def Profile(request):
    return render(request,"JudgeSystemApp/Profile.html")

def questionsList(request,poll_id):
    print(poll_id)
    if poll_id == 'C':
        lang = 'C'
        lists = CQuestions.objects.all()
        
    elif poll_id == 'CPP':
        lang = 'CPP'
        lists = CPPQuestions.objects.all()

    elif poll_id == 'JAVA':
        lang = 'JAVA'
        lists = JAVAQuestions.objects.all()

    elif poll_id == 'PYTHON':
        lang = 'PYTHON'
        lists = PYTHONQuestions.objects.all()
        
    
    list = {'lists': lists , 'slug': poll_id , 'lang':lang}
    
    return render(request,"JudgeSystemApp/questionsList.html" , list )

def explore(request):
    return render(request, "JudgeSystemApp/explore.html")







