from magicbot import AutonomousStateMachine, tunable, timed_state, state
import math
from components.driveTrain import DriveTrain

class autonomous(AutonomousStateMachine):
    """Creates the autonomous code"""
    """DO NOT USE IN PRODUCTION THIS WILL BE DELETED """
    time = 2.5
    MODE_NAME = "Two Steps"
    DEFAULT = True
    driveTrain: DriveTrain

    drive_speed = tunable(-1)

    """    
    @state(first = True, must_finish = True)
    def shoot(self):
        print("shoot")
        self.next_state = "dont_do_something"
    shooter logic
    Shooting could go here if no limelight PID"""
    
    @timed_state(duration=1, next_state="drive", first = True)
    def dont_do_something(self):
        """This happens first"""
        print("dont do something")
        self.driveTrain.setTank(0, 0)
        

    @timed_state(duration=time, next_state = "stop")
    def drive(self, state_tm):
        """This happens second"""
        
        speed = (math.sin(0.25 * math.pi * (1 / self.time) * state_tm))*.25
        """First integer is # of times to run through program, second is time. combined creates value."""
        print('{}  {}'.format(state_tm, speed))
        self.driveTrain.setTank(speed, speed)

    @timed_state(duration = 0.5)
    def stop(self):
        self.driveTrain.setTank(0, 0)
        print("stop")

    """shooting w/ limelight would go here"""