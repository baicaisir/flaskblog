# import re
# a = 'json_393939({kkkkk})'
# b = re.compile('json_393939\((.*?)\)').findall(a)
# print(b)

# a = (1,2,3)
# print(list(a))
#
# b = [1,2,3]
# print(tuple(b))
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
driver.find_element_by_id('number').send_keys('201901822146')
driver.find_element_by_id('name').send_keys('杨建')
a = input('输入验证码')
driver.find_element_by_id('yznumber').send_keys(a)
driver.find_element_by_xpath('//*[@id="PrintInfoForm"]/table[1]/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]').click()
for i in range(5000,10000):
    print(i)
    try:
        if driver.find_element_by_partial_link_text('总成绩'):
            print(driver.page_source)
            driver.save_screenshot('chengji.png')
    except Exception as e:
        pass
    driver.find_element_by_id('button').click()
    i = str(i)
    num1 = '20191{}211'.format(i.zfill(4))
    driver.find_element_by_id('number').clear()
    driver.find_element_by_id('number').send_keys(num1)
    driver.find_element_by_xpath(
        '//*[@id="PrintInfoForm"]/table[1]/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]').click()

