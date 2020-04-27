from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from .models import Pizzas, Toppings, Orders
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
def homepage(request):
    
    return render(request, "main/homepage.html")


def menu(request):

	pizzas = Pizzas.objects.all()

	context = {"pizzas":pizzas}


	return render(request, "main/menu.html", context)

def basket(request):

	return render(request, "main/basket.html")

@csrf_protect
def add_to_basket(request):
	
	if request.method == 'POST':
		
		print(request.body)
		
		
		
		# json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
		# try:
		# 	data = json_data['pizza_name']
		# except KeyError:
		# 	return HttpResponseServerError("Malformed data!")
		
		# print(data)
		return HttpResponse("Got json data")
	
	return HttpResponseNotAllowed('NO')


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

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

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

