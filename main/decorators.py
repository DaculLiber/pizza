from django.http import HttpResponse
from django.shortcuts import redirect

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

def staffOnly(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_staff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("Sorry, but you are not allowed here! :(")
    return wrapper_func