from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    shortlisted = models.BooleanField(default=False)
    interview_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
