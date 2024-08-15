import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomepage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.get_logging()
        log.info("Hello")
        homePage = HomePage(self.driver)
        homePage.getNames().send_keys(getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys("qwertyiop")
        homePage.getCheckbox().click()
        homePage.getSubmit().click()
        self.getDropdownSelection(homePage.getDropdown(), getData["gender"])
        message = homePage.getSuccess().text
        assert "Success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Rahul", "Shetty", "Male"), ("Sagar", "Rayamajhi", "Female")])
    # Parametrerzing the tests with multiple data sets using dictionary
    # Befor excel applies
    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # After excel
    @pytest.fixture(params=HomePageData.getTestData("test_homepage"))
    def getData(self, request):
        return request.param
