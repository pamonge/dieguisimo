from django.db import models

# Create your models here.
class User (models.Model):
    user_type_choices = [
            ('a', 'admin'),
            ('j', 'jugador'),
            ('o', 'organizador'),
            ('r', 'arbitro'),
        ]

    user_id = models.IntegerField(verbose_name='dni')
    user_type = models.CharField(max_length=1, choices=user_type_choices, default='j', verbose_name='tipo de usuario')
    name = models.CharField(max_length=100, verbose_name='nombre')
    lastname = models.CharField(max_length=100, verbose_name='apellido')
    phone = models.IntegerField(verbose_name='telefono')
    adress = models.CharField(max_length=150, blank=True, null=True, verbose_name='direccion')
    picture = models.ImageField( blank=True, null=True, verbose_name='imagen')
    email = models.EmailField(blank=True, null=True, verbose_name='correo')

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.user_type})'

class Team (models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre de equipo', unique=True)
    organizer_id = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='organizador id')

    def __str__(self):
        return self.name

class Player (models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='nombre del equipo')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='jugador')

    def __str__(self):
        return f'{self.user_id.name} {self.user_id.lastname} ({self.team_id.name})'

class Tournament (models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre del torneo', unique=True)
    start_date = models.DateField(verbose_name='fecha inicio')
    end_date = models.DateField(verbose_name='fecha fin')
    organizer_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='organizador')

    def __str__(self):
        return self.name

class Match (models.Model):
    tournament_id = models.ForeignKey(Tournament, verbose_name='torneo')
    team_home = models.ForeignKey(Team, related_name='local', on_delete=models.CASCADE, verbose_name='equipo local')
    team_away = models.ForeignKey(Team, related_name='foreign', on_delete=models.CASCADE, verbose_name='equipo visitante')
    date = models.DateField(verbose_name='fecha del partido')
    time = models.TimeField(verbose_name='hora del partido')
    referee_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='arbitro')

    def __str__(self):
        return f'{self.team_home.name} vs {self.team_away.name} ({self.date})'
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(team_home=models.F('team_away')),
                name='prevent_self_match'
            ),
        ]
    
class Score (models.Model):
    score_choices = [
        (3, 'w'),
        (1, 'd'),
        (0, 'l'),
    ]
    tournament = models.ForeignKey(Tournament, verbose_name='torneo')
    team_id = models.ForeignKey(Team, verbose_name='equipo')
    points = models.IntegerField(choices=score_choices, verbose_name='puntaje')

    def __str__(self):
        return f'{self.team_id.name} - {self.points}'

    class Meta:
        constraints = [
            models.UniqueConstraint (
                fields=['tournament', 'team_id'],
                name= 'unique_score_per_team'
            )
        ]
