# tasks.py
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def long_task(n):
    import time
    time.sleep(n)
    return f"{n}초 후 완료됨"
