from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from pro_history.models import Project
from pro_history.serializer import ProjectsSerializer

# Create your views here.

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

def pro_list(request, pro_id):
    return render(request, 'pro_' + pro_id + '.html')



