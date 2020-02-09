from django.db import models
import datetime


def get_default_title():
    return 'Заметка создана ' + datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y %H:%M')


class Board(models.Model):
    title = models.CharField(max_length=256, default=get_default_title())
    body = models.TextField()
    reg_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True, null=True)

    def __repr__(self):
        return f'<{self.title}>'
