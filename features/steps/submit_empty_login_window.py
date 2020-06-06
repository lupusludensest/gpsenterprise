from behave import *
from time import sleep

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()

@then("Click on Log In button first")
def click_on_log_in_btn_frst(context):
    context.app.main_page.click_on_log_in_btn_frst()
    sleep(2)

@then("Click on Log In button second")
def click_on_log_in_btn_scnd(context):
    context.app.main_page.click_on_log_in_btn_scnd()

@then('Verify text 1 is here: {text_one}')
def text_here_1(context, text_one):
    context.app.main_page.text_here_1(text_one)

@then('Verify text 2 is here: {text_two}')
def text_here_2(context, text_two):
    context.app.main_page.text_here_2(text_two)
