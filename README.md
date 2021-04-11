# Task Rabbit
A containerized framework for asynchronous tasks with Python Celery, RabbitMQ, and Reddis

## Technologies:
* Python 3.9
* Celery==5.0.5
* RabbitMQ (latest Docker image)
* Reddis (latest Docker image)

## Framework
1. Edit the environment variables accordingly in ```docker-compose.yml```. RABBITMQ_PASS and RABBITMQ_USER are the password and username for the RABBITMQ connection, CONCURRENCY is the number of workers running the tasks concurrently, and LOGLEVEL is the desired logging level for celery.
2. Add your task methods to ```consumer.py```. The current example task returns the sum of two given numbers.
3. Import your task(s) in ```producer.py``` and invoke the task(s) as desired. The current example imports and executes the add task.

Other Notes: Celery and the producer's stderr and stdout is redirected to ```/var/log/celery.log``` and ```/var/log/app.log``` respectively within the container. These paths can be changed (or removed entirely) in ```conf/supervise-celery.conf``` and ```conf/supervise-producer.conf```.

## Building and Running
``` bash
docker-compose build && docker-compose up -d
```
