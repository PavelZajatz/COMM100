import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        """Clicks the specified object"""
        self.implicit_wait(0.5)
        element = self.driver.find_element(*locator)
        element.click()

    def get_text(self, locator):
        self.implicit_wait(0.5)
        element = self.driver.find_element(*locator)
        return element.text

    def enter_text(self, locator, keys):
        self.implicit_wait(0.5)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(keys)

    def implicit_wait(self, wait_time):
        time.sleep(wait_time)
