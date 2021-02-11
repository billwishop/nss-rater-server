from django.db import models 

class Game_category(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)