from django.db import models 

class Image(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='games', height_field=None, width_field=None, max_length=None)