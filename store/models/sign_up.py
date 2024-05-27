from django.db import models

class SignUp(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.name