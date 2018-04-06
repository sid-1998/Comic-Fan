from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy,reverse
from .forms import UserForm,UserInfoForm

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            return redirect('/')
    else:
        user_form = UserForm()
        profile_form = UserInfoForm()

    return render (request,'accounts/signup.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })
