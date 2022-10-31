import time

from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.LeftTopBarPage import leftTopBarPage#class name of this page


class LoginTestmy(BasePage):

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


        # My appointments
        md.navigate()
        time.sleep(3)
        md.myappointmentys()
        time.sleep(8)
        md.pastappoint()
        time.sleep(3)
        md.backtopreviouspage4()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()