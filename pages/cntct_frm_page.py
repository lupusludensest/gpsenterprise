from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ContactFormPage(Page):

    # locators
    CNTCT_BTN = (By.XPATH, "//ul[@id='menu-header-navigation-right']//a[contains(text(),'Contact')]")
    FRST_NM_FLD = (By.ID, "firstname-9d6686cd-0cff-4088-b7e6-860da1461c18")
    LST_NM_FLD = (By.ID, "lastname-9d6686cd-0cff-4088-b7e6-860da1461c18")
    CMPN_NM_FLD = (By.ID, "company-9d6686cd-0cff-4088-b7e6-860da1461c18")
    JB_TTL_FLD = (By.ID, "jobtitle-9d6686cd-0cff-4088-b7e6-860da1461c18")
    EML_FLD = (By. ID, "email-9d6686cd-0cff-4088-b7e6-860da1461c18")
    PHN_NMBR_FLD = (By.ID, "phone-9d6686cd-0cff-4088-b7e6-860da1461c18")
    MSG_FLD = (By.ID, "message-9d6686cd-0cff-4088-b7e6-860da1461c18")
    AGREE_TICK = (By.ID, "LEGAL_CONSENT.subscription_type_7768920-9d6686cd-0cff-4088-b7e6-860da1461c18")
    SBMT_BTN = (By.CSS_SELECTOR, "input.hs-button.primary.large")
    TXT_HR = (By.XPATH, "//div[@class='hero__excerpt']//h4[contains(text(),'We will be in touch very soon! We appreciate your inquiry, and a member of our team will be in touch as soon as possible.')]")

    def clck_contact_btn(self):
        """
        Click on Contact button
        """
        self.click(*self.CNTCT_BTN)

    def inpt_frst_name(self, text):
        """
        User enters First name in the iframe
        """
        sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_id('hs-form-iframe-0'))
        self.input_text(text, *self.FRST_NM_FLD)

    def inpt_scnd_nm(self, text):
        """
        User enters Last name
        """
        self.input_text(text, *self.LST_NM_FLD)

    def inpt_cmpn_nm(self, text):
        """
        User enters Company name
        """
        self.input_text(text, *self.CMPN_NM_FLD)

    def inpt_jb_ttl(self, text):
        """
        User enters Job Title
        """
        self.input_text(text, *self.JB_TTL_FLD)

    def inpt_eml(self, text):
        """
        User enters Email
        """
        self.input_text(text, *self.EML_FLD)

    def inpt_phn_numbr(self, text):
        """
        User enters Phone number
        """
        self.input_text(text, *self.PHN_NMBR_FLD)

    def inpt_msg(self, text):
        """
        User enters into the Message field
        """
        self.input_text(text, *self.MSG_FLD)
        sleep(4)

    def clck_agree_tick(self):
        """
        User agrees with I agree to receive other communications from Analytic Partners
        """
        self.click(*self.AGREE_TICK)

    def clck_sbmt_btn(self):
        """
        User clicks on Submit button
        """
        self.click(*self.SBMT_BTN)
        sleep(4)

    def txt_hr(self, text):
        """
        Verify there is a text after departure of the iframe to default content
        """
        self.driver.switch_to.default_content()
        self.verify_text(text, *self.TXT_HR)









