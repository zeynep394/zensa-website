from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import websiteofzensa, products, post,ahsap, search,boyalar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', websiteofzensa),
    path('products/', products),
    path('ahsap/', ahsap),
    path('boyalar/', boyalar),
    path('search/', search, name='search'),
    # path('search/', search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
