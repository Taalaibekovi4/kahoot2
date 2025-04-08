from rest_framework import serializers
from .models import *

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
    student = StudentSerializer()

    class Meta:
        model = Winner
        fields = ['student', 'score']

class QuizSerializer(serializers.ModelSerializer):
    winners = WinnerEntrySerializer(many=True)
    level = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'level', 'date', 'winners']
