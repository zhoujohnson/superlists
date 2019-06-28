from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

# def Index(request):
#     return render(request,'index.html')

def index(request):
    return HttpResponse("Hello,world.You're at the police index")

def getJson(request):
    resp = {'errorcode':100,'detail':'Get success'}
    return HttpResponse(json.dumps(resp),content_type='application/json')

