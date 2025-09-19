from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)  # 문자를 담는 필드, 최대 길이 30
    content = models.TextField()  # 문자열의 길이 제한이 없는 텍스트 필드

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author: 추후 작성 예정

    # pk: 해당 포스트의 pk값
    # title: 해당 포스트의 title값
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
