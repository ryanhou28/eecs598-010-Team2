import numpy as np

# A fully connected neural network

# Define a Layer class
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    # computes the output Y of a layer for a given input X
    def forward_propagation(self, input):
        raise NotImplementedError

class FCLayer(Layer):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size, weights):
        # self.weights = np.random.randint(-5, 5,size=(input_size, output_size))
        # self.bias = np.random.rand(1, output_size) - 0.5
        self.weights = weights
        self.input_size = input_size
        self.output_size = output_size

    # returns output for a given input
    def forward_propagation(self, input_data):
        self.input = input_data
        # self.output = np.dot(self.input, self.weights) + self.bias
        # self.output = np.dot(self.input, self.weights)
        # Initialize self.output
        self.output = np.zeros(self.output_size, dtype=np.int8)
        # Perform dot product in a for loop
        for i in range(len(self.output)):
            for j in range(len(self.input)):
                product = self.input[j] * self.weights[j][i]
                product = np.clip(product, -128, 127)
                self.output[i] = np.clip(self.output[i] + product, -128, 127)

        return self.output

class ActivationLayer(Layer):
    def __init__(self, activation):
        self.activation = activation

    # returns the activated input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

# Define ReLU activation function
def ReLU(x):
    return np.maximum(0, x)

# Define the actual network class
class Network:
    def __init__(self):
        self.layers = []

    # add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # predict output for given input
    def predict(self, input_data):
        # sample dimension first
        samples = len(input_data)
        result = []

        # run network over all samples
        for i in range(samples):
            # forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

