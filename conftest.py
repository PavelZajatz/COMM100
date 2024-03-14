import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

main_url = "https://secure.comm100.com/signin"


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('http://selenium.dev/')
    request.cls.driver = driver
    driver.get(main_url)
    yield
    driver.quit()
