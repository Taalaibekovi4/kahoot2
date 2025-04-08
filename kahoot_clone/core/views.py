from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class UserAPIView(APIView):
    def get(self, request):
        data = {
            "name": "Админ",
            "avatar": "https://example.com/avatar.png",
            "schools": SchoolSerializer(School.objects.all(), many=True).data
        }
        return Response(data)

class QuizWinnersAPIView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        return Response(QuizSerializer(quizzes, many=True).data)

    def post(self, request):
        # Здесь можно сделать логику добавления победителей
        return Response({"message": "Победители сохранены!"})
