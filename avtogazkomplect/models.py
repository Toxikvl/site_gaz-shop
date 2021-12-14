from django.db import models
import PIL
class Blog(models.Model):
    title=models.CharField(max_length=100, db_index=True,verbose_name='Заголовок')
    description=models.TextField(default='',verbose_name='описание')
    image = models.ImageField(blank=True, upload_to='', verbose_name='Ссылка картинки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0,verbose_name='количество просмотров')

    def __str__(self):
        return self.title

