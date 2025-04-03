from django.db import models

# Create your models here.
class User(models.Model):
    userId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return f"{self.userId} {self.name} {self.email}"

class Task(models.Model):
    class statuschoices(models.TextChoices):
        PENDING= 'pending', 'pending'
        INPROGRESS='inprogress','inprogress'
        COMPLETED='completed','completed'
    TaskId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    status=models.CharField(max_length=50,choices=statuschoices.choices, default=statuschoices.PENDING)
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.TaskId} {self.title} {self.description} {self.status} {self.created_at}"
