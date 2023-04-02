from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=20)
    id=models.IntegerField(auto_created=True, primary_key=True)

    def __str__(self) -> str:
        return self.name