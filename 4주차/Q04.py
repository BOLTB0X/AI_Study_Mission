import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'gs',t, t**3, 'b^')
plt.show()