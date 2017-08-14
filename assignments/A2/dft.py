import matplotlib.pyplot as plt
import numpy as np

# x = [1,1,1,1, -1, -1, -1, -1]
# N = len(x)

N = 64
k0 = 7.5
# x = np.exp(-1j * 2 * np.pi * k0 / N * np.arange(N))
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

X = np.array([])
for k in kv:
  s = np.exp(1j * 2 * np.pi * k / N * nv)
  X = np.append(X, sum(x * s))

y = np.array([])
for n in nv:
  s = np.exp(1j * 2 * np.pi * n / N * kv)
  y = np.append(y, sum(X * s) / N)

plt.plot(kv, y)
plt.axis([-N/2, N/2 -1, -1, 1])
plt.show()