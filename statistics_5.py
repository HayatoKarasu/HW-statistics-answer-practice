import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

data = pd.read_csv('final_data.csv')
print(data.head(5))

new_data = data[['lastsoldprice', 'zestimate']]
print(new_data)
print(new_data.describe())

p_value = 0.05
print(ttest_ind(new_data['lastsoldprice'], new_data['zestimate']))
statistic, pvalue = ttest_ind(new_data['lastsoldprice'], new_data['zestimate'])
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

statistic, pvalue = ttest_ind(new_data['lastsoldprice'], new_data['lastsoldprice'])
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

print(new_data['lastsoldprice'].shape[0])
print(np.random.normal(size=11330))

print(new_data['lastsoldprice'] + np.random.normal(size=11330))
statistic, pvalue = ttest_ind(new_data['lastsoldprice'], new_data['lastsoldprice'] + np.random.normal(10, 10, size=11330))
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

p_value = 0.05
print(mannwhitneyu(data['bathrooms'], data['bedrooms']))
statistic, pvalue = mannwhitneyu(data['bathrooms'], data['bedrooms'])
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

p_value = 0.05
print(mannwhitneyu(data['totalrooms'], data['bedrooms']))
statistic, pvalue = mannwhitneyu(data['bathrooms'], data['bedrooms'])
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

p_value = 0.05
print(ttest_ind(data[data['yearbuilt'] < 2010]['lastsoldprice'],
                data[data['yearbuilt'] >= 2010]['lastsoldprice']))
statistic, pvalue = ttest_ind(data[data['yearbuilt'] < 2010]['lastsoldprice'],
                              data[data['yearbuilt'] >= 2010]['lastsoldprice'])
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')