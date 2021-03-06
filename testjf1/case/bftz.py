import threading
import unittest
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH


class TestTouzibf(unittest.TestCase):

    def test_bftz():
        driver=webdriver.Chrome()
        driver.get('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))


        driver.find_element_by_id ('login').send_keys ('13301307172')
        time.sleep(1)
        e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
        action = ActionChains (driver)
        action.move_to_element (e1).click ().send_keys ("2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()

        driver.find_element_by_xpath(".//*[@id='logindiv']/div/div[2]").submit()
        time.sleep(1)
        driver.get("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=477a34ea-b344-49fa-8dc2-b256b7502079")
        time.sleep(1)
        #
        driver.find_element_by_id("amount").send_keys("100")
        # driver.find_element_by_xpath(".//*[@id='clientInvestForm']/div[4]/a").click()
        driver.find_element_by_link_text("立即投资").click()
        time.sleep(3)
        #sreach_window=driver.current_window_handle
        #driver.find_element_by_xpath(".//*[@id='PDF9hFVQpC']/div[1]/div[3]/input[1]").click()
        driver.find_element_by_class_name("dialogBtn").click()
        #input class="dialogBtn" type="button" value="确定"

    threads = []
    t1 = threading.Thread(target=test_bftz)
    threads.append(t1)
    t2 = threading.Thread(target=test_bftz)
    threads.append(t2)
    t3 = threading.Thread(target=test_bftz)
    threads.append(t3)
    t4 = threading.Thread(target=test_bftz)
    threads.append(t4)
    t5 = threading.Thread(target=test_bftz)
    threads.append(t5)


    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join ()




