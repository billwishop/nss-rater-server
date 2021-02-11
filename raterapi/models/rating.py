from django.db import models 

class Rating(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    rating = models.IntegerField()