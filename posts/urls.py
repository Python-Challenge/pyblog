from django.urls import path
from . import views

#urlpatterns = [url(r'^$',views.index, name = 'index')]

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
]
