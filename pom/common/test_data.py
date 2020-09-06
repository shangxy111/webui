# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/7/5 19:36
import yaml
#返回一个对象
fileO = open('../common/data.yaml', 'r', encoding='utf-8')
fileO_data = yaml.load(stream=fileO, Loader=yaml.FullLoader)
print(fileO_data, type(fileO_data))
fileO.close()
