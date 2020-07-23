#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
given a boxcount array, it calculates the slope
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

# import fileinput
import math


def calcslope(box_arr):
    x1, y1, x2, y2, xy, n = 0, 0, 0, 0, 0, 0

    for line in box_arr:
        x, y = line  # line.strip().split()
        # x = float(x)
        # y = float(y)

        x1 += x
        y1 += y
        x2 += x * x
        y2 += y * y
        xy += x * y
        n += 1

    if n > 1:
        a = (xy - x1 * y1 / n) / (x2 - x1 * x1 / n)
        b = (y1 - a * x1) / n
        # correlation coefficient r
        r = (xy - x1 * y1 / n) / math.sqrt(x2 - x1 * x1 / n) / math.sqrt(y2 - y1 * y1 / n)
        # print("slope= ", a, "	y_intcpt= ", b, "	corr= ", r)
        return a, b, r
    else:
        # print("slope= ", 9999, "	y_intcpt= ", 0, "	corr= ", 0)
        return 9999, 0, 0



# x1, y1, x2, y2, xy, n = 0, 0, 0, 0, 0, 0
#
# for line in fileinput.input():
#     x, y = line.strip().split()
#     x = float(x)
#     y = float(y)
#
#     x1 += x
#     y1 += y
#     x2 += x * x
#     y2 += y * y
#     xy += x * y
#     n += 1
#
# if n > 1:
#     a = (xy - x1 * y1 / n) / (x2 - x1 * x1 / n)
#     b = (y1 - a * x1) / n
#     # correlation coefficient r
#     r = (xy - x1 * y1 / n) / math.sqrt(x2 - x1 * x1 / n) / math.sqrt(y2 - y1 * y1 / n)
#     print("slope= ", a, "	y_intcpt= ", b, "	corr= ", r)
# else:
#     print("slope= ", 9999, "	y_intcpt= ", 0, "	corr= ", 0)
