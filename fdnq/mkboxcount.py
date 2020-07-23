#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
computes the box-count-plot
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

import sys
import math
from collections import defaultdict


def mkboxcount(input_arr, q=2, rmin=0.0000001, rmax=1000000, factor=2,
         histogram=False, verbose=0):
    hist = 0

    if histogram:
        hist = 1

    if verbose > 1:
        print("*** verbose=", verbose)
        print("*** factor=", factor)
        print("*** q=", q)
        print("*** h=", hist)
        print("*** rmin=", rmin, " rmax=", rmax)
        print("*** datafname1=|", )

    # compute the 'floor' of each entry
    # update the appropriate count in a hash table
    box_list = []
    r = rmin
    while r <= rmax:
        hcount = defaultdict(int)  # clear the hash table with the counts per cell
        for words in input_arr:
            words = words.tolist()

            if verbose > 2:
                print("INPUT: ", words)

            if 1 == hist:   # histogram: x1, x2, ... xn, value
                val = words.pop()  # gets the last value

                if len(words) < 1:
                    sys.exit("ERROR: --histogram flag, with no coordinates - only values - exiting")
            else:  # just points: x1 x2 ... xn
                val = 1  # just one point, by default

            # like the earlier processing, with $val instead of just '1'
            floorwords = [math.floor(w_ / r) for w_ in words]

            out = ":".join(map(str, floorwords))

            if verbose > 4:
                print(out, "(value= ", val, " )")

            hcount[out] += val

        # collect the statistics:
        total = 0
        for key, val in hcount.items():
            if q == 0:
                total += 1
            elif q == 1:
                total += val * math.log(val)
            else:
                total += (val ** q)

        box_list.append((r, total))

        r *= factor

    return box_list

