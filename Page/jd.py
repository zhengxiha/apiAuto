#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/3/13 16:07
# @Author : xiha
# @File : jd.py
# @Editor : PyCharm


from selenium.webdriver.common.by import By


page_url = 'https://www.jd.com'

elements = [
    {'name': 'search_ipt', 'desc': '搜索框点击', 'by': (By.ID, u'key'), 'ec': 'presence_of_element_located', 'action': 'send_keys()'},
    {'name': 'search_btn', 'desc': '搜索按钮点击', 'by': (By.CLASS_NAME, u'button'), 'ec': 'presence_of_element_located', 'action': 'click()'},
]