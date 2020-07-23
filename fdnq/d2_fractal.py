#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Computes correlation dimension using naive pairwise distances between points
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist
from collections import namedtuple

from fdnq.killFlats import killFlats
from fdnq.calcslope import calcslope

Results = namedtuple('Results', 'slope y_intercept corr box_counts')


def d2_fractal(arr):
    # remove self and duplicate pair distances
    pairwise_distances = pdist(arr)
    pairwise_distances = np.sort(pairwise_distances)

    print('# pairs:', len(pairwise_distances))

    box_list = [(r, i+1) for i, r in enumerate(pairwise_distances)]

    num_r = len(box_list)
    box_counts = np.array(box_list)
    assert (num_r == box_counts.shape[0])

    # create log-log
    loglog_box_counts = np.log(box_counts)

    # kill_flats
    flat_box_counts = killFlats(loglog_box_counts)

    # calculate slope
    fractal_dim, y_intrcpt, corr = calcslope(flat_box_counts)
    results = Results(slope=fractal_dim, y_intercept=y_intrcpt, corr=corr, box_counts=box_counts)
    return results


def main():
    # input_arr = np.loadtxt('diagonal.inp')
    input_arr = np.loadtxt('../data/sierpinski5K.inp')

    results = d2_fractal(input_arr)
    fd, box_counts = results.slope, results.box_counts

    plt.scatter(box_counts[:, 0], box_counts[:, 1])
    plt.xscale('symlog')
    plt.yscale('symlog')
    plt.show()

    print("Computed fd=", fd)
    # # pairs: 12497500
    # slope=  1.5219190337267867 	y_intcpt=  16.36071186817289 	corr=  0.9995681029139027
    # Computed fd= 1.5219190337267867


if __name__ == '__main__':
    main()
