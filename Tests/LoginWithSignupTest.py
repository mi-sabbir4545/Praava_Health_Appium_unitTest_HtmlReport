import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

class LoginTest1(BasePage):
    def test_signup_page(self):
        lp = LoginPage(self.driver)
        time.sleep(5)

        lp.click_signup()
        time.sleep(2)

        lp.mobile("01736457478")
        time.sleep(2)

        lp.username("Tonoy")
        time.sleep(2)

        lp.password("123456789")
        time.sleep(2)

        lp.repassword("123456789")

        lp.email("saha.qups@gmail.com")

        lp.login0()


if __name__ == "__main__":
    unittest.main()