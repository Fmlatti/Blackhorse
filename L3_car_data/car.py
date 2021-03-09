# Author: Fmlatti
# Date: 2021/3/9 19:10
# File: car.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing


def main():
    data = pd.read_csv('car_data.csv', encoding='gbk')
    eblow(data)
    kmeans_result = kmeans_method(data, 3)
    kmeans_result.to_csv = ('k_means_result.csv')
    draw(kmeans_result, 3)


def eblow(data):
    data = data.iloc[:, 1:]
    data = data_clean(data)
    sse = []
    for i in range(1, 11):
#      kmeans 算法
        k_means = KMeans(n_clusters=i)
        k_means.fit(data, i)
        sse.append(k_means.inertia_)
    x = range(1, 11)
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.savefig('elbow_method_result.png')
    # plt.show()
    return plt


def data_clean(data):
    train = data.iloc[:, :]
    # 数值化特征默认区间为0到1
    minmax_scaler = preprocessing.MinMaxScaler()
    data_min_max = minmax_scaler.fit_transform(train)
    return data_min_max

def draw(kmeans_result, n):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure()
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  # 设置小多图之间的间隙

    plt.subplot(2, 2, 1)
    for i in range(0, n):
        x = kmeans_result[kmeans_result['聚类结果'] == i]['人均GDP']
        y = kmeans_result[kmeans_result['聚类结果'] == i]['百户拥有汽车量']
        plt.scatter(x, y, alpha=0.4, label=i)
        plt.xlabel('人均GDP')
        plt.ylabel('百户拥有汽车量')

    plt.subplot(2, 2, 2)
    for i in range(0, n):
        x = kmeans_result[kmeans_result['聚类结果'] == i]['交通工具消费价格指数']
        y = kmeans_result[kmeans_result['聚类结果'] == i]['百户拥有汽车量']
        plt.scatter(x, y, alpha=0.4, label=i)
        plt.xlabel('交通工具消费价格指数')
        plt.ylabel('百户拥有汽车量')

    plt.subplot(2, 2, 3)
    for i in range(0, n):
        x = kmeans_result[kmeans_result['聚类结果'] == i]['人均GDP']
        y = kmeans_result[kmeans_result['聚类结果'] == i]['城镇人口比重']
        plt.scatter(x, y, alpha=0.4, label=i)
        plt.xlabel('人均GDP')
        plt.ylabel('城镇人口比重')

    plt.subplot(2, 2, 4)
    for i in range(0, n):
        x = kmeans_result[kmeans_result['聚类结果'] == i]['百户拥有汽车量']
        y = kmeans_result[kmeans_result['聚类结果'] == i]['城镇人口比重']
        plt.scatter(x, y, alpha=0.4, label=i)
        plt.xlabel('百户拥有汽车量')
        plt.ylabel('城镇人口比重')

    plt.legend(loc='lower right', fontsize=6, frameon=True, fancybox=True, framealpha=0.2, borderpad=0.3,
               ncol=1, markerfirst=True, markerscale=1, numpoints=1, handlelength=3.5)
    plt.savefig('Kmeans_result.png')
    plt.show()


def kmeans_method(data, n):
    data_train = data.iloc[:, 1:]
    data_train = data_clean(data_train)
    kmeans = KMeans(n)
    kmeans.fit(data_train)
    predict_y = kmeans.predict(data_train)
    # 合并聚类结果，插入到原数据中
    result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
    result.rename({0: u'聚类结果'}, axis=1, inplace=True)
    return result


if __name__ == '__main__':
    main()
