# Importing tensorflow

import tensorflow as tf

# Importing some more libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

# reading the ratings data

ratings = pd.read_csv('ml-1m/ratings.dat',\
          sep="::", header = None, engine='python')

# Lets pivot the data to get it at a user level

ratings_pivot = pd.pivot_table(ratings[[0,1,2]],\
          values=2, index=0, columns=1 ).fillna(0)

# creating train and test sets

X_train, X_test = train_test_split(ratings_pivot, train_size=0.8)

n_nodes_inpl = 3706  
n_nodes_hl1  = 256  
n_nodes_outl = 3706  

# first hidden layer has 784*32 weights and 32 biases

hidden_1_layer_vals = {'weights':tf.Variable(tf.random_normal\([n_nodes_inpl+1,n_nodes_hl1]))}

# first hidden layer has 784*32 weights and 32 biases

output_layer_vals = {'weights':tf.Variable(tf.random_normal\([n_nodes_hl1+1,n_nodes_outl])) }