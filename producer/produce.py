#!/usr/bin/env python

from celery import Celery
import os

# Define the celery app
app = Celery(
    'myApp',
    broker=f'''amqp://{os.getenv('BROKER_USER')}:{os.getenv('BROKER_PASS')}@{os.getenv('BROKER_HOST')}:{os.getenv('BROKER_PORT')}''',
    backend=f'''rpc://{os.getenv('BACKEND_HOST')}:{os.getenv('BACKEND_PORT')}'''
)

def main():
    # Create an empty list to record task instances
    tasks = []
    # Send your tasks off to the queue
    for i in range(10):
        tasks.append(
            # Send a task to the queue by name (see line 14 in consumer/consume.py)
            # Note that task arguments must be a list or tuple
            app.send_task('square', (i,))
        )

    # Retrieve results
    for task in tasks:
        print(f'Task Result: {task.get()}')

if __name__ == '__main__':
    main()
