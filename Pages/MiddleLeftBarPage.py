from Pages.HomePage import HomePage
from Locators.Locators import middleLeftBar


class middleLeftBarPage(HomePage):

    def __init__(self, driver):
        self.locator = middleLeftBar
        self.driver = driver
        super(middleLeftBarPage, self).__init__(driver)

    # Book an appointment
    def book(self):
        self.driver.find_element(*self.locator.book_ID).click()

    def service(self):
        self.driver.find_element(*self.locator.service_ID).click()

    def familyphysicans(self):
        self.driver.find_element(*self.locator.familyphysicans_XPATH).click()

    def liketosee(self):
        self.driver.find_element(*self.locator.liketosee_ID).click()

    def taslima(self):
        self.driver.find_element(*self.locator.taslima_XPATH).click()

    def backtopreviouspage7(self):
        self.driver.find_element(*self.locator.backtopreviouspage7_XPATH).click()

    def backtopreviouspage8(self):
        self.driver.find_element(*self.locator.backtopreviouspage8_XPATH).click()

    # book a health check
    # Annual Membership plan
    def bookhealth(self):
        self.driver.find_element(*self.locator.bookhealth_ID).click()

    def annualplan(self):
        self.driver.find_element(*self.locator.annualplan_XPATH).click()

    def viewdetils(self):
        self.driver.find_element(*self.locator.viewdetils_ID).click()

    def ecg(self):
        self.driver.find_element(*self.locator.ecg_XPATH).click()

    def booked(self):
        self.driver.find_element(*self.locator.booked_ID).click()

    def backtopreviouspage9(self):
        # self.driver.find_element(*self.locator.email_ID).clear()
        self.driver.find_element(*self.locator.backtopreviouspage9_XPATH).click()

    # health check
    def healthcheck(self):
        self.driver.find_element(*self.locator.healthcheck_XPATH).click()

    def diabetesviewdetails(self):
        self.driver.find_element(*self.locator.diabetesviewdetails_XPATH).click()

    def booked1(self):
        self.driver.find_element(*self.locator.booked1_XPATH).click()

    def backtopreviouspage10(self):
        self.driver.find_element(*self.locator.backtopreviouspage10_XPATH).click()

    def backtopreviouspage11(self):
        self.driver.find_element(*self.locator.backtopreviouspage11_XPATH).click()

    # signup for a membership plan
    def signupmembership(self):
        self.driver.find_element(*self.locator.signupmembership_ID).click()

    def signupmembershipok(self):
        self.driver.find_element(*self.locator.signupmembershipok_ID).click()

    def backtopreviouspage12(self):
        self.driver.find_element(*self.locator.backtopreviouspage12_XPATH).click()

    # MAP
    def map(self):
        self.driver.find_element(*self.locator.map_ID).click()

    def mapallow(self):
        self.driver.find_element(*self.locator.mapallow_ID).click()

    def backtopreviouspage13(self):
        self.driver.find_element(*self.locator.backtopreviouspage13_XPATH).click()

