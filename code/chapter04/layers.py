import numpy as np

np.random.seed(0)

X = [ [ 1 ,2 , 3, 2.5 ],
      [ 2.0, 5.0, -1.0, 2.0 ],
      [ -1.5, 2.7, 3.3, -0.8 ] ]

# Dense layer
class Dense:

    # Layer initialization
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    # Forward pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        output = np.dot(inputs, self.weights) + self.biases

        return output

layer1 = Dense(4, 5)
layer2 = Dense(5, 2)

layer1_outputs = layer1.forward(X)
layer2_outputs = layer2.forward(layer1_outputs)

print(f"Layer 1: \n{layer1_outputs}")
print()
print(f"Layer 2: \n{layer2_outputs}")
