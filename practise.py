# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:59:54 2020

@author: Kudzie Dennis Mhembe
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('seaborn')


def heart_graph():
     ht_df = pd.read_csv('heart1.csv')
     ht_df = ht_df[['70','130','322']]
     df = ht_df.copy()
     df = pd.DataFrame(df)
#     df.columns = df[['B/sec','BP','Bp/m']]
     
     print(df)
     plt.subplot(211)
     df.plot(x='70',y='130',style='o')
     plt.xlabel('Beats/sec')
     plt.ylabel('Bp')
     plt.title('try-out')
#     plt.show()
     print(df[['70','130']].corr())
     
#heart_graph()

def cars_graph():
     cars_df = pd.read_csv('mtcars2.csv')
     cars_df = pd.DataFrame(cars_df)
     print(cars_df.head())
     speeds = cars_df[['model','disp']]
     x= speeds['model']
     y = speeds['disp']
     fig, axes = plt.subplots(1,1)
     
     plt.bar(x,y,color='c',label='Max Speed', animated=True)
#     yticks,xticks enables label manipulation
     plt.xticks(x, rotation='vertical')
#     creating the graph
     plt.xlabel('Car Model', fontsize=15, color='red')
     plt.ylabel('Top speed')
     plt.title('Speeds Graph')
     plt.legend()
     plt.show
#     show a list of all styles available
     print(plt.style.available)
     
cars_graph()