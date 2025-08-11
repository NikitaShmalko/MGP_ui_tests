from pages.basepage import BasePage
from pages.locators import ProjectLocators


class AddToCart(BasePage):
    def add_to_cart_actions(self, product_name):
        self.send_keys(ProjectLocators.SEARCH_BAR, product_name)
        self.click(ProjectLocators.SEARCH_BTN)
        self.click(ProjectLocators.PRODUCT_CART_IN_SEARCH)
        self.click(ProjectLocators.ADD_TO_CART_BTN)
        self.click(ProjectLocators.GO_TO_CART_BTN)

    def get_text_from_cart(self):
        self.take_screenshot()
        name = self.get_text(ProjectLocators.PRODUCT_NAME_IN_CART)
        price = self.get_text(ProjectLocators.TOTAL_PRICE_IN_CART)

        return {
            'name':name,
            'price':price
        }