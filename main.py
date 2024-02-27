# coding=utf-8
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

# 构建缩写与中文的字典（以所爬网站内的列表值为值，对应的缩写为键，提供的参考标准不全且中文表述不一因此只能手动录入）
dict = {"GBP": "英镑", "HKD": "港币", "USD": "美元", "CHF": "瑞士法郎", "DEM": "德国马克", "FRF": "法国法郎", "SGD": "新加坡元", "SEK": "瑞典克朗", "DKK": "丹麦克朗", "NOK": "挪威克朗", "JPY": "日元", "CAD": "加拿大元", "AUD": "澳大利亚元", "EUR": "欧元", "MOP": "澳门元", "PHP": "菲律宾比索", "THP": "泰国铢", "NZD": "新西兰元", "KRW": "韩元", "SUR": "卢布", "MYR": "林吉特", "TWD": "新台币", "ESP": "西班牙比塞塔", "ITL": "意大利里拉", "NLG": "荷兰盾", "BEF": "比利时法郎", "FIM": "芬兰马克", "INR": "印度卢比", "IDR": "印尼卢比", "BRC": "巴西里亚尔", "AED": "阿联酋迪拉姆", "ZAR": "南非兰特", "SAR": "沙特里亚尔", "TRL": "土耳其里拉"}
def get_forex_rate(date, currency_code):
    # 创建Chrome驱动对象
    driver = webdriver.Chrome()
    try:
        # 打开中国银行外汇牌价网站
        driver.get('https://www.boc.cn/sourcedb/whpj/')

        # 输入起始日期
        date_start = driver.find_element('id', 'erectDate')
        date_start.clear()
        date_start.send_keys(date[0:4] + '-' + date[4:6] + '-' + date[6:8])
        # time.sleep(2)

        # 输入结束日期
        date_start = driver.find_element('id', 'nothing')
        date_start.clear()
        date_start.send_keys(date[0:4] + '-' + date[4:6] + '-' + date[6:8])
        # time.sleep(2)

        # 选择货币
        currency_select = Select(driver.find_element('id', 'pjname'))
        currency_select.select_by_value(dict[currency_code])
        # time.sleep(1)

        # 点击查询按钮
        parent_element = driver.find_element('id', 'historysearchform')
        query_button = parent_element.find_element('class name', 'search_btn')
        query_button.click()
        time.sleep(1) # 等待加载完毕

        # 获取现汇卖出价
        tables = driver.find_elements('xpath', '//table') #定位到全部的table
        table = tables[1] #所需表格为第二个表格
        title = table.find_element('xpath', './/tbody/tr[1]/th[4]').text
        currency_price = table.find_element('xpath', './/tbody/tr[2]/td[4]').text

        # 打印结果
        print(f"The {title} on {date} for {currency_code} is: {currency_price}")

        # 将结果写入文件
        with open("result.txt", "w") as file:
            file.write(f"The {title} on {date} for {currency_code} is: {currency_price}")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # 关闭浏览器
        driver.quit()

# 从命令行参数获取日期和货币代号
if len(sys.argv) != 3:
    print("Usage: python3 yourcode.py <date> <currency_code>")
else:
    date = sys.argv[1]
    currency_code = sys.argv[2]
    get_forex_rate(date, currency_code)
