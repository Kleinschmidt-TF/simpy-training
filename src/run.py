import simpy
from processes import Car, driver

# run the simulation (as a script)

# create the environment
env = simpy.Environment()

# create the instance of the process within the environment (which triggers it to commence driving)
# Object-oriented functionality
car = Car(env)

# basic event functionality
env.process(driver(env, car))

# run the simulation for a period of time
env.run(until=15)
