from django.urls import path
from . import views
from myresume.views import Resume, Candidate

urlpatterns = [
    path('', Resume.as_view(), name='home'),
    path('<int:pk>', Candidate.as_view(), name='show')
]