import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student


@csrf_exempt
def students(request):
    if request.method == 'GET':
        students = Student.objects.all().values()
        data = {
            'data': list(students)
        }
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        payload = json.loads(request.body)
        student = Student(
            studentName=payload['studentName'],
            studentMajor=payload['studentMajor'],
            studentAge=payload['studentAge']
        )
        student.save()
        return JsonResponse({
            'message': 'successfully add student data',
        })
