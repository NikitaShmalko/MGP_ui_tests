import selenium
import tempfile, shutil, pytest
from selenium import webdriver
from pages.add_to_cart import AddToCart


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    # уникальная папка профиля на каждый тест
    user_data_dir = tempfile.mkdtemp(prefix="chrome-profile-")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
        shutil.rmtree(user_data_dir, ignore_errors=True)

@pytest.fixture
def cart(driver):
    return AddToCart(driver)

@pytest.fixture
def base_url():
    return 'https://m-g-p.ru/'