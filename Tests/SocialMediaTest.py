import time

from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.LeftTopBarPage import leftTopBarPage#class name of this page


class LoginTests(BasePage):

    def test_leftTopBarrPage(self):
        md = leftTopBarPage(self.driver)
        log = LogPage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)

        # social media
        md.navigate2()
        time.sleep(3)
        md.socialmedia()
        time.sleep(8)
        md.fb()
        time.sleep(3)
        md.backtopreviouspage6()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()