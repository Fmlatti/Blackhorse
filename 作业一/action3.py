# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:25:03 2021

@author: Fmlatti
"""

import pandas as pd
df=pd.read_csv('car_complain.csv')
print(df)
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
df
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)
result_brand=df.groupby(['brand'])['id'].agg(['count'])
result_brand
result_carmodel=df.groupby(['car_model'])['id'].agg(['count'])
result_carmodel
df2 = df.drop_duplicates(['car_model'])
result_brandmodel=df2.groupby(['brand'])['car_model'].agg(['count'])
result_brandmodel=result_brandmodel.sort_values('count',ascending=False)
result_brandmodel