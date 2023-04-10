# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:18:13 2023

@author: tabis
"""

import pandas as pd
import csv

df = pd.read_csv(r"C:\Users\tabis\OneDrive - Swinburne University\Semester I - 2023\Easter break_Project\ds_salary_proj\Resources\glassdoor_jobs.csv")
#salary_parsing
#company_name
#state field
#company age
#parsing job description, keywords, Python etc.


df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_knd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

min_hrly = minus_knd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))\
    
df['min_salary'] = min_hrly.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hrly.apply(lambda x: int(x.split('-')[1]))
df['average_salary'] = ((df['min_salary'])+(df['max_salary']))/2

#company name
df['company_txt_name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#company region(state/country)
df['job_region'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_region.value_counts()

#headquartersState
# df['hq_state'] = df['Headquarters'].apply(lambda x: x.split(',')[1])
df['hq_region'] = df['Headquarters'].apply(lambda x: x.split(',')[1] if len(x.split(',')) > 1 else None)


#Job at headquarters?
df['is_at_headquarters'] = df['Headquarters'] == df['Location']

#job at same region as hq
df['is_in_same_region'] = df['job_region'] == df['hq_region']

#company age.
df["company_age"] = df['Founded'].apply(lambda x: x if x < 0 else 2023 - int(x))

#parse job descrips: look for python, R studio, spark, aws, excel
# df['is_python'] = df['Job Description'].apply(lambda x: True if 'python' in x.lower() else False)
# df.is_python.value_counts()

# df['is_R'] = df['Job Description'].apply(lambda x: True if 'R studio' in x.lower() else False)
# df.is_R.value_counts()

# df['is_excel'] = df['Job Description'].apply(lambda x: True if 'excel' in x.lower() else False)
# df.is_excel.value_counts()

# df['is_spark'] = df['Job Description'].apply(lambda x: True if 'spark' in x.lower() else False)
# df.is_spark.value_counts()
tools = ['r studio', 'r-studio' , 'excel', 'apache spark', 'python','knime', 'powerbi', 'd3', 'kaggle', 'MATLAB', 'tensorflow', 'pandas', 'Tableau', 'aws']

for tool in tools:
    col_name = 'is_' + tool.replace(' ', '_')
    df[col_name] = df['Job Description'].apply(lambda x: True if tool.lower() in x.lower() else False)
    # print(df[col_name].value_counts(normalize = True))
    count_true = df[col_name].value_counts()[True]
    count_false = df[col_name].value_counts()[False]
    # print(count_true)
    # print(count_false)
    if((count_true*8) > count_false):
        print(tool + " is important")
    else: 
        print(tool + " is not important")
# df['Job Description'][0]
df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv("cleaned_job_data.csv", index = False)

clean_data = pd.read_csv('cleaned_job_data.csv')
