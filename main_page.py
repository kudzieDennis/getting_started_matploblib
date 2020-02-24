# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:29:03 2020

@author: Kudzie Dennis Mhembe
"""
import pandas as pd
cars = pd.read_csv('mtcars2.csv')

def get_info():
     return cars.info(null_counts=True)

def get_shape():
     return cars.shape

def get_mean():
     return cars.mean()

def get_median():
     return cars.median()

def get_std():
     return cars.std()

def get_describe():
     #shows most of the statistics needed mostly
     return cars.describe()

# renaming columns cars.rename(columns={old_name:new_name})
def fix_null_values():
     cars.qsec = cars.qsec.fillna(cars.qsec.mean())
     return cars

def drop_columns():
     return cars.drop(columns=['name'])

def get_correlation():
     return cars[['mpg','cyl','vs','gear','carb','qsec']].corr()
#print(get_info())

def change_dt_type():
     cars.mpg = cars.mpg.astype(float)
     return cars


#           using iloc function
# iloc[row,column]     
# iloc[:,:] all rows and all columns
#print(cars.iloc[3:10,4])
     
#           using loc function
# loc[row,column_name]
# print(cars.loc[:,'mpg'])

cars['numbers']= 2

def times_two():
     f = lambda x: x*2
     cars['numbers']=cars['numbers'].apply(f)
     return cars

def sort_by_value():
     return cars.sort_values(by='cyl',ascending=False)

#print(sort_by_value())
     
def filtering():
     more_than_6 = cars['cyl']>6
     df = cars[more_than_6]
     return df
#
#print(filtering())
data = pd.read_csv('heart1.csv')
#print(data.head())

data_line = cars.loc[:,['hp','cyl']]






     