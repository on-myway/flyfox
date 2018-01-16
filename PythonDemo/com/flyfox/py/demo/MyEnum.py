'''
Created on 2018年1月15日

@note: 枚举类
@author: huangl
'''
from enum import Enum, unique

''''
@author: huangl
@note: 自定义枚举类
'''
@unique
class MyEnum(Enum):
    Sun = 0; # Sun的value被设定为0
    Mon = 1;
    Tue = 2;
    Wed = 3;
    Thu = 4;
    Fri = 5;
    Sat = 6;
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));
#     for name, member in Month.__members__.items():
#         print(name, '=>', member, ',', member.value);#value属性则是自动赋给成员的int常量，默认从1开始计数