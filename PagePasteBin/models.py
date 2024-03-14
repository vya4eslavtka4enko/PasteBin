from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=80)
    email_name=models.EmailField(max_length=80)
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name