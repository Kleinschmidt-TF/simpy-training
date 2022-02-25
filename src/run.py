import simpy
from processes import Car

# run the simulation (as a script)

# create the environment
env = simpy.Environment()

# create the instance of the process within the environment (which triggers it to commence driving)
car = Car(env)

# run the simulation for a period of time
env.run(until=15)
