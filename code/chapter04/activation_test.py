#!/usr/bin/env python3
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

# A parameter of 0 will insure the data is repeatable for testing purposes
nnfs.init(0)

from activations import ReLU
from layers import Dense

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

# Create dataset
X, y = spiral_data(samples=100, classes=3)

# Create Dense layer with 2 input features and 3 output values
dense1 = Dense(2, 3)

activation1 = ReLU()

# Perform a forward pass of our training data through this layer
layer_output = dense1.forward(X)

# Let's see output of the first few samples:
print()
print(f"<layer forward output = {layer_output[:10]}")

act_output = activation1.forward(layer_output)

print()
print(f"activation forward output = {act_output[:10]}")
