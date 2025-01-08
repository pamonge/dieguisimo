from django.shortcuts import render
from .model import User, Team, Player, Tournament, Match, Score
from .serializers import UserSerializer, TeamSerializer, PlayerSerializer, TournamentSerializer, MatchSerializer, ScoreSerializer

# Create your views here.
class UserViewSet (viewsets.ModelViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet (viewsets.ModelViewset):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TournamentViewSet (viewsets.ModelViewset):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class MatchViewSet (viewsets.ModelViewset):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class ScoreViewSet (viewsets.ModelViewset):
    queryset = Score.objects.all()
    serializers_class = ScoreSerializer