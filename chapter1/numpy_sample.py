import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x)

type(x)

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x.shape)
print(x.dtype)

print(x * 10)

z = np.array([[51, 55], [14, 19], [0, 4]])
print(z)

print(z[0][1])

print(z.flatten())
print(z[z > 15])
