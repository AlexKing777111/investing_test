import random
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from base_app import BasePage


class Locators:
    LOCATOR_NAV = (By.XPATH, "//*[@id='navMenu']/ul/li[1]/a")
    LOCATOR_STOKS = (By.XPATH, '//*[@id="navMenu"]/ul/li[1]/ul/li[4]/a')
    LOCATOR_RUSSIAN_STOCKS = (
        By.XPATH,
        '//*[@id="navMenu"]/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a',
    )
    LOCATOR_STOCKS_TYPE = (By.ID, "stocksFilter")
    LOCATOR_ALL_STOCKS_RUSSIA = (By.ID, "all")
    LOCATOR_STOCKS_TABLE = (
        By.XPATH,
        "//*[@id='cross_rate_markets_stocks_1']/tbody/tr",
    )
    LOCATOR_STOCK_NAME = (
        By.XPATH,
        '//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[1]/div[1]/h1',
    )


class SearchHelper(BasePage):
    def open_russian_stocks(self):
        main_menu = self.find_element(Locators.LOCATOR_NAV, time=2)
        to_main_menu = ActionChains(self.driver).move_to_element(main_menu)
        to_main_menu.perform()
        stocks = self.find_element(Locators.LOCATOR_STOKS, time=2)
        to_stocks = ActionChains(self.driver).move_to_element(stocks)
        to_stocks.perform()
        russian_stocks = self.find_element(
            Locators.LOCATOR_RUSSIAN_STOCKS, time=2
        )
        russian_stocks.click()
        return main_menu

    def choice_stock_type(self):
        select_stoks_type = self.find_element(
            Locators.LOCATOR_STOCKS_TYPE, time=2
        )
        select_stoks_type.click()
        self.find_element(Locators.LOCATOR_ALL_STOCKS_RUSSIA, time=2).click()
        time.sleep(5)
        return select_stoks_type

    def choice_random_stock(self):
        stocks_list = self.find_elements(Locators.LOCATOR_STOCKS_TABLE, time=2)
        count_stocks = len(stocks_list)
        assert count_stocks > 0, "No stocks at action list."
        random_index = random.randint(0, count_stocks)
        random_line = stocks_list[random_index]
        line_id = random_line.get_attribute("id")
        locator_random_stock = (By.XPATH, f'//*[@id="{line_id}"]/td[2]/a')
        random_stock = self.find_element(locator_random_stock, time=2)
        random_stock_text = random_stock.get_attribute("title").replace(
            "  ", " "
        )
        random_stock.click()
        header = self.find_element(Locators.LOCATOR_STOCK_NAME, time=2)
        header_text = header.text.split("(")[0].strip()
        assert (
            random_stock_text == header_text
        ), f"{random_stock_text} != {header_text}"
        return random_stock
