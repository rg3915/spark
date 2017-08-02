from django.db import models
from django.shortcuts import resolve_url as r
from django.utils.text import slugify
from spark.authentication.models import Profile


class Course(models.Model):
    name = models.CharField('nome', max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    photo = models.URLField('foto', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Course, self).save()


class Classe(models.Model):
    team = models.CharField('turma', max_length=50)
    course = models.ForeignKey(
        Course, verbose_name='curso', related_name='classe_course')
    date_initial = models.DateField('data inicial', null=True, blank=True)
    date_final = models.DateField('data final', null=True, blank=True)
    short_description = models.CharField(
        'breve descrição', max_length=50, null=True, blank=True)
    description = models.TextField('descrição', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ('team',)
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def __str__(self):
        return self.team

    def get_absolute_url(self):
        return r('classe_detail', slug=self.slug)

    def save(self):
        self.slug = slugify('%s-%s' % (self.course, self.team))
        super(Classe, self).save()

    def matriculated(self):
        qs = self.classedetail.values_list('user', flat=True)
        return [q for q in qs]


class ClasseDetail(models.Model):
    classe = models.ForeignKey(Classe, related_name='classedetail')
    user = models.ForeignKey(
        Profile, verbose_name='aluno', related_name='classedet_user')

    class Meta:
        ordering = ('classe',)
        verbose_name = 'detalhe'
        verbose_name_plural = 'detalhes'

    def __str__(self):
        return str(self.classe)
