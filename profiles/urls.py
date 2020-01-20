from django.urls import path
from . import views

urlpatterns = [
	path('',views.funderprofile, name='funder-profile'),
]