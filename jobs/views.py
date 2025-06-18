from django.shortcuts import render, redirect
from .models import JobOffer
from .forms import JobOfferForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    jobs = JobOffer.objects.all()
    form = JobOfferForm()
    context = {
        'jobs': jobs,
        'form': form,
        'now': datetime.now()
    }
    return render(request, 'jobs/home.html', context)

def submit_offer(request):
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')

@login_required
def submission_list(request):
    submissions = JobOffer.objects.all()
    return render(request, 'jobs/submissions.html', {'submissions': submissions})