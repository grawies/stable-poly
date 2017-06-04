# stable-poly
Code from my thesis work, used to investigate stable polynomials in general and a matrix of Wanless in particular.

# TESTS
To test the code in a Linux environment, simply execute the script python/runtests.sh from python/.

# RUN
To compute the coefficients of the mixed characteristic polynomial of Wanless' counterexample, execute the python script python/wanless_coefficients.py as follows:

python/wanless_coefficients.py 3 4 all

To verify that the smallest root of said MCP is smaller than that of the corresponding scaled associated Laguerre polynomial, run the Mathematica notebook mathematical/wanless_root_counting.nb.

# REQUIREMENTS

Mathematica 1.1

Python 3.X, with Numpy

The script "permanent.py", author Jan Verschelde, found at the location below at the time of writing.
Source: http://homepages.math.uic.edu/~jan/mcs507f13/
Store it as python/stabpoly/external/permanent.py
