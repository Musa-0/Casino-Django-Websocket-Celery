import asyncio

from celery.signals import worker_ready

from Core.main_program import main_casino_worker
from RedBlue.celery import app


@worker_ready.connect
def pusk_main_casino(sender, **kwargs):
    with sender.app.connection() as conn:
         sender.app.send_task('Core.tasks.start_main_casino',connection=conn)

@app.task
def start_main_casino():
    asyncio.run(main_casino_worker())

