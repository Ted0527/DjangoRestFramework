from .models    import Score, Teacher, Student
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class TeacherSerializer(ModelSerializer):
    student_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = '__all__'
        
    def get_student_name(self, data):
        student = data.student_set.all()
        return student.values()
    
class StudentSerializer(ModelSerializer):
    teacher_name = serializers.SerializerMethodField()
    score_total = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        
    def get_teacher_name(self, data):
        return data.teacher.name

    def get_score_total(self, data):
        score = data.score_set.get()
        total = score.korean + score.english + score.math

        result = {
            'total' : total,
            'avg' : total/3
        }
        return result

class ScoreSerializer(ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'