from Pages.HomePage import HomePage
from Locators.Locators import middleRightBar


class middleRightBarPage(HomePage):

    def __init__(self, driver):
        self.locator = middleRightBar
        self.driver = driver
        super(middleRightBarPage, self).__init__(driver)

    # register
    def register(self):
        self.driver.find_element(*self.locator.register_XPATH).click()

    def reg_fstname(self, reg_fstname):
        self.driver.find_element(*self.locator.reg_fstname_ID).send_keys(reg_fstname)

    def reg_middlename(self, reg_middlename):
        self.driver.find_element(*self.locator.reg_middlename_ID).send_keys(reg_middlename)

    def reg_lastname(self, reg_lastname):
        self.driver.find_element(*self.locator.reg_lastname_ID).send_keys(reg_lastname)

    def dateofbirth(self):
        self.driver.find_element(*self.locator.dateofbirth_ID).click()

    def date_ok_ID(self):
        self.driver.find_element(*self.locator.date_ok_ID).click()

    def email_ID(self, email_ID):
        self.driver.find_element(*self.locator.email_ID).send_keys(email_ID)

    def selectgender(self):
        self.driver.find_element(*self.locator.selectgender_ID).click()

    def gendercancel(self):
        self.driver.find_element(*self.locator.gendercancel_ID).click()

    def nationality(self, nationality):
        self.driver.find_element(*self.locator.nationality_ID).send_keys(nationality)

    def selectstatus(self):
        self.driver.find_element(*self.locator.selectstatus_ID).click()

    def statuscancel(self):
        self.driver.find_element(*self.locator.statuscancel_ID).click()

    def selectoccupation(self):
        # self.driver.find_element(*self.locator.email_ID).clear()
        self.driver.find_element(*self.locator.selectoccupation_ID).click()

    def occupationcancel(self):
        self.driver.find_element(*self.locator.occupationcancel_ID).click()

    def phnnmbr(self, phnnmbr):
        self.driver.find_element(*self.locator.phnnmbr_ID).send_keys(phnnmbr)

    def address(self, address):
        self.driver.find_element(*self.locator.address_ID).send_keys(address)

    def city(self, city):
        self.driver.find_element(*self.locator.city_ID).send_keys(city)

    def state(self, state):
        self.driver.find_element(*self.locator.state_ID).send_keys(state)

    def country(self, country):
        self.driver.find_element(*self.locator.country_ID).send_keys(country)

    def postalcode(self, postalcode):
        self.driver.find_element(*self.locator.postalcode_ID).send_keys(postalcode)

    def emergncycontact(self, emergncycontact):
        self.driver.find_element(*self.locator.emergncycontact_ID).send_keys(emergncycontact)

    def selectrelation(self):
        self.driver.find_element(*self.locator.selectrelation_ID).click()

    def relationcancel(self):
        self.driver.find_element(*self.locator.relationcancel_ID).click()

    def emergncycontact1(self, emergncycontact1):
        self.driver.find_element(*self.locator.emergncycontact1_ID).send_keys(emergncycontact1)

    def aboutus(self):
        self.driver.find_element(*self.locator.aboutus_ID).click()

    def aboutuscancel(self):
        self.driver.find_element(*self.locator.aboutuscancel_ID).click()

    def radioclick1_ID(self):
        self.driver.find_element(*self.locator.radioclick1_ID).click()

    def radioclick2_ID(self):
        self.driver.find_element(*self.locator.radioclick2_ID).click()

    def backtopreviouspage_XPATH(self):
        self.driver.find_element(*self.locator.backtopreviouspage_XPATH).click()

    # link your + your family's accounts
    def linkfamilysaccount(self):
        self.driver.find_element(*self.locator.linkfamilysaccount_ID).click()

    def linkfamilysaccountok(self):
        self.driver.find_element(*self.locator.linkfamilysaccountok_ID).click()

    def addprofile(self):
        self.driver.find_element(*self.locator.addprofile_ID).click()

    def pbhl(self):
        self.driver.find_element(*self.locator.pbhl_ID).click()

        #driver.back

    def add(self):
        self.driver.find_element(*self.locator.add_ID).click()

    def cross(self):
        self.driver.find_element(*self.locator.cross_ID).click()

    def backtopreviouspage1(self):
        self.driver.find_element(*self.locator.backtopreviouspage1_XPATH).click()

    # how can we serve you better?
    def serve(self):
        self.driver.find_element(*self.locator.serve_ID).click()

    def addmemberok(self):
        self.driver.find_element(*self.locator.addmemberok_ID).click()

    def backtopreviouspage2(self):
        self.driver.find_element(*self.locator.backtopreviouspage2_XPATH).click()

    # contact us
    def contactus(self):
        self.driver.find_element(*self.locator.contactus_ID).click()

    def contactallow(self):
        self.driver.find_element(*self.locator.contactallow_ID).click()

    def backtopreviouspage3(self):
        self.driver.find_element(*self.locator.backtopreviouspage3_XPATH).click()
