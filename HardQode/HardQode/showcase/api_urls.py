from django.urls import path
from . import views

urlpatterns = [
    # Маршруты API
    path('lesson-list/', views.LessonListView.as_view(), name='lesson-list'),
    path('product/<int:product_id>/lessons/', views.LessonViewList.as_view(), name='product-lessons-list'),
    path('api/product-stats/', views.ProductStatsView.as_view(), name='product-stats'),
    
]
