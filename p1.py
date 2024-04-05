inputs = [1.7, 2.3, 10.7]

weights1 = [4, 2, -6.3]
weights2 = [-4.3, 2.4, 3]
weights3 = [6.3, 3.4, -6.3]

bias1 = 1
bias2 = 2
bias3 = 3

neuron1 = inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias1
neuron2 = inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias2
neuron3 = inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + bias3

output = [neuron1, neuron2, neuron3]

print(output)