
from django.shortcuts import render
import requests
import json
from .models import Ecospot
# Create your views here.


def Ecospots(request):
        ecospots = Ecospot.objects.all
        return render(request, 'ecospot.html', {'ecospots':ecospots})