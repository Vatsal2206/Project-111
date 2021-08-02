# Importing modules

import random
import plotly.figure_factory as pff
import statistics as stc
import pandas as pd

#  Reading csv file

df = pd.read_csv('StudentsPerformance.csv')
data = df['writing score'].tolist()

# Mean of population data

mean_population = stc.mean(data)

# Getting sampled data

sampled_data_list = []
for i in range(0,30):
    index = random.randint(0, len(data))
    random_data = data[index]
    sampled_data_list.append(random_data)

# Getting mean of sampled data

mean_sampled_data = stc.mean(sampled_data_list)
print('Mean of sampling distribution : ',mean_sampled_data)

# Getting standard deviation of sampled data

stdev_sampled_data = stc.stdev(sampled_data_list)
print('Standard Deviation of sampling distribution : ',stdev_sampled_data)

# Getting Z score

zscore_sampled_data = (mean_sampled_data - mean_population)/stdev_sampled_data
print('The Z score is : ',zscore_sampled_data)