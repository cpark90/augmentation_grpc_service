import numpy as np

class PrototypeAlgorithm(object):

    def __init__(self, args):
        self.args = args
        self.np_array = np.array([0, 1, 2, 3, 4])
    
    def run(self, input):
        print(input)
        print(self.np_array)