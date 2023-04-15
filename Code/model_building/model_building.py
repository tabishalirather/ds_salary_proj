# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:32:17 2023

@author: tabis
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(r"C:\Users\tabis\OneDrive - Swinburne University\Semester I - 2023\Easter break_Project\ds_salary_proj\Code\jupyter_eda\cleaned_job_data2.0.csv")
print(df.columns)
#TODO: 1) Choose relevant models.
# df['is_python'] = df['is_python'].astype(int)
# df['is_excel'] = df['is_excel'].astype(int)
# df['is_apache_spark'] = df['is_apache_spark'].astype(int)
# df['is_aws'] = df['is_aws'].astype(int)
# df['is_in_same_region'] = df['is_in_same_region'] .astype(int)
# convert booleans to numeric booleans
tools = ['is_python', 'is_excel', 'is_apache_spark', 'is_aws', 'is_in_same_region']
for tool in tools:
    df[tool] = df[tool].astype(int)

df_model = df[['average_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'competitor_count', 'hourly', 'competitor_count', 
            'employer_provided' , 'job_region', 'is_in_same_region', 'company_age', 
            'is_python', 'is_apache_spark', 'is_excel', 'is_aws',
                'job_simplified', 'seniority', 'description_length']]
# df_model = df[['average_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'competitor_count', 'hourly', 'competitor_count',
#                'employer_provided', 'job_region', 'company_age','job_simplified', 'seniority',
#                'description_length', 'is_python', 'is_apache_spark', 'is_aws', 'is_excel', 'is_in_same_region']]
# get dummy data
# problem data: 'is_in_same_region, 'is_python'..... boolean values
df_dum = pd.get_dummies(df_model)
#train test split

from sklearn.model_selection import train_test_split
X = df_dum.drop('average_salary', axis = 1)
y = df_dum.average_salary.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Multiple linear regression model

import statsmodels.api as sm
X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()
# results.params
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

#Lasso regression model
lm_l = Lasso()
neg_abs_mean_error = np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha = (i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3)))
# print(error)
plt.plot(alpha,error)
err = tuple(zip(alpha,error))

df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]

#Random forest model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
cross_val_score(rf, X_train, y_train,scoring = 'neg_mean_absolute_error', cv=3)

#tune models GridSearchCV
#test ensembles 
