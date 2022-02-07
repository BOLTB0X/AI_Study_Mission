import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.01;

for i in range(1000):
    prediction = (x_train * y_train) + bias
    error = pow((x_train - y_train),2).mean()
    
    gd_w = ((prediction - y_train) * 2 * x_train).mean()
    gd_b = ((prediction - y_train) * 2).mean()
    
    beta_gd -= learning_rate * gd_w
    bias -= learning_rate * gd_b
    
    if i % 100 == 0:
        print('Epoch ({:10d}/1000) cost: ({:10f}, w: {:10f}, b: {:10f}'.format(i, error, beta_gd.item(), bias.item()))