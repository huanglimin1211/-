from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

brow=webdriver.Firefox()
def is_element_exist(css):
    s=brow.find_elements_by_css_selector(css_selector=css)
    if len(s)==0:
        print('未找到元素%s'  %(css))
        return False
    elif len(s)==1:
        print('找到元素%s' %(css))
        return True
    else:
        print('找到%s个元素' %(length(s)))
        return True

def web_login(ip,username,password):
    time.sleep(5)
    brow.get(ip)
    time.sleep(3)
    brow.find_element_by_id("username").send_keys(username)
    time.sleep(3)
    #定位密码发现通过xpath定位不到，xpath比较慢，建议使用css定位
    # brow.find_element_by_xpath('//*[@id="password"]').send_keys("admin123")
    # time.sleep(2)
    brow.find_element_by_css_selector('span.ant-input-affix-wrapper:nth-child(2) > input:nth-child(1)').send_keys(password)
    time.sleep(2)
    is_element_exist('span.ant-input-affix-wrapper:nth-child(2) > input:nth-child(1)')
    brow.find_element_by_id("loginbtn").click()
    time.sleep(2)

def web_upgrade(url):    
    brow.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/ul/li[6]/div').click()
    time.sleep(1)
    brow.find_element_by_css_selector('#firpath').clear()
    time.sleep(1)
    brow.find_element_by_css_selector('#firpath').send_keys(url)
    time.sleep(1)
    brow.find_element_by_css_selector('#firpath').send_keys(Keys.ENTER)
    time.sleep(1)

    # brow.find_element_by_css_selector('#container > div > div > div.main-container.ant-layout > div.main-content > div.content-container.config-container.ant-layout > div.ant-tabs.ant-tabs-top.config-tab.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > form > div:nth-child(12) > div > div > button > span').click()
    try:
        time.sleep(30)
        reboot=is_element_exist('#container > div > div > div:nth-child(4) > div:nth-child(2) > div')
        if reboot==True:
            print("升级成功")
    except Exception as e:
        print("升级失败",format(e))

def web_reboot():
    brow.find_element_by_css_selector('#container > div > div > div.header-container.ant-layout > ul > div.header-btn-div > div:nth-child(3) > a').click()
    time.sleep(2)
    brow.find_element_by_css_selector('.poweroff').click()
    time.sleep(2)
    brow.find_element_by_css_selector('body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm > span').click()   
    try:
        time.sleep(5)
        reboot=is_element_exist('#container > div > div > div.reboot_title > div.reboot_title_span')
        if reboot==True:
            print("重启成功")
    except Exception as e:
        print("重启失败",format(e))

def web_reset():
    brow.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/ul/li[6]/div').click()
    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div[5]').click()
    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[4]/form/div[5]/div[2]/div/button/span').click()
    time.sleep(2)
    brow.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button[2]/span').click()
    try:
        time.sleep(5)
        reset=is_element_exist('.reboot_title_span')
        if reset==True:
            print("恢复出厂成功")
            pass
    except Exception as e:
        print("恢复出厂失败")


if __name__ == '__main__':
    ip1='http://192.168.125.253'
    ip2='http://192.168.125.121'
    username='admin'
    password='admin123'
    url701='http://192.168.120.166/html/hz/firmware/bat/1.0.1.33/'
    url702='http://192.168.120.166/html/hz/firmware/bat/1.0.1.28/'
    url80='http://192.168.120.166/html/hz/firmware/GXV3380/10.19.04.10/'
    # web_login(ip1,username,password)  
    # web_upgrade(url701)
    # # time.sleep(3)
    # web_login(ip1,username,password)  
    # web_upgrade(url701)
    web_login(ip1,username,password)  
    web_upgrade(url80)
# 