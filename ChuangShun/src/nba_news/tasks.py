from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests

@shared_task
def hello_world():
    with open("output.txt", "a") as f:
        f.write("hello world")
        f.write("\n")

@shared_task
def update_news():
    url2="https://nick-nba-scraping.herokuapp.com/nba-news/"
    url = "http://localhost:8000/nba-news"
    requests.get(url)
    requests.get(url2)
