import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

data = pd.read_csv('final_data.csv')
print(data.head(5))

#влияние вида жилья на цену
print(data['usecode'].value_counts())

single_price = data.query('usecode == "SingleFamily"')['lastsoldprice']
flat_price = data.query('usecode == "Condominium"')['lastsoldprice']
p_value = 0.05
print(ttest_ind(single_price, flat_price))
statistic, pvalue = ttest_ind(single_price, flat_price)
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

print(single_price.mean(), single_price.std(), single_price.median())
print(flat_price.mean(), flat_price.std(), flat_price.median())

#влияние площади вида жилья на цену
single_sqft = data.query('usecode == "SingleFamily"')['finishedsqft']
flat_sqft = data.query('usecode == "Condominium"')['finishedsqft']
p_value = 0.05
print(ttest_ind(single_sqft, flat_sqft))
statistic, pvalue = ttest_ind(single_sqft, flat_sqft)
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

print(single_sqft.mean(), single_sqft.std(), single_sqft.median())
print(flat_sqft.mean(), flat_sqft.std(), flat_sqft.median())

#влияние района на цену
print(data['neighborhood'].value_counts())

mission_price = data.query('neighborhood == "Mission"')['lastsoldprice']
south_price = data.query('neighborhood == "South of Market"')['lastsoldprice']
p_value = 0.05
print(ttest_ind(mission_price, south_price))
statistic, pvalue = ttest_ind(mission_price, south_price)
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')

print(mission_price.mean(), mission_price.std(), mission_price.median())
print(south_price.mean(), south_price.std(), south_price.median())

mission_price = data.query('neighborhood == "Mission"')['lastsoldprice']
south_price = data.query('neighborhood == "South of Market"')['lastsoldprice']
p_value = 0.05
print(ttest_ind(mission_price, south_price))
statistic, pvalue = ttest_ind(mission_price, south_price, equal_var=False)
print(round(pvalue, 5))
print('Нуль гипотеза верна!') if pvalue >= p_value else print('Принимаем алтернативную гипотезу!')