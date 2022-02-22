device = torch.device('cuda', if torch.cuda.is_availble() else 'cpu')
linear = torch.nn.Linear(785, 10, bias = True).to(device)
torch.nn.init.normal_(liner.weight)
