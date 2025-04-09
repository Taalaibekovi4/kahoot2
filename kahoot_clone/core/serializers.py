from rest_framework import serializers
from .models import Student, School, Classroom, Level, Quiz, Winner


# Сериализатор для модели Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']


# Сериализатор для модели School
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name']


# Сериализатор для модели Classroom
class ClassroomSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Classroom
        fields = ['id', 'name', 'school', 'students']


# Сериализатор для модели Level
class LevelSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Level
        fields = ['id', 'title', 'school', 'participants']


# Сериализатор для модели Winner
class WinnerEntrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='student.name')

    class Meta:
        model = Winner
        fields = ['name', 'score']


# Сериализатор для модели Quiz
class QuizCreateSerializer(serializers.ModelSerializer):
    quiz_name = serializers.CharField()
    level = serializers.CharField()
    date = serializers.DateTimeField()
    winners = WinnerEntrySerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'level', 'date', 'winners']

    def create(self, validated_data):
        winners_data = validated_data.pop('winners')
        quiz = Quiz.objects.create(**validated_data)
        for winner_data in winners_data:
            student_name = winner_data['name']
            student = Student.objects.get(name=student_name)  # Извлекаем студента по имени
            Winner.objects.create(quiz=quiz, student=student, score=winner_data['score'])
        return quiz


# Сериализатор для вывода списка викторин
class QuizSerializer(serializers.ModelSerializer):
    level = LevelSerializer()
    winners = WinnerEntrySerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'level', 'date', 'winners']
