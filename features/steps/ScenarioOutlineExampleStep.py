import logging
import time

import allure
from allure_commons._allure import severity
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import configreader
from Utilities.LogUtil import Logger

from features.pageobjects.LoginPage import LoginPage


log = Logger(__name__, logging.INFO)


@given(u'we navigate to Rediffmail account')
def step_impl(context):
    context.reg = LoginPage(context.driver)
    context.reg.open(configreader.ConfigReader("base info", "URL"))
    log.logger.info("Navigated to Rediffmail Login Page")
    time.sleep(3)
    print("Pass")

@when(u'we validate the username text')
def step_impl(context):
    context.reg.validUsernameText("Username")
    log.logger.info("Username Text Validated")
    time.sleep(3)
    print("Pass")


@when(u'we type in the "{username}" edit box')
def step_impl(context, username):
    context.reg.setUsername(username)
    log.logger.info("Username field typed")
    time.sleep(3)
    print("Pass")

@when(u'we validate the password text')
def step_impl(context):
    context.reg.validPasswordText("Password")
    log.logger.info("Password Text Validated")
    time.sleep(3)
    print("Pass")

@when(u'we type in the "{password}" field')
def step_impl(context, password):
    context.reg.setPassword(password)
    log.logger.info("Password field typed")
    time.sleep(3)
    print("Pass")

@when(u'we click on the sign in button')
def step_impl(context):
    context.reg.clickSignIn()
    log.logger.info("Signin button clicked")
    time.sleep(3)
    print("Pass")

@then(u'type "{searchtext}" in search bar')
def step_impl(context,searchtext):
    context.reg.text_search(searchtext)
    log.logger.info("searched")
    time.sleep(3)

@then(u'click on search button')
def step_impl(context):
    context.reg.Click_searchBUTTON()
    log.logger.info("search button clicked")
    time.sleep(3)




