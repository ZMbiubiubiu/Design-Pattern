#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/02"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    简单的工厂模式
    目标:实现一个计算器
"""

class Operation:
    def __init__(self, number1=0, number2=0):
        self._number1 = number1
        self._number2 = number2

    #number1可读可写
    @property
    def number1(self):
        return self._number1
    @number1.setter
    def number1(self, value):
        self._number1 = value

    # number2 可读可写
    @property
    def number2(self):
        return self._number2
    @number2.setter 
    def number2(self, value):
        self._number2 = value
    
    # 需要被子类重写的方法
    def get_result(self):
        return 0

# 接下来实现加减乘除类
class OperationAdd(Operation):
    def get_result(self):
        return self.number1 + self.number2

class OperationSub(Operation):
    def get_result(self):
        return self.number1 - self.number2

class OperationMul(Operation):
    def get_result(self):
        return self.number1 * self.number2

class OperationDiv(Operation):
    def get_result(self):
        if self.number2 == 0:
            raise ZeroDivisionError("除数不能为0")
        else:
            return self.number1 / self.number2

# 简单的工厂模式, 进行实例化
class OperationFactory:
    def create_operation(self, oper):
        operation = None
        if oper == "+":
            operation = OperationAdd()
        elif oper == "-":
            operation = OperationSub()
        elif oper == "*":
            operation = OperationMul()
        else:
            operation = OperationDiv()
        return operation

if __name__ == "__main__":
    # op = Operation()
    # print(op.number1)

    # add = OperationAdd(1,2)
    # print(add.get_result())
    factory = OperationFactory()
    operation = factory.create_operation("/")
    print(operation.get_result())
    operation.number1 = 44
    operation.number2 = 56
    print(operation.get_result())
