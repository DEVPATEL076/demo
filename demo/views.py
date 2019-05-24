from django.contrib import messages
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                 )
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserLoginForm, UserRegistrationForm, UserForm
from .models import User

from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request,'index.html')
def register_view(request):  # Creates a New Account & login New users
    # in_use=User.objects.latest('email')
    if request.user.is_authenticated:
        return redirect("index")
    else:
        title = "Create a signup"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            messages.success(
                request,
                '''Thank You For Creating A Bank Account {}.
                Your Account Number is {}, Please use this number to login
                '''.format(new_user.full_name, new_user.email))

            return redirect("index")

        context = {"title": title, "form": form}

        return render(request, "form.html", context)


def login_view(request):  # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect("index")
    else:
        title = "Load Account Details"
        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            user_obj = User.objects.filter(email=email).first()
            password = form.cleaned_data.get("password")
            # authenticates Email & Password
            user = authenticate(email=user_obj.email, password=password)
            login(request, user)
            messages.success(request, 'Welcome, {}!' .format(user.full_name))
            return redirect("index")

        context = {"form": form,
                   "title": title
                   }

        return render(request, "form.html", context)


def logout_view(request):  # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logout(request)
        return redirect("index")

def MyView(request):
    query_results = User.objects.all()
    context= {'results': query_results}

        
    return render(request, 'pro.html', context)

class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    # Setting returning URL
    success_url = reverse_lazy('pro')
    
class UserDelete(DeleteView):
    model = User
    # Setting returning URL
    success_url = reverse_lazy('pro')