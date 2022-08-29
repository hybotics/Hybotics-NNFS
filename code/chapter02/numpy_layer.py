import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [ [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87] ]


biases = [2.0, 3.0, 0.5]

outputs = np.dot(weights, inputs) + biases

layer_outputs = ([ np.dot(weights[0], inputs),
              np.dot(weights[1], inputs),
              np.dot(weights[2], inputs) ])

print(outputs)

print(layer_outputs)

np.dot
