"""
华氏温度转换为摄氏温度
C=(F - 32) \div 1.8

Author : Garry Gao
"""
a = float(input('请输入华氏温度：'))
c = (a-32)/1.8
print("%.2f华氏温度换算为摄氏度是%.2f度"%(a,c))