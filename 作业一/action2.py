# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:22:36 2021

@author: Zhang huida
"""
import numpy as np
persontype=np.dtype({'names':['name','chinese','math','english'],
                     'formats':['S32','i','i','i']})
people=np.array([("zhangfei",68,65,30),("guanyu",95,76,98),("liubei",98,86,88),("dianwei",90,88,77),("xuchu",80,90,90)],dtype=persontype)
name=people['name']
chinese=people['chinese']
math=people['math']
english=people['english']
print("语文平均成绩为：",np.mean(chinese))
print("数学平均成绩为:",np.mean(math))
print("英语平均成绩为：",np.mean(english))
print("语文最小成绩为：",np.min(chinese))
print("数学最小成绩为：",np.min(math))
print("英语最小成绩为：",np.min(english))
print("语文成绩方差为：",np.std(chinese))
print("数学成绩方差为：",np.std(math))
print("英语成绩方差为：",np.std(english))
print("语文成绩标准差为：",np.var(chinese))
print("数学成绩标准差为：",np.var(math))
print("英语成绩标准差为：",np.var(english))
print(np.sort(chinese+math+english))