import stabpoly.bistochastic as bistochastic
import stabpoly.polynomials as polynomials
from stabpoly.external.permanent import permanent

def gensamples(sample_count, variable_count, degree, max_local_degree, value_function, no_polynomials=False):
  values = []
  # for each sample
  for i in range(sample_count):
    # generate a polynomial
    matrix = bistochastic.generate_matrix(degree, variable_count, max_local_degree=max_local_degree)
    if no_polynomials:
      values.append(value_function(matrix))
    else:
      poly = polynomials.product_polynomial(matrix)
      values.append(value_function(poly))
  # return list of sampled values
  return values

# generate <count> permanent values with given parameters
def get_permanent_samples(count, symbol_count, degree, local_degree):
  symbols = polynomials.getvars(count=symbol_count)
  no_poly = True
  valfunc = permanent
  outcomes = gensamples(count, symbol_count, degree, local_degree, valfunc, no_polynomials=no_poly)
  return outcomes


