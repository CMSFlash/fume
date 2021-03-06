from typing import List, Union

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^tags/', include(('tags.urls', 'tags'), namespace='tags')),
    url(r'^games/', include(('games.urls', 'games'), namespace='games')),
    url(r'^purchase/', include(
        ('purchase.urls', 'purchase'),namespace='purchase'
    )),
    url(r'^member/', include(('member.urls', 'member'), namespace='member')),
    url(r'^accounts/', include(('member.urls', 'member'), namespace='member')),
    url(r'^oauth/', include(
        ('social_django.urls', 'social'), namespace='social'
    )),
    url(r'^reviews/', include(
        ('reviews.urls', 'reviews'), namespace = 'reviews'
    )),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
