from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    NewListAPIView,
    NewDetailAPIView
    )

urlpatterns = [
    url(r'^$', NewListAPIView.as_view(), name='list'), # /api/tweet/
    url(r'^(?P<pk>\d+)/$', NewDetailAPIView.as_view(), name='api-detail'),

]
