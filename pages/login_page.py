from selenium.webdriver.common.by import By
from base_page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """
        Login Page Locators
    """
    email_field = (By.NAME, "email")
    password_field = (By.NAME, "password")
    login_btn =(By.XPATH, '//*[@id="form"]//button')
    email_error_msg = (By.XPATH, '//*[@name="email"]/..//../../p')
    password_error_msg = (By.XPATH, '//*[@name="password"]/..//../../p')

    def enter_creds(self, login, password):
        self.enter_text(self.email_field, login)
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.click(self.login_btn)

    def get_email_error_msg(self):
        return self.get_text(self.email_error_msg)

    def get_password_error_msg(self):
        return self.get_text(self.password_error_msg)
