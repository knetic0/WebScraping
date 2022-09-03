from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"chromedriver")
url = "https://www.bundle.app/gundem"
driver.get(url)
SCROLL_PAUSE_TIME = 0.5

print(driver.title)

def Start():
    last_height = driver.execute_script("return document.body.scrollHeight")
    timer_loop = 0
    try:
        while True:
            elements = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "nnewsSliderCardTitle"))
            )

            sources = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "newsSliderSource"))
            )
            time.sleep(2)

            # scroll page
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height or timer_loop == 9:
                break
            timer_loop = timer_loop + 1
    finally:
        timer = 0
        for value in elements[3:]:   
            if value.text: 
                print(sources[timer].text, "\n", value.text, "\n")
            timer += 1   

if __name__ == "__main__":
    Start()

