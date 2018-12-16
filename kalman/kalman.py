#!/usr/local/bin/python3

# Python class to implement a Kalman Filter

import numpy as np 
import matplotlib.pyplot as plt
from random import random
from math import *

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
        x = self.x
        P = self.P

        # Predict
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.transpose()))
        return(x, P)

def line(n, dx):
    x0 = 0
    y0 = 0
    theta = pi/4
    v = 10
    dt = 0.1

    t = np.linspace(0, 10, 101)
    pos = np.empty([n, 2])
    for i in range(n):
        x_new = x0 + t[i] * v * cos(theta)
        y_new = y0 + t[i] * v * sin(theta)
        pos[i,:] = [x_new, y_new]
    
    return(t, pos)
        


def main():

    # Initialize
    dx = 0.1    # m uncertainty in position measurement
    k = kalman(0, dx)

    n = 51
    t, truth = line(n, dx)
    meas = np.empty([n, 2])
    filt = np.empty([n, 4])

    for i in range(n):
        z = np.array(truth[i,:], ndmin=2)
        z = z.transpose()
        x, P = k.step(t[i], z)
        filt[i,:] = np.transpose(x)


    plt.subplot(2,1,1)
    plt.plot(truth,'+')
    plt.plot(filt,'--')

    plt.subplot(2,1,2)
    plt.plot()
    plt.show()

main()