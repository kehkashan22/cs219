import numpy
import pandas
import matplotlib.pyplot as plt
from pandas import read_csv
import tensorflow
from tensorflow import keras
import math
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import LSTM
dataframe = read_csv('inputs_signal_strength_2.csv', usecols=[0,1], engine='python', skipfooter=3)
prev_best = -1000
threshold = 8
avg = dataframe.groupby('carrier').mean()
strongest_signal = avg.max()
if strongest_signal > prev_best:
	diff = strongest_signal - prev_best
	if diff > threshold: 
		#switch to the new signal and output that as the new carrier if the difference is high enough
	else: 
		#don't switch and output the existing signal (be stable)
else:
	#don't switch and output the existing signal

print(strongest_signal)


