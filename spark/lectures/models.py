from django.db import models
from django.shortcuts import resolve_url as r
from django.utils.text import slugify
from spark.courses.models import Course


class Lecture(models.Model):
    title = models.CharField('título', max_length=50)
    course = models.ForeignKey(Course,
                               verbose_name='cursos',
                               related_name='lecture_course')
    description = models.TextField('descrição', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    position = models.SmallIntegerField('posição', default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'leitura'
        verbose_name_plural = 'leituras'

    def __str__(self):
        return str(self.course)

    def get_absolute_url(self):
        return r('lecture_detail', pk=self.pk)

    def save(self):
        self.slug = slugify('%s-%s' % (self.course, self.title))
        ''' Replace text in url '''
        self.url = self.url.replace('watch?v=', 'embed/')
        super(Lecture, self).save()
