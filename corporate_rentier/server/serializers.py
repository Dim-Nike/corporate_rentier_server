from rest_framework import serializers
from .models import *


class DignitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dignities
        fields = ['id', 'name', 'dsc']

class ServicesSerializer(serializers.ModelSerializer):
    included_in_the_service = DignitiesSerializer(many=True, read_only=True)
    class Meta:
        model = Services
        fields = ['id', 'name', 'category', 'dsc', 'included_in_the_service']

class DcsCatServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcsCatServices
        fields = ['id', 'category', 'name', 'dsc']





class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    quotes = QuotesSerializer(many=True, read_only=True)
    photo_realization = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ['id', 'name', 'category_services', 'bw_preview_photo',
                  'c_preview_photo', 'title_photo', 'dsc_project', 'dsc_task',
                  'photo_task', 'dsc_realization', 'photo_realization', 'quotes']

    def get_photo_realization(self, obj):
        request = self.context.get('request')
        if obj.photo_realization:
            return request.build_absolute_uri(obj.photo_realization)
        return None

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'



