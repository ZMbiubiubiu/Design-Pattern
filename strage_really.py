#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/02"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    1.利用简单的工厂模式+策略模式模拟商场的促销活动.
    2.策略模式: 它定义了算法家族, 分别封装起来, 让它们之间可以
      互相替换, 此模式让算法的变化, 不会影响到使用算法的客户.
    3.我在这里如何解析促销的描述性语句? 使用的是正则表达式
      匹配正则表达式中数字的个数
        (1)如果没有数字, 表示正常出售
        (2)有一个数字, 表示打折(bug: 打九折, 不用数字用汉字的话, 就无能为力了)
        (3)有两个数字, 表示满减
"""

import re

# 解析函数
def parse(description):
    """
    1.正常出售
    2.打n折
    3.满n减m
    """
    type = None
    rebate = None
    condition = None
    returns = None
    numbers = re.findall('\d+', description)
    length = len(numbers)
    if length == 0:
        type = "normal"
    elif length == 1:
        type = "rebate"
        rebate = int(numbers[0]) / 10
    else:
        type = "return"
        condition = int(numbers[0])
        returns = int(numbers[1])
    return type, rebate, condition, returns

# 基类
class Cash:
    def accept(self, money):
        pass
# 正常出售
class CashNormal(Cash):
    def accept(self, money):
        return money

# 打折出售
class CashRebate(Cash):
    def __init__(self, rebate):
        self.rebate = rebate
    def accept(self, money):
        return money * self.rebate

# 满减出售
class CashReturn(Cash):
    def __init__(self, condition, returns):
        self.condition = condition
        self.returns = returns
    def accept(self, money):
        times = money // self.condition
        return money - times * self.returns

# 
class Context:
    def __init__(self, description):
        type, rebate, condition, returns = parse(description)
        if type == "normal":
            cs = CashNormal()
        elif type == "rebate":
            cs = CashRebate(rebate)
        else:
            cs = CashReturn(condition, returns)
        self.cs = cs
    
    def get_result(self, money):
        return self.cs.accept(money)

if __name__ == "__main__":
    cs = Context("满300减100")
    print(cs.get_result(1000))
    cs2 = Context("正常出售")
    print(cs2.get_result(1000))
    cs3 = Context("打9折")
    print(cs3.get_result(1000))