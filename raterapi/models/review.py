from django.db import models 

class Review(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    review = models.CharField(max_length=50)