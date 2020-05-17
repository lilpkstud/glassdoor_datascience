#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:32:30 2020

@author: lilpkstud
"""

import pandas as pd

df = pd.read_csv('sharon_socialMedia.csv')

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

test = df['Job Description'][12]
test1 = df['Job Description'][41]
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
df['entry_level'] = df['Job Description'].apply(lambda x: 1 if '3 year' in x.lower() or '2 year' in x.lower()  or 'three year' in x.lower() or 'two year' in x.lower() else 0 )
df['mid_level'] = df['Job Description'].apply(lambda x: 1 if '4 year' in x.lower() or '5 year' in x.lower() or '6 year' in x.lower()  or 'four year' in x.lower() or 'five year' in x.lower() or 'six year' in x.lower() else 0)
df['sentio_level'] = df['Job Description'].apply(lambda x: 1 if '7 year' in x.lower() or '8 year' in x.lower() or '9 year' in x.lower() or 'seven year' in x.lower() or 'eight year' in x.lower() or 'nine year' in x.lower() else 0)
#Notes for the future - Some df have both I.E: df.44 becuase 3 years in Project management AND 6 years in people management


df['social_media'] = df['Job Description'].apply(lambda x: 1 if 'social media market' in x.lower() else 0)
df['hootsuite'] = df['Job Description'].apply(lambda x: 1 if 'hootsuite' in x.lower() else 0)
df['email_marketing'] = df['Job Description'].apply(lambda x: 1 if 'email market' in x.lower() else 0)
df['mailchimp'] = df['Job Description'].apply(lambda x: 1 if 'mailchimp' in x.lower() else 0)
print(df.email_marketing.value_counts())

df.to_csv('sharon_salary_data_cleaned.csv', index = False)