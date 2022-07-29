#导入seleniumfrom selenium import webdriver#导入谷歌浏览器驱动赋值为driver
driver = webdriver.Chrome(r'H:\Pycharm\chromedriver.exe')#让驱动暂停10s，防止页面渲染未完成无法获取数据
driver.implicitly_wait(10)#通过驱动的get方法打开前程无忧官网
driver.get('http://www.51job.com')#通过id找到输入框并设置其内容为测试工程师
driver.find_element_by_id("kwdselectid")#通过id找到城市选择的按钮并点击
driver.find_element_by_id("work_position_input").click()
#获取热门城市中每一个城市的em标签
cityEles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
for city in cityEles:
    cityName = city.text　　#打印城市名字
    selected = city.get_attribute('class') =='on'　　#查看每个城市是否被选中
    if (cityName == '深圳'and not selected) or (cityName !='深圳' and selected):　　　　#如果深圳没被选择 或者 除深圳以外都被选中 则点击
        city.click()
#获取确定按钮并点击
driver.find_element_by_id('work_position_click_bottom_save').click()#获取搜索按钮并点击
driver.find_element_by_css_selector('.ush  button').click()#获取测试岗位信息的所有行
jobs = driver.find_elements_by_css_selector('#resultList  div.el')#打印职位信息
for job in jobs:
    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print (' | '.join(strField))
driver.quit()