# Created by rapid at 6/5/2020
Feature: # submit_empty_login_window
  # User goes to main page and push login button with empty login and username fields

  Scenario: User goes to main page and push login button with empty login and username fields
    Given Loginpage
    Then Click on Log In button first
    Then Click on Log In button second
    Then Verify text 1 is here: Please enter your username
    Then Verify text 2 is here: Please enter your password