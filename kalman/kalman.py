#!/usr/local/bin/python3

# Python class to implement a Kalman Filter

import numpy as np 

class kalman():

    # Init assuming 2d problem with no control input or process noise
    def __init__(self, t0, dx):
        self.t = t0
        # Measurement function
        self.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
        # Measurement uncertainty
        self.R = np.array([[dx, 0], [0, dx]])
        # Initialize state
        self.x = np.zeros([4,1])
        # Initialize variance
        self.P = 1000 * np.identity(4)

    def step(self, t, z):
        dt = t - self.t
        self.t = t
        # State function with new dt
        self.F = np.identity(4)
        self.F[0,2] = dt
        self.F[1,3] = dt

        # Update
        y = z - np.dot(self.H, self.x)
        S = np.dot(self.H, np.dot(self.P, self.H.transpose())) + self.R
        K = np.dot(np.dot(self.P, self.H.transpose()), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.P = np.dot((np.identity(4) - np.dot(K, self.H)), self.P)
        print(self.x)

        # Predict
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.transpose()))

dx = 0.1    # m uncertainty in position measurement
k = kalman(0, dx)

data = [[0, 0, 0], [0.1, 1, 1], [0.2, 2, 2], [0.3, 3, 3], [0.4, 4, 4], [0.5, 5, 5]]

x = []

for i in data:
    z = np.array([i[1:2]])
    z = z.transpose()
    t = i[0]
    k.step(t, z)

