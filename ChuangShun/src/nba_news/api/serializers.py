from rest_framework import serializers

from nba_news.models import New


class NewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = [
            'unique_id',
            'title',
            'content',
            'image_link',
        ]
