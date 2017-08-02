from django.db import models


class Task(models.Model):
    task = models.CharField('tarefa', max_length=50)
    module = models.CharField('módulo', max_length=50)

    class Meta:
        ordering = ('task',)
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return self.task
