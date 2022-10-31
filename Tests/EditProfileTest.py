import time
from Pages.LoginPage import LoginPage
from Pages.LogPage import LogPage
from Pages.BasePage import BasePage
from Pages.LeftTopBarPage import leftTopBarPage  # class name of this page


class LoginTeste(BasePage):

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


        # Edit profile
        md.navigate0()
        time.sleep(3)

        md.pencil()
        time.sleep(8)

        md.pancilallow()
        time.sleep(3)

        md.pencil1()
        time.sleep(3)

        md.pencil2()
        time.sleep(3)

        md.name("Tonoy Kumar Saha")
        time.sleep(8)

        md.dateofb()
        time.sleep(3)

        md.dateofbok()
        time.sleep(3)

        md.male()
        time.sleep(3)

        md.mail("tonoysaha@46gmail.com")
        time.sleep(8)

        md.address("Mohadevpur naogaon")
        time.sleep(3)

        md.phone("01736457478")
        time.sleep(3)

        md.cancel()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()