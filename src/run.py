import simpy
from processes import car

# run the simulation (as a script)

# create the environment
env = simpy.Environment()

# create the instance of the process within the environment
env.process(car(env))

# run the simulation for a period of time
env.run(until=15)
