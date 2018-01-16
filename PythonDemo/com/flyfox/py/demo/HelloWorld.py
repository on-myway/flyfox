#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(r'''你好''')
a = '张三';
b = a;
a = '李四';
print(b);

a = 10;
c = a // 3;
print(c);
c = a / 3;
print(c);
c = a % 3;
print(c);
#占位符
a = '你好，%s%s您已欠费%d元，请尽快缴费' %('张三','先生',100);
print(a);
print("########List集合 START ########");
listDemo = ["张三",120,["lisi","王五"]];
print(listDemo[0]);
print(listDemo[1]);
print(listDemo[-1]);
print(listDemo[2][0]);
print(listDemo[2][1]);
mymap = {"111":"张三","222":100,"333":"李四"};
name = mymap.get("111",-1);
if name == -1:
    print("map不存在");
else:
    print(name);

print("########条件判断 ########");
weight = 80.5;height = 1.75;
bmi = 80.5 / (1.75*1.75);
if bmi< 18.5:
    print("过轻");
elif bmi >= 18.5 and bmi <= 25:
    print("正常");
elif bmi > 25 and bmi <= 28:
    print("过重");
elif bmi >28 and bmi <= 32:
    print("肥胖");
elif bmi >32:
    print("严重肥胖");

print("########集合循环########");
for item in listDemo:
    print(item);