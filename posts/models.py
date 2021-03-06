from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


    '''
    # https://qiita.com/okoppe8/items/86776b8df566a4513e96
    attach = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf', ])],
    )

    url_height = models.IntegerField(
        editable=False,
    )

    url_width = models.IntegerField(
        editable=False,
    )
    '''


    def __str__(self):
        return self.title


# https://narito.ninja/blog/detail/55/
class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title
