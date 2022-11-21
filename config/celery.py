import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Configure redis as the broker
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

app.autodiscover_tasks()

# Configure celery beat
app.conf.beat_schedule = {
    'send-daily-stats': {
        'task': 'apps.dailystat.tasks.send_daily_stats',
        'schedule': crontab(hour=0, minute=22, day_of_week='*'),
    },
}
