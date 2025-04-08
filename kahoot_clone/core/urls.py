from django.urls import path
from .views import UserAPIView, QuizWinnersAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('winners/', QuizWinnersAPIView.as_view()),
]
