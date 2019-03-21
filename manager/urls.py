from django.urls import path
from . import views


app_name = 'manager'
#app_name = 'worker'

urlpatterns = [
    path('', views.get,),
    #path('', views.get, name='index'),
    #path('detail/<int:blog_id>/', views.detail, name='detail'),
  # url(r'^worker_list/', manager_view.WorkerListView.as_view()) 
]
