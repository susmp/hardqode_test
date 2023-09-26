from rest_framework import serializers
from .models import Lesson, LessonView, Product

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration_seconds')

class LessonViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer() 
    class Meta:
        model = LessonView
        fields = ('id', 'user', 'lesson', 'view_time_seconds', 'is_watched')

class ProductStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'