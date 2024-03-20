#importing tensforflow lib
import tensorflow as tf
#importing numpy
import numpy as np
#MatPlot lib 
import matplotlib.pyplot as plt
#math lib import
import math


#Generate many Sample dataPoints
SAMPLES = 1000

# Set a "seed" value, so we get the same random numbers each time we run this
# notebook. Any number can be used here.
SEED = 1337

np.random.seed(SEED)
tf.random.set_seed(SEED)

# Generate a uniformly distributed set of random numbers in the range from
# 0 to 2π, which covers a complete sine wave oscillation
x_values = np.random.uniform(low=0, high=2*math.pi, size= SAMPLES)
print(x_values)
print(x_values.size)

# Shuffle the values to guarantee they're not in order
np.random.shuffle(x_values)

## Calculate the corresponding sine values
y_values = np.sin(x_values)

# Plot our data. The 'b.' argument tells the library to print blue dots.
plt.plot(x_values, y_values,'b.')
plt.show()

#Adding some noise 

# Add a smal random number to each y value 
y_values += 0.1*b