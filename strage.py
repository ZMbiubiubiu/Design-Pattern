#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/02"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    利用简单的工厂模式模拟商场的促销活动
    正常结账
    打折
    满减活动
    我们需要一个基类, 三个促销手段的收费类, 一个收费对象生成工厂
"""

# 基类
class Cash:
    def __init__(self, price=100, item=10):
        self.total = price * item
    def accept(self, money):
        pass

# 正常收费类
class CashNormal(Cash):
    def accept(self, money):
        return money

# 打折收费类
class CashRebate(Cash):
    def __init__(self, rebate=1):
        self.rebate = rebate
    def accept(self, money):
        return money * self.rebate

# 满减收费类
class CashReturn(Cash):
    def __init__(self, condition=0, returns=0):
        self.condition = condition
        self.returns = returns
    def accept(self, money):
        times = money // self.condition
        return money - times * self.returns

# 收费对象生成工厂
class CashFactory:
    def create_cash(self, type, *,rebate=1, condition=0, returns=0): #只能使用关键字参数
        cash = None
        if type == "normal":
            cash = CashNormal()
        elif type == "rebate":
            cash = CashRebate(rebate)
        else:
            cash = CashReturn(condition, returns)
        return cash

if __name__ == "__main__":
    factory = CashFactory()
    cashre = factory.create_cash('return',condition=1000,returns=300)
    print(cashre.accept(10000))
    cashno = factory.create_cash('normal')
    print(cashno.accept(10000))
    cashrebate = factory.create_cash('rebate', rebate=0.8)
    print(cashrebate.accept(10000))