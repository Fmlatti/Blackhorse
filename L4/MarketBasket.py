# Author: Fmlatti
# Date: 2021/3/10 19:28
# File: MarketBasket.py

import pandas as pd
from efficient_apriori import apriori

def main():
    data = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
    # data.to_excel('Market_basket.xlsx')
    # print(data.shape)
    efficient_mode(data)


def data_clean(data):
 # 清除数据中的nan值
    transaction = []
    t = []
    for i in range(0, data.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(data.values[i, j]) != 'nan':
                temp.append(str(data.values[i, j]))
        transaction.append(temp)
    # t = pd.DataFrame(transaction)
    # t.to_excel('new.xlsx')
    return transaction


def efficient_mode(data):
    transactions = data_clean(data)
    item, rules = apriori(transactions, min_support=0.04, min_confidence=0.4)
    print('频繁项集：', item)
    print('关联规则：', rules)


if __name__ == '__main__':
    main()