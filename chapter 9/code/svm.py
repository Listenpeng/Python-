#encoding = uft-8

import pandas as pd
#引入随机函数
from numpy.random import shuffle
from sklearn import svm
import pickle
from sklearn import metrics

#加载数据文件
inputfile = '../data/moment.csv'
#读取数据，指定编码为gbk
data = pd.read_csv(inputfile, encoding='gbk')
data = data.as_matrix()

#随机打乱数据
shuffle(data)
data_train = data[: int(0.8*len(data)), :]
data_test = data[int(0.8*len(data)) : ,:]

#构造特征和标签，为什么有x,y_train之分
#X_train提取的是各阶颜色矩的值，
#y_train提取的时专家的水质评价
#使用DataFrame的切片提取，行在前列在后，
x_train = data_train[:, 2:] *30 #放大特征值
y_train = data_train[:, 0].astype(int) #类型转换
x_test = data_test[:, 2:] #放大特征值
y_test = data_test[:,0].astype(int)

model = svm.SVC()
model.fit(x_train, y_train)

#保存模型
pickle.dump(model, open('../tmp/svm.model','wb'))
#可以通过下面语句重新加载模型
#model = pickle.load(open('../tmp/svm.model','rb') 

#导入相关的库生成混淆矩阵
#训练样本的混淆矩阵
cm_train =s metrics.confusion_matrix(y_train, model.predict(x_train)) 
#测试样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test, model.predict(x_test))

print(cm_train)
print('score:',model.score(x_train,y_train))
print(cm_test)
print('score:',model.score(x_test,y_test))


#保存结果
pd.DataFrame(cm_train,index=range(1,6),columns=range(1,6)).to_excel('cm_train.xls')
pd.DataFrame(cm_test, index=range(1,6), columns=range(1,6)).to_excel('cm_test.xls')

