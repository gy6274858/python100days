"""
百分制成绩转换为等级制成绩
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E
"""
cent = float(input("请输入百分制成绩："))
if cent>=90:
    grade = 'A'
elif cent>=80:
    grade = 'B'
elif cent>=70:
    grade = 'C'
elif cent>=60:
    grade = 'D'
else:
    grade = 'E'

print('%.1f的百分制成绩对应的绩点是%s'%(cent, grade))