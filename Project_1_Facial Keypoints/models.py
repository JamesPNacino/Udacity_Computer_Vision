## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 5)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        
        # add a dropout
        self.dropout = nn.Dropout(p=0.2)
        
        # after first convolution shape is (224 - 5)/1 + 1 = 220 --> (32, 220, 220)
        # after pooling, shape is (32, 110, 110)
        self.pool = nn.MaxPool2d(2, 2)
        
        
        # after this second convolution, shape is (110 - 5)/1 + 1 == (20, 106, 106)
        self.conv2 = nn.Conv2d(32, 20, 5)
        #after pooling, shape is (20, 53, 53)
        
        # now flatten out the feature vector
        self.fc1 = nn.Linear(20*53*53, 220)
        
        self.fc2 = nn.Linear(220, 136)

    
        
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        x = self.pool(F.relu(self.dropout(self.conv1(x))))
        x = self.pool(F.relu(self.dropout(self.conv2(x))))
        x = x.view(x.size(0), -1)
        x = F.relu(self.dropout(self.fc1(x)))
        x = F.relu(self.fc2(x))
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
