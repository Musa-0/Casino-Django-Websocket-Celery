import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedBlue.settings')

app = Celery('RedBlue')#создаем объект селери и задаем ему имя
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


#создаем надстройку, вызывать каждые пять минут таск по рассылке писем всем клиентам
app.conf.beat_schedule = {
    'take-bitcoin-data':{#имя таска
        'task': 'Account.tasks.clear_verifications_code',#путь к самому таску
        'schedule': timedelta(minutes=1),#периодичность отправки (*/ - каждые, 5 - пять минут)
    },
}