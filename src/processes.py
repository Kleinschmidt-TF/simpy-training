import simpy


def driver(env, car):
    """Driver process which wants to commence driving after 3 time units"""
    yield env.timeout(3)
    car.action.interrupt()


class Car(object):
    def __init__(self, env):
        self.env = env
        # start the run process everytime an instance is created
        self.action = env.process(self.run())

    def run(self):
        """Car running process - park/charge then drive infinitely!"""
        while True:
            print(f"Start parking and charging at {self.env.now}")
            charge_duration = 5

            # hand control back to the sim engine until timeout reached
            # (yield the process, and wait for it to finish or is interrupted!)
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                # when we receive an interrupt, stop charging and switch state
                print("Charging interrupted! Hope there is enough charge...")

            print(f"Start driving at {self.env.now}")
            trip_duration = 2
            # yield basic timeout event
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        """Charge process

        Args:
            duration: how long will the charge take
        """
        yield self.env.timeout(duration)
