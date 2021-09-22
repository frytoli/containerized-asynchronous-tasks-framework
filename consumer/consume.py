#!/usr/bin/env python

from celery import Celery
import time
import os

# Define the celery app
app = Celery(
    'myApp',
    broker=f'''amqp://{os.getenv('BROKER_USER')}:{os.getenv('BROKER_PASS')}@{os.getenv('BROKER_HOST')}:{os.getenv('BROKER_PORT')}''',
    backend=f'''rpc://{os.getenv('BACKEND_HOST')}:{os.getenv('BACKEND_PORT')}'''
)

@app.task(name='square')
def square(a):
    # Sleep a little to emulate a longer-running task
    time.sleep(10)
    # Perform the task and return the result
    print(f'{a} squared is {a**2}')
    return a**2
