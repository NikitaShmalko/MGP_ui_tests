import pytest
import allure

@allure.title('Тест добавления товара в корзину')

@pytest.mark.parametrize('product_name, product_price',[
    ('ВЕ 6.34', '3 900'),
    ('ВЕ 10.574', '4 800')
])
def test_add_to_cart(cart, base_url,product_name, product_price):
    with allure.step('Запускам браузер и загружаем главную страницу сайта'):
        cart.load(base_url)

    with allure.step('Ищем и добавляем товар в корзину'):
        cart.add_to_cart_actions(product_name)

    with allure.step('Проверяем, что в корзине правильно отображаются цена и название товара'):
        text = cart.get_text_from_cart()
        assert product_price in text['price']
        assert product_name in text['name']

