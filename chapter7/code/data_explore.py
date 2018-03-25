#encoding = utf-8
#对数据进行基本的探索
#返回缺失值个数以及最大最小值

import pandas as pd
datafile = '../data/air_data.csv'
resultfile = '../tmp/explore.xls'

data = pd.read_csv(datafile, encoding='utf-8')
#包括对数据的基本描述,describe()函数可以做基本的统计
explore = data.describe(percentiles=[], include='all').T 
#percentiles参数时指定计算多少的分位数表(如1/4分位数、中位数)，T是转置
#describe()函数自动计算非空值数，需要手动计算空值数
'''
describe()函数自动计算的字段由count(非空值)、unique(唯一值)、top(频数最高者)、freq(最高频者)、mean(平均值)、std(标准差)、50%(中位数)、max(最大值)
'''
explore['null'] = len(data) - explore['count'] 
explore = explore[['null', 'max', 'min']]
explore.columns = [u'null', u'max',u'min'] #表头重命名
explore.to_excel(resultfile)
