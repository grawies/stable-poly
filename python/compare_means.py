#!/usr/bin/python3

from random import random

sumrecip = lambda p,q,r: sum([1/val for val in [p,q,r]])

sym2 = lambda p,q,r: p*q+q*r+r*p

def twoprint(p,q):
  print('{:.03f}\t{:.03f}'.format(p,q))

def printall(a,b,c,x,y,z):
  print('=======================')
  twoprint(sumrecip(x,y,z), sumrecip(a,b,c))
  print('-----------------------')
  twoprint(x,a)
  twoprint(x+y,a+b)
  twoprint(x+y+z,a+b+c)

coeffs = [1.0, 3.0, 2.0, 2.0/9]

def main():
  NUM_TESTS = 100000
  m = 3
  rep = 0
  tots = 0
  for n in range(NUM_TESTS):
    x = random()*m
    y = random()*(m-x)
    z = m - x - y
    x,y,z = sorted([x,y,z], key=lambda p: -p)
    
    # uniform roots:
    #a,b,c = (2.0966, 0.7648, 0.1386)
    # temporary test roots:
    a,b,c = (1.606, 2.509-1.606, 3.000-2.509)
    # sort away unqualified polynomials
    if not (sym2(x,y,z) >= coeffs[2] and x*y*z >= coeffs[3]):
      continue
    # verify that this is a deviant (Wanloss-like) polynomial
    if sumrecip(x,y,z) <= 9.0:
      continue
    tots+=1
    #if sumrecip(a,b,c) > sumrecip(x,y,z):
    #  a,b,c,x,y,z=x,y,z,a,b,c

    report_all = False

    if report_all or (x<=a and x+y<=a+b):
      printall(a,b,c,x,y,z)
      rep+=1
  print('printed {}/{} reports.'.format(rep,tots))

if __name__ == '__main__':
  main()
