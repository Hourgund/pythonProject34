import time
from selenium import webdriver


def main():
    url = "https://www.python.org"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    time.sleep(5)

    # driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
