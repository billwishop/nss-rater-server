from django.db import models 

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    year = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    age_recommendation = models.IntegerField()