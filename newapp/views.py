from django.shortcuts import render
from django.views.generic.edit import CreateView
from newapp.models import NewApp


class Add(CreateView):
    model = NewApp
    fields = ('title', 'app_name', 'content')
    template_name = 'add_new_app.html'
    success_url = '/newapp'
