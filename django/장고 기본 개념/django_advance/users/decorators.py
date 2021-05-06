from django.shortcuts import redirect
from .models import Users

def adminRequired(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user :
            # return redirect('/')
            return redirect('/user/login/')
        user = Users.objects.get(email = user)
        if user.level != 'admin':
            return redirect('/')
        return func(request, *args, **kwargs)

    return wrap

def loginRequired(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user :
            return redirect('/user/login/')
        return func(request, *args, **kwargs)

    return wrap