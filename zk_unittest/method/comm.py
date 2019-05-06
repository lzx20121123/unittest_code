import sys,time
from selenium import webdriver
sys.path.append('F:\\zk_unittest')
from method.get_url import Get_url






def Login(driver,user,passwd):
   
    driver.find_element_by_id('uname').send_keys(user)
    driver.find_element_by_id('pwd').send_keys(passwd)
    driver.find_element_by_id('login').click()
    time.sleep(2)


#登录
def Login_success(driver):
    #url = Get_url('correcturl')
    #time.sleep(1)
    Login(driver,'admin','vsecure2016')

#打开首页
def shou_Ye(driver):
    #driver.find_element_by_class_name('current').click()
    url = Get_url('correcturl')
    driver.get(url)
    
#打开终端管理
def zdgl_page(driver):
    url = Get_url('currenturl')
    driver.get(url)
#打开中控日志
def zk_log_open(driver):
    url = Get_url('log_zk')
    driver.get(url)
#打开版本管理
def zk_version_mgr(driver):
    url = Get_url('version_mgr1')
    print(url)
    driver.get(url)


#全选-静默-闪电查杀
def fast_kill(driver):
    driver.find_element_by_class_name('mgr-chk').click()                         #全选
    driver.find_element_by_id('mgr-q').click()                                        #闪电查杀
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="inside"]/div/div[2]/a[1]').click()          #静默
    time.sleep(1)

#点击闪电查杀   
def click_fast_scan(driver):
    driver.find_element_by_id('mgr-q').click()   
#点击全盘查杀
def click_overall_scan(driver):
    driver.find_element_by_id('mgr-f').click()
#升级全部
def click_update_all(driver):
    driver.find_element_by_id('mgr-u').click()
    driver.find_element_by_xpath('//*[@id="menu-lst-update"]/ul/li[1]/a').click()
#升级病毒库
def click_update_virus(driver):
    driver.find_element_by_id('mgr-u').click()
    driver.find_element_by_xpath('//*[@id="menu-lst-update"]/ul/li[2]/a').click()
#升级客户端
def click_update_client(driver):
    driver.find_element_by_id('mgr-u').click()
    driver.find_element_by_xpath('//*[@id="menu-lst-update"]/ul/li[3]/a').click()
#全选在线终端
def click_all_select(driver):
    driver.find_element_by_id('lst-status').click()
    #time.sleep(1)
    driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element_by_class_name('mgr-chk').click()
    time.sleep(1)
#选择在线终端
def online_select(driver):
    driver.find_element_by_id('lst-status').click()
    #time.sleep(2)
    driver.find_element_by_xpath('//*[@id="menu-lst-status"]/ul/li[2]/a').click()
    time.sleep(1)
#静默
def Silent(driver):
    driver.find_element_by_xpath('//*[@id="inside"]/div/div[2]/a[1]').click()
#非静默
def No_Silent(driver):
    driver.find_element_by_xpath('//*[@id="inside"]/div/div[2]/a[2]').click()
#打开任务管理
def Open_Rwgl(driver):
    #driver.find_element_by_xpath('//*[@id="c_task_mng"]/span').click()

    driver.find_element_by_xpath('//*[@id="c_task_mng"]/div').click()                  #点击任务管理
    iFrame = driver.find_element_by_xpath('//*[@id="inside"]/iframe')                  #iframe元素
    driver.switch_to.frame(iFrame)                                                     #切换iframe
#打开新建分组
def Creat_group(driver):
    driver.find_element_by_id('add-group').click()                  #点击任务管理
    iFrame = driver.find_element_by_xpath('//*[@id="inside"]/iframe')                  #iframe元素
    driver.switch_to.frame(iFrame)                                                     #切换iframe

#任务管理取消一个任务
def Qx_task(driver):
    driver.find_element_by_xpath('//*[@id="task-table"]/table/tbody[2]/tr[2]/td[9]/a').click()
#任务管理--任务个数
def Num_task(driver):
    num = driver.find_element_by_id('task-total-count').text
    return num 
#更改分组
def Change_group(driver):
    driver.find_element_by_id('mgr-m').click()         #更多操作
    driver.find_element_by_xpath('//*[@id="menu-lst-more"]/ul/li[1]/a').click() #更改分组