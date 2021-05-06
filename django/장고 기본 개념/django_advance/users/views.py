from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Users
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html', {'user':request.session.get('user')})


class LoginView(FormView) :
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

def logout(request):
    if request.session.get('user') :
        del(request.session['user'])
    return redirect('/')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = Users(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            level = 'user'
        )
        user.save()

        return super().form_valid(form)



