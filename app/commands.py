from flask import current_app as app

from app.tasks import sync_data


@app.cli.command('sync-data')
def sync_data_cli():
    """
        Sync data
    """

    sync_data.appy_async()
