import pandas as pd

df = pd.read_excel('IMD_2019.xlsx', sheet_name = 'IMD2019')

print("Column names:")
print(df.columns)
print("\nFirst few rows:")
print(df.head())

df_clean = df[['Local Authority District name (2019)', 'Index of Multiple Deprivation (IMD) Rank', 'Index of Multiple Deprivation (IMD) Decile']]

print(df_clean.head())

results = df.groupby('Local Authority District name (2019)').size().reset_index(name = 'Total_LSOAs')
print(results)

decile1 = df[df['Index of Multiple Deprivation (IMD) Decile'] == 1].groupby('Local Authority District name (2019)').size()
print(decile1)

results['Total_In_Decile_1'] = results['Local Authority District name (2019)'].map(decile1).fillna(0)

print(results)

results['Percentage_Decile_1'] = (results['Total_In_Decile_1']/results['Total_LSOAs']) * 100
print(results)

