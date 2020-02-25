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

        


    @timed_state(duration=2, next_state="do_something", first=True)
    def dont_do_something(self):
        """This happens first"""
        print("dont do something")
        self.driveTrain.setTank(0, 0)
        

    @timed_state(duration=time, next_state = "stop")
    def do_something(self, state_tm):
        """This happens second"""
        
        speed = -(math.sin(0.25 * math.pi * (1 / self.time) * state_tm))*.25
        """First integer is # of times to run through program, second is time. combined creates value."""
        print('{}  {}'.format(state_tm, speed))
        self.driveTrain.setTank(speed, speed)

    @state(must_finish = True)
    def stop(self):
        self.driveTrain.setTank(0, 0)
        print("stop")
        self.next_state("turn")
    
    @state(must_finish = True)
    def turn(self):
        pass
        """
        if limelight value = limelight PID value when detecting reflective tape:
            self.driveTrain.setTank(0, 0)
            self.next_state("get_to_position")
        else:
            self.driveTrain.setTank(.25, -.25)
        
    @state(must_finish = True)
    def get_to_position(self):
        if distace = the distance we can get 100% accuracy from:
            self.driveTrain.setTank(0,0)
            self.next_state("shoot")
        else:
            self.driveTrain.setTank
    
    @timed_state(duration = 3)
    def shoot(self):
        shooter code
    """