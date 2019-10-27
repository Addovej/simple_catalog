from app.celery import celery_app
from app.utils.csv import SyncDataFromFile


@celery_app.task(name='app.tasks.sync_data')
def sync_data():
    sync = SyncDataFromFile()
    sync.run()
