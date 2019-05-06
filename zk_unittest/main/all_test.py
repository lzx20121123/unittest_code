import unittest
import HTMLTestRnner
import time
import os

test_dir ='../zk_unittest/case'
discover= unittest.defaultTestLoader.discover(test_dir,pattern='test*.py', top_level_dir=None)







if __name__ == "__main__":
    filename = '../zk_unittest/logfile/report%s.html' % time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(filename,'w',encoding='utf-8') 
    runner = HTMLTestRnner.HTMLTestRunner(
        stream=fp, 
        title='中控测试报告',   
        description='用例执行情况：'
    )
    #runner = unittest.TextTestRunner()

    runner.run(discover)
    fp.close()
    