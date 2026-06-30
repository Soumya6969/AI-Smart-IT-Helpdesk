from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    return render(request, "helpdesk/helpdesk.html")


def about(request):
    return render(request, "helpdesk/about.html")


def contact(request):
    return render(request, "helpdesk/contact.html")

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            if User.objects.filter(username=username).exists():

                messages.error(
                    request,
                    "Username already exists."
                )

            elif User.objects.filter(email=email).exists():

                messages.error(
                    request,
                    "Email already exists."
                )

            else:

                user = User.objects.create_user(

                    username=username,

                    first_name=form.cleaned_data['first_name'],

                    last_name=form.cleaned_data['last_name'],

                    email=email,

                    password=form.cleaned_data['password']

                )

                user.save()

                messages.success(

                    request,

                    "Registration Successful."

                )

                return redirect('login')

    else:

        form = RegisterForm()

    return render(

        request,

        "helpdesk/register.html",

        {

            'form': form

        }

    )
def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login Successful."
            )

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid Username or Password."
            )

    return render(
        request,
        "helpdesk/login.html"
    )


@login_required(login_url='login')
def dashboard(request):

    return render(
        request,
        "helpdesk/dashboard.html"
    )


def logout_user(request):

    logout(request)

    messages.success(
        request,
        "Logged Out Successfully."
    )

    return redirect("login")