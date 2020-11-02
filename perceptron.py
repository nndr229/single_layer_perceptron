
import random
class Perceptron:
    weights=[]
    lr =0.01
    def __init__(self,n):
        # self.weights = []
        # lr = 0.01
        for i in range(n):
            Perceptron.weights.append(random.uniform(-1,1))

    def guess(self,inputs):

        sum = 0
        for i in range(len(Perceptron.weights)):
            sum+= inputs[i] * Perceptron.weights[i]
        output = self.sign(sum)
        return output
# activation function
    def sign(self,n):
        if n>0:
            return 1
        else:
            return -1

    def train(self,inputs,target):
        guess_value = self.guess(inputs)
        error = target - guess_value
# TUNE ALL THE WEIGHTS
        for i in range(len(Perceptron.weights)):
            Perceptron.weights[i] += error *inputs[i]  *Perceptron.lr

    def guessY(self,x):
        try:
            w0 = Perceptron.weights[0]
            w1 = Perceptron.weights[1]
            w2 = Perceptron.weights[2]

            return -(w2/w1) - (w0/w1)*x   
            # m = self.weights[0] /self.weights[1]
            # b = self.weights[2]
            # return m * x +b
        except ZeroDivisionError:
            print("divide by 0")
