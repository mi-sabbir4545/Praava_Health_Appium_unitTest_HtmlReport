import time
from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.HomePage import HomePage
from Pages.MiddlerightBarPage import middleRightBarPage  # class name of this page


class LoginTestr(BasePage):

    def test_MiddlerightBarPage(self):
        md = middleRightBarPage(self.driver)
        log = LogPage(self.driver)
        hm = HomePage(self.driver)
        time.sleep(5)

        log .loginuser()

        log .loginpass()

        log .login()


        md.register()
        time.sleep(3)
        md.reg_fstname("Tonoy")
        time.sleep(3)
        hm.scroll_down1(1089, 381)

        md.reg_middlename("Kumar")
        time.sleep(3)
        md.reg_lastname("Saha")
        time.sleep(3)
        md.dateofbirth()
        time.sleep(3)
        md.date_ok_ID()
        time.sleep(3)
        md.email_ID("saha.qups@gmail.com")
        time.sleep(3)
        hm.scroll_down2(1154, 197)

        md.selectgender()
        time.sleep(3)
        md.gendercancel()
        time.sleep(3)
        md.nationality("BANGLADESHI")
        time.sleep(3)
        md.selectstatus()
        time.sleep(3)
        md.statuscancel()
        time.sleep(3)
        hm.scroll_down3(1350, 544)

        md.selectoccupation()
        time.sleep(3)
        md.occupationcancel()
        time.sleep(3)
        hm.scroll_down3(1470, 730)
        md.phnnmbr("01736457478")
        time.sleep(3)
        md.address("Dhaka banasree")
        time.sleep(3)
        hm.scroll_down3(1150, 344)
        md.city("Dhaka")
        time.sleep(3)
        md.state("Dhaka")
        time.sleep(3)
        md.country("Bangladesh")
        time.sleep(3)
        md.postalcode("1219")
        time.sleep(3)
        hm.scroll_down4(1244, 544)

        md.emergncycontact("Saha")
        time.sleep(3)
        md.selectrelation()
        time.sleep(3)
        md.relationcancel()
        time.sleep(3)
        md.emergncycontact1("01736457478")
        time.sleep(3)
        hm.scroll_down5(1338, 626)

        md.aboutus()
        time.sleep(3)
        md.aboutuscancel()
        time.sleep(3)
        md.radioclick1_ID()
        time.sleep(3)
        md.radioclick2_ID()
        time.sleep(3)
        md.backtopreviouspage_XPATH()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()