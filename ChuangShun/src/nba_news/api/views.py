from rest_framework import generics


from nba_news.models import New
from .serializers import NewModelSerializer


class NewListAPIView(generics.ListAPIView):
    serializer_class = NewModelSerializer

    def get_queryset(self):
        return New.objects.all().order_by('-unique_id')
