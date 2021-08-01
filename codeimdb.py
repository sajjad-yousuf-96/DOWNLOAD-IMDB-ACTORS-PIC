from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()
code='0000001'
number=1
for i in range(10):
    actor="nm"+str(code)
    urls="https://www.imdb.com/name/"+actor
    driver.get(urls)
    number=str(number)
    with open('Logo'+number+".png", 'wb') as file:
        l = driver.find_element_by_xpath('//*[@id="name-poster"]')
        file.write(l.screenshot_as_png)
    number=int(number)+1
    code=int(code)+1
    code=str(code)
    if len(code)<7:
        a="0"*(7-len(code))
    code=a+code
driver.quit()
