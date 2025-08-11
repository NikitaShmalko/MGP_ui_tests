import selenium
import pytest
from selenium import webdriver
from pages.add_to_cart import AddToCart


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()

@pytest.fixture
def cart(driver):
    return AddToCart(driver)

@pytest.fixture
def base_url():
    return 'https://m-g-p.ru/'