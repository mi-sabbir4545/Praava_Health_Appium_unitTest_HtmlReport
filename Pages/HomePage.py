# from telnetlib import EC
#
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
#
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from Locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def scroll_down(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(400, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(400, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down1(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(716, 1289)
        actions.w3c_actions.pointer_action.move_to_location(716, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(716, 581)
        actions.w3c_actions.pointer_action.move_to_location(716, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down2(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(687, 1354)
        actions.w3c_actions.pointer_action.move_to_location(687, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(687, 397)
        actions.w3c_actions.pointer_action.move_to_location(687, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down3(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(671, 1350)
        actions.w3c_actions.pointer_action.move_to_location(671, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(671, 544)
        actions.w3c_actions.pointer_action.move_to_location(671, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down4(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(675, 1244)
        actions.w3c_actions.pointer_action.move_to_location(675, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(675, 544)
        actions.w3c_actions.pointer_action.move_to_location(675, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down5(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(724, 1338)
        actions.w3c_actions.pointer_action.move_to_location(724, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(724, 626)
        actions.w3c_actions.pointer_action.move_to_location(724, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down6(self, y1, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(687, 1346)
        actions.w3c_actions.pointer_action.move_to_location(687, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(687, 716)
        actions.w3c_actions.pointer_action.move_to_location(687, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


