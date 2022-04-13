from django.shortcuts import render

# Create your views here.
from .models import Projects


def show_display(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def projects_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'projects': project
    }
    return render(request, 'project_detail.html', context)
