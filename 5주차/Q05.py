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

for epoch in range(training_epochs):
    for i, (img, labels) in enumerate(train_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1, 28 * 28)
        
        output = linear(imgs)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backword()
        optimize.step()
        
        _, argmax = torch.max(outputs, 1)
        accuracy = (labels == argmax).float().mean()
        
        if (i+1) % 100 == 0:
            print('Epoch [{}/{}], Step[{}/{}], Loss: {:.4f}, Accuarcy: {:.2f}%'.format(epoch + 1, training_epochs, i + 1, len(train_loader), loss.item(), accuracy.item()* 100))
        

linear.eval()

with torch.no_grad():
    correct = 0
    total = 0
    
    for i, (img, labels) in enumerate(test_loader):
        img, labels = img.to(device), labels.to(device)
        imgs =imgs.view(-1, 28 * 28)
        outputs = linear(imgs);
        _, argmax = torch.max(outputs, 1)
        total += imgs.size(0);
        correct += (labels == argmax).sum().item()
        
    print('Test accuracy for {} images" {:.2f}%'.format(total, correct/total * 100))
