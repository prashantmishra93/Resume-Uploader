from django.shortcuts import render, HttpResponseRedirect
from .models import ResumeUpload
from .forms import ResumeForm
from django.views import View

class Resume(View):
    def get(self, request):
        form = ResumeForm()
        datas = ResumeUpload.objects.all()
        return render(request, 'home.html', {'form':form, 'datas':datas})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form':form})
        return render(request, 'home.html', {'form':form})

class Candidate(View):
    def get(self, request, pk):
        data = ResumeUpload.objects.get(pk=pk)
        return render(request, 'candidate.html', {'data':data})
