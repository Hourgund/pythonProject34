import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SimpleGoogleTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def testSearchSelenium(self):
        expected_title = "Selenium"

        self.driver.get("https://google.com")
        question_input = self.driver.find_element(By.NAME, "q")
        question_input.send_keys("Selenium")
        question_input.send_keys(Keys.ENTER)

        # selenium_link =
        # self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
        # selenium_link.click()

        actual_title = self.driver.title

        self.assertIn(expected_title, actual_title)
