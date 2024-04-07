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

neurons = numpy.dot(weights, numpy.array(inputs).T) + biases

output = neurons

print(output)