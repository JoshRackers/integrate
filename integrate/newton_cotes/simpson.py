"""
This file contains the implementation of the Simpson rule
"""

import numpy as np

def evaluate(bounds, f):
    """

    Evaluate simpson's rule on an array of values and a function pointer
    \int_{a}^{b} = \sum_i ...

    Parameters
    ----------
    bounds : array_like
        An array with a dimension of two that contains the starting and ending points of the integrand.
    f : function
        Evaluates the integrand at a point

    Returns
    -------
    integral : float
        The integral of the function between the bounds.

    """

    if len(bounds) != 2:
        raise ValueError("Bounds should be a length of two, found %d." % len(bounds))

    a = bounds[0]
    b = bounds[1]
    ya = f(a)
    yb = f((a+b)/2.0)
    yc = f(b)
    I = (b-a) * (ya + 4 * yb + yc) / 6.0
    return I

