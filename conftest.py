import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

main_url = "https://secure.comm100.com/signin"


@pytest.fixture(scope='function')
def driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://selenium.dev/')
    request.cls.driver = driver
    driver.get(main_url)
    yield
    driver.quit()
