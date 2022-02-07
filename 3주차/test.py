import numpy as np

def l1_norm(x):
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

def l2_norm(x):
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm

def angle(x,y):
    v = np.inner(x,y) / (l2_norm(x) * l2_norm(y)) #cos theta
    theta = np.arccos(v) #arc_cos(cocs(theta)) = theta
    return theta

x=np.array([1,-1,1,-1])
y=np.array([4,-4,4,-4])

print(np.inner(x, y))
