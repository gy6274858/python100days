"""
输入三条边长，如果能构成三角形就计算周长和面积

"""
import math

a = float(input('请输入第一条边长: '))
b = float(input('请输入第二条边长: '))
c = float(input('请输入第三条边长: '))

if (a + b > c) & (a + c > b) & (b + c > a):
    l = a + b + c
    p = l / 2
    s = math.sqrt((p * (p - a)*(p - b)*(p - c)))
    print('该三角形的面积是%.2f，周长是%.2f' % (s, l))
else:
    print('这三条边不能构成三角形')
