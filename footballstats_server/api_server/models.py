from django.db import models
from django.contrib.auth.models import User, Permission

# Create your models here.
class AdminAction(models.Model):
    action_type: models.ForeignKey = models.ForeignKey(Permission, on_delete=models.CASCADE)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    action_date: models.DateField = models.DateField()