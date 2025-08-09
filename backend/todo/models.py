from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=520)
    completed=models.BooleanField(default=False)

    def __main__(self):
       return self.title
      

