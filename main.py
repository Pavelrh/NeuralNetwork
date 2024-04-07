import numpy 

inputs = [[1.7, 2.3, 10.7],
          [2.7, 4.3, 0.7],
          [3.7, 6.3, -10.7]]

weights =  [[4, 2, -6.3],
            [-4.3, 2.4, 3],
            [6.3, 3.4, -6.3]]

biases = [1,
          2,
          3]

weights2 =  [[3, 1, -5.3],
            [-3.3, 1.4, 2],
            [5.3, 1.4, -5.3]]

biases2 = [4,
          5,
          6]

layer1_output = numpy.dot(inputs, numpy.array(weights).T) + biases

layer2_output = numpy.dot(layer1_output, numpy.array(weights2).T) + biases2



print(layer1_output)
print(layer2_output)