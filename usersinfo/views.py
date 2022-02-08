from django.shortcuts import render, render
from django.views import generic


class  HomeView(generic.View):
     def get(self, request, *args, **kwargs):
         return render(request, 'tempaltes/home.html')
    


