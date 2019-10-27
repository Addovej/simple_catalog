from celery.schedules import crontab


class CeleryConfig(object):
    """
        Celery config.
    """

    CELERY_IMPORTS = ('app.tasks',)
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'

    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    CELERYBEAT_SCHEDULE = {
        'get_data': {
            'task': 'app.tasks.get_data',
            # Every day
            'schedule': crontab(minute=0, hour=0),
            # 'schedule': crontab(minute='*/15'),
        }
    }
