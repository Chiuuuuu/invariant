#!/usr/bin/env python

from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
t0 = time.time()
for i in xrange(iters):
    r = f()
print('Looping %d times took'%iters, time.time() - t0, 'seconds')
print('Result is', r)
print('Used the','cpu' if numpy.any( [isinstance(x.op,T.Elemwise) for x in f.maker.env.toposort()]) else 'gpu')
