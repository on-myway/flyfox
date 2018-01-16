import math;
#求解一元二次方程
def quadratic(a,b,c):
    dlt = b*b - 4*a*c;
    if (a==0):
        return ('这是一个一元一次方程')
    if (dlt <0) and (a != 0):
        return ('无实根')
    if dlt>0 and a != 0:
        x1 = (-b + math.sqrt(dlt))/(2*a);
        x2 = (-b - math.sqrt(dlt))/(2*a);
        return x1,x2;

a = int(input('请输入系数a：'));
b = int(input('请输入系数b：'));
c = int(input('请输入系数c：'));
print('%dx^2+%dx+%d=0的根是：%s'%(a,b,c,quadratic(a, b, c)));

#计算输入数字的
def countSquare(*nums):
    sum = 0;
    print(type(nums));
    for n in nums:
        print(n);
        sum = sum + n*n;
    return sum;

print('计算结果：%s'%(countSquare(5)));

#集合|字符串切片
mylist = [1,2,3,4,5];
print(mylist[1:3:2]);
mystr = "ABCDEFGH";
print(mystr[:6:2]);

#列表生成式
result = [x*x for x in range(1,11)]
print("列表生成式结果：")
print(result);
result = [m+n for m in ['A','B','C'] for n in ['x','y','z']];
print("列表生成式结果：")
print(result);
#查找集合中最大最小值
def findMaxAndMin(numList):
    if numList == []:
        return (None,None);
    min = max = numList[0];
    for num in numList:
        if num > max:
            max = num;
        if num < min:
            min = num;
    return (max,min);
result = findMaxAndMin([1,3,-3,6,54,6,8,2,19]);
print("最大最小值是：");
print(result);

#python内置map/reduce
def f1(x):
    return x*x;
result = map(f1,[1,2,3,4,5,6]);
print("map之后的结果：");
print(list(result));
def f3(name):
    return name[0].upper()+name[1:].lower();
result = map(f3,['admin','james','LIN']);
print("map之后的结果：");
print(list(result));

from functools import reduce;#引入reduce函数
def f2(x,y):
    return x+y;
result = reduce(f2,[1,2,3,4,5,6,7,8,9,10]);
print("reduce之后的结果：");
print(result);

#python内置filter
def f4(num):
    return num % 2 == 1;
result = filter(f4,[1,2,3,4,5,6,7,8,9,10]);#将偶数去除,关键在于函数的实现
print("filter之后的结果：");
print(list(result));

#python内置sorted
result = sorted([-2,45,24,-67,123,56,90,-456]);
print("排序后的结果：");
print(result);
#忽略大小写，反向排序
result = sorted(['Create','zoo','hadoop','spark','Admin'],key=str.lower,reverse=True);
print("排序后的结果：");
print(result);