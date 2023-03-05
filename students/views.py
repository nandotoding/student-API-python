import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student


@csrf_exempt
def students(request):
    response = {}

    if request.method == 'GET':
        students = Student.objects.all().values()
        response = {
            'message': 'successfully get all students',
            'data': list(students),
        }
    elif request.method == 'POST':
        payload = json.loads(request.body)
        student = Student(
            studentName=payload['studentName'],
            studentMajor=payload['studentMajor'],
            studentAge=payload['studentAge']
        )
        student.save()
        response = {
            'message': 'successfully add student',
            'data': dict(Student.objects.all().values().get(id=student.id)),
        }
    else:
        response = {
            'message': 'HTTP request method not supported',
        }

    return JsonResponse(response, safe=False)


@csrf_exempt
def student(request, id):
    response = {}
    students = Student.objects.all()

    if request.method == 'GET':
        response = {
            'message': 'successfully get student',
            'data': dict(students.values().get(id=id)),
        }
    elif request.method == 'DELETE':
        students.get(id=id).delete()
        response = {
            'message': 'successfully delete student {}'.format(id),
        }
    else:
        response = {
            'message': 'HTTP request method not supported',
        }

    return JsonResponse(response, safe=False)
