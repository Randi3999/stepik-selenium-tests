import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    def test_button_add_to_basket_is_present(self, browser):
        """Проверяет, что на странице товара есть кнопка добавления в корзину."""
        # 1. Открываем страницу товара
        browser.get(LINK)
        
        # 2. Принудительная задержка для визуальной проверки языка (требование критерия)
        time.sleep(30) 
        
        # 3. Ищем кнопку добавления в корзину по уникальному CSS-селектору
        # Селектор взят из реальной верстки страницы
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        
        # 4. Проверяем, что кнопка существует
        assert button is not None, "Кнопка добавления в корзину не найдена!"
