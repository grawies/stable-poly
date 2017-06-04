#!/home/sam/shared-space/linux-system/anaconda3/bin/python

from sys import stderr
import itertools

from stabpoly.external.permanent import permanent

# takes a matrix A and non-negative integer k, computes the sum of all k-subpermanents.
def getsubpermanentsum(A, k):
  if k==0:
    # conventional value
    return 1
  permanentsum = 0
  for I in itertools.combinations(range(A.shape[0]), k):
    for J in itertools.combinations(range(A.shape[1]), k):
      permanentsum += permanent(A[[(i,) for i in I],J])
  return permanentsum

