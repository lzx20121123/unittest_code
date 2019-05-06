from selenium import webdriver
from time import sleep
import unittest

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.anenda.com")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        sleep(2)
        cls.driver.find_element_by_id("liger-textbox-user").send_keys("chen")
        cls.driver.find_element_by_id("liger-textbox-pwd_old").clear()
        cls.driver.find_element_by_id("liger-textbox-pwd").send_keys("chen")
        cls.driver.find_element_by_id("go").click()
        sleep(3)

    def test01(self):
        result1 = self.driver.find_element_by_xpath(".//*[@id='l-topmenu-r-bottm']/span[2]").text
        print(result1)
        result2 = "安恩达,欢迎您"
        self.assertIn(result2,result1,msg="失败原因：%s中没有发现%s"%(result1,result2))
        sleep(2)

    def test02(self):
        result1 = self.driver.find_element_by_id("hour").text
        print(result1)
        result2 = "2018年"
        self.assertIn(result2,result1,msg="失败原因：%s中没有发现%s"%(result1,result2))
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(exit=False)