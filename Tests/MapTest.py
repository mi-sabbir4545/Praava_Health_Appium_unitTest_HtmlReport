import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.MiddleLeftBarPage import middleLeftBarPage #class name of this page


class LoginTestm(BasePage):

    def test_MiddleLeftBarPage(self):
        md = middleLeftBarPage(self.driver)
        lp = LoginPage(self.driver)
        log = LogPage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)

        # signup for a membership plan
        md.map()
        time.sleep(3)
        md.mapallow()
        time.sleep(8)
        md.backtopreviouspage13()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()