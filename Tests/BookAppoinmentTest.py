import time
from Pages.LogPage import LogPage
from Pages.BasePage import BasePage
from Pages.MiddleLeftBarPage import middleLeftBarPage #class name of this page


class LoginTestbo(BasePage):

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


        md.book()
        time.sleep(3)
        md.service()
        time.sleep(3)
        md.familyphysicans()
        time.sleep(3)
        md.liketosee()
        time.sleep(3)
        md.taslima()
        time.sleep(3)
        md.backtopreviouspage7()
        time.sleep(3)
        md.backtopreviouspage8()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
