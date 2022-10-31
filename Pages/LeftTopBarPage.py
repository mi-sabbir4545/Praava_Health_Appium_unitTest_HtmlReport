from Pages.HomePage import HomePage
from Locators.Locators import leftTopBar


class leftTopBarPage(HomePage):

    def __init__(self, driver):
        self.locator = leftTopBar
        self.driver = driver
        super(leftTopBarPage, self).__init__(driver)

    # profile pencil
    #edit profile
    def navigate0(self):
        self.driver.find_element(*self.locator.navigate0_XPATH).click()

    def pencil(self):
        self.driver.find_element(*self.locator.pencil_ID).click()

    def pancilallow(self):
        self.driver.find_element(*self.locator.pancilallow_ID).click()

    def pencil1(self):
        self.driver.find_element(*self.locator.pencil1_ID).click()

    def pencil2(self):
        self.driver.find_element(*self.locator.pencil2_ID).click()

    def name(self, name):
        self.driver.find_element(*self.locator.name_ID).clear()
        self.driver.find_element(*self.locator.name_ID).send_keys(name)

    def dateofb(self):
        self.driver.find_element(*self.locator.dateofb_ID).click()

    def dateofbok(self):
        self.driver.find_element(*self.locator.dateofbok_ID).click()

    def male(self):
        self.driver.find_element(*self.locator.male_ID).click()

    def mail(self, mail):
        self.driver.find_element(*self.locator.mail_ID).clear()
        self.driver.find_element(*self.locator.mail_ID).send_keys(mail)

    def address(self, address):
        self.driver.find_element(*self.locator.address_ID).clear()
        self.driver.find_element(*self.locator.address_ID).send_keys(address)

    def phone(self, phone):
        self.driver.find_element(*self.locator.phone_ID).clear()
        self.driver.find_element(*self.locator.phone_ID).send_keys(phone)

    def cancel(self):
        self.driver.find_element(*self.locator.cancel_ID).click()

    #change password

    def changepass(self):
        self.driver.find_element(*self.locator.changepass_ID).click()

    def oldpass(self, oldpass):
        self.driver.find_element(*self.locator.oldpass_ID).clear()
        self.driver.find_element(*self.locator.oldpass_ID).send_keys(oldpass)

    def newpass(self, newpass):
        self.driver.find_element(*self.locator.newpass_ID).clear()
        self.driver.find_element(*self.locator.newpass_ID).send_keys(newpass)

    def confirmpass(self, confirmpass):
        self.driver.find_element(*self.locator.confirmpass_ID).clear()
        self.driver.find_element(*self.locator.confirmpass_ID).send_keys(confirmpass)

    def cancelpass(self):
        self.driver.find_element(*self.locator.cancelpass_ID).click()

    def backtopreviouspage100(self):
        self.driver.find_element(*self.locator.backtopreviouspage100_XPATH).click()

    # Navigation top
    # My appointments
    def navigate(self):
        self.driver.find_element(*self.locator.navigate_XPATH).click()

    def myappointmentys(self):
        self.driver.find_element(*self.locator.myappointmentys_XPATH).click()

    def pastappoint(self):
        self.driver.find_element(*self.locator.pastappoint_XPATH).click()

    def backtopreviouspage4(self):
        self.driver.find_element(*self.locator.backtopreviouspage4_XPATH).click()

    # FAQs
    def navigate1(self):
        self.driver.find_element(*self.locator.navigate1_XPATH).click()

    def faqs(self):
        self.driver.find_element(*self.locator.faqs_XPATH).click()

    def backtopreviouspage5(self):
        self.driver.find_element(*self.locator.backtopreviouspage5_XPATH).click()

    # social media
    def navigate2(self):
        self.driver.find_element(*self.locator.navigate2_XPATH).click()

    def socialmedia(self):
        self.driver.find_element(*self.locator.socialmedia_XPATH).click()

    def fb(self):
        self.driver.find_element(*self.locator.fb_XPATH).click()

    def backtopreviouspage6(self):
        self.driver.find_element(*self.locator.backtopreviouspage6_XPATH).click()

    # LogOut
    def navigate3(self):
        self.driver.find_element(*self.locator.navigate3_XPATH).click()

    def logout(self):
        self.driver.find_element(*self.locator.logout_XPATH).click()
