from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application

@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        Job.objects.create(title=title, description=desc, employer=request.user)
        return redirect('job_list')
    return render(request, 'jobs/post_job.html')

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    Application.objects.create(job=job, applicant=request.user)
    return redirect('job_list')

@login_required
def view_applicants(request):
    jobs = Job.objects.filter(employer=request.user)
    applications = Application.objects.filter(job__in=jobs)
    return render(request, 'jobs/applicants.html', {'applications': applications})
