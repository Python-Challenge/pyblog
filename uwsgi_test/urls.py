"""pyblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static


# https://qiita.com/okoppe8/items/702dab51e4db5d0ed677
admin.site.site_title = 'タイトルタグ' 
admin.site.site_header = 'PyBlog' 
admin.site.index_title = 'メニュー'


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('manager/', include('manager.urls', namespace='manager')),
    path('csv_upload/', include('csv_upload.urls', namespace='csv_upload')),
    #path('robots\.txt$' include('django2_url_robots.views.robots_txt')),
    path('', include('posts.urls')),
    path('', include('pyblogapp.views.reload', name='reload')),
]
