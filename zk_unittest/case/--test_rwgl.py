from selenium import webdriver
import sys
sys.path.append('F:\\zk_unittest')
from method.comm import *
from method.file_path import Get_filepath
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class RWGL_test(unittest.TestCase):
    def setUp(self):
        u'''登录，打开首页'''
        print('start')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        url =Get_url('loginurl')
        self.driver.get(url)
        Login_success(self.driver)                                      #--登录
        time.sleep(2)
        shou_Ye(self.driver)                                            #--进入首页
        time.sleep(1)
        self.driver.implicitly_wait(5)                                  #设置超时
    
    def test_c_task_mng(self):
        '''首页--任务管理--取消任务'''
        Open_Rwgl(self.driver)                                                  #打开任务管理并切换iframe
        time.sleep(1)
        Num_ = Num_task(self.driver)
        New_Task_Num = int(Num_)                                               #最新任务个数
        print ('New_task 是%s'% New_Task_Num)
        self.driver.find_element_by_id('tab-history').click()                                   #切到历史任务页
        time.sleep(1)
        Num2 = Num_task(self.driver)
        Old_Task_Num = int(Num2)                                               #历史任务个数
        print ('Old_task 是%s'% Old_Task_Num)
        self.driver.find_element_by_id('tab-new').click()                                       #回到最新任务页
        time.sleep(1)
        if New_Task_Num !=0 and New_Task_Num != 100:
            Qx_task(self.driver)  #取消一个任务
            time.sleep(0.5)
            New_Task_Num2 = int(Num_task(self.driver))                                           #获得最新任务个数
            print ('New_task2 是%s'% New_Task_Num2)
            Num =New_Task_Num2+1 
            self.assertEqual(str(New_Task_Num),str(Num))
            self.driver.find_element_by_id('tab-history').click()                                #切到历史任务页
            time.sleep(1)
            Old_Task_Num2 = int(Num_task(self.driver))                                            #历史任务个数
            print ('Old_task2 是%s'% Old_Task_Num2)
            print(Old_Task_Num2)
            Old_Num = Old_Task_Num2 -1    
            self.assertEqual(Old_Num,Old_Task_Num)
        elif New_Task_Num ==0:
            Currect_url = Get_url('currenturl')
            self.driver.get(Currect_url)
            #self.driver.switch_to.parent_frame()
            time.sleep(1)          
            #打开终端管理，先下发几个任务
            
            #time.sleep(1)
            fast_kill(self.driver)                                                                  #闪电查杀
            time.sleep(1)
            self.driver.switch_to.alert.accept()                                                    #确定
            shou_Ye(self.driver)                                                                    #进入首页   
            Open_Rwgl(self.driver)
            time.sleep(1) 
            New_Task_Num3 = int(Num_task(self.driver))                                              #最新任务个数 
            self.driver.find_element_by_id('tab-history').click()                                   #切到历史任务页
            time.sleep(1)
            Old_Task_Num3 = int(Num_task(self.driver))                                               #历史任务个数
            print ('Old_task 是%s'% Old_Task_Num3)
            self.driver.find_element_by_id('tab-new').click()                                       #回到最新任务页               
            Qx_task(self.driver)  #取消一个任务
            time.sleep(0.5)
            New_Task_Num2 = int(Num_task(self.driver))                                               #获得最新任务个数
            print ('New_task2 是%s'% New_Task_Num2)
            Num =New_Task_Num2+1 
            self.assertEqual(str(New_Task_Num3),str(Num))
            self.driver.find_element_by_id('tab-history').click()                                     #切到历史任务页
            time.sleep(1)
            Old_Task_Num2 = int(Num_task(self.driver))                                               #历史任务个数
            print ('Old_task2 是%s'% Old_Task_Num2)
            print(Old_Task_Num2)
            Old_Num = Old_Task_Num2 -1    
            self.assertEqual(Old_Num,Old_Task_Num3)
        elif New_Task_Num == 100:
            pass    

    def  test_c_task_mng2(self):
        '''删除历史任务'''
        Open_Rwgl(self.driver)                                                                  #打开任务管理并切换iframe
        time.sleep(1)
        self.driver.find_element_by_id('tab-history').click()                                   #历史任务
        time.sleep(1)
        His_Task_Num = int(Num_task(self.driver))                                                #历史任务任务个数
        print (His_Task_Num)
        if His_Task_Num == 0:
            Currect_url = Get_url('currenturl')
            self.driver.get(Currect_url)
            #self.driver.switch_to.parent_frame()
            time.sleep(1)          
            #打开终端管理，先下发几个任务
            fast_kill(self.driver)                                                                  #闪电查杀
            self.driver.switch_to.alert.accept()                                                    #确定
            shou_Ye(self.driver)                                                                    #进入首页   
            Open_Rwgl(self.driver)                                                                  #打开任务管理并切换iframe
            time.sleep(1)             
            Qx_task(self.driver)  #取消一个任务
            time.sleep(0.5)
            self.driver.find_element_by_id('tab-history').click()                                   #切到历史任务页
        time.sleep(1)
        Old_Task_Num2 = int(Num_task(self.driver))                                                   #历史任务个数 
        time.sleep(0.5)
        print (Old_Task_Num2)
        Qx_task(self.driver)                                                                      #删除（和取消的xpath一样0
        time.sleep(0.5)
        Old_Task_Num3 = int(Num_task(self.driver))                                                  #删除后的历史任务个数
        print (Old_Task_Num3)
        Old_Num = Old_Task_Num3+1

        self.assertEquals(Old_Num,Old_Task_Num2)



    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == "__main__":
    #添加测试套件
    sui = unittest.TestSuite()
    sui.addTest(RWGL_test('test_c_task_mng'))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(sui)
