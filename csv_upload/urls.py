from django.urls import path
from .views import UploadView

app_name = 'csv_upload'

urlpatterns = [
    path('', UploadView.as_view(), name='index'),
]
