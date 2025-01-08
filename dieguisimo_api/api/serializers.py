from rest_framework import serializers
from .models import User, Team, Player, Tournament, Match, Score

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class TeamSerializer (serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TournamentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class MatchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class ScoreSerializer (serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'