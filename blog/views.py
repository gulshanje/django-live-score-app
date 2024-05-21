from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
import requests

def index(request):
    # today = datetime.today().strftime('%y-%m-%d')
    # url = os.environ.get('URLAPI')
    url = os.environ.get('URLAPILIVE')
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'blog/index.html', {"jsonResponse" : jsonResponse})