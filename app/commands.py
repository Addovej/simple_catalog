from flask import current_app as app


@app.cli.command('sync-data')
def sync_data_cli():
    from app.tasks import sync_data

    print('Sync data was launched')
    sync_data.apply_async()
