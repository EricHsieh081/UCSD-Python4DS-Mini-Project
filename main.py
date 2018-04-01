import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('world-development-indicators/Indicators.csv')
data.head()

countries = data['CountryName'].unique().tolist()
indicators = data['IndicatorName'].unique().tolist()

condition1 = 'ARB'
condition2 = 'Life expectancy at birth, total'
mask1 = data['CountryCode'].str.contains(condition1)
mask2 = data['IndicatorName'].str.contains(condition2)

lifeExp = data[mask1 & mask2]
type(lifeExp)

condition3 = 'Hospital'
mask3 = data['IndicatorName'].str.contains(condition3)
hospitalBed = data[mask1 & mask3]
hospitalBed

table = pd.merge(lifeExp, hospitalBed, how='inner', on=['Year'])
table

ax1 = plt.plot()
plt.xlabel('Year')
plt.plot(table['Year'].values, table['Value_x'].values, 'r')
plt.ylabel('Average Age',color='r')
plt.ylim((0,75))

ax2 = plt.gca().twinx()
ax2.plot(table['Year'].values, table['Value_y'].values, 'b')
plt.ylabel('Hospital Beds',color='b')
plt.title('Correlation Between Hospital Beds and Average Age') 
plt.ylim((0,2))
plt.show()