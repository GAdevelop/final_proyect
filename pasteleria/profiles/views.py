from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import CostumUser 
from profiles.forms import ProfileForm
from django.http import HttpResponse

# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    '''user = request.user

    if request.method == "POST":
        
        edit_profileForm = ProfileForm(request.POST)

        if edit_profileForm.is_valid():

            data = edit_profileForm.cleaned_data

            user.email = data['email']
            password = data['password1']
            user.set_password(password)
            user.save()
            messages.success(request, 'Profile has been updated.')
    #form = ProfileForm(instance=request.user)

    else:
        edit_profileForm = ProfileForm(initial={'email':user.email})

    return render( request , "edit_profile.html" , {"profileForm":edit_profileForm , "user":user})'''
   

    if request.method=='POST':
        profileForm=ProfileForm(request.POST, instance=request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request, 'Profile has been updated.')

    form = ProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form':form})