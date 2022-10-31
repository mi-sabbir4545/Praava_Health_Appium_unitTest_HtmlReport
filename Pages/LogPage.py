from Pages.HomePage import HomePage
from Locators.Locators import LogIn


class LogPage(HomePage):

    def __init__(self, driver):
        self.locator = LogIn
        self.driver = driver
        super(LogPage, self).__init__(driver)

    #LOGIN
    def loginuser(self):
        # self.driver.find_element(*self.locator.login_user_ID).clear()
        self.driver.find_element(*self.locator.loginuser_ID).send_keys("01408290385")

    def loginpass(self):
        # self.driver.find_element(*self.locator.login_pass_ID).clear()
        self.driver.find_element(*self.locator.loginpass_ID).send_keys("Tonoy123")

    def login(self):
        self.driver.find_element(*self.locator.login_ID).click()
