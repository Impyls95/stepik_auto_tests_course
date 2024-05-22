from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_first_ver_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('dsa')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('sfsf')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('fdxfs')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test_second_ver_registration(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('dsa')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('sfsf')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('fdxfs')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
