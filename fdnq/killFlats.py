#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
expects an array with points and drops the parts that are within log(2) from
the top and the bottom of the plot
It is supposed to replace 'choptop' and 'chopbottom' simultaneously
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

import math


def killFlats(box_count_arr=None, verbose=0):
    flat_arr = []

    HUGE = 2 ^ 30
    miny = HUGE
    maxy = -HUGE
    width = math.log(2)  # drop all points with $y within $width from min or max

    lineno = 0
    xa, ya = {}, {}
    for line in box_count_arr: #  fileinput.input():  #
        lineno += 1
        # x, y = line.strip().split()
        x, y = line
        x = float(x)
        y = float(y)

        if verbose > 0:
            print(x, " ", y)

        xa[lineno] = x
        ya[lineno] = y

        if y < miny:
            miny = y

        if y > maxy:
            maxy = y

    totpts = lineno

    if verbose > 0:
        print("maxy=", maxy, " miny=", miny)

    for i in range(1, totpts+1):
        y = ya[i]
        if (y > (miny + width)) and (y < (maxy - width)):
            # print(xa[i], " ", ya[i])
            flat_arr.append((xa[i], ya[i]))

    return flat_arr


# if __name__ == '__main__':
#     killFlats()
