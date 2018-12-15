#!/usr/local/bin/python3

# Python class to implement a Kalman Filter

import numpy as np 

class kalman():

    # Init assuming 2d problem with no control input or process noise
    def __init__(self, dt, dx):
        # Measurement function
        self.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
        # Measurement uncertainty
        self.R = np.array([[dx, 0], [0, dx]])
        # State function
        self.F = np.identity(4)
        self.F[0,2] = dt
        self.F[1,3] = dt

    def update(self, x, P, z):
        y = z - np.dot(self.H, x)
        S = np.dot(self.H, np.dot(P, self.H.transpose())) + self.R
        K = np.dot(np.dot(P, self.H.transpose()), np.linalg.inv(S))
        x = x + np.dot(K, y)
        P = np.dot((np.identity(4) - np.dot(K, self.H)), P)
        return(x, P)

    def predict(self, x, P):
        x = np.dot(self.F, x)
        P = np.dot(self.F, np.dot(P, self.F.transpose()))
        return(x, P)

dt = 0.1    # sec timestep
dx = 0.1      # m uncertainty in position measurement
dxi = 1000  # m initial uncertainty in position


k = kalman(dt, dx)
x = np.zeros([4,1])
P = 1000 * np.identity(4)

data = [[0, 0], [1,1], [2,2], [3,3], [4,4]]

for i in data:
    z = np.array([i])
    z = z.transpose()
    x, P = k.update(x, P, z)
    x, P = k.predict(x, P)
    print(x)
    print(P)

