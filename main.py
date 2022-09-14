import numpy as np
import scipy.linalg
from scipy import io, integrate, linalg, signal

a = np.array([[1, 2, 3, 4, 5],
               [-1, 0, 5, 6, 7],
               [-10, 6, 3, -1, -2],
               [2, 3, 4, -3, 6],
               [4,5,6, 2, 3]])

b = np.array([[1, 2, 3, 4, 5],
               [-1, 0, 5, 6, 7],
               [-10, 6, 3, -1, -2],
               [2, 3, 4, -3, 6],
               [4,5,6, 2, 3]])

print(a)
print(a.size)
print(a.shape)
print(a.shape[1])
print(np.array([[1,2,3], [4,5,6]]))
print(a[-1])
print(a[1,4])
print(a[1, : ])
print(a[0: 5])
print(a[0:3, 4:9])
print(a[np.ix_([1, 3, 4], [0, 2])])
print(a[2:21:2,:])
print(a[ ::2,:])
print(a[::-1,:])
print(a[np.r_[:len(a),0]])
print(a.T)
print(a.conj().T)
print(a @ b)
print(a * b)
print(a/b)
print(a**3)
print((a > 0.5))
print(np.nonzero(a > 0.5))
a[a < 0.5]=0
print(a * (a > 0.5))
a[:] = 3
x = a
y = x.copy()
y = x[1, :].copy()
y = x.flatten()
print(y)
print(np.arange(1., 11.))
print(np.arange(10.))
print(np.arange(1.,11.)[:, np.newaxis])
print(np.zeros((3, 4)))
print(np.zeros((3, 4, 5)))
print(np.ones((3, 4)))
print(np.eye(3))
print(np.diag(a))
print(np.diag(a, 0))
print(np.linspace(1,3,4))
print(np.mgrid[0:9.,0:6.])
print(np.meshgrid([1,2,4],[2,4,5]))
a = [2]
print(np.tile(a, (3,3)))
b = [3]
print(np.concatenate((a,b),0))
a = np.array([[1,2,3],
            [4,5,6]])
print(a.max())
print(a.max(0))
print(a.max(1))
print(np.maximum(a, b))
v = np.array([1,2,3])
print(np.sqrt(v @ v))
print(a&b)
print(a|b)
a = np.array([[1,2],
              [3,4]])
print(linalg.inv(a))
print(linalg.pinv(a))
U, S, Vh = linalg.svd(a)
print(U,S,Vh)
D,V = linalg.eig(a)
print(D,V)
print(np.unique(a))
print(a.squeeze())
