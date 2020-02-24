# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:11:07 2020

@author: Kudzie Dennis Mhembe
"""

import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
from matplotlib import style
style.use('ggplot')

df_car = pd.read_csv('mtcars2.csv')
#creating plots
def scatter_graph():     
     df_car.plot(x='hp',y='cyl',style='o')
     plt.title('Scatter')
     plt.xlabel('x-axis(hp)')
     plt.ylabel('y-axis(cyl)')
     plt.show()

#preparing data
def prep_data():
     x = pd.DataFrame(df_car['hp'])
     y = pd.DataFrame(df_car['cyl'])
     return (x.size,y.size)

def fig_create():
     fig = plt.figure()
     #adding subplots
     #to create space for more than one graph
     ax1 = fig.add_subplot(2,2,1)
     ax2 = fig.add_subplot(2,2,2)
     ax3 = fig.add_subplot(2,2,3)
     #creating an empty figure

#scattered graph
def scatter2():
     #plot random data
     plt.plot(randn(50).cumsum(), 'k--')

#histogram 
def histogram():
     _ = ax1.hist(randn(100),bins=20,color='r',alpha=0.7)
#histogram()

def create_fig():
#     creating and empty figure
     fig, axes = plt.subplots(2,2)
     print(axes)

#create_fig()
def _plot():
     x = [1,2,3,4,5]
     y = [5,6,7,8,9]
     x1 = [11,12,13,14,5]
     y1 = [15,16,17,18,9]
     plt.plot(x,y,'g',label='Line one',linewidth=5)
     plt.plot(x1,y1,'r',label='Line oe',linewidth=5)
     plt.title('Sketch')
     plt.xlabel('X-axis')
     plt.ylabel('Y-axis')
     
     plt.grid(True, color='k')
     plt.legend()
  
     plt.show()



def bar_graph():
     x = [1,2,3,4,5]
     y = [7,6,5,4,3]
     x1 = [1.5,2.5,3.5,4.5,5.5]
     y2 = [7.5,6.5,5.5,4.5,3.5]
     plt.bar(x,y,color='c',label='bar1')
     plt.bar(x1,y2,color='g',label='bar2')
     plt.title('Bars')
     plt.xlabel('bar foot')
     plt.ylabel('bar height')
     plt.legend()
     plt.show()
     
def histogram():
     pop_ages = [22,55,67,89,78,36,26,41,25,90,111,75,90,1,92,83,112,11]
     bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
     plt.hist(pop_ages,bins,histtype='bar',rwidth=0.8)
     
     plt.xlabel('age-range')
     plt.ylabel('occurance')
     plt.title('Histogram')
     plt.legend()
     
     plt.show()
     
def pie_chart():
     slices = [7,2,2,13]
     activities = ['sleeping','eating','working','playing']
     cols = ['c','r','m','b']
     
     plt.pie(slices, labels=activities,colors=cols,
             startangle=90,shadow=True,explode=(0,0.1,0,0),
             autopct='%1.1f%%')
     plt.title('Pie Plot')
     plt.show()
     
pie_chart()



