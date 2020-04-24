"""
英制单位英寸与公制单位厘米互换
1厘米(cm)=0.3937008英寸(in)
1英寸(in)=2.54厘米(cm)
"""
unit = input('请输入单位：')
num = float(input('请输入数值'))

if (unit == '英寸') or( unit =='inch'):
    print('%.2f英寸等于%.2f厘米'%(num,num*2.54))
else:
    print('%.2f厘米等于%.2f英寸'%(num,num/2.54))