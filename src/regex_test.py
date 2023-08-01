#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    regex_test.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Nacht
    :copyright: (c) 2023, GuiltyCrown
    :date created: 2023/8/1
    
"""
import re


def setup_function():
    print('')
    print('---------------------------------------------')

def teardown_function():
    print('')
    print('---------------------------------------------')


def test_regex():
    """
    正则测试
    {}用于表示量词, 表示匹配括号内指定数量的字符
    []用于表示字符组, 表示匹配括号内指定范围的字符
    ()用于表示分组, 表示括号内匹配上的字符短语会作为一个整体处理
    :return:
    """
    print('')
    # 贪心匹配(尽可能匹配更多字符)
    str1 = 'aa aa aaaa'
    regex1 = r'a{2,5}'  # 匹配2-5个a, 贪心匹配
    print_match_phases(regex1, str1)  # ['aa', 'aa', 'aaaa']
    # 非贪心匹配(匹配上之后就停止匹配)
    str2 = 'aa aa aaaa'
    regex2 = r'a{2,5}?'  # 匹配2-5个a, 加?代表非贪心匹配
    print_match_phases(regex2, str2)  # ['aa', 'aa', 'aa', 'aa']
    # 提取手机号的简单case
    str3 = '联系人: 13977892920'
    regex3 = r'1[0-9]{10}'  # 1开头, 后面是10位数字, 提取手机号, 比较简单的匹配号码正则
    print_match_phases(regex3, str3)  # ['13977892920']
    # 纵向匹配
    str4 = 'hello  hallo hjllo hfuckllo'
    regex4 = r'h[ej]llo'  # 匹配h开头, llo结尾的单词, 中间的字母可以是e/j
    print_match_phases(regex4, str4)  # ['hello', 'hjllo']
    # 字符组的简写方式1 - 范围法
    str5 = 'ha hb hc hd he hf hg hh hi hj haa'
    regex5 = r'h[a-d]{1}'  # 匹配h开头, 后面为a~d的单词
    print_match_phases(regex5, str5)  # ['ha', 'hb', 'hc', 'hd', 'ha']
    # 字符组的简写方式2 - 排除范围法
    str6 = 'ha hb hc hd he hf hg hh hi hj haa'
    regex6 = r'h[^a-d]{1}'  # 匹配h开头, 后面不为a~d(加了^表示排除)的单词
    print_match_phases(regex6, str6)  # ['he', 'hf', 'hg', 'hh', 'hi', 'hj']





def print_match_phases(regex, s):
    """
    打印匹配的短语列表
    :param regex:
    :param s:
    :return:
    """
    matches = re.findall(regex, s)
    print([match for match in matches])
