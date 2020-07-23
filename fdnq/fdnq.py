#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Translated from perl code written by Prof. Christos Faloutsos.
Computes Dq fractal dimension.
Computes the slope of the log-log plot after box counting.
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

import sys
import argparse
import numpy as np
from collections import namedtuple

from mkboxcount import mkboxcount
from killFlats import killFlats
from calcslope import calcslope

Results = namedtuple('Results', 'slope y_intercept corr box_counts')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-D', type=int, default=0)
    parser.add_argument('-r', type=float, default=0.0000001)
    parser.add_argument('-R', type=float, default=1000000)
    parser.add_argument('-f', type=float, default=2)  # 1.3
    parser.add_argument('-q', type=int, default=2)
    parser.add_argument('-v', action='store_true')
    # hist = 0; hist=1 means that the last column contains 'values':
    parser.add_argument('--hist', action='store_true')
    parser.add_argument('--input', type=str, default=None)
    args, _ = parser.parse_known_args()
    return args


def fdnq(input_arr, q=2, rmin=0.0000001, rmax=1000000, factor=2,
         histogram=False, verbose=0, save_plot_file=None):
    '''
    Function to calculate fractal dimension given an input array of points
    :param input_arr:
    :param q:
    :param r:
    :param R:
    :param factor:
    :param hist:
    :return:
    '''

    if q == 1:
        sys.exit("q=1 is not implemented yet")

    # compute box count
    box_counts = mkboxcount(input_arr, q=q, rmin=rmin, rmax=rmax,
                            factor=factor, histogram=histogram,
                            verbose=verbose)
    if save_plot_file:
        np.savetxt(save_plot_file, box_counts, delimiter=' ', fmt='%s')

    num_r = len(box_counts)
    box_counts = np.array(box_counts)
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
    args = parse_args()
    rmin = args.r
    rmax = args.R
    factor = args.f
    q = args.q
    verbose = 0

    if args.v:
        verbose += 1

    if q == 1:
        sys.exit("q=1 is not implemented yet")

    # compute box count

    # args.input = '../data/diagonal.inp'
    inp = args.input
    input_arr = np.loadtxt(inp)

    results = fdnq(input_arr, q=q, rmin=rmin, rmax=rmax,
                   factor=factor, histogram=args.hist,
                   verbose=verbose)
    fd = results.slope
    print("slope= ", fd, "	y_intcpt= ", results.y_intercept, "	corr= ", results.corr)


if __name__ == '__main__':
    main()
