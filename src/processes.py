import simpy


def car(env):
    """Car process - park then drive infinitely!

    Args:
        env: the simulation environment this occurs within
    """
    while True:
        print(f"Start parking at {env.now}")
        parking_duration = 5

        # hand control back to the sim engine until timeout reached
        yield env.timeout(parking_duration)

        print(f"Start driving at {env.now}")
        trip_duration = 2
        yield env.timeout(trip_duration)
