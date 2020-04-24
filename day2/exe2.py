"""
输入圆的半径计算计算周长和面积
s= pi * r * r

Author : Garry Gao
"""
import math

r = float(input('请输入圆的半径：'))
s = math.pi*r*r
l = 2*math.pi*r
print('半径%.2f的圆的面积是%.2f，周长是%.2f'%(r, s, l))