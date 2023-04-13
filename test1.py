# 好好学习 努力赚钱
# huhaoran
# coding=utf-8
# description: 装饰器模式 方法可以作为装饰器
import logging

logging.basicConfig(level=logging.INFO)


def loggingDecorator(func):
    """记录日志的装饰器"""

    def wrapperLogging(*args, **kwargs):
        logging.info("开始执行%s()..." % func.__name__)
        func(*args, **kwargs)
        logging.info("开始结束%s()..." % func.__name__)

    return wrapperLogging


def showInfo(*args, **kwargs):
    print("这是一个测试函数，参数：", args, kwargs)


@loggingDecorator
def showSum(a, b):
    print("%d、%d 的和为：%d" % (a, b, a + b))


if __name__ == '__main__':
    decoratedShowInfo = loggingDecorator(showInfo)
    decoratedShowInfo('arg1', 'arg2', kwarg1=1, kwarg2=2)
    showSum(1, 1)
