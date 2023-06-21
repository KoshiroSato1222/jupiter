#モンテカルロ法
import matplotlib.pyplot as plt
import numpy as np

samples = 1000
xs = np.random.rand(samples)
ys = np.random.rand(samples)

inner = 0
for i in range(samples):
    x = xs[i]
    y = ys[i]
    if x**2 + y**2 < 1:
        inner += 1

print(inner*4 / samples)
ci = plt.Circle((0,0), radius=1, fc="None", ec="r", linewidth=3)
ax = plt.gca()
ax.add_patch(ci)

plt.axis("scaled")
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.scatter(xs, ys, marker="x")
plt.show()