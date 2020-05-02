from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import NewUserForm, NewPizza
from .models import Pizzas, Toppings, Orders
from .decorators import allowedUsers, staffOnly, unauthenticatedOnly, authenticatedOnly


# Create your views here.

def homepage(request):
# Homepage view, if user is in the staff, he'll get the staff version of the app
	
	if request.user.is_staff:

		orders = Orders.objects.all()
		print(orders[0].content.all())

		context = {"orders":orders, "staff":"yes"}

		return render(request, "main/homepage_staff.html", context)
	else:
		return render(request, "main/homepage.html")


def menu(request):
# Menu  view, if user is in the staff, he'll get the staff version of the app
	pizzas = Pizzas.objects.all()
	context = {"pizzas":pizzas, "staff":"yes"}

	if request.user.is_staff:
		return render(request, "main/menu_staff.html", context)
	else:
		return render(request, "main/menu.html", context)

@authenticatedOnly
def basket(request):

	return render(request, "main/basket.html")

@authenticatedOnly
@staffOnly
def crm(request):

	context = {"staff":"yes"}
	return HttpResponse("IN PROGRESS!!")

@authenticatedOnly
@staffOnly
def edit(request, id):
	
	pizza = Pizzas.objects.get(id=id)
	context = {"pizza":pizza, "staff":"yes"}

	return render(request, "main/edit.html", context)

@authenticatedOnly
@staffOnly
def add_new_pizza(request):

	context = {"staff":"yes"}

	if request.method == "POST":
		form = NewPizza(request.POST)
		if form.is_valid():
			form.save()
			return redirect("main:menu")
		

	return render(request, "main/add_new_pizza.html", context)

@unauthenticatedOnly
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
 

	form = NewUserForm()
	return render(request,
				  "main/register.html",
				  context={"form":form})

@unauthenticatedOnly
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})

@authenticatedOnly
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")