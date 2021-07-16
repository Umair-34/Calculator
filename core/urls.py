from django.urls import path

from .views import calculation, history, ProfileUpdateView, updatepassword


app_name = "core"

urlpatterns = [
    path('calculation', calculation, name='calculation'),
    path('history', history, name='history'),
    path('updatepassword', updatepassword, name='updatepassword'),
    path('updateprofile', ProfileUpdateView.as_view(), name='update')
]
