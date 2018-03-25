#encoding= utf-8
#K-Means聚类算法
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法

inputfile = '../tmp/zscoreddata.xls' 
k = 5
#读取数据并进行聚类分析
data = pd.read_excel(inputfile)
#调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters=k, n_jobs=2) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型
b = kmodel.cluster_centers_ #查看聚类中心
c  =kmodel.labels_ #查看个样本对应的类别

print(b)
print(c)

