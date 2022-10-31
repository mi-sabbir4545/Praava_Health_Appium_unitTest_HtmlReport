from Pages.HomePage import HomePage
from Locators.Locators import LogIn


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = LogIn
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    # signup
    def click_signup(self):
        self.driver.find_element(*self.locator.signup_XPATH).click()

    def mobile(self, mobile):
        # self.driver.find_element(*self.locator.mobile_ID).clear()
        self.driver.find_element(*self.locator.mobile_ID).send_keys(mobile)

    def username(self, username):
        # self.driver.find_element(*self.locator.username_ID).clear()
        self.driver.find_element(*self.locator.username_ID).send_keys(username)

    def password(self, password):
        # self.driver.find_element(*self.locator.password_ID).clear()
        self.driver.find_element(*self.locator.password_ID).send_keys(password)

    def repassword(self, repassword):
        # self.driver.find_element(*self.locator.repassword_ID).clear()
        self.driver.find_element(*self.locator.repassword_ID).send_keys(repassword)

    def email(self, email):
        # self.driver.find_element(*self.locator.email_ID).clear()
        self.driver.find_element(*self.locator.email_ID).send_keys(email)

    def login0(self):
        self.driver.find_element(*self.locator.login0_ID).click()

    # forget password
    def forgetpass(self):
        self.driver.find_element(*self.locator.forgetpass_ID).click()

    def forgetusername(self, forgetusername):
        # self.driver.find_element(*self.locator.forgetusername_ID).clear()
        self.driver.find_element(*self.locator.forgetusername_ID).send_keys(forgetusername)

    def login1(self):
        # self.driver.find_element(*self.locator.login1_ID).clear()
        self.driver.find_element(*self.locator.login1_ID).click()

    # forget user name / mobile
    def forgetusern(self):
        self.driver.find_element(*self.locator.forgetusern_ID).click()

    def forgetusermob(self, forgetusermob):
        # self.driver.find_element(*self.locator.forgetusermob_ID).clear()
        self.driver.find_element(*self.locator.forgetusermob_ID).send_keys(forgetusermob)

    def login2(self):
        # self.driver.find_element(*self.locator.forgetusermob_ID).clear()
        self.driver.find_element(*self.locator.login2_ID).click()


