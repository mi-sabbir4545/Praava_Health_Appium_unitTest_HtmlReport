import time

from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.MiddlerightBarPage import middleRightBarPage  # class name of this page


class LoginTestli(BasePage):

    def test_MiddlerightBarPage(self):
        md = middleRightBarPage(self.driver)
        log = LogPage(self.driver)
        time.sleep(5)

        log.loginuser()
        time.sleep(3)
        log.loginpass()
        time.sleep(3)
        log.login()
        time.sleep(5)

        md.linkfamilysaccount()
        time.sleep(3)
        md.linkfamilysaccountok()
        time.sleep(3)
        md.addprofile()
        time.sleep(3)
        md.pbhl()
        time.sleep(3)
        self.driver.back()
        md.add()
        time.sleep(3)
        md.cross()
        time.sleep(3)
        md.backtopreviouspage1()
        time.sleep(3)

        md.serve()
        time.sleep(3)
        md.addmemberok()
        time.sleep(3)
        md.backtopreviouspage2()
        time.sleep(3)

        md.contactus()
        time.sleep(3)
        md.contactallow()
        time.sleep(3)
        md.backtopreviouspage3()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()