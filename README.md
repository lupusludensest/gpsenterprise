# gpsenterprise
gpsenterprise

Test Case

# Created by Gurov Vic at 04/06/2020
Feature: System rejects empthy login and password

Scenario: User just clicks login button when login and password fields are emthy and system rejects
	
Preconditions:
Runnable on: Windows 10
Browser: Chrome
Tools: Java, Selenium Webdriver

===========================================================================================
If you will install allure(java should be here)-you would be able to see the visual report. 
See steps:
$ pip install allure-behave
$ pip install allure-pytest
$ pip install pytest-allure-adaptor

to launch tests and generate reports folder: 
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
to extract report into browser: 
$ allure serve test_results/
