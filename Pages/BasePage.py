# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import os
import unittest

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class BasePage(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={"platformName": "Android",
                                  "appium:platformVersion": "9",
                                  "appium:deviceName": "Tonoy",
                                  "appium:automationName": "UiAutomator2",
                                  "appium:app": "C:\\Users\\USER\\Downloads\\APK\\Praava Health_v1.19_apkpure.com.apk"

                                  }
        )
        print("Test Started.......")


    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        cls.driver.quit()
        print("Test Complete")



