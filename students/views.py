import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student


@csrf_exempt
def students(request):
    response = {}
    students = Student.objects.all().values()

    if request.method == 'GET':
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
            'data': dict(students.get(id=student.id)),
        }
    else:
        response = {
            'message': 'HTTP request method not supported',
        }

    return JsonResponse(response, safe=False)


@csrf_exempt
def student(request, id):
    response = {}
    # students = Student.objects.all()
    # student = students.get(id=id)
    student_obj = Student.objects.filter(id=id)

    if request.method == 'GET':
        response = {
            'message': 'successfully get student',
            'data': dict(student_obj.values()[0]),
        }
    elif request.method == 'DELETE':
        student_obj.delete()
        response = {
            'message': 'successfully delete student {}'.format(id),
        }
    elif request.method == 'PUT':
        payload = json.loads(request.body)
        student = Student.objects.all().get(id=id)
        student.studentName = payload['studentName']
        student.studentMajor = payload['studentMajor']
        student.studentAge = payload['studentAge']
        student.save()
        response = {
            'message': 'successfully update student',
            'data': {
                'id': id,
            },
        }
    else:
        response = {
            'message': 'HTTP request method not supported',
        }

    return JsonResponse(response, safe=False)
