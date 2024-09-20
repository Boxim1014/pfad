import pandas
from numba.np.arraymath import np_imag

dfs=pandas.read_html('https://www.td.gov.hk/mini_site/atd/2022/en/section7-2.html')
print(dfs)
# from scroping_utills import get_url, parse
from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

url="https://www.td.gov.hk/mini_site/atd/2022/en/section7-2.html"
responese = requests.get(url)

if responese.ok:
    print("Data is ready")

    # 使用 BeastifulSoup 解析 HTML
    soup = bs(responese.text, 'html.parser')
    # 找到包含数据的表格 （假设数据在第一个表格中）
    table =  soup.find('table') #根据实际情况选择合适的解释器

type(table)

table_str = str(table)

    #使用StringIO 包含字符串
table_io = StringIO(table_str)

    #使用 pandas 读取 HTML 表格
df = pd.read_html(table_io, header=1)[0]


# print(df['2019']) #df['Motor cycle']  df['Motor cycle']
# df = df.drop(index=0)

# df=df.values
df = df.rename(columns={
    'Class of vehicle': 'Vehicle Type',
    '2,245': '2012',
    '2,222': '2013',
    '2,281': '2014',
    '2,328': '2015',
    '2,355': '2016',
    '2,280': '2017',
    '2,386': '2018',
    '2,678': '2019',
    '3,003': '2020',
    '3,376': '2021'

})


# df= df[1:]
print(df.columns)
print(df.iloc[2])
plt.figure(figsize=(10, 6))

# 绘制每种车辆类型的折线图
for vehicle in df['Motor cycle']:
    plt.plot(df.columns[2:], df[df['Motor cycle'] == vehicle].iloc[0, 2:], label=vehicle)

# 添加图表标题和标签
plt.title('Vehicle Data Over Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.legend()

# 显示图表
plt.show()