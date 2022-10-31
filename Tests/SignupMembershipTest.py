import time
from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.MiddleLeftBarPage import middleLeftBarPage #class name of this page


class LoginTestsi(BasePage):

    def test_MiddleLeftBarPage(self):
        md = middleLeftBarPage(self.driver)
        log = LogPage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)

        # signup for a membership plan
        md.signupmembership()
        time.sleep(3)
        md.signupmembershipok()
        time.sleep(3)
        md.backtopreviouspage12()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()