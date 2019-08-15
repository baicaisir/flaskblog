#CSDN自动点赞

import time,json,random
from selenium import webdriver

#CSDN账号
account_CSDN = "17172447586"
#CSDN密码
password_CSDN = "1235678912356789qq"

def CSDN_login():
	'''
	登录CSDN并保存cookies
	'''
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
	driver.get("https://passport.csdn.net/account/login")
	time.sleep(3)
	#进入账号密码登录界面
	driver.find_element_by_xpath("//li[@class='text-tab border-right']").click()
	time.sleep(1)
	#清空账号框中的内容
	driver.find_element_by_xpath("//input[@name='all']").clear()
	print("账号框清空完成")
	#自动填入登录用户名
	driver.find_element_by_xpath("//input[@name='all']").send_keys(account_CSDN)
	print("账号输入完成")
	#清空密码框中的内容
	driver.find_element_by_xpath("//input[@name='pwd']").clear()
	#自动填入登录密码
	driver.find_element_by_xpath("//input[@name='pwd']").send_keys(password_CSDN)
	time.sleep(3)
	#点击登录
	driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

	#获取并保存cookies
	cookies = driver.get_cookies()
	with open("cookies.txt", "w") as fp:
		json.dump(cookies, fp)


def dianZan(url_list):
	'''
	实现自动点赞功能
	'''
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
	driver.get("https://blog.csdn.net/young_foryou/article/details/86677827")
	with open("cookies.txt", "r") as fp:
		cookies = json.load(fp)
		for cookie in cookies:
			driver.add_cookie(cookie)

	print("cookies加载完成，成功登录")
	time.sleep(3)
	driver.get("https://blog.csdn.net/young_foryou/article/details/86677827")
	time.sleep(3)
	driver.find_element_by_xpath("//button[@title='点赞']").click()
	print("点赞完成！")
	time.sleep(1)




if __name__ == '__main__':
	url_list = ""
	CSDN_login()
	dianZan(url_list)
time.sleep(3)
driver.get("https://blog.csdn.net/young_foryou/article/details/86677827")
time.sleep(3)
driver.find_element_by_xpath("//button[@title='点赞']").click()
print("点赞完成！")
time.sleep(1)
