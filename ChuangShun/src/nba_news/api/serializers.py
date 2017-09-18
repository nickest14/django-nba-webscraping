from rest_framework import serializers

from nba_news.models import New


class NewModelSerializer(serializers.ModelSerializer):

    date_display = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = [
            'unique_id',
            'title',
            'content',
            'image_link',
            'date_display',
        ]
    def get_date_display(self, obj):
        return obj.created_date.strftime("%Y, %b %d")
