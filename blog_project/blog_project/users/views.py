from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        messages.success(self.request, f'Account is created successfully')
        return super().form_valid(form)

def Profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'your account has been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)

    context = {'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'users/profile.html', context)
