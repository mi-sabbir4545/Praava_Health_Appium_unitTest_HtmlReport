import time

from Pages.LoginPage import HomePage
from Pages.LogPage import LogPage
from Pages.BasePage import BasePage
from Pages.LeftTopBarPage import leftTopBarPage #class name of this page


class LoginTestl(BasePage):

    def test_leftTopBarrPage(self):
        md = leftTopBarPage(self.driver)
        log = LogPage(self.driver)
        hm = HomePage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)

        # LogOut
        md.navigate3()
        time.sleep(3)

        hm.scroll_down(2249, 1134)
        md.logout()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()