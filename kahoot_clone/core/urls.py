from django.urls import path
from .views import UserAPIView, QuizWinnersAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user_info'),
    path('winners/', QuizWinnersAPIView.as_view(), name='quiz_winners'),
]
