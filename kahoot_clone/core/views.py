from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import SchoolSerializer, QuizSerializer, QuizCreateSerializer


# Представление для отображения информации о пользователе
class UserAPIView(APIView):
    def get(self, request):
        data = {
            "name": "Админ",
            "avatar": "https://example.com/avatar.png",
            "schools": SchoolSerializer(School.objects.all(), many=True).data
        }
        return Response(data)


# Представление для работы с викторинами и победителями
class QuizWinnersAPIView(APIView):
    def get(self, request):
        # Пример структуры данных, которую клиент может отправить для POST-запроса
        example_data = {
            "id": None,  # id будет создано автоматически
            "quiz_name": "",
            "level": "",
            "date": "2025-04-03T14:30:00Z",
            "winners": [
                {"name": "", "score": 0},
                {"name": "", "score": 0},
                {"name": "", "score": 0}
            ]
        }
        return Response(example_data)

    def post(self, request):
        serializer = QuizCreateSerializer(data=request.data)
        if serializer.is_valid():
            quiz = serializer.save()
            return Response(QuizSerializer(quiz).data, status=201)
        return Response(serializer.errors, status=400)
