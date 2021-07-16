from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import History
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


@login_required(login_url='accounts:login')  # login required decorator
def calculation(request):
    final_result = ''
    values = ''
    if request.method == "POST":
        values = request.POST['values']  # string having whole ques
        try:
            final_result = eval(values)
        except ZeroDivisionError or BaseException:
            if ZeroDivisionError:
                final_result = "Undefined: Division by Zero"
            else:
                final_result = "Undefined Error"
        History.objects.create(user=request.user, expression=values, result=final_result)

    return render(request, 'core/index.html', {'result': final_result, 'values': values})


@login_required(login_url='accounts:login')  # login required decorator
def history(request):
    user = request.user
    obj = History.objects.filter(user=user)
    return render(request, 'core/history.html', {'obj': obj})


@login_required(login_url='accounts:login')  # login required decorator
def updatepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # converting password to hash
            messages.success(request, 'Form submission successful')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/passwordupdate.html', {'form': form})


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    fields = ("username", "first_name", "last_name")
    template_name = 'core/profileupdate.html'
    success_url = reverse_lazy('core:update')
    success_message = 'Profile Updated'

    def get_object(self):
        return self.request.user
