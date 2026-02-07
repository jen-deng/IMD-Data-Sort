#Calculating percentage of neighbourhoods in each local authority district (England) with a 10% Index of Multiple Deprivation (IMD)
import pandas as pd
#Reading the Excel file
df = pd.read_excel('IMD_2019.xlsx', sheet_name = 'IMD2019')

#Checking this works
print("Column names:")
print(df.columns)
print("\nFirst few rows:")
print(df.head())
#Isolating relevant data
df_clean = df[['Local Authority District name (2019)', 'Index of Multiple Deprivation (IMD) Rank', 'Index of Multiple Deprivation (IMD) Decile']]
#Checking headings of cleaned data
print(df_clean.head())

#Counting number of LSOAs by recurrence of Local Authority District names
##Note that LSOAs = Lower layer Super Output Areas - neighbourhood units for statistical analysis
results = df.groupby('Local Authority District name (2019)').size().reset_index(name = 'Total_LSOAs')
print(results)
#Counting number of LSOAs with an IMD Decile 1 (top 10% most deprived areas in England), grouped by Local Authority District
decile1 = df[df['Index of Multiple Deprivation (IMD) Decile'] == 1].groupby('Local Authority District name (2019)').size()
print(decile1)
#Adding this information to the results table
results['Total_In_Decile_1'] = results['Local Authority District name (2019)'].map(decile1).fillna(0)
#Checking output
print(results)

#Calculating percentage
results['Percentage_Decile_1'] = (results['Total_In_Decile_1']/results['Total_LSOAs']) * 100

#Output with additional column for percentages
print(results)

