from selenium.webdriver.common.by import By
from pages.base_page import Page

class ContactFormPage(Page):

    # locators
    CNTCT_BTN = (By.XPATH, "//li[@class='active menu-item menu-contact'][1]") # "menu-header-navigation-right"# "li.active.menu-item.menu-contact" # "//a[@aria-current='page']" # "//a[@href='https://analyticpartners.com/contact-us/']"
    FRST_NM_FLD = (By.ID, "firstname-9d6686cd-0cff-4088-b7e6-860da1461c18")
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


    def inpt_frst_nm(self, text):
        """
        User enters First name
        """
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

    def inpt_phn_nmbr(self, text):
        """
        User enters Phone number
        """
        self.inpt_phn_nmbr(text, *self.PHN_NMBR_FLD)

    def inpt_msg(self, text):
        """
        User enters into the Message field
        """
        self.inpt_phn_nmbr(text, *self.MSG_FLD)

    def clck_agree_tick(self):
        """
        User agrees with I agree to receive other communications from Analytic Partners
        """
        self.click(*self.AGREE_TICK)

    def txt_hr(self, text):
        """
        Verify there is a text
        """
        self.verify_text(text, *self.SBMT_BTN)









