from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class School(models.Model):
    name = models.CharField(max_length=255)

class Classroom(models.Model):
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    students = models.ManyToManyField(Student, related_name='classrooms')

class Level(models.Model):
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(Student, related_name='levels')

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Winner(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='winners', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
