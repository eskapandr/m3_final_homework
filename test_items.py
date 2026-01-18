from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_find_button_add_item_to_basket(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )

    assert button, "Кнопка добавления товара в корзину отсутствует"