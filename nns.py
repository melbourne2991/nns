import numpy

inputs = (
  (0, 1),
  (1, 0),
  (1, 0),
  (1, 0),
  (0, 0),
  (1, 1),
  (0, 1),
  (0, 0)
)

weights = []

for i, input in enumerate(inputs):
  weights.append(abs(numpy.random.normal(0.5, 0.25)))
  print input[0], input[1], weights[i]

