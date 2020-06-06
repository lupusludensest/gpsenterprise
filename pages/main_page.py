from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    LOG_IN_BTN_1 = (By.CSS_SELECTOR, "a.nav-eyebrow__login")
    LOG_IN_BTN_2 = (By.CSS_SELECTOR, "button.ant-btn._1gF6tIm20jrHjFL8gIxetc.ant-btn-primary.ant-btn-lg")
    NO_USER_NAME = (By.XPATH, "//div[contains(text(), 'Please enter your username.')]")
    NO_PASSWORD = (By.XPATH, "//div[contains(text(), 'Please enter your password.')]")

    def click_on_log_in_btn_frst(self):
        """
        Click on Log In button first and go to the new url
        """
        self.click(*self.LOG_IN_BTN_1)
        window_before = self.driver.window_handles[0]
        print('window_before: ' + window_before)
        self.driver.wait.until(EC.new_window_is_opened)
        window_after = self.driver.window_handles[1]
        print('window_after: ' + window_after)
        self.driver.switch_to_window(window_after)

    def click_on_log_in_btn_scnd(self):
        """
        Click on Log In button second
        """
        self.click(*self.LOG_IN_BTN_2)

    def text_here_1(self, text):
        """
        Text is here
        """
        self.verify_text(text, *self.NO_USER_NAME)

    def text_here_2(self, text):
        """
        Text is here
        """
        self.verify_text(text, *self.NO_PASSWORD)



