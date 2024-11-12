from django.urls import path
from .views import ProcessCSVData

urlpatterns = [
    path('process_csv/', ProcessCSVData.as_view(), name='process_csv'),
]
