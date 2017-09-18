from rest_framework import generics


from nba_news.models import New
from .serializers import NewModelSerializer
from .pagination import StandardResultsPagination

class NewListAPIView(generics.ListAPIView):
    serializer_class = NewModelSerializer
    pagination_class = StandardResultsPagination
    def get_queryset(self):
        return New.objects.all().order_by('-unique_id')


class NewDetailAPIView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewModelSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        qs = New.objects.filter(pk=id)
        return qs
