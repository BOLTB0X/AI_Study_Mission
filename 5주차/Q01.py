import imp
from inspect import ismethoddescriptor
from random import shuffle
import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transform as transforms
from torch.utils.data import DataLoader

training_epochs = 15; #반복 횟수
batch_size =100

root = "data"
mnist_train = dset.MNIST(root = root, transform = transform,download = True);
mnist_test = dset.MNIST(root = root, train = False, transform = transform,download = True)

#data loder를 직접 구현
train_loader = DataLoader(train_data, batch_size = batch_size, shuffle = True)
test_loader = DataLoader(train_data, batch_size = batch_size, shuffle = False)