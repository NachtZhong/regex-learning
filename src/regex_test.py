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
    s = 'aa aa aaaa'
    regex = r'a{2,5}'  # 匹配2-5个a, 贪心匹配
    print_match_phases(regex, s)  # ['aa', 'aa', 'aaaa']
    # 非贪心匹配(匹配上之后就停止匹配)
    s = 'aa aa aaaa'
    regex = r'a{2,5}?'  # 匹配2-5个a, 加?代表非贪心匹配
    print_match_phases(regex, s)  # ['aa', 'aa', 'aa', 'aa']
    # 提取手机号的简单case
    s = '联系人: 13977892920'
    regex = r'1[0-9]{10}'  # 1开头, 后面是10位数字, 提取手机号, 比较简单的匹配号码正则
    print_match_phases(regex, s)  # ['13977892920']
    # 纵向匹配
    s = 'hello  hallo hjllo hfuckllo'
    regex = r'h[ej]llo'  # 匹配h开头, llo结尾的单词, 中间的字母可以是e/j
    print_match_phases(regex, s)  # ['hello', 'hjllo']
    # 字符组的简写方式1 - 范围法
    s = 'ha hb hc hd he hf hg hh hi hj haa'
    regex = r'h[a-d]{1}'  # 匹配h开头, 后面为a~d的单词
    print_match_phases(regex, s)  # ['ha', 'hb', 'hc', 'hd', 'ha']
    # 字符组的简写方式2 - 排除范围法
    s = 'ha hb hc hd he hf hg hh hi hj haa'
    regex = r'h[^a-d]{1}'  # 匹配h开头, 后面不为a~d(加了^表示排除)的单词
    print_match_phases(regex, s)  # ['he', 'hf', 'hg', 'hh', 'hi', 'hj']
    # 字符组的简写方式3 - 常见的缩写
    s = 'd3k 123 332 98 kk9 abc ddd efg'
    regex = r'\d{2,}'  # 匹配2-n个数字  \d表示数字(digit)
    print_match_phases(regex, s)  # ['123', '332', '98']
    s = 'd3k 123 332 98 kk9 abc ddd efg'
    regex = r'\D{2,}'  # 匹配2-n个非数字  \D表示非数字(digit)
    print_match_phases(regex, s)  # ['k ', ' kk', ' abc ddd efg']
    s = 'd3k 123 332 98 kk9 abc ddd efg'
    regex = r'\w{2,}'  # 匹配2-n个数字、大小写字母和下划线 \w表示数字、大小写字母和下划线(word)
    print_match_phases(regex, s)  # ['d3k', '123', '332', '98', 'kk9', 'abc', 'ddd', 'efg']
    s = 'd3k 123 332 98 kk9 abc ddd efg'
    regex = r'\W{1,}'  # 匹配1-n个非数字、大小写字母和下划线 \W表示非单词字符(word)
    print_match_phases(regex, s)  # [' ', ' ', ' ', ' ', ' ', ' ', ' ']  - 只能匹配到空格
    # 量词的简写方式
    s = 'a a1 a11 a111 a1111 a11111'
    regex = r'a[1]?'  # a开头, 后面有0个或者1个"1"  ? 表示匹配0/1个
    print_match_phases(regex, s)  # ['a', 'a1', 'a1', 'a1', 'a1', 'a1']
    s = 'a a1 a11 a111 a1111 a11111'
    regex = r'a[1]+'  # a开头, 后面有1个或以上个"1"  +表示匹配1-n个
    print_match_phases(regex, s)  # ['a1', 'a11', 'a111', 'a1111', 'a11111']
    s = 'a a1 a11 a111 a1111 a11111'
    regex = r'a[1]*'  # a开头, 后面有0个或以上个"1"  *表示匹配0-n个
    print_match_phases(regex, s)  # ['a', 'a1', 'a11', 'a111', 'a1111', 'a11111']
    # 多选分支
    s = 'fuck the world'
    regex = r'fuck|the'  # 匹配fuck或the   | 表示或匹配
    print_match_phases(regex, s)  # ['fuck', 'the']
    # 时间匹配练习
    s = '''
        22: 00
        23: 15
        22:09
        25:01
        09:09
        9:9
    '''
    regex = r'\b((?:0?[0-9]|1[0-9]|[2][0-3]):[ ]?(?:0?[0-9]|[1-5][0-9]))\b'
    print_match_phases(regex, s)  # [('22: 00', '22', '00'), ('23: 15', '23', '15'), ('22:09', '22', '09'), ('09:09', '09', '09'), ('9:9', '9', '9')]






def print_match_phases(regex, s):
    """
    打印匹配的短语列表
    :param regex:
    :param s:
    :return:
    """
    matches = re.findall(regex, s)
    print([match for match in matches])
