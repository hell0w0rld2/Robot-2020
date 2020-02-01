import wpilib.drive
import team3200.motorHelper as motorHelper

class DriveTrain: #Note - The way we will want to do this will be to give this component motor description dictionaries from robotmap and then creating the motors with motorhelper. After that, we simply call wpilib' differential drive
    driveTrain_motorsList: dict

    def on_enable(self):
        self.tankLeftSpeed = 0
        self.tankRightSpeed = 0
        self.arcadeSpeed = 0
        self.arcadeRotation = 0
        self.controllingOverArcade = False
        self.controllingOverTank = False

        leftMotorDescs = self.driveTrain_motorsList['left']
        rightMotorDescs = self.driveTrain_motorsList['right']

        self.leftMotor = motorHelper.createMotor(leftMotorDescs)
        self.rightMotor = motorHelper.createMotor(rightMotorDescs)

        print("{}".format(leftMotorDescs))
        print("{}".format(rightMotorDescs))

        self.driveTrain = wpilib.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        print("DriveTrain component Enabled")

    def getLeft(self):
        return self.leftMotor.get()

    def getRight(self):
        return self.rightMotor.get()

    def isStopping(self):
        pass

    def setTank(self, leftSpeed, rightSpeed):
        self.controllingOverTank = True
        self.tankLeftSpeed = leftSpeed
        self.tankRightSpeed = rightSpeed

    def setArcade(self, speed, rotation):
        self.controllingOverArcade = True
        self.arcadeSpeed = speed
        self.arcadeRotation = rotation

    def stop(self, coast = False):
        self.controllingOverTank = False
        self.controllingOverArcade = False

    def getMeasuredSpeed(self):
        pass

    def execute(self):
        if self.controllingOverTank:
            self.driveTrain.tankDrive(self.tankLeftSpeed, self.tankRightSpeed, False)
            #self.controllingOverTank = False
        elif self.controllingOverArcade:
            self.driveTrain.arcadeDrive(self.arcadeSpeed, self.arcadeRotation, False)
            #self.controllingOverArcade = False