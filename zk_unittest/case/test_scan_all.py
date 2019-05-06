import sys,time,unittest
sys.path.append('F:\\zk_unittest')
from method.get_url import Get_url
from method.comm import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Scan_all(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')
        cls.driver = webdriver.Chrome()
        url = Get_url('loginurl')
        cls.driver.get(url)
        cls.driver.maximize_window()
        Login_success(cls.driver)        
        #zdgl_page(self.driver)              #进入终端管理
        cls.driver.implicitly_wait(5)


    def test_z_all_scan1(self):
        '''全盘查杀-未勾选终端'''
        zdgl_page(self.driver)              #进入终端管理
        click_overall_scan(self.driver)
        te = self.driver.switch_to.alert
        self.assertEqual('请选择要处理的项',te.text)
        te.accept()

    def test_z_all_scan2(self):
        '''全盘查杀-静默'''
        zdgl_page(self.driver)              #进入终端管理
        click_all_select(self.driver)               #全选在线终端
        time.sleep(1)
        click_overall_scan(self.driver)                #全盘扫描   
        Silent(self.driver)                         #静默   
        time.sleep(1)                 
        mess = self.driver.switch_to.alert
        self.assertEqual('操作已下发!',mess.text)
        mess.accept()
        t = time.strftime('%Y-%m-%d %H:%M')
        #print (t)
        time.sleep(8)
        zdgl_page(self.driver)
        online_select(self.driver) 
        time.sleep(1)
        scan_time = self.driver.find_element_by_xpath('//*[@id="table"]/table/tbody[2]/tr[2]/td[9]').text  
        #print (scan_time)
        self.assertEquals(t,scan_time)      #验证客户端上传的时间

    #新版本中控取消了任务管理
    '''def test_z_all_scan3(self):
        全盘查杀--检查任务管理记录 
        zdgl_page(self.driver)              #进入终端管理
        click_all_select(self.driver)               #全选在线终端
        click_overall_scan(self.driver)                #全盘扫描   
        Silent(self.driver)                         #静默   
        t = time.strftime('%Y-%m-%d %H:%M') 
        time.sleep(1)                 
        mess = self.driver.switch_to.alert             
        self.assertEqual('操作已下发!',mess.text)
        mess.accept()
        #t = time.strftime('%Y-%m-%d %H:%M')
        print(t)
        shou_Ye(self.driver)
        Open_Rwgl(self.driver)
        time.sleep(2)
        time1 = self.driver.find_element_by_xpath('//*[@id="task-table"]/table/tbody[2]/tr[2]/td[5]').text
        print (time1)
        self.assertIn(t,time1)
        mesg = self.driver.find_element_by_xpath('//*[@id="task-table"]/table/tbody[2]/tr[2]/td[3]/span').text
        self.assertEquals('闪电查杀',mesg)
'''
    def test_z_all_scan4(self):
        '''全盘查杀--检查中控日志记录 '''
        zdgl_page(self.driver)              #进入终端管理
        click_all_select(self.driver)               #全选在线终端
        click_fast_scan(self.driver)                #闪电扫描  
        Silent(self.driver)                         #静默  
        t = time.strftime('%Y-%m-%d %H:%M') 
        time.sleep(1)                 
        mess = self.driver.switch_to.alert             
        self.assertEqual('操作已下发!',mess.text)
        mess.accept()
        #t = time.strftime('%Y-%m-%d %H:%M:')
        #print(t)
        #shou_Ye(self.driver)
        #Open_Rwgl(self.driver)
        time.sleep(2)
        zk_log_open(self.driver)
        time.sleep(2)
        t2 = self.driver.find_element_by_xpath('//*[@id="admin-log-table"]/table/tbody[2]/tr[2]/td[2]').text
        #print(t2)
        self.assertIn(t,t2)
        mesg = self.driver.find_element_by_xpath('//*[@id="admin-log-table"]/table/tbody[2]/tr[2]/td[6]').text
        #print(mesg)
        self.assertEqual('扫描威胁',mesg)

    def test_down_file(self):
        '''导出报表'''
        #打开终端管理页面
        zdgl_page(self.driver)  
        #设置下载路径以及禁止弹窗
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'F:\\'}  
        options.add_experimental_option('prefs', prefs)  
                
        self.driver.find_element_by_id('mgr-m').click()
        self.driver.find_element_by_xpath('//*[@id="menu-lst-more"]/ul/li[2]/a').click()#导出报表
        time.sleep(10)
    #测试
    def test_tt(self):
        zdgl_page(self.driver)  
        js = 'document.getElementById("mgr-q").click();'
        self.driver.execute_script(js)
        time.sleep(10)



        
    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()

if __name__ == "__main__":
    sui = unittest.TestSuite()
    sui.addTest(Scan_all('test_tt'))
    

    runner = unittest.TextTestRunner()
    runner.run(sui)

