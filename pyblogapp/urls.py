"""pyblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views 2. Add a URL to urlpatterns:  path('', views.home, name='home')
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

# https://narito.ninja/blog/detail/55/
from django.contrib.sitemaps.views import sitemap
from posts.sitemap import PostSitemap, StaticSitemap

# https://ymgsapo.com/show-image-imagefield/
# https://narito.ninja/blog/detail/92/
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


sitemaps = {
    'posts': PostSitemap,
    'static': StaticSitemap,
}


# https://qiita.com/okoppe8/items/702dab51e4db5d0ed677
admin.site.site_title = 'タイトルタグ' 
admin.site.site_header = 'PyBlog' 
admin.site.index_title = 'メニュー'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #path('img_upload/', include('img_upload.urls', namespace='img_upload')),
    #path('csv_upload/', include('csv_upload.urls', namespace='csv_upload')),
    #path('robots\.txt$' include('django2_url_robots.views.robots_txt')),
    #path('manager/', include('manager.urls', namespace='manager')),
    path('', include('posts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

