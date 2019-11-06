# -*- coding: UTF-8 -*-
'''
这是个例子～
使用很简单，直接简单粗暴的用就好啦～
格式：名字.内容
如：Miku.age
Miku=初音未来
age=年龄
详见README。
By FunctionSir 2019年11月。
'''
from virtualsinger import *
print('初音未来的年龄是：{}岁'.format(Miku.age))
print('初音未来的声优是：{}'.format(Miku.cv))
#不知道的话，输出是这样的#
print('月正绫的日文名字是：{}'.format(YueZhengling.name_ja))
#输出为'$UNKNOW$'#
#想获取一份图片？#
print('图片链接：{}'.format(LuoTianyi.img))
#还是想知道资料来源？#
print('洛天依的资料来源：{}'.format(LuoTianyi.source))
#注意：来源之间以空格隔开#
#当然，几乎所有不同信息都是空格隔开的，如：#
print('洛天依的声优是：{}'.format(LuoTianyi.cv))
print('初音未来的生日是：{}'.format(Miku.birthday))
#此处注意：birthday为以空格分割的二数字组成的字符串。格式MM DD。#
