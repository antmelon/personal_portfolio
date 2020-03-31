from django.shortcuts import render
from personal_portfolio.models import Header
import os
# Create your views here.
def home(request):
    people = Header.objects.all()

    context = { 'anthony' : people[0] }
    return render(request, 'home.html', context)
