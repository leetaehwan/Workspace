import numpy as np
import pandas as pd

data = pd.Series([1,2,3,4], dtype = "float", index=['a','b','c','d'])
print(data)

print(data['c'])
print(type(data))

print(data.values)

print(type(data.values))

print(data.dtype)


population_dict = dict(zip(['china','japan','korea','usa'],[1415000,12718,5180,32676]))
population = pd.Series(population_dict)

print(population)

data = {
  'country' : ['china','japan','korea','usa'],
  'gdp' : [1409250000, 516700000, 169320000, 2041280000],
  'population': [141500, 12717, 5180, 32676]
}

country = pd.DataFrame(data)
print(country)
print(country.shape)
country = country.set_index('country')
print(country)


print(country.shape)

# country.to_csv("./country.csv")
# country.to_excel("country.xlsx")


# Selecting Data
print(country.loc['china'])
print(country.loc['japan':'korea', :'population'])

# Indexing Data

print(country.iloc[0])
print(country.iloc[1:3,:2])

# Extracting sereis or dataframe
print(country['gdp'])
print(country[['gdp']])

# Selecting Data with conditon expression

print(country[country['population'] < 10000])
print(country.query("population > 100000"))

# Calculating GPC from the data and adding it into dataframe

gdp_per_capita = country['gdp'] / country['population']
country['gdp per capita'] = gdp_per_capita

print(country)

df = pd.DataFrame(columns = ['이름', '나이','주소'])
df.loc[0] = ['길동', '26','서울']
print(df)
df.loc[1] = {'이름':'철수','나이':'25', '주소':'인천'}
print(df)
df.loc[1, '이름'] = '영희'
print(df)

df['전화번호'] = np.nan
df.loc[0, '전화번호'] = '01012341234'
print(df)

df.drop('전화번호',axis = 1, inplace= True)
print(df)