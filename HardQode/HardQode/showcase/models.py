from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product)

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_seconds = models.PositiveIntegerField()
    is_watched = models.BooleanField(default=False)

    def check_watched_status(self):
        if (self.view_time_seconds / self.lesson.duration_seconds) >= 0.8:
            self.is_watched = True
        else:
            self.is_watched = False
        self.save()