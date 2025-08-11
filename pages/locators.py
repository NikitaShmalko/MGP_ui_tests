from selenium.webdriver.common.by import By

class ProjectLocators:
    SEARCH_BAR = (By.XPATH, '//input[@class="input-search__input input-text input-text_size_s input-text_fill ui-autocomplete-input"]')
    SEARCH_BTN = (By.XPATH, '//button[@class="input-search__button button"]')
    PRODUCT_CART_IN_SEARCH = (By.XPATH, '//a[@class="product-thumb__name link link_style_hover"]')
    ADD_TO_CART_BTN = (By.XPATH, '//button[@class="product-add-to-cart__button add-to-cart button button_size_l button_fill"]')
    GO_TO_CART_BTN = (By.XPATH, '//a[@class="button button_size_l cart-item-modal__button"]')
    PRODUCT_NAME_IN_CART = (By.XPATH, '//a[@class="wa-name link link_style_hover"]')
    TOTAL_PRICE_IN_CART = (By.XPATH, '//span[@class="wa-price js-price"]')


