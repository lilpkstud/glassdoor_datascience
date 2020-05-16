#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:13:41 2020

@author: lilpkstud
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
#Size of company
#Parsing of job description (years of experience, pmp, etc.)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['average_salary'] = (df.min_salary+df.max_salary)/2

#Company Name Text Only - Removing the Rating
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#City Field
df['job_city'] = df['Location'].apply(lambda x: x.split(",")[0])
print(df.job_city.value_counts())

#State Field
#df['job_state'] = df['Location'].apply(lambda x: x.split(",")[1])
#df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#Parsing job description
#print(df['Job Description'][0])

test = df['Job Description'][44]
print(test)
#print(df['Job Description'][80])
#print(df['Job Description'][40])


years = test.find('years of')
print(years)


#'x years of '
#'x years in'
#

#print(years)

#Years of Expereince
df['minimum_years'] = df['Job Description'].apply(lambda x: 1 if '3 year' in x.lower() or '2 year' in x.lower()  or 'three year' in x.lower() or 'two year' in x.lower() else 0 )
df['mid_years'] = df['Job Description'].apply(lambda x: 1 if '4 year' in x.lower() or '5 year' in x.lower() or '6 year' in x.lower()  or 'four year' in x.lower() or 'five year' in x.lower() or 'six year' in x.lower() else 0)

#Notes for the future - Some df have both I.E: df.44 becuase 3 years in Project management AND 6 years in people management

#print(df.minimum_years.value_counts())
print(df.mid_years.value_counts())
#df['minimum_years'] = df['Job Description'].apply(lambda x: 1 if 'years of' in x.lower() else 0 )


#df.minimum_years.value_counts()
#PMP Certified
df['pmp'] = df['Job Description'].apply(lambda x: 1 if 'pmp' in x.lower() or 'project management certification' in x.lower() else 0)
print(df.pmp.value_counts())

df.to_csv('salary_data_cleaned.csv', index = False)