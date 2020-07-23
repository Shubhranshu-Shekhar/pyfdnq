#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NOT used in pyfdnq.
expects numbers, and prints their logs.
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

import fileinput
import math

for line in fileinput.input():
	words = line.split()
	# words = map(float, words)
	print(math.log(float(words[0])+1), " ", math.log(float(words[1])+1))