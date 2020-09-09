# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/6/25 15:45
import logging
import time

class Logger:

    #构造函数
    def get_logger(self):
        #获取日志器
        logger = logging.getLogger('logger')
        # 设置日志等级
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            # 创建控制台输出日志处理器对象
            sh = logging.StreamHandler()
            # 将控制台日志处理器添加到日志器中
            logger.addHandler(sh)
            # 创建文件日志处理器对象
            # fh = logging.FileHandler("{}_log.txt".format(time.strftime('%Y%m%d%H%M%S', time.localtime())), encoding='utf-8')
            # 将处理器添加到日志器中
            # logger.addHandler(fh)
            # 格式器：注意格式
            formatter = logging.Formatter(fmt="%(asctime)s-%(filename)s-行号:%(lineno)d-函数:%(funcName)s:%(message)s",
                                          datefmt='%Y%m%d%H%M%S')
            sh.setFormatter(formatter)
            # fh.setFormatter(formatter)
        return logger

def sum(*args):
    #传入元组的时候，args[0]打印的是整个元组
    print(args[0], type(args[0]))

if __name__ == '__main__' :
    log = Logger().get_logger()
    log.info('message')
    #普通格式化
    print('%s %d %f'%('hello', 33, 1.24))
    dict1 = {"filename":'aaa.txt', 'lineno':33}
    #通过字典的方式，输入格式化字符串有四种方式
    print('%(filename)s %(lineno)d'%{"filename":'aaa.txt', 'lineno':33})
    print("{filename}, {lineno}".format(**dict1))     #**dict代表字典
    print("{filename}, {lineno}".format(filename='aaa', lineno=33))
    print("{0[filename]}, {0[lineno]}".format(dict1))
    fileter=[1,2,3,4]
    tupe=(1,2,3,4)
    print(*fileter,  *tupe)  #结果输入元组中的元素->1 2 3 4
    sum(fileter)
