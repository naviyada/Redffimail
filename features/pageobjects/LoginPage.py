from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configreader
from features.pageobjects.Base import BaseSettingsPage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def validUsernameText(self, expectedText):
        self.DynamicImplicitWait(40)
        self.AssertText("usernaneText_XPATH", expectedText)

    def setUsername(self, username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("username_ID",username)

    def validPasswordText(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("passwordText_XPATH", expectedTextVal)

    def setPassword(self, password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("password_ID",password)

    def clickSignIn(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("signinButton_NAME")

    def text_search(self,searchtext):
        WebDriverWait(self.driver,40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.ID,"inp_search_box")))
        self.DynamicImplicitWait(10)
        self.TypeEditBox("search_ID",searchtext)

    def Click_searchBUTTON(self):
        self.DynamicImplicitWait(10)
        self.ClickButton("SearchButton_XPATH")

