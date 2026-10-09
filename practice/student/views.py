from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home_page(req):
    return render(req,'home.html')
@csrf_exempt
def login(req):
    #json_data=json.loads(req.body)
    #user=json_data.get('username)
    #password=json_data.get('password')
    user=req.POST.get('username')
    password=req.POST.get('password')
    return JsonResponse({'status':'login success!'})
    if user=='lavanya' and password=='lav@123':
        return JsonResponse({'status':'login success!'})
    else:
         return JsonResponse({'status':'invalid credentials!'})