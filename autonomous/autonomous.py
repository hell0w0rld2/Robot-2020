from magicbot import AutonomousStateMachine, tunable, timed_state, state
import math
from components.driveTrain import DriveTrain
from components.ShooterLogic import ShooterLogic
class autonomous(AutonomousStateMachine):
    """Creates the autonomous code"""
    """DO NOT USE IN PRODUCTION THIS WILL BE DELETED """
    time = 2.5
    MODE_NAME = "Two Steps"
    DEFAULT = True
    driveTrain: DriveTrain
    shooter: ShooterLogic
    drive_speed = tunable(-1)

        
    @state(first = True, must_finish = True)
    def engage_shooter(self):
        self.shooter.engage()
        print("engaged")
        self.next_state("shooter_wait")

    @state(must_finish = True)
    def shooter_wait(self, state_tm):
        if self.shooter.done() or state_tm > 8:
            self.next_state("drive")

    @timed_state(duration=time, next_state = "stop")
    def drive(self, state_tm):
        """This happens second"""
        
        speed = .25
        """First integer is # of times to run through program, second is time. combined creates value."""
        self.driveTrain.setTank(speed, speed)

    @timed_state(duration = 0.5)
    def stop(self):
        self.driveTrain.setTank(0, 0)

    """shooting w/ limelight would go here"""