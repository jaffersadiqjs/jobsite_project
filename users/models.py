from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    USER_TYPES = (
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
