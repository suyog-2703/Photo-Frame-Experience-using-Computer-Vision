# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def home(request):
#     # return render(request, 'home.html');
#     return render(request, 'home.html',{'name':'Suyog'})

# def add(request):
#     val1=int(request.POST['num1'])
#     val2=int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})



# registration/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully submit the  details')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})
