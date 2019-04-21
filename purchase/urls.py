from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<game_product_id>[0-9]+)/$', views.purchase, name='purchase'),
    url(r'^(?P<game_product_id>[0-9]+)/pay/$', views.pay, name='pay'),
    url(r'^clear/(?P<game_id>[0-9]+)$', views.clear, name='clear'),
]
