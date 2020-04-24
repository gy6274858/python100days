"""
输入年份判断是不是闰年
能被400整除
能被4整除不能被100整除
Author: Garry Gao
"""
year = int(input('请输入年份：'))

if year%400 ==0:
    print('%d是闰年'%year)
elif (year %4 ==0) & (year %100 !=0):
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)