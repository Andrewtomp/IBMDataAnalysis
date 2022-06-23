# Using a dataframe from a csv answer the prompts listed in the comments IBM Capstone Week 3

import pandas as pd

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")

# Plot the distribution curve for the column ConvertedComp.
df['ConvertedComp'].plot.density()

# Plot the histogram for the column ConvertedComp.
df['ConvertedComp'].plot.hist()

# What is the median of the column ConvertedComp?
df['ConvertedComp'].median()

# How many responders identified themselves only as a Man?
df['Gender'].value_counts()

#Find out the median ConvertedComp of responders identified themselves only as a Woman?
w=df[df['Gender'] == 'Woman']
w["ConvertedComp"].median()

# Give the five number summary for the column Age?
df['Age'].describe()

# Plot a histogram of the column Age.
df['Age'].plot.hist()

# Find out if outliers exist in the column ConvertedComp using a box plot?
df['ConvertedComp'].plot.box()

# Find out the Inter Quartile Range for the column ConvertedComp.
q3 = df['ConvertedComp'].quantile(0.75)
q1 = df['ConvertedComp'].quantile(0.25)
iqr = q3 - q1
print(iqr)

# Find out the upper and lower bounds.
upper = (q3 + iqr*1.5)
lower = (q1 - iqr*1.5)
print(upper, lower)

# Identify how many outliers are there in the `ConvertedComp` column.
outliers = df[(df['ConvertedComp'] < lower) | (df['ConvertedComp'] > upper)]
len(outliers['ConvertedComp'])

# Create a new dataframe by removing the outliers from the ConvertedComp colum
df2 = df[~df.isin(outliers)]
df2.describe()

#Find the correlation between Age and all other numerical columns.
df.corr()
