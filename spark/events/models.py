from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from spark.activities.models import Activity


class Event(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField('título', max_length=200)
    date_start = models.DateField('data')
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)
    address = models.TextField('local', null=True, blank=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ('date_start',)
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'

    def __str__(self):
        return self.title

    @staticmethod
    def get_events(from_event=None):
        if from_event is not None:
            events = Event.objects.filter(id__lte=from_event)
        else:
            events = Event.objects.all()
        return events

    @staticmethod
    def get_events_after(event):
        events = Event.objects.filter(id__gt=event)
        return events

    def calculate_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk).count()
        self.likes = likes
        self.save()
        return self.likes

    def get_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk)
        return likes

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers


class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    date_start = models.DateField('data')
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField(
        'Speaker', verbose_name='palestrantes', blank=True)

    # objects = PeriodManager()

    class Meta:
        ordering = ['start']
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
