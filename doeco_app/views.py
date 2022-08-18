
from django.shortcuts import render
import requests
import json
from .models import Ecospot
# Create your views here.


def main(request):
        return render(request, 'main.html')

def Ecospots(request):
        ecospots = Ecospot.objects.all
        return render(request, 'ecospot.html', {'ecospots':ecospots})