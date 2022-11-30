from django.shortcuts import render
from .models import TodoListItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'index.html')



def todolistView(request): #getting entire data from model and passing it to html file
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',  {'all_items':all_todo_items})


def addTodoView(request):
    # x = request.POST.get('todotext')
    new_item = TodoListItem()
    new_item.content = request.POST.get('content')
    new_item.choices = request.Post.get('choice')#when user enters something we save it 
    new_item.save()
    return HttpResponseRedirect('/todo/') 

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 


@login_required(login_url='/login')
def todoappView(request):
    
    user_email = request.user.email
    # all_todo_items = TodoListItem.objects.all()
    all_todo_items = TodoListItem.objects.filter(user=user_email)
    return render(request, 'todolist.html',  {'all_items':all_todo_items})

@login_required(login_url='/login')
def addTodoView(request):
    # x = request.POST.get('todotext')
    user_email = request.user.email
    new_item = TodoListItem()
    new_item.user = user_email
    new_item.content = request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/todo/') 
    
@login_required(login_url='/login')
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 
    
    
    
