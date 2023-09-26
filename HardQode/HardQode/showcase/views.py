from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ProductAccess
from .serializers import *

class LessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        
        products = ProductAccess.objects.filter(user=user).values_list('product', flat=True)
        
        lessons = Lesson.objects.filter(products__in=products)
        
        lesson_views = LessonView.objects.filter(user=user, lesson__in=lessons)
        return lesson_views
    

class LessonViewList(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']  
        
        
        if not ProductAccess.objects.filter(user=user, product_id=product_id).exists():
            return LessonView.objects.none()

        
        lesson_views = LessonView.objects.filter(lesson__products=product_id, user=user)

        return lesson_views
    
class ProductStatsView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer

    def get_queryset(self):
        # Получите список всех продуктов
        products = Product.objects.all()

        # Получите статистику по каждому продукту
        product_stats = []
        for product in products:
            # Количество просмотренных уроков от всех учеников
            total_watched_lessons = LessonView.objects.filter(lesson__products=product, is_watched=True).count()

            # Общее время, потраченное всеми учениками на просмотр роликов
            total_time_watched = LessonView.objects.filter(lesson__products=product, is_watched=True).aggregate(Sum('view_time_seconds'))['view_time_seconds__sum']

            # Количество учеников, занимающихся на продукте
            total_students = ProductAccess.objects.filter(product=product).count()

            # Процент приобретения продукта
            total_users = User.objects.count()
            product_access_count = ProductAccess.objects.filter(product=product).count()
            acquisition_percentage = (product_access_count / total_users) * 100 if total_users > 0 else 0

            product_stat = {
                'product': product,
                'total_watched_lessons': total_watched_lessons,
                'total_time_watched': total_time_watched,
                'total_students': total_students,
                'acquisition_percentage': acquisition_percentage,
            }

            product_stats.append(product_stat)

        return product_stats
