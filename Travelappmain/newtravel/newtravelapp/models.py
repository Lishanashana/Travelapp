from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def __str__(self):
        return self.name



class team(models.Model):
    imageofteam=models.ImageField(upload_to='pics')
    nameofteam = models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.nameofteam