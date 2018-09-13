from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from diary import views
from diary.models import UserProfile


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        register = request.POST.get('register')
        if register.__str__() == 'on':
            current_user = User.objects.create(username=username)
            current_user.set_password(password)
            current_user.save()
            profile = UserProfile.objects.create(user=current_user)
            # profile.author = current_user
            profile.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('diary:index')
            else:
                # куда?
                return redirect(reverse('auth:auth'))
        return redirect(request.path)



def log_in(request):
    if request.method == 'GET':
        return render(request, 'auth/auth.html', {})

    else:
        password = request.POST['password']
        username = request.POST['username']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect(reverse('kpi:profile', args={user.id}))
            else:
                # куда?
                return redirect(reverse('authen:authen'))

        return redirect(request.path)



@login_required
def log_out(request):
    logout(request)
    return redirect('diary:index')


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

