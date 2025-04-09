from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    students = models.ManyToManyField(Student, related_name='classrooms')

    def __str__(self):
        return self.name


class Level(models.Model):
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(Student, related_name='levels')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Winner(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='winners', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.score}'
