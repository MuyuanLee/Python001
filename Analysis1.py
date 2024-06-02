#导入Excel文件
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
#导入数据
data = pd.read_excel('D:/2020-07.xlsx')
#对于有若干中分类的数据，当两个分类相同的时候，求和
data = data.groupby(['销售日期','单品编码']).sum()
#创建另一个Excel文件，并将计算后的数据写回到这个Excel文件
# data.to_excel('D:/2020-07-1.xlsx')
