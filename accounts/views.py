from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView

from accounts.form import ProfileForm
from accounts.models import Profile


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'accounts/profile.html'
#
#
# profile = ProfileView.as_view()

@login_required
def profile_edit(request):
    # Profile.objects.get(user=request.user)와 같은 코드
    # profile = request.user.profile
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm
#
#
# profile_edit = ProfileUpdateView.as_view()

def signup(request):
    return HttpResponse('TO DO create signup template')


def logout(request):
    return HttpResponse('TO DO create logout')
