from django.db import models

# Create your models here.
class User (models.Model):
    dni = models.IntegerField(primary_key=True, verbose_name='dni'),
    user_type = models.ForeignKey(User_Type, on_delete=models.CASCADE),
    name = models.CharField(max_length=100, verbose_name='nombre'),
    lastname = models.CharField(max_length=100, verbose_name='apellido'),
    telephone = models.IntegerField(verbose_name='telefono'),
    adress = models.CharField(max_length=150, verbose_name='direccion'),
    picture = models.ImageField(verbose_name='imagen')

    def __str__(self):
        return dni

class User_Type (models.Model):
    user_type_choices = [
        ('a', 'admin'),
        ('j', 'jugador'),
        ('o', 'organizador'),
        ('a', 'arbitro'),
    ]

    user_type = models.CharField(max_length=1, primary_key=True, choices=user_type_choices, default='j')

    def __str__(self):
        return user_type

class Score (models.Model):
    points_choices = [
        (3, 'w'),
        (1, 'e'),
        (0, 'l'),
    ]

    points = models.IntegerField(choices=points_choices, )