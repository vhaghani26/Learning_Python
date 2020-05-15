#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

from math import sqrt
import fileinput

# Creating an array with the data file
data = []
total = 0
count = 0
for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip()
    total += float(line)
    data.append(float(line))

# Calculating count and mean
count = int(len(data))    
mean = total/len(data)

# Calculating standard deviation
stddev = 0
for i in range(0, len(data)):
    stddev += (data[i] - mean) * (data[i] - mean)
stddev = sqrt(stddev/(count))

data.sort() # Sorts data to allow for calculations of min, max, and median 

# Calculating min and max
min = data[0]
max = data[-1]

# Calculating the median
# "If" is for even number, "else" is for odd number
if count % 2 == 0:
    median1 = data[int(count/2)-1] #have to use -1 because the count counts 0 as the first number so everything will be off by 1 without the -1
    median2 = data[int(count/2)]
    median = (median1 + median2)/2
else:
    median = data[int(count/2)]
    
# Print the information calculated above
print(f'Count: {count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {mean}')
print('Standard Deviation: ''%.3f' % (stddev))
print(f'Median: {median}')

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
