'''
The following code is a simple example of forward propagation
The neural network contains:
1 Input layer(2nodes), 1 Hidden Layer(2 nodes) and 1 Output Layer

'''

import numpy as np


input_data = np.array([2,3])

weights = {'node_0': np.array([1,1]),
           'node_1': np.array([-1,1]),
           'output': np.array([2,-1])}

node_0_value = (input_data * weights['node_0']).sum()
node_1_value = (input_data * weights['node_1']).sum()

hidden_layer_values = np.array([node_0_value, node_1_value])

print('The values of the hidden layers are : ')
print(hidden_layer_values)

output_layer_value = (hidden_layer_values * weights['output']).sum()

print('The value of the output layer is : ')
print(output_layer_value)
