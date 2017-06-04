import sys

from bigfloat import *

from stabpoly.polynomials import get_uniform_polynomial_coefficients as generate_c1

c0 = [1099511627776, 24189255811072, 246256244883456, 1540192452214784, 6626856438595584, 20815424782336000, 49440127780388864, 90760917330952192, 130542353846894592, 148265935982034944, 133428419454468096, 95108105357443072, 53488147262651392, 23554849430486016, 8027417270841888, 2081476529958960, 400922025297120, 55442911547664, 5236669900566, 312666583437, 10336730112, 143644347, 295245]
c1 = generate_c1(22,22)
print(c1)

c0 = [36028797018963968, 1116892707587883008, 16395354443442290688, 151639577153285128192, 991922215974862848000, 4883373265772884262912, 18800695611164876341248, 58063426600570307215360, 146421084563734593011712, 305324916949206337323008, 531263837485934837760000, 776290556365837472628736, 956702004316173735297024, 996999960546448183918592, 879554548481726733090816, 656712421182217211871232, 414347152085608822112256, 220288926800260157898752, 98269511180306698176512, 36570494273311056890880, 11267822299389441057312, 2846566385296390516608, 582342768190959777504, 94950093134577442896, 12086539674754485420, 1168783567387459308, 82722897967994280, 4064194998644607, 127892178348733, 2249895769521, 16644208060, 14348907]
c1 = generate_c1(31,31)

def eval_wanloss_poly(x):
  value = BigFloat(0.0)
  sign = +1
  power = 1
  for i in range(len(c0)):
    value += sign * c0[i] * power
    sign = -sign
    power *= x
  return value

_EPSILON = 1e-10
_MAX_ITER = 100

def search(x, y):
  mean = lambda a,b: (a+b)*.5
  prev_val = eval_wanloss_poly(mean(x,y))
  val = -1
  iters = 0
  while abs(val) >= _EPSILON and iters < _MAX_ITER:
    prev_val, val = val, eval_wanloss_poly(mean(x,y))
    if val > 0:
      x = mean(x,y)
    else:
      y = mean(x,y)
    iters +=1
    #print(val, x, sep='\t')
  if iters == _MAX_ITER:
    print('unreliable results: reached max iterations, with value {}.'.format(val))
  return mean(x,y)

def silly_search(x):
  delta = BigFloat(1.0 / 2**16)
  param = BigFloat(0.0)
  val = BigFloat(1.0)
  while val > 0 and param < x:
    param += delta
    val = eval_wanloss_poly(param)
  return param
  
def main():
  if len(sys.argv) != 2:
    print('Bad input! Provide exactly one non-negative integer argument.')
    return
  x = float(sys.argv[1])
  with precision(2000):
    #print(eval_wanloss_poly(x))
    #print(search(0,BigFloat(x)))
    print(silly_search(BigFloat(x)))



if __name__ == '__main__':
  main()
