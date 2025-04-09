# from rest_framework import serializers
# from .models import *
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name']
#
# class ClassroomSerializer(serializers.ModelSerializer):
#     students = StudentSerializer(many=True)
#
#     class Meta:
#         model = Classroom
#         fields = ['id', 'name', 'students']
#
# class LevelSerializer(serializers.ModelSerializer):
#     participants = StudentSerializer(many=True)
#
#     class Meta:
#         model = Level
#         fields = ['id', 'title', 'participants']
#
# class SchoolSerializer(serializers.ModelSerializer):
#     classes = ClassroomSerializer(many=True)
#     levels = LevelSerializer(many=True)
#
#     class Meta:
#         model = School
#         fields = ['id', 'name', 'classes', 'levels']
#
# class WinnerEntrySerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#
#     class Meta:
#         model = Winner
#         fields = ['student', 'score']
#
# class QuizSerializer(serializers.ModelSerializer):
#     winners = WinnerEntrySerializer(many=True)
#     level = serializers.StringRelatedField()
#
#     class Meta:
#         model = Quiz
#         fields = ['id', 'quiz_name', 'level', 'date', 'winners']
from rest_framework import serializers
from .models import Student, School, Classroom, Level, Quiz, Winner


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']


class ClassroomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Classroom
        fields = ['id', 'name', 'students']


class LevelSerializer(serializers.ModelSerializer):
    participants = StudentSerializer(many=True)

    class Meta:
        model = Level
        fields = ['id', 'title', 'participants']


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClassroomSerializer(many=True)
    levels = LevelSerializer(many=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'classes', 'levels']


class WinnerEntrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='student.name')

    class Meta:
        model = Winner
        fields = ['name', 'score']


class QuizSerializer(serializers.ModelSerializer):
    winners = serializers.SerializerMethodField()
    level = serializers.StringRelatedField()
    quiz_name = serializers.CharField(source='name')

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'level', 'date', 'winners']

    def get_winners(self, obj):
        winners = obj.winners.all()
        if winners.exists():
            return WinnerEntrySerializer(winners, many=True).data
        else:
            return [
                {"name": "", "score": None},
                {"name": "", "score": None},
                {"name": "", "score": None}
            ]
