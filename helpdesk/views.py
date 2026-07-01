from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, TicketForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

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

@login_required(login_url='login')
def raise_ticket(request):

    if request.method == "POST":

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.user = request.user

            ticket.save()

            messages.success(
                request,
                "Ticket Submitted Successfully."
            )

            return redirect('raise_ticket')

    else:

        form = TicketForm()

    return render(
        request,
        "helpdesk/raise_ticket.html",
        {
            'form': form
        }
    )
@login_required(login_url='login')
def my_tickets(request):

    tickets = Ticket.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        "helpdesk/my_tickets.html",
        {
            "tickets": tickets
        }
    )
@login_required(login_url='login')
def ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    return render(
        request,
        "helpdesk/ticket_detail.html",
        {
            "ticket": ticket
        }
    )
@login_required(login_url='login')
def edit_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    # Closed ticket edit nahi hoga
    if ticket.status == "Closed":

        messages.error(
            request,
            "Closed tickets cannot be edited."
        )

        return redirect(
            "ticket_detail",
            ticket_id=ticket.id
        )

    if request.method == "POST":

        form = TicketForm(
            request.POST,
            instance=ticket
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Ticket Updated Successfully."
            )

            return redirect(
                "ticket_detail",
                ticket_id=ticket.id
            )

    else:

        form = TicketForm(
            instance=ticket
        )

    return render(
        request,
        "helpdesk/edit_ticket.html",
        {
            "form": form,
            "ticket": ticket
        }
    )
@login_required(login_url='login')
def close_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    if ticket.status != "Closed":

        ticket.status = "Closed"

        ticket.save()

        messages.success(
            request,
            "Ticket Closed Successfully."
        )

    return redirect(
        "ticket_detail",
        ticket_id=ticket.id
    )
@staff_member_required(login_url='login')
def admin_dashboard(request):

    search_query = request.GET.get("search", "").strip()
    status_filter = request.GET.get("status", "").strip()
    priority_filter = request.GET.get("priority", "").strip()

    tickets = Ticket.objects.all().order_by("-created_at")

    if search_query:
        tickets = tickets.filter(
            Q(subject__icontains=search_query) |
            Q(user__username__icontains=search_query)
        )

    if status_filter:
        tickets = tickets.filter(status=status_filter)

    if priority_filter:
        tickets = tickets.filter(priority=priority_filter)

    context = {
        "tickets": tickets,

        "search_query": search_query,
        "status_filter": status_filter,
        "priority_filter": priority_filter,

        "total_tickets": Ticket.objects.count(),
        "open_tickets": Ticket.objects.filter(status="Open").count(),
        "progress_tickets": Ticket.objects.filter(status="In Progress").count(),
        "closed_tickets": Ticket.objects.filter(status="Closed").count(),
    }

    return render(
        request,
        "helpdesk/admin_dashboard.html",
        context
    )
@staff_member_required(login_url='login')
def admin_ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if request.method == "POST":

        ticket.status = request.POST.get("status")

        ticket.save()

        messages.success(
            request,
            "Ticket Status Updated Successfully."
        )

        return redirect(
            "admin_ticket_detail",
            ticket_id=ticket.id
        )

    return render(
        request,
        "helpdesk/admin_ticket_detail.html",
        {
            "ticket": ticket
        }
    )
def logout_user(request):

    logout(request)

    messages.success(
        request,
        "Logged Out Successfully."
    )

    return redirect("login")