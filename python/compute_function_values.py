#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import sys
import os.path

import stabpoly.polynomials as polynomials
import stabpoly.sampling as sampling

import matlabify

# set seed
import numpy.random
SEED = 1
numpy.random.seed(SEED)

DATA_DIR = 'matlab/data/'

def main():
  print('running example sampling')
  num_matrices_per_interval = 300
  intervals = 100
  # parameters: symbols, degree, local degree
  param_list = [#(3, 2),
                #(3, 3),
                #(4, 3),
                (7, 2),
                ]
  for degree,local_degree in param_list:
    num_symbols = degree
    output_filename = 'permanents_sym{}_deg{}_locdeg{}.m'.format(num_symbols, degree, local_degree)
    output_filepath = os.path.join(DATA_DIR, output_filename)
    print(' == FILE: {} == '.format(output_filepath))
    output_file = open(output_filepath,'w')
    generate_permanents_for_matlab(num_matrices_per_interval, intervals, num_symbols, degree, local_degree, output_file)
    output_file.close()

def generate_permanents_for_matlab(num_matrices_per_interval, intervals, num_symbols, degree, local_degree, output_file):
  num_matrices = num_matrices_per_interval * intervals
  params = {'sample_count' : num_matrices, 'variable_count' : num_symbols, 'degree' : degree,
              'max_local_degree' : local_degree, 'value_function' : 'permanent'}
  print('generating permanents for params: ' + str(params))
  outcomes = []
  for i in range(intervals):
    new_outcomes = sampling.get_permanent_samples(num_matrices_per_interval, num_symbols, degree, local_degree)
    outcomes += new_outcomes
    print('finished interval {}/{}'.format(i+1, intervals))
  # print results
  theolim = polynomials.gurvits_bound(degree, local_degree)
  print('% PARAMS: ' + str(params), file=output_file)
  count_str = matlabify.init_variable('N', num_matrices)
  theolim_str = matlabify.init_variable('theolim', theolim)
  array_str = matlabify.init_variable('data', outcomes)
  print(count_str, file=output_file)
  print(theolim_str, file=output_file)
  print(array_str, file=output_file)

if __name__ == '__main__':
  main()
