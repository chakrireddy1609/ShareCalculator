import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self,driver):
        self.driver = driver

    search_box = (By.NAME, 'q')
    display_price = (By.XPATH,"//span[@jsname='vWLAgc']")

    def send_share_name(self,name):
        return self.driver.find_element(*SearchPage.search_box).send_keys(name)

    def click_enter(self):
        return self.driver.find_element(*SearchPage.search_box).send_keys(Keys.ENTER)

    def find_present_price(self, count_of_shares, actual_price):
        display_price = self.driver.find_element(*SearchPage.display_price).text
        display_price = display_price.replace(",", "")
        display_price = float(display_price)
        profit = count_of_shares*(display_price - actual_price)
        return profit

    def search_clear(self):
        return self.driver.find_element(*SearchPage.search_box).clear()