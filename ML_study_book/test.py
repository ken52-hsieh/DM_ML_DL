import numpy as np
import matplotlib.pyplot as plt

x= 2* np.random.rand(100, 1)
y= 4+ 3* x+ np.random.randn(100, 1)

plt.plot(x, y, "o", color= "blue")
plt.xlabel("x1")
plt.ylabel("y")
plt.show()