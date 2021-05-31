# Petstore App Webservices Test Automation #

This code is the QA API Test Automation in Python which follows pytest to run test. 

### What is this repository for? ###

* QA Automation source code for API Testing using Python 3

### How do I get set up? ###

* Summary of set up 
  -The set up requires Python 3, Pycharm as an IDE and pytest to run tests.
* Configuration
  -Install Python 3.
  -Set the Environment Variables.
  -Point the environment variable to the Virtual Environment of the project.
  -Install PIP to install other useful python packages.
  -Install Pycharm IDE and point python interpreter to the local installed interpreter.
 * Dependencies
   -Clone this repository into your IDE and run "python setup.py develop" to get the dependencies installed.
   -Checkout the feature branch you wish to view or work on.
* How to run tests
  -"pytest -m <test case ID> --html=<name of report>.html --self contained-html"
  This will generate the report in HTML format.
  - or simply run "pytest -m <test case ID>"

### Contribution guidelines ###

** Writing tests ** - Using Python language write a test with extension .py and place in tests/<specific module folder>
** Code review ** -  Push your changes to the feature branch with **detail comments** on what
   was done/changed/added in the commit along with the screens modified with your initials
** Other guidelines ** - Keep Json payloads under src/payloads/<Respective API File>.
   -Keep URLs in "properties.ini" file.
   -Keep resource URI in "resource_uri.py" file.

### Who do I talk to? ###

* QA Team contributor:  Manoj Sahu