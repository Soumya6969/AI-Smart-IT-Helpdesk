from django.shortcuts import render


def home(request):
    return render(request, "helpdesk/helpdesk.html")


def about(request):
    return render(request, "helpdesk/about.html")


def contact(request):
    return render(request, "helpdesk/contact.html")