import numpy as np

### Define a Perceptron Class
class Perceptron:
    ### Defining the constructor (Called when an object is created)
    def __init__(self, learning_rate=0.01, epoch=1000, threshold=0.001, prediction='classification'):
        self.lr = learning_rate
        self.n_epoch = epoch
        if prediction == 'classification':
            self.activation_func = self.sigmoid
            self.activation_func_derv = self.sigmoid_derv
        else:
            self.activation_func = self.linear
            self.activation_func_derv = self.linear_derv
        self.weights = None
        self.threshold = threshold
        self.avg_error = []
        
    ### Function for training the data
    def train(self, X, y, epoch=True):
        ### Get the number of data records and dimention of the data
        n_samples, n_features = X.shape
        ### Create the input data by appending the 1 in each record (used for the bias) 
        inputs = np.hstack((X, np.ones((n_samples, 1))))
        ### Initialize the weights (there is one extra weights used as bias)
        np.random.seed(100)
        self.weights = np.random.rand(n_features+1,1)
        ### Create 2-D output array from a list or 1-D output array
        y = y.reshape((n_samples,1))
        ### This conditional block of code is for fixed number of epoch
        if epoch == True:
            ### Loop for each epoch
            noOfNoChangeError = 0
            for _ in range(self.n_epoch):
                ### Randomize the input data
#                 rand_index = np.random.permutation(len(inputs))
#                 inputs = inputs[rand_index]
#                 y = y[rand_index]
                a_n = np.dot(inputs, self.weights)
                ### Apply the activation function
                s_n = self.activation_func(a_n)
                # weight update rule (backpropagation)
                error_diff = (y - s_n)
                df_a_n = self.activation_func_derv(a_n, b=1)
                delta = error_diff * df_a_n
                delta_weight = self.lr * np.dot(inputs.T, delta)
                self.weights += delta_weight
                self.avg_error.append((np.sum(error_diff*error_diff))/(4*n_samples))
                if noOfNoChangeError >=20:
                    break
                else:
                    if len(self.avg_error) >= 4:
                        if self.avg_error[-1] == self.avg_error[-2] and self.avg_error[-2] == self.avg_error[-3]:
                            noOfNoChangeError += 1
        ### This conditional block of code is for fixed threshold of average error
        else:
            error = 10000000
            noOfNoChangeError = 0
            self.n_epoch = 0
            while error > self.threshold:
                ### Randomize the input data
#                 np.random.shuffle(inputs)
                a_n = np.dot(inputs, self.weights)
                ### Apply the activation function
                s_n = self.activation_func(a_n)
                # weight update rule (backpropagation)
                error_diff = (y - s_n)
                df_a_n = self.activation_func_derv(a_n, b=1)
                delta = error_diff * df_a_n
                delta_weight = self.lr * np.dot(inputs.T, delta)
                self.weights += delta_weight
                self.avg_error.append((np.sum(error_diff*error_diff))/(4*n_samples))
                self.n_epoch += 1
                if noOfNoChangeError >=20:
                    break
                else:
                    if len(self.avg_error) >= 4:
                        if error == self.avg_error[-1] and error == self.avg_error[-2]:
                            noOfNoChangeError += 1
                error = self.avg_error[-1]
    
    ### Function for prediction of an input array (2-D)
    def predict(self, X):
        n_samples, n_features = X.shape
        X = np.hstack((X, np.ones((n_samples, 1))))
        a_n = np.dot(X, self.weights)
        y_predicted = self.activation_func(a_n)
        return np.around(y_predicted)
    
    def predictR(self, X):
        n_samples, n_features = X.shape
        X = np.hstack((X, np.ones((n_samples, 1))))
        a_n = np.dot(X, self.weights)
        y_predicted = self.activation_func(a_n)
#         print(y_predicted)
        return y_predicted
    ### Defining the sigmoid function
    def sigmoid(self, x, b=1):
        return 1.0/(1.0+np.exp(-(b*x)))
    ### Defining the sigmoid derivative function
    def sigmoid_derv(self, x, b=1):
        return b*self.sigmoid(x, b)*(1-self.sigmoid(x, b))

    ### Defining the linear function
    def linear(self, x, b=1):
        return b*x
    ### Defining the linear derivative function
    def linear_derv(self, x, b=1):
        return b