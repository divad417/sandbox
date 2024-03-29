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

        # Predict
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.transpose()))
        
        x = self.x
        P = self.P
        return(x, P)

def line(n, dx):
    x0 = 0
    y0 = 0
    theta = pi/4
    v = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9.5, 9, 8.5, 8, 7, 6, 5, 4, 2, 1, 0.5]
    dt = 0.1

    t = np.linspace(0, 10, 101)
    pos = np.empty([n, 2])
    for i in range(n):
        x_new = np.random.normal(x0 + t[i] * v[i] * cos(theta), dx)
        y_new = np.random.normal(y0 + t[i] * v[i] * sin(theta), dx)
        pos[i,:] = [x_new, y_new]
    
    return(t, pos)
        


def main():

    # Initialize the kalman filter
    dx = 0.2    # measurement uncertainty
    k = kalman(0, dx)

    n = 21
    t, truth = line(n, dx)
    filt_pos = np.empty([n, 4])
    filt_spd = np.empty(n)
    spd_var = np.empty(n)

    for i in range(n):
        # Prepare the measurement input
        z = np.array(truth[i,:], ndmin=2).transpose()

        # Run the Kalman Filter
        x, P = k.step(t[i], z)

        # Record the output
        filt_pos[i,:] = np.transpose(x)
        filt_spd[i] = np.linalg.norm([x[2][0], x[3][0]])
        spd_var[i] = np.linalg.norm([P[2][2], P[3][3]])


    # Plot the results
    plt.subplot(2,1,1)
    plt.plot(truth[:,0],truth[:,1],'+')
    plt.plot(filt_pos[:,0],filt_pos[:,1],'--')
    plt.axis('equal')

    plt.subplot(2,1,2)
    plt.plot([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9.5, 9, 8.5, 8, 7, 6, 5, 4, 2, 1, 0.5])
    plt.plot(filt_spd)
    plt.plot(spd_var)
    plt.axis([0, 50, 0, 15])
    plt.show()

main()