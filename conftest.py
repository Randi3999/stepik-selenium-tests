import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавляет опцию --language для выбора языка интерфейса."""
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, fr, es, etc.')

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера Chrome с указанным языком."""
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции Chrome для установки языка
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })
    
    print(f"\nstart chrome browser for test with language: {user_language}..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)  # Неявное ожидание для стабильности
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()
