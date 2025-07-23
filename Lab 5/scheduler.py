import schedule
import time
from main import run_pipeline

def start_scheduler():
    schedule.every().day.at("08:00").do(run_pipeline)
    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(60)
        