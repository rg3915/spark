from django.db import models
from spark.courses.models import Course


class Video(models.Model):
    course = models.ForeignKey(Course,
                               verbose_name='cursos',
                               related_name='video_course')
    url = models.URLField()
    position = models.SmallIntegerField('posição', default=0)

    class Meta:
        # ordering = ('-created',)
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return str(self.course)

    def save(self, *args, **kwargs):
        ''' Replace text in url '''
        self.url = self.url.replace('watch?v=', 'embed/')
        super(Video, self).save(*args, **kwargs)
