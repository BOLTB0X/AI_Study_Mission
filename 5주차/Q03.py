criterion = torch.nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.SGD(linear, Parameters(), lr = 0.1)
