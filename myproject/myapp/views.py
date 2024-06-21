from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def hello(request):
    return HttpResponse("Hello, world. You're at the hello page.")

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def new_user(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        User.objects.create(name=name, email=email, age=age)
        return HttpResponse("User created successfully!")
     return render(request, 'new_user.html')

def user_detail(request,id):
    try:
         user = User.objects.get(pk=id)
         return render(request, 'user_detail.html', {'user': user})
    except User.DoesNotExist:
         return HttpResponse("User not found", status=404)
