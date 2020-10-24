import schedule
import time
import os


def job():
    os.system('scrapy crawl ponisha')


schedule.every(10).hours.do(job)


job()
while True:
    schedule.run_pending()
    time.sleep(1)
