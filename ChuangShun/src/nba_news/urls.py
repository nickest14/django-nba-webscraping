from django.conf.urls import url

from .views import nba

urlpatterns = [
    url(r'^$', nba, name='nba'), #/
]
