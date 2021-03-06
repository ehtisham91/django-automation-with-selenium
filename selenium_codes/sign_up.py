from selenium import webdriver
import unittest

class UserSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/HAIER/Desktop/selenium-java/chromedriver.exe")
        cls.driver.get("http://127.0.0.1:8000/accounts/register/")
        cls.driver.maximize_window()

    def test_sign_up(self):
        self.driver.find_element_by_id("id_username").send_keys("anyuser")
        self.driver.find_element_by_id("id_email").send_keys("anyuser@gmail.com")
        self.driver.find_element_by_id("id_password1").send_keys("12345")
        self.driver.find_element_by_id("id_password2").send_keys("12345")
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div/form/input[2]").click()


    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()


