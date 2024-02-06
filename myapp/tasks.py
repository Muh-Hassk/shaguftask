# myapp/tasks.py
from celery import shared_task
from .utils import fetch_and_insert_data

@shared_task
def sync_data():
    fetch_and_insert_data()
