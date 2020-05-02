from django.http import HttpResponse
from django.shortcuts import redirect


# Only let's certain roles see this page
def allowedUsers(allowedRoles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()
            
            if group in allowedRoles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Sorry, but you are not allowed here! :(")
        return wrapper_func
    return decorator


# Only let's staff accounts see this page
def staffOnly(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_staff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("Sorry, but you are not allowed here! :(")
    return wrapper_func


# Only let's unauthenticated user see this page (ex: register and login should not be accessed by authenticated users)
def unauthenticatedOnly(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:homepage')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

# Only let's authenticated user see this page
def authenticatedOnly(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('main:homepage')
    
    return wrapper_func