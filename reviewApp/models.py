from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
#태그 기능 모듈
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description= models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    create_dt= models.DateField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateField('MODIFY DATE', auto_now = True)
    tags = TaggableManager(blank=True)
    class Meta:
        verbose_name = 'post'
        verbose_name_plural='posts'
        db_table = 'review_posts'
        ordering=('-modify_dt',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('review:post_detail', args=(self.slug,))
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    def get_next(self):
        return self.get_next_by_modify_dt()

    #게시글 작성자이름 불러오는 함수
    def get_owner_name(self):
        return self.owner
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