if __name__ == "__main__":
    # Input data
    in_data = np.array([[-8, -5, 8, 0, 8, 7, -2, 7, 9, 7]], dtype=np.int8)

    layer1_weights = np.array([[2, -1, -2, 1, 2, -5, 0, 2, -1, -1],
                 [-4, 0, -1, -4, 4, 3, -1, -3, -3, 4],
                 [2, -2, -5, 1, -2, -2, 2, -5, 1, 3],
                 [4, 1, -4, -1, -3, -2, 0, -5, 0, 1],
                 [0, 0, -1, 4, -4, -4, -3, 0, -2, 3],
                 [-5, 4, 2, -1, -1, -2, 2, -3, -4, 1],
                 [-4, 0, -1, -2, -2, -2, -4, 2, 3, -5],
                 [-5, 2, 0, -4, 3, 4, 1, 0, -4, -3],
                 [-4, -4, -5, -1, 3, 3, -1, 0, 1, 1],
                 [2, 4, -1, -1, 2, -4, 3, -1, -3, -3]], dtype=np.int8)

    layer2_weights = np.array([[-2, 3, 1, -3, 0, -4, 1, 1, 3, -5, -2, -3, 4, -5, -1, -2, -3, 4, 2, 1],
                           [1, 3, -5, 4, -2, 1, -1, -5, -1, -3, -4, -1, 1, -1, -4, 0, -3, 0, 3, -2],
                           [-3, 2, -2, 4, -5, 4, -2, -1, -2, 3, 0, 4, -3, -4, -4, -3, -3, -4, 4, -2],
                           [-1, 2, 1, 0, 0, -5, 1, 1, 4, -5, -3, 3, 2, 3, 3, -4, 0, 4, 4, 0],
                           [3, -2, 4, 0, -2, -2, -4, -4, 3, -5, 0, -2, -5, 1, 4, 0, -2, 2, 0, 1],
                           [-4, -4, 4, -4, 3, 4, 4, -4, -2, -3, -2, -5, -5, -1, 2, 3, 0, 1, -5, -1],
                           [-5, -3, -4, 2, 4, -2, 3, -1, -1, -2, 4, 2, 4, -2, -4, 0, -1, 0, 2, 4],
                           [-4, 2, 3, 3, -5, -4, 3, 0, -2, 4, 1, 2, -4, 0, -5, 0, 3, -2, -2, 4],
                           [-3, -1, -5, -1, -3, 4, -4, -2, 1, -1, 3, -5, -1, 2, 1, -3, 4, -1, -1, 2],
                           [-3, 4, 3, -2, 2, -2, 1, -4, 1, -3, 1, -5, 2, 0, -2, -2, 2, -4, 4, -4]], dtype=np.int8)

    layer3_weights = np.array([[0, -1, 0, 1, 1, -4, 1, 1, 4, 1, 0, -4, 1, 4, 4, -4, -3, 1, 4, 3, 3, -2, 1, 1, 4, 4, 2, -5, 2, -4, 3, 1],
                 [1, -4, 2, 2, -5, -1, 2, 4, -1, 3, 1, -4, -3, 0, -1, 4, 3, 4, -4, -1, -5, 2, 2, 2, 0, 2, 1, -5, -2, 4, 0, -2],
                 [4, 4, -3, 3, 2, -2, -2, -5, 2, -4, -3, -2, 3, -3, 1, -4, -5, 3, 4, 1, 4, 2, 1, 4, -1, -4, -1, -2, -3, 2, -1, 2],
                 [-3, 3, -2, -1, -5, -1, 4, -3, 0, -1, -5, 0, -1, -1, 4, -4, -1, 0, 4, -5, -4, -5, 3, 2, -3, 0, 0, -2, 3, 0, 2, -1],
                 [-5, 3, 0, -3, -1, -5, 2, 0, 3, -3, -1, 1, 2, 3, 3, 1, 2, -3, -5, -1, 2, 2, 3, 4, -4, 4, -3, 0, -1, 1, -4, -5],
                 [-5, -3, 3, -1, -2, -4, 3, -3, 1, -5, -4, 4, 1, 3, -3, 2, -1, 1, 1, 3, 2, -4, -2, 4, 2, 4, -5, -2, 2, 4, 0, 0],
                 [3, 0, -1, -1, 4, -1, 2, 4, 1, 0, 0, -3, -1, 0, 2, 2, -5, 4, -2, 2, -1, -3, 0, 1, -1, 3, -4, -1, -5, 2, 2, -5],
                 [-5, -2, 3, -4, -4, -2, -4, -2, -3, 2, 4, 1, -2, -1, -5, 0, 4, -2, -1, -5, 4, 3, -5, -2, 4, -4, 2, -1, 3, 2, -2, 3],
                 [0, -5, 2, 0, -2, 4, -3, -4, 1, 4, 2, -2, -1, -2, 3, -3, 4, -3, 4, 2, 4, 3, -2, -2, -4, 3, 0, 1, 4, 3, -4, 4],
                 [-3, 4, 4, 3, -4, 4, 4, -1, 2, 1, 1, 3, 2, -3, 3, -1, 1, -2, -3, 3, 0, 1, 3, -3, 3, 2, -3, -4, 3, -4, 3, -5],
                 [0, -5, 2, 4, 1, 1, 1, -3, -5, 3, -5, 1, -4, -1, 0, -1, 4, 1, 2, 2, -5, 0, 3, -1, -5, -3, 3, 2, 0, -3, -1, -4],
                 [-5, 4, -3, -1, -4, 4, -3, -4, -1, -5, 2, 0, -5, -4, 0, 3, -4, 4, 2, -2, 4, 4, 4, -2, 2, 4, -1, -2, -5, 1, -1, -2],
                 [0, 3, -1, -3, 2, 0, 0, -3, -5, 4, 4, 2, 0, 1, 3, -4, 0, 0, -2, -3, 2, -2, -2, 3, -1, -5, 2, 4, -4, -5, -2, -4],
                 [-3, -4, -1, 2, -4, 0, 1, 0, 2, 3, -4, 4, 4, -5, -5, -1, -3, 1, -2, 1, 2, 3, 3, 1, 3, -1, -4, -4, -5, 3, 3, -1],
                 [-3, 2, -3, -4, -2, -4, 1, -5, 0, -1, -5, -3, -3, -3, -4, 1, 0, -2, -3, -1, 2, -4, -2, 2, 4, -1, -2, -4, 3, -2, -5, -4],
                 [3, -1, -5, 3, 1, 2, -3, -2, -3, -5, -5, 4, -2, -3, -3, 0, 1, 1, 3, 3, 1, 0, -4, -2, 4, -2, 3, -2, -4, -5, 2, -3],
                 [0, 2, 0, -5, -3, 4, 3, -1, 2, 3, 4, 0, 0, 0, 4, 4, -2, 3, 4, 1, -2, -4, -3, 1, -1, -1, -2, 1, -4, -4, -4, -4],
                 [0, -5, 2, -1, 4, 1, -5, 4, 2, 4, 0, -2, 2, -4, -3, -1, 2, 0, 0, 1, 1, -3, -2, 2, -5, -2, 1, -1, -1, -3, 0, -4],
                 [-3, -5, 2, 2, -2, 2, -3, 1, -4, 3, 3, 0, -4, 2, -3, -2, -5, -4, 4, -5, 1, -5, 2, 4, -2, -3, 3, -2, -5, -1, 0, -2],
                 [-1, 1, 3, 3, 3, 0, -1, 4, 1, 1, -4, -2, -5, 4, 4, 0, -1, 4, 0, -3, -5, -4, -1, 4, -1, 1, 0, 0, 4, -5, -1, 1]], dtype=np.int8)

    layer4_weights = np.array([[-2, -2],
                 [-2, -2],
                 [3, -4],
                 [-3, -1],
                 [0, -5],
                 [-3, -3],
                 [-3, 3],
                 [1, -4],
                 [4, 1],
                 [-5, 0],
                 [-4, -2],
                 [4, -2],
                 [-3, -4],
                 [2, -1],
                 [2, 3],
                 [-2, 4],
                 [4, -4],
                 [-4, 1],
                 [1, 3],
                 [-1, -5],
                 [-5, 3],
                 [-1, 3],
                 [2, 0],
                 [2, -2],
                 [-1, -2],
                 [0, -3],
                 [-4, -4],
                 [3, -3],
                 [3, 4],
                 [-3, -4],
                 [1, -5],
                 [1, -1]], dtype=np.int8)

    # Define the network architecture
    net = Network()
    net.add(FCLayer(10, 10, layer1_weights))
    net.add(ActivationLayer(ReLU))
    net.add(FCLayer(10, 20, layer2_weights))
    net.add(ActivationLayer(ReLU))
    net.add(FCLayer(20, 32, layer3_weights))
    net.add(ActivationLayer(ReLU))
    net.add(FCLayer(32, 2, layer4_weights))
    net.add(ActivationLayer(ReLU))

    out = net.predict(in_data)
    print(out)