class Simple_Neuron():

  def __init__(self, inputs, weights, bias):
    self.length_inputs = len(inputs)

    if self.length_inputs != len(weights):
      raise ValueError("inputs and weights must be the same length!")

    self.sum = 0
    self.inputs = inputs
    self.weights = weights
    self.bias = bias

  def output(self):
    for nr in range(self.length_inputs):
      self.sum += (self.inputs[nr] * self.weights[nr])

    return self.sum + self.bias

class Simple_Layer(Simple_Neuron):
  def __init__(self, inputs, weights, biases):
    if len(biases) != len(weights):
      raise ValueError("length of weights list must be the same as length of bias list!")

    self.inputs = inputs
    self.weights = weights
    self.biases = biases

  def output(self):
    layer_outputs = []

    for nr, wt in enumerate(self.weights):
      neuron = Simple_Neuron(self.inputs, wt, self.biases[nr])
      layer_outputs.append(neuron.output())

    return layer_outputs
