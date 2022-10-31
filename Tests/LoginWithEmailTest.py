import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.LogPage import LogPage


class LoginTest(BasePage):
    def test_login_page(self):
        log = LogPage(self.driver)

        time.sleep(5)
        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()

if __name__ == "__main__":
    unittest.main()