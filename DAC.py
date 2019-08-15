from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
driver.find_element_by_id('number').send_keys('201901822146')
driver.find_element_by_id('name').send_keys('张国良')
a = input('输入验证码')
driver.find_element_by_id('yznumber').send_keys(a)
driver.find_element_by_xpath('//*[@id="PrintInfoForm"]/table[1]/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]').click()
for i in range(5787,10000):
    print(i)
    try:
        if driver.find_element_by_partial_link_text('总成绩'):
            print(driver.page_source)
            driver.save_screenshot('chengji.png')
    except Exception as e:
        pass
    driver.find_element_by_id('button').click()
    i = str(i)
    num1 = '20192{}185'.format(i.zfill(4))
    driver.find_element_by_id('number').clear()
    driver.find_element_by_id('number').send_keys(num1)
    driver.find_element_by_xpath(
        '//*[@id="PrintInfoForm"]/table[1]/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]').click()
