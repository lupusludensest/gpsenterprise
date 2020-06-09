from behave import *

@then("Click on Contact button")
def clck_contact_btn(context):
    context.app.cntct_frm_page.clck_contact_btn()

@then("User enters First name {frst_nm}")
def inpt_frst_nm(context, frst_nm):
    context.app.cntct_frm_page.inpt_frst_name(frst_nm)

@then("User enters Last name {scnd_nm}")
def inpt_scnd_nm(context, scnd_nm):
    context.app.cntct_frm_page.inpt_scnd_nm(scnd_nm)

@then("User enters Company name {cmpn_nm}")
def inpt_cmpn_nm(context, cmpn_nm):
    context.app.cntct_frm_page.inpt_cmpn_nm(cmpn_nm)

@then("User enters Job Title {jb_ttl}")
def inpt_jb_ttl(context, jb_ttl):
    context.app.cntct_frm_page.inpt_jb_ttl(jb_ttl)

@then("User enters Email {eml}")
def inpt_eml(context, eml):
    context.app.cntct_frm_page.inpt_eml(eml)

@then("User enters Phone number {phn_nmbr}")
def inpt_phn_nmbr(context, phn_nmbr):
    context.app.cntct_frm_page.inpt_phn_numbr(phn_nmbr)

@then("User enters into the Message field {msg}")
def inpt_msg(context, msg):
    context.app.cntct_frm_page.inpt_msg(msg)

@then("User agrees with I agree to receive other communications from Analytic Partners")
def clck_agree_tick(context):
    context.app.cntct_frm_page.clck_agree_tick()

@then("User clicks on Submit button")
def clck_sbmt_btn(context):
    context.app.cntct_frm_page.clck_sbmt_btn()

@then("Verify there is a text {txt_cnfrmtn}")
def txt_hr(context, txt_cnfrmtn):
    context.app.cntct_frm_page.txt_hr(txt_cnfrmtn)