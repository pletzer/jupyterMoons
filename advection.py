import numpy

n = 40 # number of cells

# initial condition
f0 = numpy.zeros((n,), numpy.float64)
f0[0] = 1

def step(f, c):
	newf = (1 - c)*f 
	newf[1:] += c*f[:-1]
	newf[0] += c*f[-1] # periodic boundary conditions
	return newf

def advance(f, c, nsteps=10):
	for i in range(nsteps):
		f = step(f, c)
	return f

c = 0.9
f = f0[:]
print(advance(f, c, 10000))
print(f.sum())

