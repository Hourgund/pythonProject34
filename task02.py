import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    url = "https://www.google.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

   # time.sleep(5)

    question_input = driver.find_element(By.NAME, "q")
    question_input.send_keys("Selenium")
    question_input.send_keys(Keys.ENTER)

    time.sleep(5)

    # driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
