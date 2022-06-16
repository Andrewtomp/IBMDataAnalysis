# Code uses the House Sales in King County, USA from May 2014 to May 2015 used for IBM Course

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
%matplotlib inline

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df=pd.read_csv(file_name)

# Question 1: Display the data types of each column using the function dtypes, then take a screenshot and submit it, include your code in the image.
df.dtypes
df.describe()

# Question 2: Drop the columns "id" and "Unnamed: 0" from axis 1 using the method drop(), then use the method describe() to obtain a statistical summary of the data

df.drop(["id", "Unnamed: 0"], axis = 1, inplace = True)
df.describe()

#  replace the missing values of 'bedrooms', 'bathrooms' with the means using the method replace()
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

# Question 3: Use the method value_counts to count the number of houses with unique floor values, use the method .to_frame() to convert it to a dataframe.

housePlans = df.value_counts()
housePlans.to_frame()

# Question 4: Use the function boxplot in the seaborn library to determine whether houses with a waterfront view or without a waterfront view have more price outliers.

sns.boxplot(df['waterfront'], df['price'])
plt.title("'Boxplot 'Waterfront' vs 'Price'")

# Question 5: Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price.

sns.regplot(x="sqft_above", y="price", data=df)
# We can use the Pandas method corr() to find the feature other than price that is most correlated with price.
df.corr()['price'].sort_values()

# We can Fit a linear regression model using the longitude feature 'long' and caculate the R^2.

X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

# Question 6: Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2

sqvp = LinearRegression()
sqvp.fit(df[['sqft_living']], df[['price']])
sqvp.score(df[['sqft_living']], df[['price']])


# Question 6: Fit a linear regression model to predict the 'price' using the list of features:
features = ["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     

p = LinearRegression()
px = df[features]
py = df['price']
p.fit(px, py)
p.score(px, py)

# Creates a list of tuples for Question 8
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]

#Question 8: Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2.

pipe = Pipeline(Input)
pipe.fit(px,py)
pipe.score(px,py)

# Setup for Questions 9, 10
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

# Question 9: Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data.
from sklearn.linear_model import Ridge

rm = Ridge(alpha = 0.1)
rm.fit(x_train, y_train)
rm.score(x_test, y_test)

# Question 10: Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided.

pr = PolynomialFeatures(degree = 2)
x_train_pr = pr.fit_transform(x_train[features])
x_test_pr = pr.fit_transform(x_test[features])

rm = Ridge(alpha = 0.1)
rm.fit(x_train_pr, y_train)
rm.score(x_test_pr, y_test)
