# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User, auth
# # Create your views here.
# def register(request):
     
#     if request.method == "POST":
#         first_name=request.POST('first_name')
#         last_name=request.POST('last_name')
#         user_name=request.POST('user_name')
#         password1=request.POST('password1')
#         password2=request.POST('password2')
#         email=request.POST('email')

#         if password1==password2:
#             if User.objects.filter(user_name=user_name).exists():
#                 print('User taken')
#             elif User.objects.filter(email=email).exists():
#                 print('email take')
#             else:
#                 user=User.objects.create_user(user_name=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
#                 user.save()
#                 print('User Created')
#         else:
#             print('password not matching..')
#         return redirect('/')
#     else:
#         return render(request,'register.html')

from .models import CustomUser
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if CustomUser.objects.filter(username=user_name).exists():
                print('User taken')
            elif CustomUser.objects.filter(email=email).exists():
                print('Email taken')
            else:
                user = CustomUser.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
        else:
            print('Passwords not matching..')
        return redirect('register')
    else:
        return render(request, 'register.html')






















