#!/usr/bin/env python3

class Activation_ReLU():
  def __init__(self, inputs):
    self.outputs = []


  def forward(self, inputs):
    for inp in inputs:
      if inp > 0:
        outputs.append(1)
      else:
        outputs.append(0)

    return outputs
