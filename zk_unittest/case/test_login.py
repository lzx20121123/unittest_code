import sys,time,unittest
sys.path.append('F:\\zk_unittest')
from method.get_url import Get_url
from method.comm import Login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Logincase(unittest.TestCase):
    #每个用例执行之前执行
    def setUp(self):
        print ('before test')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        url =Get_url('loginurl')
        print (url)
        self.driver.get(url)           
        
    def test_login_success1(self):
        '''登录成功'''
        url = Get_url('correcturl')
        time.sleep(1)
        Login(self.driver,'admin','vsecure2016')
        dq_url = self.driver.current_url
        self.assertEquals(dq_url,url,msg=None)
        succ_text = self.driver.find_element_by_xpath('//*[@id="user"]/ul/li/a').text 
        self.assertIn('admin' ,succ_text)    
        
    def test_logout(self):
        '''退出登录'''
        url = Get_url('correcturl')
        Login(self.driver,'admin','vsecure2016')
        time.sleep(2)
        dq_url = self.driver.current_url 
        self.assertEquals(dq_url,url,msg=None)
        A = self.driver.find_element_by_xpath('//*[@id="user"]/ul/li/a')        
        ActionChains(self.driver).move_to_element(A).perform()                  #鼠标悬停操作
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="umenu"]/li[2]/a').click()
        time.sleep(0.5)
        title = self.driver.find_element_by_id('title')
        self.assertEqual('管理员登录',title.text)

    def test_login_fail1(self):
        '''账号不能为空'''

        time.sleep(1)
        Login(self.driver,'','vsecure2016')
        time.sleep(1)
        failtext = self.driver.find_element_by_css_selector('#result')
        self.assertEquals('帐号不能为空',failtext.text)
        time.sleep(1)
        
    def test_login_fail2(self):
        '''密码不能为空'''

        time.sleep(1)
        Login(self.driver,'admin','')
        time.sleep(1)
        error_message= self.driver.find_element_by_id('result')
        self.assertEqual('密码不能为空',error_message.text)
        time.sleep(1)
    def test_login_fail3(self):
        '''帐号或密码输入错误 '''
        time.sleep(1)
        Login(self.driver,'admin','ecure2016')
        time.sleep(1)
        error_message= self.driver.find_element_by_id('result')
        self.assertIn('帐号或密码输入错误' , error_message.text)
        time.sleep(1)   
    
    #每个用例执行之后执行
    def tearDown(self):
        print ('after every test')
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main(exit=False)
    #构造测试集
    sui = unittest.TestSuite()
    sui.addTest(Logincase('test_login_success1'))
    #sui.addTest(Logincase('test_login_success1'))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(sui)