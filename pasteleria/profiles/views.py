from django.shortcuts import render
from profiles.forms import UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def viewProfile(request):
    users = User.objects.filter()

    return render(request, 'view_profile.html', {'users':users})

@login_required
def editProfile(request):
    users = User.objects.filter()
    user = request.user

    if request.method == 'POST':
        my_form = UserEditForm(request.POST)

        if my_form.is_valid():
            info = my_form.cleaned_data

            user.username = info['username']
            user.email = info['email']
            password = info['password1']
            user.set_password(password)
            user.save()

            return render(request, 'view_profile.html', {'users': users})
    
    else:
        my_form = UserEditForm(initial={'email': user.email, 'username': user.username})

    return render(request, 'edit_profile.html', {'my_form': my_form, 'user':user})