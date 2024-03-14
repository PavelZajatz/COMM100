import pytest
from base_page.base_test import BaseTest
from pages.login_page import LoginPage


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def driver_parse(self, driver):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize("email, password, email_err, pass_err", [
        ("", "", "Email cannot be empty.", "Password cannot be empty."),
        ("user", "Admin12345!", "Email address is invalid.", None)
    ])
    def test_incorrect_creds(self, email, password, email_err, pass_err):
        self.login_page.enter_creds(email, password)
        self.login_page.click_login()
        assert self.login_page.get_email_error_msg() == email_err, \
            f"Should be email error message - '{self.login_page.get_email_error_msg()}' but '{email_err}' is shown"
        if pass_err is not None:
            assert self.login_page.get_password_error_msg() == pass_err, \
                f"Should be pass error message - '{self.login_page.get_password_error_msg()}' but '{pass_err}' is shown"
