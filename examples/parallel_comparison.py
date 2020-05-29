# make an example of the workflow with gridded anuga output data

import numpy as np
import time
from particlerouting.parallel_routing import parallel_routing

# for serial run comparison import the regular iterator
from particlerouting.particle_track import Particle

### Define the parameters that are being used

# define an empty class
class pobj():
    pass

# create params and then assign the parameters
params = pobj()

# load some variables from a deltarcm output so stage is varied
data = np.load('ex_anuga_data.npz')

# pull depth and stage from that data
depth = data['depth']
qx = data['qx']
qy = data['qy']

# define the params variables
params.depth = depth
params.stage = depth # use depth as proxy for stage in this example
params.qx = qx
params.qy = qy

params.seed_xloc = list(range(20,30))
params.seed_yloc = list(range(48,53))
params.Np_tracer = 50
params.dx = 50.
params.theta = 1.0
params.model = 'Anuga'

### Apply the parameters to run the particle routing model

# use 2 cores to route in parallel
print('start parallel')
start_par_time = time.time()
par_result = parallel_routing(params,50,2)
par_time = time.time() - start_par_time
print('end parallel')

# compare to a serial run
print('start serial')
start_serial_time = time.time()
# do twice to match number of particles parallel is doing
for z in list(range(0,2)):
    all_walk_data = None # initialize walk data list
    particle = Particle(params)
    # do 50 iterations to match parallel
    for i in list(range(0,50)):
        all_walk_data = particle.run_iteration(previous_walk_data=all_walk_data)
        
# get time
serial_time = time.time() - start_serial_time
print('end serial')

### print times elapsed
print('Serial Compute Time: ' + str(serial_time))
print('Parallel Compute Time: ' + str(par_time))
