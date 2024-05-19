import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(' https://suninjuly.github.io/selects2.html')
num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text
sum_nums = int(num1) + int(num2)

browser.find_element(By.ID, 'dropdown')
browser.find_element(By.CSS_SELECTOR, f'[value="{sum_nums}"]').click()
browser.find_element(By.TAG_NAME, 'button').click()
time.sleep(5)
