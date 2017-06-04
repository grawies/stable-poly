#!/usr/bin/python3

# Plots c(n,k) := e_k(\partial) T^n P(\1), given c(0,*) and the range of n's.

#separator = '\t'
separator = ', '

def print_list(c):
  print( separator.join(['{}'.format(x) for x in c]).replace('e','*^') )

def plot_recurrence(c0, N):
  D = M = len(c0) - 1
  c1 = [0]*(D + 1)
  print_list(c0)

  for n in range(N):
    # compute c1
    c1[0] = c0[0]
    for k in range(1, D + 1):
      c1[k] = (M - k + 1)*(D - k + 1)/D/M * c0[k-1] + (D - k)/D * c0[k]
    # print
    print_list(c1)
    # swap
    c0, c1 = c1, c0

c0 = [1.0, 5.0, 9.25, 8.0, 3.25, 0.5]
#c0 = [1.0, 1.71, 0.817, 0.108, 0.001] # roots -0.01, -0.2, -0.5, -1.0
wanless_numerators = [1099511627776, 24189255811072, 246256244883456, 1540192452214784, 6626856438595584, 20815424782336000, 49440127780388864, 90760917330952192, 130542353846894592, 148265935982034944, 133428419454468096, 95108105357443072, 53488147262651392, 23554849430486016, 8027417270841888, 2081476529958960, 400922025297120, 55442911547664, 5236669900566, 312666583437, 10336730112, 143644347, 295245]
wanless_coeffs = [wn/1099511627776.0 for wn in wanless_numerators]

def main():
  #plot_recurrence(c0, 2)
  plot_recurrence(wanless_coeffs, 2)

if __name__ == '__main__':
  main()
