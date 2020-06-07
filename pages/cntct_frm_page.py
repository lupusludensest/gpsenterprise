from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ContactFormPage(Page):

    # locators
    CNTCT_BTN = (By.XPATH, "//ul[@id='menu-header-navigation-right']//a[contains(text(),'Contact')]")
    FRST_NM_FLD = (By.ID, "hs-form-iframe-0")
    LST_NM_FLD = (By.ID, "lastname-9d6686cd-0cff-4088-b7e6-860da1461c18")
    CMPN_NM_FLD = (By.ID, "company-9d6686cd-0cff-4088-b7e6-860da1461c18")
    JB_TTL_FLD = (By.ID, "jobtitle-9d6686cd-0cff-4088-b7e6-860da1461c18")
    EML_FLD = (By. ID, "email-9d6686cd-0cff-4088-b7e6-860da1461c18")
    PHN_NMBR_FLD = (By.ID, "phone-9d6686cd-0cff-4088-b7e6-860da1461c18")
    MSG_FLD = (By.ID, "message-9d6686cd-0cff-4088-b7e6-860da1461c18")
    AGREE_TICK = (By.ID, "LEGAL_CONSENT.subscription_type_7768920-9d6686cd-0cff-4088-b7e6-860da1461c181")
    SBMT_BTN = (By.CSS_SELECTOR, "input.hs-button.primary.large")

    def clck_contact_btn(self):
        """
        Click on Contact button
        """
        self.click(*self.CNTCT_BTN)
        sleep(4)

    def inpt_frst_nm(self, text):
        """
        User enters First name
        """
        sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='hs-form-iframe-0']"))
        self.input_text(text, *self.FRST_NM_FLD)
        # self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe#hs-form-iframe-0.hs-form-iframe")
        # self.input_text(text, *self.FRST_NM_FLD)
        sleep(4)

    def inpt_scnd_nm(self, text):
        """
        User enters Last name
        """
        self.input_text(text, *self.LST_NM_FLD)
        sleep(4)

    def inpt_cmpn_nm(self, text):
        """
        User enters Company name
        """
        self.input_text(text, *self.CMPN_NM_FLD)
        sleep(4)

    def inpt_jb_ttl(self, text):
        """
        User enters Job Title
        """
        sleep(4)
        self.input_text(text, *self.JB_TTL_FLD)

    def inpt_eml(self, text):
        """
        User enters Email
        """
        self.input_text(text, *self.EML_FLD)
        sleep(4)

    def inpt_phn_nmbr(self, text):
        """
        User enters Phone number
        """
        self.inpt_phn_nmbr(text, *self.PHN_NMBR_FLD)
        sleep(4)

    def inpt_msg(self, text):
        """
        User enters into the Message field
        """
        self.inpt_phn_nmbr(text, *self.MSG_FLD)
        sleep(4)

    def clck_agree_tick(self):
        """
        User agrees with I agree to receive other communications from Analytic Partners
        """
        self.click(*self.AGREE_TICK)
        sleep(4)

    def txt_hr(self, text):
        """
        Verify there is a text
        """
        self.verify_text(text, *self.SBMT_BTN)









