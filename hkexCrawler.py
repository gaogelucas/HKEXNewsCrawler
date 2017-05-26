#!/usr/bin/env python2
# coding:utf-8
# lucas zhang 20170526


# 参考https://www.zhihu.com/question/46528604?sort=created

# 载入webdriver（需要先安装:pip install selenium）
from selenium import webdriver

# 调用浏览器模拟，需要下载chromedriver，地址https://chromedriver.storage.googleapis.com/index.html?path=2.29/
driver = webdriver.Chrome("/Users/ZhangGaoge/Downloads/chromedriver") #把链接改成你的chromedriver地址

# 模拟打开网页
driver.get("http://www.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main_c.aspx")

# 模拟填入股票代码
driver.find_element_by_name('ctl00$txt_stock_code').send_keys('00005')
# 此处以汇丰控股00005为例
# 需要在搜索页填入其他文本的话，参考element_name，逻辑同上。

# 模拟单击“搜索”
driver.find_element_by_css_selector('#aspnetForm > table > tbody > tr:nth-child(7) > td:nth-child(3) > label > a:nth-child(1)').click()

# 打印这个页面的html
print(driver.page_source)
# 通过driver.page_source获取静态html
# 有了这个静态html，就可以用一般的方法进行解析了。

# 模拟在这个页面单击下一页
driver.find_element_by_css_selector('#ctl00_btnNext2').click()

# 后续工作同上，把这些步骤打包成循环就可以实现自动解析。
# 注意这个页面采用的是繁体中文，需要采用繁体中文填入数据和解析数据。

# 以上o(￣ε￣*)
