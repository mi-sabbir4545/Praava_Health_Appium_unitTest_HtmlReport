import time
from Pages.LogPage import LogPage
from Pages.BasePage import BasePage
from Pages.MiddleLeftBarPage import middleLeftBarPage #class name of this page


class LoginTestb(BasePage):

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

        # Annual Membership plan
        md.bookhealth()
        time.sleep(3)
        md.annualplan()
        time.sleep(3)
        md.viewdetils()
        time.sleep(3)
        md.ecg()
        time.sleep(3)
        md.booked()
        time.sleep(3)
        md.backtopreviouspage9()
        time.sleep(3)

        # health check
        md.healthcheck()
        time.sleep(3)
        md.diabetesviewdetails()
        time.sleep(3)
        md.booked1()
        time.sleep(3)
        md.backtopreviouspage10()
        time.sleep(3)
        md.backtopreviouspage11()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()