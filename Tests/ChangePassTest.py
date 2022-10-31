import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.LogPage import LogPage            # page name then class name of this page
from Pages.BasePage import BasePage
from Pages.LeftTopBarPage import leftTopBarPage          # class name of this page


class LoginTestc(BasePage):

    def test_leftTopBarrPage(self):
        md = leftTopBarPage(self.driver)
        lp = LoginPage(self.driver)
        log = LogPage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)


        # change password
        md.navigate0()
        time.sleep(3)

        md.pencil()
        time.sleep(8)

        md.pancilallow()
        time.sleep(3)

        md.pencil1()
        time.sleep(3)

        md.changepass()
        time.sleep(8)

        md.oldpass("123456789")
        time.sleep(3)

        md.newpass("123456789")
        time.sleep(3)

        md.confirmpass("123456789")
        time.sleep(3)

        md.cancelpass()
        time.sleep(8)

        md.backtopreviouspage100()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
