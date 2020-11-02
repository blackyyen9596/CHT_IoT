import pandas as pd
from matplotlib import pyplot as plt

csv_name = '2020-11-02.csv'
sample_data = pd.read_csv('./csv/' + csv_name)

plt.figure()
plt.plot(sample_data.date, sample_data.Dissolved_oxygen, 'o-', color = 'dodgerblue', label='Training loss') #將a、b所繪製的圖表更改顯示方式
plt.title('')
plt.xticks(sample_data.date, rotation='vertical') # 設定x軸label以及垂直顯示
plt.legend() #標示ab、ac的圖示
plt.savefig('./plot/test.jpg')
plt.show() #執行