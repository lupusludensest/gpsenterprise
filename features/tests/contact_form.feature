# Created by rapid at 6/6/2020
Feature: # contact_form
  # User goes to contact and fills out the fields. System allows and text: is here after submitting.


  Scenario: # User goes to contact and fills out the fields. System allows and text: is here after submitting.
    Given Loginpage
    Then Click on Contact button
    Then User enters First name Vic
    Then User enters Last name Gurov
    Then User enters Company name NA
    Then User enters Job Title QA
    Then User enters Email gurovvic@gmail.com
    Then User enters Phone number 4074354433
    Then User enters into the Message field Test for QA purposes
    Then User agrees with I agree to receive other communications from Analytic Partners
    Then User clicks on Submit button
    Then Verify there is a text We will be in touch very soon! We appreciate your inquiry, and a member of our team will be in touch as soon as possible.

