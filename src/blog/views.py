
from django.shortcuts import render


#Create your views here.

def index(request):
    
    posts = [
        {'id':1, 'title':'first posts', 'body':'this is my first posts'},
        {'id':2, 'title':'second posts', 'body':'this is my second posts'},
        {'id':3, 'title':'third posts', 'body':'this is my third posts'},


    ]
    
    
    return render(request, 'index.html', {'posts': posts})