import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import StudentDetails
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentDetailsSerializer
def home(req):
    return render(req,'home.html')

# Create your views here.
def create_student(req):
    StudentDetails.objects.create(
        name = 'Nayab',
        age = 27,
        marks = 99,
        place = 'Hyd'
    )
    return JsonResponse({'status':'Student Added!'})

@csrf_exempt
def add_student(req):
    json_data = json.loads(req.body)
    stu_obj = StudentDetailsSerializer(data=json_data)
    if stu_obj.is_valid():
        stu_obj.save()
        return JsonResponse({'status':'Student Added Successfully!'})
    else:
        return JsonResponse(stu_obj.errors)

def get_student(req,id):
    try:
        stu_obj = StudentDetails.objects.get(id=id)
        json_data = StudentDetailsSerializer(stu_obj)
        return JsonResponse(json_data.data)
    except StudentDetails.MultipleObjectsReturned:
        return JsonResponse({'status':'Too Many Records!'})
    except StudentDetails.DoesNotExist:
        return JsonResponse({'status':'ID Does Not Exists!'})

def get_all_students(req):
    all_stu = StudentDetails.objects.all()
    json_data = StudentDetailsSerializer(all_stu,many=True)
    return JsonResponse({'all_student':json_data.data})

def delete_student(req,id):
    try:
        StudentDetails.objects.get(id=id).delete()
        return JsonResponse({'status':'Student Deleted Successfully!'})
    except StudentDetails.DoesNotExist:
            return JsonResponse({'status':'ID Does Not Exists!'})
    except StudentDetails.MultipleObjectsReturned:
            return JsonResponse({'status':'Too Many Records!'})

@csrf_exempt
def update_student(req,id):
    if req.method in ('PUT','PATCH'):
        json_data = json.loads(req.body)
        try:
            stu_obj = StudentDetails.objects.get(id=id)
            method = None
            if req.method == 'PUT':
                method = False
            else:
                method = True
            new_stu = StudentDetailsSerializer(stu_obj,data=json_data,partial=method)
            if new_stu.is_valid():
                new_stu.save()
                return JsonResponse({'status':'Student Details Updated Successfully!'})
            else:
                return JsonResponse(new_stu.errors)
        except StudentDetails.DoesNotExist:
            return JsonResponse({'status':'ID Does not Exists'})
        except StudentDetails.MultipleObjectsReturned:
            return JsonResponse({'status':'Too many objects!'})  
    else:
        return JsonResponse({'status':'Invalid Method!'})
                    