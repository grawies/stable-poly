#!/usr/bin/python3

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# VERIFICATION SCRIPT - DO NOT USE AS DEFAULT
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# This script computes the number of k-matchings of the Wanless 22x22-matrix graph,
# using a grotesque recursion.

DEF_DEBUG = False

M_memory = {}

def M(n, k, l1, l2, a, b, c):
  params = (n,k,l1,l2,a,b,c)
  if a+b+c != k:
    print('ERROR! a+b+c is not k!')
    print('{}, {}, {} doesn\'t sum to {}'.format(a,b,c,k))
    return None
  if any([x < 0 for x in params]):
    return 0
  if a > n+1:
    return 0
  if n == 0:
    if l1 == 1 and l2 == 1 and a == 1 and b == 0 and c == 0:
      return 1
    if l1 == 0 and l2 == 0 and a == 0 and b == 0 and c == 0:
      return 1
    else:
      return 0
  # TODO return 0 if a > n+1 and verify that this does not change result
  if params in M_memory:
    return M_memory[params]

  matching_count = 0
  if l2 == 0:
    # pick first w2
    matching_count += M(n-1, k-1, l1, 0, a  , b-1, c  ) * 2
    matching_count += M(n-1, k-1, l1, 1, a  , b-1, c  ) * 2
    # pick two w2's
    matching_count += M(n-1, k-2, l1, 0, a  , b-2, c  ) * 4
    # pick two w2's and a w3
    matching_count += M(n-1, k-3, l1, 0, a  , b-2, c-1) * 4
    # pick first w2, one w3
    matching_count += M(n-1, k-2, l1, 0, a  , b-1, c-1) * 4
    matching_count += M(n-1, k-2, l1, 1, a  , b-1, c-1) * 4
    # pick one w3
    matching_count += M(n-1, k-1, l1, 0, a  , b  , c-1) * 4
    matching_count += M(n-1, k-1, l1, 1, a  , b  , c-1) * 4
    # pick two w3's
    matching_count += M(n-1, k-2, l1, 0, a  , b  , c-2) * 2
    matching_count += M(n-1, k-2, l1, 1, a  , b  , c-2) * 2
    # pick one w3, last w2
    matching_count += M(n-1, k-2, l1, 0, a  , b-1, c-1) * 4
    # pick last w2
    matching_count += M(n-1, k-1, l1, 0, a  , b-1, c  ) * 2
    # skip everything
    matching_count += M(n-1, k  , l1, 0, a  , b  , c  )
    matching_count += M(n-1, k  , l1, 1, a  , b  , c  )

  else:
    # skip remaining
    matching_count += M(n-1, k-1, l1, 0, a-1, b  , c  )
    matching_count += M(n-1, k-1, l1, 1, a-1, b  , c  )
    # pick one w3
    matching_count += M(n-1, k-2, l1, 0, a-1, b  , c-1) * 4
    matching_count += M(n-1, k-2, l1, 1, a-1, b  , c-1) * 4
    # pick two w3's
    matching_count += M(n-1, k-3, l1, 0, a-1, b  , c-2) * 2
    matching_count += M(n-1, k-3, l1, 1, a-1, b  , c-2) * 2
    # pick w2
    matching_count += M(n-1, k-2, l1, 0, a-1, b-1, c  ) * 2
    # pick w2 and w3
    matching_count += M(n-1, k-3, l1, 0, a-1, b-1, c-1) * 4

  M_memory[params] = matching_count
  return matching_count


def NecklaceMatchings(n, k):
  matching_count = 0
  for j1 in range(2):
    for j2 in range(2):
      for a in range(k+1):
        for b in range(k+1):
          c = k - a - b
          if c < 0:
            continue
          if DEF_DEBUG:
            print('----------------------------------')
          matching_count += M(n, k, j1, j2, a, b, c)
  return matching_count

# n1 and n2 crystals in each (s,t)-separated segment
j1vals = (0,0,0,0,0,0,1,1,1)
j2vals = (0,0,0,0,1,1,0,0,1)
j3vals = (0,0,1,1,0,1,0,0,0)
j4vals = (0,1,0,1,0,0,0,1,0)
w1 = 0.5;   w1_int = 4
w2 = 0.25;  w2_int = 2
w3 = 0.375; w3_int = 3
int_denominator    = 8
def WanlessMatchings(n1,n2,k, int_quotient=False):
  matching_weight_sum = 0
  for i in range(k+1): # i edges from the n1-segment
    for j1,j2,j3,j4 in zip(j1vals, j2vals, j3vals, j4vals):
      matching_weight_sum1 = 0
      for a1 in range(i+1):
        for b1 in range(i+1):
          c1 = i - a1 - b1
          if c1 < 0:
            continue
          matching_count = M(n1, i, j1, j2, a1, b1, c1)
          weight = w1**a1 * w2**b1 * w3**c1
          if int_quotient:
            weight = w1_int**a1 * w2_int**b1 * w3_int**c1
          matching_weight_sum1 += matching_count * weight
      matching_weight_sum2 = 0
      for a2 in range(k-i+1):
        for b2 in range(k-i+1):
          c2 = k-i - a2 - b2
          if c2 < 0:
            continue
          matching_count = M(n2, k-i, j3, j4, a2, b2, c2)
          weight = w1**a2 * w2**b2 * w3**c2
          if int_quotient:
            weight = w1_int**a2 * w2_int**b2 * w3_int**c2
          matching_weight_sum2 += matching_count * weight
      matching_weight_sum += matching_weight_sum1 * matching_weight_sum2
  if int_quotient:
    return matching_weight_sum, int_denominator**k
  return matching_weight_sum 
