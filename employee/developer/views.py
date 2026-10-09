import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(req):
    return HttpResponse("This is Developer's Home page")


@csrf_exempt
def login(req):
    if req.method == 'POST':
        db_username = 'lavanya'
        db_password = 'lavanya123'

        json_data = json.loads(req.body)

        inp_user = json_data.get('username')
        inp_pass = json_data.get('password')

        if db_username == inp_user and db_password == inp_pass:
            return HttpResponse('Welcome to login page')

        else:
            return JsonResponse({'status': 'Invalid credentials'})

    else:
        return JsonResponse({'status': 'Invalid Request'})
