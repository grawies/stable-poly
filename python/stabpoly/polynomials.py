#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import sympy as sp
import sympy.abc as spabc
from math import log, exp

import stabpoly.subpermanents as subpermanents

# generates a list of variables
# by default [x1, x2, x3]
def getvars(symbol='x', count=3):
  variable_iterator = sp.numbered_symbols(symbol, start=1)
  return [next(variable_iterator) for i in range(count)]

# computes the product polynomial of a given matrix
def product_polynomial(A):
  degree, variable_count = A.shape
  symbols = getvars(count=variable_count)
  affine_factors = [sum(coeff*x for coeff,x in zip(row, symbols)) for row in A]
  polynomial = 1
  for factor in affine_factors:
    polynomial *= factor
  return polynomial

# computes the matching polynomial of a given matrix
def matching_polynomial(A):
  rows,cols = A.shape
  degree = min(rows,cols)
  t = spabc.t
  polynomial = t**degree
  for k in range(degree):
    polynomial += t**k * subpermanents.getsubpermanentsum(A, degree-k) * (-1)**(degree-k)
  return sp.Poly(polynomial), t

def gurvits_bound_G(k):
  if k < 2:
    return 1
  return ((k-1.0)/k)**(k-1)

def gurvits_bound_log_G(k):
  if k < 2:
    return 0
  return (k-1)*log((k-1.0)/k)

def gurvits_bound(degree, local_degree=0):
  if local_degree == -1:
    local_degree = degree
  log_factors = [gurvits_bound_log_G(min(k, local_degree)) for k in range(1,degree+1)]
  bound = exp(sum(log_factors))
  return bound

# Returns the coefficients of the uniform polynomial, decreasing powers.
# The k:th coefficient is k! * (m choose k) * (d choose k) * m^(m-k).
def get_uniform_polynomial_coefficients(m,d):
  unif_coeffs = [m**m]*(d+1)
  for k in range(1,d+1):
    unif_coeffs[k] =  unif_coeffs[k-1] * (m - k + 1) * (d - k + 1) // k // m;
  return unif_coeffs
