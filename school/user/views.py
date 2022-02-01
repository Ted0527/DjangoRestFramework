import json
from django.db.models.query import QuerySet
from django.db.models   import Count, Avg
from django.views   import View
from django.http    import JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import *  # * 함부로 쓰면 안됨

from user.models    import Teacher, Student, Score
from .serializers   import TeacherSerializer, StudentSerializer, ScoreSerializer

class TeacherModelViewSet(viewsets.ModelViewSet):  # 클래스명은 룰임
    permission_classes = [AllowAny] # 누구나 접근 가능(디폴트)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
class StudentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    
class ScoreModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    

# class TeacherView(View):
#     def get(self, request):
#         teachers = Teacher.objects.all()
        
#         result = [{'name' : [teacher_data.name]}for teacher_data in teachers]
#         return JsonResponse({'result':result}, status=200)
        
#     def post(self, request):
#         data = json.loads(request.body)
        
#         Teacher.objects.create(
#             name = data['name']
#         )
#         return JsonResponse({'message' : 'Created'}, status=201)
        
#     def patch(self, request):
#         data = json.loads(request.body)
#         teacher = Teacher.objects.get(id=data['id'])
#         teacher.name = data['new_name']
#         teacher.save()
        
#         return JsonResponse({'message' : 'Success'}, status=200)
    
#     def delete(self, request):
#         teacher_id = request.GET.get('id')
#         Teacher.objects.filter(id=teacher_id).delete()
        
#         return JsonResponse({'message' : 'Delete Success'}, status=200)
    
# class StudentView(View):
#     def get(self, request):
#         students = Student.objects.all()
        
#         result = [
#             {
#                 'teacher' : student_data.teacher.name,
#                 'name'    : student_data.name,
#                 'email'   : student_data.email
#                 } for student_data in students
#             ]
        
#         return JsonResponse({'result':result}, status=200)

#     def post(self, request):
#         data         = json.loads(request.body)
#         teacher_data = data['teacher_data']
        
#         teacher_id = Teacher.objects.get(id=teacher_data)
        
#         Student.objects.create(
#             name       = data['name'],
#             email      = data['email'],
#             teacher_id = teacher_id.id
#         )
#         return JsonResponse({'message' : 'Created'}, status=201)
        
#     def patch(self, request):
#         data = json.loads(request.body)
#         student = Student.objects.get(id=data['id'])
        
#         student.name = data['new_name']
#         student.email = data['new_email']
#         student.save()
        
#         return JsonResponse({'message' : 'Success'}, status=200)
    
#     def delete(self, request):
#         student_id = request.GET.get('id')
#         Student.objects.filter(id=student_id).delete()
        
#         return JsonResponse({'message' : 'Delete Success'}, status=200)