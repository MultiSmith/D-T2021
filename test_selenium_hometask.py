import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPayGrade:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_new_pay_grade(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades")
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "payGrade_name").click()
        self.driver.find_element(By.ID, "payGrade_name").send_keys("MaxKoval")
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "btnAddCurrency").click()
        self.driver.find_element(By.ID, "payGradeCurrency_currencyName").click()
        self.driver.find_element(By.ID, "payGradeCurrency_currencyName").send_keys("UAH - Ukraine Hryvnia")
        self.driver.find_element(By.ID, "payGradeCurrency_minSalary").send_keys("6000")
        self.driver.find_element(By.ID, "payGradeCurrency_maxSalary").send_keys("20000")
        self.driver.find_element(By.ID, "btnSaveCurrency").click()

    def test_remove_pay_grade(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades")
        self.driver.find_element(By.LINK_TEXT, "MaxKoval").click()
        URL = self.driver.current_url
        id = URL.split("=")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades")
        self.driver.find_element(By.ID, "ohrmList_chkSelectRecord_" + id[1]).click()
        self.driver.find_element(By.ID, "btnDelete").click()
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()

if __name__ == "__main__":
    pytest.main()