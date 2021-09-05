from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            'C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe')
        print("Launching the Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching the Firefox Browser")
    else:
        driver = webdriver.Ie()
        print("Launching default Ie browser")
    return driver


# this will get the values from CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


###########PyTest HTML Report########

# Hook for adding the environment info to teh report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NopCommerceApp'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pranay'


# Hook to delete/Modify Environment info to the HTML Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
