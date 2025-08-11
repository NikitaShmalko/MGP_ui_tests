import pytest
import selenium
from selenium import webdriver
from pages.add_to_cart import AddToCart

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def cart(driver):
    return AddToCart(driver)

@pytest.fixture
def base_url():
    return 'https://m-g-p.ru/'