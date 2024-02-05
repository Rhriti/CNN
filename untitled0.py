import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')  # comment out for "light" theme
plt.rcParams["font.size"] = 12

plt.rcParams["figure.figsize"] = (12, 7)

fname='paste.png'
fname2='2.png'

im_data=plt.imread(fname)
im_data2=plt.imread(fname2)

KERNELS = {"Edge Detection 3x3": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
           "Sharpen 3x3": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])}

edge_kernal=KERNELS['Edge Detection 3x3']


def RGB_convolve(im1, kern):
    im2 = np.empty_like(im1)
    for dim in range(im1.shape[-1]):  # loop over rgb channels
        im2[:, :, dim] = sp.signal.convolve2d(im_data[:, :, dim],
                                              kern,
                                              mode="same",
                                              boundary="symm")
    return im2

RGB_convolve(im_data2,edge_kernal)