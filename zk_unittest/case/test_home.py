from selenium import webdriver
import sys
sys.path.append('F:\\zk_unittest')
from method.comm import *
from method.file_path import Get_filepath
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class Homez_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        u'''登录，打开首页'''
        print('start')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        url =Get_url('loginurl')
        cls.driver.get(url)
        Login_success(cls.driver)                                      #--登录
        time.sleep(2)
        #shou_Ye(self.driver)                                            #--进入首页
        time.sleep(1)
        cls.driver.implicitly_wait(5)                                  #设置超时


    def test_current(self):
        u'''进入全网查杀'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_full_scan"]/a/span').click()
        currenturl = Get_url('currenturl')          #终端管理url
        time.sleep(0.5)
        url = self.driver.current_url               #获取当前页面url
        self.assertEqual(currenturl,url)
    def test_c_config_send(self):
        u'''进入配置下发'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_config_send"]/a/span').click()
        c_config_send = Get_url('c_config_send')    #策略中心 > 终端配置页面
        time.sleep(0.5)
        url = self.driver.current_url               #获取当前页面
        self.assertEqual(c_config_send,url)

    def test_c_white_list(self):
        '''进入企业白名单'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_white_list"]/a/span').click()
        c_white_list = Get_url('c_white_list') 
        #print(c_white_list)
        time.sleep(0.5)
        url = self.driver.current_url
        self.assertEqual(c_white_list,url)

    def test_c_shedule_task(self):
        '''首页--计划任务'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_shedule_task"]/a/span').click()
        c_shedule_task = Get_url('c_shedule_task')
        #print(c_shedule_task)
        time.sleep(0.5)
        url = self.driver.current_url
        self.assertEqual(c_shedule_task,url)
    #def Cancel_Task(self):
        



    def test_virus_manage(self):
        '''首页--查看更多统计：威胁管理'''
        shou_Ye(self.driver)                                            #--进入首页
        see_more_count = self.driver.find_element_by_css_selector('.wordStyle')
        ActionChains(self.driver).move_to_element(see_more_count).perform()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="thread_tend_content"]/div[2]/ul/li/ul/li[2]/a').click()
        currenturl = self.driver.current_url
        url = Get_url('virus_manage')
        self.assertEquals(url ,currenturl)

    def test_leak_manage(self):
        '''查看更多统计：漏洞管理'''
        shou_Ye(self.driver)                                            #--进入首页
        see_more_count = self.driver.find_element_by_css_selector('.wordStyle')
        ActionChains(self.driver).move_to_element(see_more_count).perform()
        self.driver.find_element_by_xpath('//*[@id="thread_tend_content"]/div[2]/ul/li/ul/li[1]/a').click()
        currenturl = self.driver.current_url
        url = Get_url('leak_manage')
        self.assertEqual(url,currenturl)

    def test_warning_refresh(self):
        '''安全动态--刷新'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_id('warining-refresh').click()       #刷新
        now_time = str(time.strftime('%Y'))   
        now_time2 = str(int(time.strftime('%m')))
        now_time3 = str(int(time.strftime('%d')))
        now_time4 = str(time.strftime('%H:%M'))     
        now = '%s-%s-%s %s'%(now_time,now_time2,now_time3,now_time4)     #拼接出与中控格式一样的时间   
        time_text = self.driver.find_element_by_id('warning-info')       #获取最新刷新时间
        self.assertIn(now,time_text.text)

    def test_more_info(self):
        '''安全动态--查看更多动态'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_css_selector('#s_status .more_info').click()      #进入威胁管理
        time.sleep(0.5)
        currenturl = self.driver.current_url
        url = Get_url('virus_manage')                           
        self.assertEquals(url ,currenturl)


    def test_d_info_footer(self):
        '''上级控制中心--级联设置'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="d_info_footer"]/td[3]/a').click()
        time.sleep(1)
        jl_Url = self.driver.current_url
        url = Get_url('d_info_footer')
        self.assertEquals(jl_Url,url)

    def test_c_msg_notice(self):
        '''消息公告'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_msg_notice"]/span').click()
        xx = self.driver.find_element_by_xpath('//*[@id="inside"]/iframe')          #iframe 切换
        self.driver.switch_to.frame(xx)
        self.driver.find_element_by_xpath('//*[@id="ipt-title"]').send_keys('123')  
        self.driver.find_element_by_id('tt-content').send_keys('111')
        self.driver.find_element_by_id('btn-send').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        text = alert.text
        self.assertIn('消息发送成功',text)
        #self.driver.switch_to.parent_frame() 
    def test_c_msg_notice2(self):
        '''消息公告--未填写内容'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="c_msg_notice"]/div').click()
        #
        xx = self.driver.find_element_by_class_name('w_iframe')
        self.driver.switch_to.frame(xx)
        self.driver.find_element_by_id('ipt-title').send_keys(22222)
        #self.driver.find_element_by_id('tt-content').send_keys('')
        self.driver.find_element_by_id('btn-send').click()
        time.sleep(1)
        te = self.driver.switch_to.alert
        self.assertEquals('请输入消息内容',te.text)

    def test_online_count(self):
        '''在线台数验证'''
        #首页在线台数
        shou_Ye(self.driver)                                            #--进入首页
        syzx = self.driver.find_element_by_id('online_count').text      
        #print (syzx)
        #进入终端管理页面获取在线台数
        zdgl_page(self.driver)  
        time.sleep(1)
        self.driver.find_element_by_id('lst-status').click()                      
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('mgr-chk').click()
        time.sleep(1)
        zdzx = self.driver.find_element_by_xpath('//*[@id="select-count"]/span').text
        self.assertEquals(syzx,zdzx)
        #print (zdzx)
    def test_online_rate(self):
        '''在线率验证'''
        shou_Ye(self.driver)                                            #--进入首页
        #首页在线率
        syzxl = self.driver.find_element_by_id('online_rate').text      #首页在线率
        #进入终端管理页面获取在线台数
        zdgl_page(self.driver) 
        time.sleep(1)
        #获取全部台数
        self.driver.find_element_by_class_name('mgr-chk').click()
        zdqb = int(self.driver.find_element_by_xpath('//*[@id="select-count"]/span').text ) #全部台数
        #print(zdqb)
        #获取在线台数
        zdgl_page(self.driver)
        self.driver.find_element_by_id('lst-status').click()                      
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('mgr-chk').click()
        time.sleep(1)
        zdzx = int(self.driver.find_element_by_xpath('//*[@id="select-count"]/span').text)   #在线台数       
        #由于Python计算的在线率四舍五入存在问题，所以比较 计算的在线率和首页计算率的误差大于0.01 说明在线率不准确
        zxl= float('%.2f' % (zdzx/zdqb))

        syzxl = float(syzxl.strip('%'))/100       
        x = syzxl - zxl
        if x == 0:
            self.assertEquals(zxl,syzxl)
        elif x > 0.011:
            self.assertEquals(zxl,syzxl)
        else:
            pass

    def test_s_infos_des(self):
        '''验证累计清除威胁数量'''
        shou_Ye(self.driver)                                            #--进入首页
        sy_num = int(self.driver.find_element_by_id('total_cleaned').text)
        #进入威胁管理
        self.driver.find_element_by_xpath('//*[@id="threat_manager"]/a').click()
        time.sleep(1)
        #选取已处理威胁
        self.driver.find_element_by_id('lst-status').click()
        self.driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[3]/a').click()
        self.driver.find_element_by_class_name('mgr-chk').click()
        #获得勾选的已处理威胁数量
        wx_num = int(self.driver.find_element_by_class_name('count').text)
        if sy_num <wx_num:
            self.assertEquals(sy_num,wx_num)
        else:
            pass

    def test_item_title(self):
        '''首页--安全概况'''
        shou_Ye(self.driver)                                            #--进入首页
        zdgl_page(self.driver)               #终端管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="filter"]/div[2]/a[1]').click()  #勾选所有终端
        time.sleep(1)
        terminal_Num = int(self.driver.find_element_by_xpath('//*[@id="select-count"]/span').text) #终端个数
        print ('%s 个终端'% terminal_Num)
        if terminal_Num ==0:
            self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[1]/a').click() #打开首页
            time.sleep(2)
            print(2)
            self.driver.find_element_by_xpath('//*[@id="s_info_title0"]/div[2]/span').click()  #点击立即部署
            iFrame = self.driver.find_element_by_xpath('//*[@id="inside"]/iframe')  
            self.driver.switch_to.frame(iFrame)
            url = self.driver.find_element_by_id('url').text
            DownUrl = Get_url('downUrl')
            #比对url是否一致
            self.assertEquals(url,DownUrl)
        else:
            self.driver.find_element_by_xpath('//*[@id="threat_manager"]/a').click()                #打开威胁管理
            time.sleep(2)
            self.driver.find_element_by_id('lst-status').click()                                    #所有状态
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[2]/a').click()      #新发现
            time.sleep(1)
            self.driver.find_element_by_class_name('mgr-chk').click()                                #全选
            time.sleep(1)
            Virus_Num = int(self.driver.find_element_by_xpath('//*[@id="select-count"]/span').text) #获取新发现病毒个数
            print('%s个新发现病毒'% Virus_Num)
            if Virus_Num ==0:
                #全网扫描   
                self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[1]/a').click()                 #打开首页
                time.sleep(1)
                print(3)
                self.driver.find_element_by_id('s_scan_des').click() 
                self.driver.find_element_by_xpath('//*[@id="inside"]/div/div[2]/a').click()             #全网扫描
                time.sleep(1)
                mess = self.driver.find_element_by_id('s_scan_des').text                   
                self.assertEquals(mess,'指令已下达')
            else:
                #病毒清除
                self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[1]/a').click()                 #打开首页
                print (1)
                time.sleep(1)
                self.driver.find_element_by_id('s_clean_desc').click()                                  #病毒清除
                time.sleep(1)
                mess2 = self.driver.find_element_by_id('s_clean_desc').text                             #获取文本
                self.assertEquals(mess2,'指令已下达')

    def test_deploy_tips(self): 
        '''部署安装'''
        shou_Ye(self.driver)                                            #--进入首页
        self.driver.find_element_by_xpath('//*[@id="deploy_tb"]/tbody/tr[6]/td[2]/a').click()
        iFrame = self.driver.find_element_by_xpath('//*[@id="inside"]/iframe')
        self.driver.switch_to.frame(iFrame)
        down_url = self.driver.find_element_by_id('url').text 
        self.driver.find_element_by_id('preview').click()
        now_windows = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != now_windows:
                self.driver.switch_to.window(handle)
        now_url=  self.driver.current_url
        self.assertEquals(down_url,now_url)
        text = self.driver.find_element_by_id('tip').text
        self.assertIn('请根据以下平台下载客户端并安装',text)

    def test_Z_btn_vup(self):
        '''首页-软件升级-检查版本'''
        shou_Ye(self.driver)                                            #--进入首页
        url = Get_url('version_mgr1')
        self.driver.get(url)
        time.sleep(1)
        textt = self.driver.find_element_by_xpath('//*[@id="win-normal"]/div[2]/div[1]/span[2]/span').text  #获取终端管理页面的版本号
        print(textt)
        if textt =='':
            self.driver.find_element_by_id('win-normal').click()
            time.sleep(1)
            filepath = Get_filepath('zhongduan')
            self.driver.find_element_by_id('file').send_keys(filepath)      
            time.sleep(15)
            te = self.driver.switch_to.alert
            self.assertIn('上传成功',te.text)
            te.accept()
            time.sleep(2)
            textt = self.driver.find_element_by_xpath('//*[@id="win-normal"]/div[2]/div[1]/span[2]/span').text      #获取终端管理页面的版本号
            print(textt)
        time.sleep(1)
        shou_Ye(self.driver)
        self.driver.find_element_by_id('btn-sversion').click()              #首页的'软件版本'
        version = self.driver.find_element_by_id('newest_version').text    #首页的版本号
        print(version)
        self.assertEqual(textt,version)
        #print

    def test_btn_sup(self):
        '''首页-病毒库升级-检查版本'''
        shou_Ye(self.driver)                                            #--进入首页
        url = Get_url('version_mgr1')
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_id('virusdb-nav').click()
        self.driver.find_element_by_id('manual-radio').click()
        textt = self.driver.find_element_by_xpath('//*[@id="jingyun"]/div[2]/div[1]/span[1]/span').text  #获取终端管理页面的病毒库版本号
        #print(textt)
        if textt =='':
            self.driver.find_element_by_id('jingyun').click()
            time.sleep(1)
            filepath = Get_filepath('bingduku')
            self.driver.find_element_by_id('file').send_keys(filepath)      
            time.sleep(15)
            te = self.driver.switch_to.alert
            self.assertIn('上传成功',te.text)
            te.accept()
            time.sleep(2)
            textt = self.driver.find_element_by_xpath('//*[@id="jingyun"]/div[2]/div[1]/span[1]/span').text      #获取终端管理页面的病毒库版本号
            #print(textt)
        time.sleep(1)
        shou_Ye(self.driver)
        time.sleep(2)
        #self.driver.find_element_by_id('btn-sversion').click()             #首页的'软件版本'
        version = self.driver.find_element_by_id('newest_version').text    #首页的版本号
        #print(version)   
        self.assertEqual(textt,version)
    def test_v_name_url(self):
        '''公司网址、标题'''
        shou_Ye(self.driver)                                            #--进入首页
        gsmc = self.driver.find_element_by_xpath('//*[@id="logo"]/span').text
        print (gsmc)
        if gsmc == '景云网络防病毒系统':
            gsxx =self.driver.find_element_by_id('copyright').text
            self.assertIn('北京辰信领创信息技术有限公司 版权所有 | 版本号', gsxx) 
            now_windows = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//*[@id="office-site"]/a').click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != now_windows:
                    self.driver.switch_to.window(handle)
                    time.sleep(2)
                    gw = self.driver.current_url    
                    self.assertEqual('http://www.v-secure.cn/',gw)
        if gsmc == '北信源网络防病毒系统':
            gsxx =self.driver.find_element_by_id('copyright').text
            self.assertIn('北信源软件股份有限公司 版权所有 | 版本号', gsxx)
            now_windows = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//*[@id="office-site"]/a').click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != now_windows:
                    self.driver.switch_to.window(handle)
                    time.sleep(2)
                    gw = self.driver.current_url    
                    self.assertEqual('http://www.vrv.com.cn/',gw)

    


    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()

if __name__ == "__main__":
    #添加测试套件
    sui = unittest.TestSuite()
    sui.addTest(Homez_test('test_v_name_url'))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(sui)


