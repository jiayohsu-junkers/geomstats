"""Numpy based computation backend."""

import numpy as np

pi = np.pi


def abs(val):
    return np.abs(val)


def zeros(val):
    return np.zeros(val)


def ones(val):
    return np.ones(val)


def all(val):
    return np.all(val)


def allclose(a, b):
    return np.allclose(a, b)


def sin(val):
    return np.sin(val)


def cos(val):
    return np.cos(val)


def tan(val):
    return np.tan(val)


def arcsin(val):
    return np.arcsin(val)


def arccos(val):
    return np.arccos(val)


def shape(val):
    return val.shape


def dot(a, b):
    return np.dot(a, b)


def maximum(a, b):
    return np.maximum(a, b)


def greater_equal(a, b):
    return np.greater_equal(a, b)


def to_ndarray(element, to_ndim, axis=0):
    element = np.asarray(element)

    if element.ndim == to_ndim - 1:
        element = np.expand_dims(element, axis=axis)
    assert element.ndim == to_ndim
    return element


def sqrt(val):
    return np.sqrt(val)


def norm(val, axis):
    return np.linalg.norm(val, axis=axis)


def rand(*args, **largs):
    return np.random.rand(*args, **largs)


def isclose(a, b):
    return np.isclose(a, b)


def less_equal(a, b):
    return np.less_equal(a, b)
