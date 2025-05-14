
import schedule
import time
from login import login_and_navigate
from checker import has_new_post
from notify import send_notification

def job():
    browser = login_and_navigate()
    new_post_time = has_new_post(browser)
    if new_post_time:
        send_notification(f"🆕 Nový příspěvek zveřejněn: {new_post_time}")
    browser.quit()

schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
