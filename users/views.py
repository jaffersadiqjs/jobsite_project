from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, ProfileForm

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})
