from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('Project', views.ProjectsViewSet)

urlpatterns = [
    path('Project/<str:pro_id>', views.pro_list, name="pro_list"),
    path('', include(router.urls)),

]