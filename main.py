import numpy 

numpy.random.seed(0)

X = [[1.7, 2.3, 10.7],
          [2.7, 4.3, 0.7],
          [3.7, 6.3, -10.7]]

class layer:
    def __init__(self, n_inputs, n_neurons):
         # its gotta be this way cus for matrix multiplication the no of rows in matrix 1 should be equal to no of columns in matrx 2
         self.weights = numpy.random.randn(n_inputs, n_neurons)
         self.biases = numpy.zeros((1, n_neurons))
    def forward(self, inputs):
         self.output = numpy.dot(inputs, self.weights) + self.biases
    
layer1 = layer(3, 6)
layer2 = layer(6, 2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)