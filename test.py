import math
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-5, 5, 0.001)
f = []
for i in t:
    f.append(np.arcsin(i))

plt.plot(t, f)
plt.show()


