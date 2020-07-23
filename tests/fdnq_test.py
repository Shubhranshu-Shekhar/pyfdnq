#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test module to test if the python fdnq produces same results as perl fdnq.
"""
__author__ = 'Shubhranshu-Shekhar'
__date__ = 'July, 2020'

from os import sys, path

print(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'fdnq'))

import pytest
import subprocess
import numpy as np

from fdnq import fdnq


def compare_floats(f1, f2, significant=6):
    if significant == 0:
        return True if f1 - f2 == 0 else False

    if abs(f1 - f2) >= 10 ** -significant:
        return False

    return True


def n_digits_after_decimal(n):
    s = str(n)
    if '.' not in s:
        return 0
    return len(s) - s.index('.') - 1


def exec_fdnq_perl(data_path):
    args_ = ['perl', 'fdnq.pl', '-q2', data_path]
    pipe = subprocess.Popen(args_, stdout=subprocess.PIPE, cwd="../legacy/")
    out, err = pipe.communicate()
    out_lst_ = out.strip().split()
    slope, y_intcpt, corr = float(out_lst_[1]), float(out_lst_[3]), float(out_lst_[5])
    return slope, y_intcpt, corr


test_data = ['../data/diagonal.inp', '../data/sierpinski5K.inp']


@pytest.mark.parametrize("data_file", test_data)
def test_diagonal_fd(data_file):
    # data_file = '../data/diagonal.inp'
    # data_file = '../data/sierpinski5K.inp'
    # python version
    input_arr = np.loadtxt(data_file)
    results = fdnq.fdnq(input_arr, q=2, rmin=0.0000001, rmax=1000000,
                        factor=2, histogram=False,
                        verbose=0)
    fd = results.slope
    y_intrcpt = results.y_intercept
    corr = results.corr

    # perl version
    pl_slope, pl_y_intcpt, pl_corr = exec_fdnq_perl(data_file)

    # assert that slope, intercept as well as corr are equal in python and perl
    print("In test")
    assert compare_floats(fd, pl_slope, significant=n_digits_after_decimal(pl_slope))
    assert compare_floats(y_intrcpt, pl_y_intcpt, significant=n_digits_after_decimal(pl_y_intcpt))
    assert compare_floats(corr, pl_corr, significant=n_digits_after_decimal(pl_corr))


if __name__ == '__main__':
    test_diagonal_fd('../data/diagonal.inp')
