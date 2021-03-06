#-*- coding:utf-8 -*-
import datetime
import unittest
import time
import sys

from testjf1.common.fredpackgepage import PfRedpackage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf1.common.loginpage import LoginPage

class Test_Pfredpackage (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = PfRedpackage ()
                driver = login_page.driver
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()
                # time.sleep(1)
                login_page.click_hbgl ()
                time.sleep (0.5)
                login_page.click_pfhb ()
                time.sleep (0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.set_tel (int (d['login']))
                login_page.click_sousuo()
                login_page.click_choose()
                login_page.click_pfhbl()
                time.sleep(0.5)
                login_page.set_value("100")
                a = datetime.datetime.now ()
                b = str(a + datetime.timedelta(days=365))
                login_page.set_enddate(b)    #2018-07-28 14:52:04
                login_page.set_packetSendReason("派发原因是123")
                login_page.click_queding()
                time.sleep(1)
                #红包审核
                driver.switch_to_default_content ()
                login_page.click_cwgl()
                time.sleep(0.5)
                login_page.click_hbsh()
                time.sleep(0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.set_dhuser(int(d['login']))
                login_page.click_sousuo()
                login_page.click_quanxuan()
                time.sleep(0.5)
                login_page.click_plsh ()
                time.sleep(0.5)
                login_page.set_shreason("派发红包审核通过")
                login_page.click_tongyi()
                # login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

