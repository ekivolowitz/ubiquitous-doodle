from star_tides.create_app import celery_app as celery
import os

@celery.task()
def add_numbers(one, two):
    return 5
