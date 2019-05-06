import sys,time,unittest
import random
import string
sys.path.append('F:\\zk_unittest')
from method.get_url import Get_url
from method.comm import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from method.mysql_search import MySql

class Group(unittest.TestCase):
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
        
 
 
    def test_create_group(self):
        '''新建分组'''
        zdgl_page(self.driver)
        Creat_group(self.driver)
        name1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        name2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        name3 = ''.join(random.sample(string.ascii_letters + string.digits, 8))#生成三个随机名字
        name4 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        self.driver.find_element_by_id('group-name').send_keys(name1)          #创建第一个分组
        self.driver.find_element_by_id('ok').click()                            #确定
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        time.sleep(2)
        #创建二级分组
        Creat_group(self.driver)
        self.driver.find_element_by_id('lst-client').click()
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name1).click()     #very good
        self.driver.find_element_by_xpath('//*[@id="d-cur"]/span').click()
        self.driver.find_element_by_id('group-name').send_keys(name2)          #创建第2个分组
        self.driver.find_element_by_id('ok').click() 
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        #创建三级分组
        time.sleep(2)
        Creat_group(self.driver)
        self.driver.find_element_by_id('lst-client').click()
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name1).click()     #very good
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name2).click()     #very good
        self.driver.find_element_by_xpath('//*[@id="d-cur"]/span').click()
        self.driver.find_element_by_id('group-name').send_keys(name3)          #创建第2个分组
        self.driver.find_element_by_id('ok').click() 
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        #再创建一级分组
        time.sleep(2)
        Creat_group(self.driver)
        self.driver.find_element_by_id('lst-client').click()
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name1).click()     #very good
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name2).click()     #very good
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name3).click() 
        self.driver.find_element_by_xpath('//*[@id="d-cur"]/span').click()
        self.driver.find_element_by_id('group-name').send_keys(name4)          #创建第2个分组
        self.driver.find_element_by_id('ok').click() 
        time.sleep(1)
        m = self.driver.find_element_by_xpath('//*[@id="group-content"]/div[3]')
        self.assertEqual('添加失败：分组最多三层！',m.text)    
        self.driver.switch_to.parent_frame()

    
    def test_change_group2(self):
        '''编辑分组'''
        zdgl_page(self.driver)
        Creat_group(self.driver)
        name1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        name2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        print (name2)
        self.driver.find_element_by_id('group-name').send_keys(name1)          #创建第一个分组
        self.driver.find_element_by_id('ok').click()                            #确定
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        #检验修改的终端是否在新的分组里
        time.sleep(2)
        #通过数据库查询name对应的ID
        sq = 'select hash_key from report_group where name="%s"'%name1
        Id = MySql(sq)
        #print (Id)
        ID = 'tree_li_'+Id
        Xpath = '//*[@id="%s"]/div[1]/span[1]/a'%ID
        print(Xpath)
        #定位到要悬停的元素
        move = self.driver.find_element_by_id(ID)
        #对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(Xpath).click()
        iF = self.driver.find_element_by_xpath('//*[@id="inside"]/iframe')
        self.driver.switch_to.frame(iF)
        #修改分组名称
        self.driver.find_element_by_id('group-name').clear()
        self.driver.find_element_by_id('group-name').send_keys(name2)
        self.driver.find_element_by_id('ok').click()
        time.sleep(1)
        te = self.driver.switch_to.alert
        self.assertEqual('修改分组成功',te.text)
        te.accept()
        sq2 = 'select name from report_group where hash_key="%s"'%Id
        n = MySql(sq2)
        print (n)
        self.assertEqual(n,name2)

    
    def test_del_group(self):
        '''删除分组'''
        zdgl_page(self.driver)
        Creat_group(self.driver)
        name1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        name2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        self.driver.find_element_by_id('group-name').send_keys(name1)          #创建第一个分组
        self.driver.find_element_by_id('ok').click()                            #确定
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        #检验修改的终端是否在新的分组里
        time.sleep(2)
        #通过数据库查询name对应的ID
        sq = 'select hash_key from report_group where name="%s"'%name1
        Id = MySql(sq)
        #print (Id)
        ID = 'tree_li_'+Id
        Xpath = '//*[@id="%s"]/div[1]/span[2]/a'%ID
        print(Xpath)
        #定位到要悬停的元素
        move = self.driver.find_element_by_id(ID)
        #对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(Xpath).click()
        time.sleep(1)
        me = self.driver.switch_to.alert
        self.assertEqual('确定删除分组？',me.text)
        me.accept()           
        sq2 = 'select deleted name from report_group where name="%s"'%name1
        re = MySql(sq2)
        print (re)
        self.assertEqual(re,1)
        
        
    

    def test_change_group(self):
        '''更改分组-未勾选'''
        #打开终端管理页面
        zdgl_page(self.driver)  
        Change_group(self.driver)
        mess = self.driver.switch_to.alert
        self.assertEqual('请选择要更改分组的终端',mess.text)
        mess.accept()


    def test_change_group3(self):
        '''更改分组-'''  
        zdgl_page(self.driver)
        #添加一个分组
        Creat_group(self.driver)
        name1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        self.driver.find_element_by_id('group-name').send_keys(name1)          #创建第一个分组
        self.driver.find_element_by_id('ok').click()                            #确定
        time.sleep(1)
        mess = self.driver.switch_to.alert
        self.assertEqual('添加分组成功',mess.text)
        mess.accept()
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]/a'%name1)
        time.sleep(2)
        IP = self.driver.find_element_by_xpath('//*[@id="table"]/table/tbody[2]/tr[2]/td[4]').text  
        #修改分组
        self.driver.find_element_by_xpath('//*[@id="table"]/table/tbody[2]/tr[2]/td[1]/a').click() #勾选第一个终端
        Change_group(self.driver) #更改分组
        iFrame = self.driver.find_element_by_xpath('//*[@id="inside"]/iframe')
        self.driver.switch_to.frame(iFrame)
        self.driver.find_element_by_id('lst-client').click()
        self.driver.find_element_by_xpath('//span[@class="tree_ic" and @title="%s"]'%name1).click()
        self.driver.find_element_by_xpath('//*[@id="d-up-level"]/span').click()
        time.sleep(1)
        self.driver.find_element_by_id('ok').click()
        time.sleep(1)
        mes = self.driver.switch_to.alert
        self.assertEqual('更改分组成功',mes.text)
        mess.accept()
        #检验修改的终端是否在新的分组里
        time.sleep(2)
        #通过数据库查询name对应的ID
        sq = 'select hash_key from report_group where name="%s"'%name1
        Id = MySql(sq)
        #print (Id)
        ID = 'tree_li_'+Id
        #print (ID)
        self.driver.find_element_by_id(ID).click()
        IP2 = self.driver.find_element_by_xpath('//*[@id="table"]/table/tbody[2]/tr[2]/td[4]').text
        print(IP2)
        self.assertEqual(IP, IP2)



    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()


if __name__ == "__main__":
    sui = unittest.TestSuite()
    sui.addTest(Group('test_del_group'))
    

    runner = unittest.TextTestRunner()
    runner.run(sui)
