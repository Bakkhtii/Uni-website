from django.db import models


class CategoryModel(models.Model):
    University_title = models.CharField(max_length= 30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.University_title

    class Meta:
        verbose_name = 'BG University'
        verbose_name_plural = 'University catalog'


class UniversityModel(models.Model):
    University_title = models.CharField(max_length=50, help_text='Write')
    University_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    University_description = models.TextField()
    University_image = models.FileField(upload_to='University_images')
    University_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.University_title

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Info for categories'