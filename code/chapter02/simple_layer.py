from neurons import Simple_Layer

inputs = [1.0, 2.0, 3.0, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
weights4 = [0.54, -0.85, 0.19, -0.35]
weights5 = [-0.25, 0.42, 0.81, -0.63]

weights = [weights1, weights2, weights3]

bias1 = 2
bias2 = 3
bias3 = 0.5
bias4 = 2.5
bias5 = 0.25

biases = [bias1, bias2, bias3]

#n1 = Simple_Neuron(inputs, weights1, bias1)
#n2 = Simple_Neuron(inputs, weights2, bias2)
#n3 = Simple_Neuron(inputs, weights3, bias3)
#n4 = Simple_Neuron(inputs, weights4, bias4)
#n5 = Simple_Neuron(inputs, weights5, bias5)

layer = Simple_Layer(inputs, weights, biases)

#outputs = [n1.output(), n2.output(), n3.output()]
outputs = layer.output()

print(outputs)
