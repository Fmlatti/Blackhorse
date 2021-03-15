# Author: Fmlatti
# Date: 2021/3/15 18:56
# File: MarketBasket.py
import pandas as pd
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

data = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
# print(data.shape)
transactions = []
item_count = {}
for i in range(0, data.shape[0]):
    temp = []
    for j in range(0, 20):
        item = str(data.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
# print(transactions)


# 去掉停用词，即常常使用的但是对数据无用的词汇（虚词、你好等）
def remove_stop_word(f):
    stop_words = []
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


def create_word_cloud(f):
    f = remove_stop_word(f)
    cut_text = word_tokenize(f)
    cut_text = " ".join(cut_text)
    wc = WordCloud(max_words=100, width=2000, height=1200,)
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("wordcloud.jpg")


all_word = ' '.join('%s' % item for item in transactions)
create_word_cloud(all_word)

print(sorted(item_count.items(), key=lambda x:x[1], reverse=True)[:10])