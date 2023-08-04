from django.urls import path
from newapp import views

urlpatterns = [
    path('', views.Add.as_view(), name='add new app'),
]
