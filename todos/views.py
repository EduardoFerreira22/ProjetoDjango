from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Helo Web!</h1>')
    return render(request, "todos/home.html") #A função render renderiza templates html, caso vc já tenha um criado

  # Create your views here.
