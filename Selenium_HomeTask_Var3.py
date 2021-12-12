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

class Test1():
  def set_up(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def AddAndRemoveNewPayGrade(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades")
    self.driver.find_element(By.ID, "payGrade_name").click()
    self.driver.find_element(By.ID, "payGrade_name").send_keys("MaxKoval")

    self.driver.find_element(By.ID, "btnSave").click()
    self.driver.find_element(By.ID, "btnAddCurrency").click()
    self.driver.find_element(By.ID, "payGradeCurrency_currencyName").click()
    self.driver.find_element(By.ID, "payGradeCurrency_currencyName").send_keys("UAH - Ukraine Hryvnia")
    self.driver.find_element(By.ID, "payGradeCurrency_minSalary").send_keys("6000")
    self.driver.find_element(By.ID, "payGradeCurrency_maxSalary").send_keys("20000")
    self.driver.find_element(By.ID, "btnSaveCurrency").click()
    self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades")
    self.driver.find_element(By.LinkText, "MaxKoval").click()
    assert self.driver.find_element(By.LinkText, "Ukraine Hryvnia").get_attribute("innerText") == "Ukraine Hryvnia", "Currency UAH doesn't exist."
    self.driver.get_element(By.LinkText, "MaxKoval")
    URL = self.driver.current_url
    id = URL.split("=")[1]
    self.driver.find_element(By.ID, "ohrmList_chkSelectRecord_"+id).click()
    self.driver.find_element(By.ID, "btnDelete").click()
    self.driver.find_element(By.ID, "dialogDeleteBtn").click()
    self.driver.close
