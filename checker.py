
from selenium.webdriver.common.by import By
import re
import os

LAST_SEEN_FILE = "last_seen.txt"

def read_last_seen():
    if not os.path.exists(LAST_SEEN_FILE):
        return ""
    with open(LAST_SEEN_FILE, "r") as f:
        return f.read().strip()

def write_last_seen(timestamp):
    with open(LAST_SEEN_FILE, "w") as f:
        f.write(timestamp)

def has_new_post(driver):
    elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Posted')]")
    for el in elements:
        match = re.search(r"Posted (\d{2}/\d{2}/\d{4}, \d{2}:\d{2})", el.text)
        if match:
            current = match.group(1)
            last_seen = read_last_seen()
            if current != last_seen:
                write_last_seen(current)
                return current
    return None
