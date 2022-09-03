from rest_framework import serializers

from Themes.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['pk', 'title', 'type_lesson']